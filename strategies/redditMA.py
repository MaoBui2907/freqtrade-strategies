"""
3. sma ema with complicated support
4. sma ema with simple support
4-0.2. sma ema with simple support with 0.2 SL
5. sma wma with simple support
6. sma wma with VWAP simple support
"""

# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
# --------------------------------

import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy as np  # noqa


class redditMA(IStrategy):
    minimal_roi = {"0": 0.5, "30": 0.3, "60": 0.125, "120": 0.06, "180": 0.01}

    # Optimal stoploss designed for the strategy
    # This attribute will be overridden if the config file contains "stoploss"
    stoploss = -0.5

    # Optimal ticker interval for the strategy
    ticker_interval = "15m"

    # trailing stoploss
    trailing_stop = False

    # run "populate_indicators" only for new candle
    process_only_new_candles = True

    # Experimental settings (configuration will overide these if set)
    use_exit_signal = True
    exit_profit_only = True
    ignore_roi_if_entry_signal = True

    # Optional order type mapping
    order_types = {
        "entry": "limit",
        "exit": "limit",
        "stoploss": "market",
        "stoploss_on_exchange": False,
    }

    startup_candle_count = 34

    def informative_pairs(self):
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["SLOWMA"] = ta.EMA(dataframe, 13)
        dataframe["FASTMA"] = ta.EMA(dataframe, 34)

        # dataframe = self.mods(dataframe)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            qtpylib.crossed_above(dataframe["FASTMA"], dataframe["SLOWMA"]), "enter_long"
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            qtpylib.crossed_below(dataframe["FASTMA"], dataframe["SLOWMA"]), "exit_long"
        ] = 1

        return dataframe
