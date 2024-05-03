"""
Supertrend strategy:
* Description: Generate a 3 supertrend indicators for 'entry' strategies & 3 supertrend indicators for 'exit' strategies
               Buys if the 3 'entry' indicators are 'up'
               Sells if the 3 'exit' indicators are 'down'
* Author: @juankysoriano (Juan Carlos Soriano)
* github: https://github.com/juankysoriano/

*** NOTE: This Supertrend strategy is just one of many possible strategies using `Supertrend` as indicator. It should on any case used at your own risk.
          It comes with at least a couple of caveats:
            1. The implementation for the `supertrend` indicator is based on the following discussion: https://github.com/freqtrade/freqtrade-strategies/issues/30 . Concretelly https://github.com/freqtrade/freqtrade-strategies/issues/30#issuecomment-853042401
            2. The implementation for `supertrend` on this strategy is not validated; meaning this that is not proven to match the results by the paper where it was originally introduced or any other trusted academic resources
"""

from freqtrade.strategy.interface import IStrategy
from freqtrade.strategy.hyper import IntParameter
from pandas import DataFrame
import talib.abstract as ta
import numpy as np
import time
import pandas as pd


class FastSupertrendOpt(IStrategy):
    # Buy params, Sell params, ROI, Stoploss and Trailing Stop are values generated by 'freqtrade hyperopt --strategy Supertrend --hyperopt-loss ShortTradeDurHyperOptLoss --timerange=20210101- --timeframe=1h --spaces all'
    # It's encourage you find the values that better suites your needs and risk management strategies

    # Buy hyperspace params:
    buy_params = {
        "buy_m1": 4,
        "buy_m2": 7,
        "buy_m3": 1,
        "buy_p1": 8,
        "buy_p2": 9,
        "buy_p3": 8,
    }

    # Sell hyperspace params:
    sell_params = {
        "sell_m1": 1,
        "sell_m2": 3,
        "sell_m3": 6,
        "sell_p1": 16,
        "sell_p2": 18,
        "sell_p3": 18,
    }

    # ROI table:
    minimal_roi = {"0": 0.087, "372": 0.058, "861": 0.029, "2221": 0}

    # Stoploss:
    stoploss = -0.265

    # Trailing stop:
    trailing_stop = True
    trailing_stop_positive = 0.05
    trailing_stop_positive_offset = 0.144
    trailing_only_offset_is_reached = False

    timeframe = "1h"

    startup_candle_count = 18

    buy_m1 = IntParameter(1, 7, default=4, space="entry", load=True, optimize=True)
    buy_m2 = IntParameter(1, 7, default=4, space="entry", load=True, optimize=True)
    buy_m3 = IntParameter(1, 7, default=4, space="entry", load=True, optimize=True)
    buy_p1 = IntParameter(7, 21, default=14, space="entry", load=True, optimize=True)
    buy_p2 = IntParameter(7, 21, default=14, space="entry", load=True, optimize=True)
    buy_p3 = IntParameter(7, 21, default=14, space="entry", load=True, optimize=True)

    sell_m1 = IntParameter(1, 7, default=4, space="exit", load=True, optimize=True)
    sell_m2 = IntParameter(1, 7, default=4, space="exit", load=True, optimize=True)
    sell_m3 = IntParameter(1, 7, default=4, space="exit", load=True, optimize=True)
    sell_p1 = IntParameter(7, 21, default=14, space="exit", load=True, optimize=True)
    sell_p2 = IntParameter(7, 21, default=14, space="exit", load=True, optimize=True)
    sell_p3 = IntParameter(7, 21, default=14, space="exit", load=True, optimize=True)

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["supertrend_1_buy"] = self.supertrend(
            dataframe, self.buy_m1.value, int(self.buy_p1.value)
        )["STX"]
        dataframe["supertrend_2_buy"] = self.supertrend(
            dataframe, self.buy_m2.value, int(self.buy_p2.value)
        )["STX"]
        dataframe["supertrend_3_buy"] = self.supertrend(
            dataframe, self.buy_m3.value, int(self.buy_p3.value)
        )["STX"]
        dataframe["supertrend_1_sell"] = self.supertrend(
            dataframe, self.sell_m1.value, int(self.sell_p1.value)
        )["STX"]
        dataframe["supertrend_2_sell"] = self.supertrend(
            dataframe, self.sell_m2.value, int(self.sell_p2.value)
        )["STX"]
        dataframe["supertrend_3_sell"] = self.supertrend(
            dataframe, self.sell_m3.value, int(self.sell_p3.value)
        )["STX"]

        dataframe.loc[
            (
                (dataframe["supertrend_1_buy"] == "up")
                & (dataframe["supertrend_2_buy"] == "up")
                & (
                    dataframe["supertrend_3_buy"] == "up"
                )  # The three indicators are 'up' for the current candle
                & (dataframe["volume"] > 0)  # There is at least some trading volume
            ),
            "enter_long",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe["supertrend_1_sell"] == "down")
                & (dataframe["supertrend_2_sell"] == "down")
                & (
                    dataframe["supertrend_3_sell"] == "down"
                )  # The three indicators are 'down' for the current candle
                & (dataframe["volume"] > 0)  # There is at least some trading volume
            ),
            "exit_long",
        ] = 1

        return dataframe

    """
        Supertrend Indicator; adapted for freqtrade
        from: https://github.com/freqtrade/freqtrade-strategies/issues/30
    """

    def supertrend(self, dataframe: DataFrame, multiplier, period):
        start_time = time.time()

        df = dataframe.copy()
        last_row = dataframe.tail(1).index.item()

        df["TR"] = ta.TRANGE(df)
        df["ATR"] = ta.SMA(df["TR"], period)

        st = "ST_" + str(period) + "_" + str(multiplier)
        stx = "STX_" + str(period) + "_" + str(multiplier)

        # Compute basic upper and lower bands
        BASIC_UB = ((df["high"] + df["low"]) / 2 + multiplier * df["ATR"]).values
        BASIC_LB = ((df["high"] + df["low"]) / 2 - multiplier * df["ATR"]).values

        FINAL_UB = np.zeros(last_row + 1)
        FINAL_LB = np.zeros(last_row + 1)
        ST = np.zeros(last_row + 1)
        CLOSE = df["close"].values

        # Compute final upper and lower bands
        for i in range(period, last_row + 1):
            FINAL_UB[i] = (
                BASIC_UB[i]
                if BASIC_UB[i] < FINAL_UB[i - 1] or CLOSE[i - 1] > FINAL_UB[i - 1]
                else FINAL_UB[i - 1]
            )
            FINAL_LB[i] = (
                BASIC_LB[i]
                if BASIC_LB[i] > FINAL_LB[i - 1] or CLOSE[i - 1] < FINAL_LB[i - 1]
                else FINAL_LB[i - 1]
            )

        # Set the Supertrend value
        for i in range(period, last_row + 1):
            ST[i] = (
                FINAL_UB[i]
                if ST[i - 1] == FINAL_UB[i - 1] and CLOSE[i] <= FINAL_UB[i]
                else FINAL_LB[i]
                if ST[i - 1] == FINAL_UB[i - 1] and CLOSE[i] > FINAL_UB[i]
                else FINAL_LB[i]
                if ST[i - 1] == FINAL_LB[i - 1] and CLOSE[i] >= FINAL_LB[i]
                else FINAL_UB[i]
                if ST[i - 1] == FINAL_LB[i - 1] and CLOSE[i] < FINAL_LB[i]
                else 0.00
            )
        df_ST = pd.DataFrame(ST, columns=[st])
        df = pd.concat([df, df_ST], axis=1)

        # Mark the trend direction up/down
        df[stx] = np.where((df[st] > 0.00), np.where((df["close"] < df[st]), "down", "up"), np.NaN)

        df.fillna(0, inplace=True)

        end_time = time.time()
        # print("total time taken this loop: ", end_time - start_time)

        return DataFrame(index=df.index, data={"ST": df[st], "STX": df[stx]})