import talib.abstract as ta
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame


class YOLO(IStrategy):
    # Buy hyperspace params:
    buy_params = {"adx": 34, "aroon-down": 33, "aroon-up": 98}

    # Sell hyperspace params:
    sell_params = {}

    # ROI table:
    minimal_roi = {"0": 0.03, "7": 0.02, "33": 0.01, "71": 0.005}

    # Stoploss:
    stoploss = -0.01

    # Trailing stop:
    trailing_stop = True
    trailing_stop_positive = 0.03289
    trailing_stop_positive_offset = 0.05723
    trailing_only_offset_is_reached = False

    """
    END HYPEROPT
    """

    timeframe = "1m"

    use_exit_signal = False
    exit_profit_only = False
    ignore_roi_if_entry_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["adx"] = ta.ADX(dataframe, timeperiod=90)  # 90
        aroon = ta.AROON(dataframe, timeperiod=60)  # 60

        dataframe["aroon-down"] = aroon["aroondown"]
        dataframe["aroon-up"] = aroon["aroonup"]

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        params = self.buy_params

        dataframe.loc[
            (
                (dataframe["adx"] > params["adx"])
                & (dataframe["aroon-up"] > params["aroon-up"])
                & (dataframe["aroon-down"] < params["aroon-down"])
                & (dataframe["volume"] > 0)
            ),
            "entry",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        no sell signal
        """
        dataframe["exit_long"] = 0
        return dataframe
