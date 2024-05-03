# --- Do not remove these libs --- freqtrade backtesting --strategy SmoothScalp --timerange 20210110-20210410
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame

# --------------------------------
import talib.abstract as ta
# --------------------------------


# V1
class heikin(IStrategy):
    # do not use this strategy in live mod. It is not good enough yet and can only be use to find trends.
    timeframe = "1h"
    # I haven't found the best roi and stoplost, so feel free to explore.
    minimal_roi = {
        "0": 10,
    }
    stoploss = -0.99

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["hclose"] = (
            dataframe["open"] + dataframe["high"] + dataframe["low"] + dataframe["close"]
        ) / 4
        dataframe["hopen"] = (
            dataframe["open"].shift(2) + dataframe["close"].shift(2)
        ) / 2  # it is not the same as real heikin ashi since I found that this is better.
        dataframe["hhigh"] = dataframe[["open", "close", "high"]].max(axis=1)
        dataframe["hlow"] = dataframe[["open", "close", "low"]].min(axis=1)

        dataframe["emac"] = ta.SMA(
            dataframe["hclose"], timeperiod=6
        )  # to smooth out the data and thus less noise.
        dataframe["emao"] = ta.SMA(dataframe["hopen"], timeperiod=6)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["emao"] < dataframe["emac"]), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["emao"] > dataframe["emac"]), "exit_long"] = 1
        return dataframe