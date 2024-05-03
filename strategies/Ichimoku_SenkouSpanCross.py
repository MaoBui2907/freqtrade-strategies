from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
from technical.indicators import ichimoku


class Ichimoku_SenkouSpanCross(IStrategy):
    """ """

    minimal_roi = {"0": 1000}
    stoploss = -0.99
    timeframe = "4h"
    # startup_candle_count: int = 300
    # trailing stoploss
    trailing_stop = True
    trailing_stop_positive = 0.45
    trailing_stop_positive_offset = 0.50
    trailing_only_offset_is_reached = True
    order_types = {
        "entry": "market",
        "exit": "market",
        "stoploss": "market",
        "stoploss_on_exchange": False,
    }
    order_time_in_force = {"entry": "gtc", "exit": "gtc"}

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
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (qtpylib.crossed_above(dataframe["senkou_a"], dataframe["senkou_b"]))
                & (dataframe["close"] > dataframe["senkou_a"])
                & (dataframe["close"] > dataframe["senkou_b"])
                & (dataframe["cloud_green"] is True)
            ),
            "enter_long",
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (qtpylib.crossed_above(dataframe["senkou_b"], dataframe["senkou_a"]))
                & (dataframe["close"] < dataframe["senkou_a"])
                & (dataframe["close"] < dataframe["senkou_b"])
                & (dataframe["cloud_red"] is True)
            ),
            "exit_long",
        ] = 1
        return dataframe