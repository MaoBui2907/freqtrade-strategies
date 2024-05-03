from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame

# from technical.indicators import accumulation_distribution
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from technical.indicators import ichimoku


class Ichimoku_v33(IStrategy):
    """ """

    minimal_roi = {"0": 100}

    stoploss = -1  # -0.35

    ticker_interval = "4h"  # 3m

    # startup_candle_count: int = 2

    # trailing stoploss
    # trailing_stop = True
    # trailing_stop_positive = 0.40 #0.35
    # trailing_stop_positive_offset = 0.50
    # trailing_only_offset_is_reached = False

    def informative_pairs(self):
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        ichi = ichimoku(
            dataframe,
            conversion_line_period=20,
            base_line_periods=60,
            laggin_span=120,
            displacement=30,
        )
        # dataframe['chikou_span'] = ichi['chikou_span']
        dataframe["tenkan"] = ichi["tenkan_sen"]
        dataframe["kijun"] = ichi["kijun_sen"]
        dataframe["senkou_a"] = ichi["senkou_span_a"]
        dataframe["senkou_b"] = ichi["senkou_span_b"]
        dataframe["cloud_green"] = ichi["cloud_green"]
        dataframe["cloud_red"] = ichi["cloud_red"]

        # Parabolic SAR
        dataframe["sar"] = ta.SAR(dataframe)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (qtpylib.crossed_above(dataframe["close"].shift(2), dataframe["senkou_a"]))
                & (dataframe["close"].shift(2) > dataframe["senkou_a"])
                & (dataframe["close"].shift(2) > dataframe["senkou_b"])
            ),
            "enter_long",
        ] = 1

        dataframe.loc[
            (
                (qtpylib.crossed_above(dataframe["close"].shift(2), dataframe["senkou_b"]))
                & (dataframe["close"].shift(2) > dataframe["senkou_a"])
                & (dataframe["close"].shift(2) > dataframe["senkou_b"])
            ),
            "enter_long",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (qtpylib.crossed_below(dataframe["tenkan"], dataframe["kijun"]))
                & (dataframe["close"] < dataframe["senkou_a"])
                & (dataframe["close"] < dataframe["senkou_b"])
                & (dataframe["cloud_red"] is True)
            ),
            "exit_long",
        ] = 1

        dataframe.loc[(dataframe["close"] < dataframe["sar"]), "exit_long"] = 1

        return dataframe