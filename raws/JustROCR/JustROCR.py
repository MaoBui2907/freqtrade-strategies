from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
import talib.abstract as ta


class JustROCR(IStrategy):
    minimal_roi = {"0": 0.20}

    stoploss = -0.20
    trailing_stop = True
    ticker_interval = "1h"

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["rocr"] = ta.ROCR(dataframe, period=499)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["rocr"] > 1.10), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(), "exit_long"] = 1
        return dataframe
