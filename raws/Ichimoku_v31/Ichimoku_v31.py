# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame
from freqtrade.strategy.interface import IStrategy

# --------------------------------
# Add your lib to import here
import freqtrade.vendor.qtpylib.indicators as qtpylib
from freqtrade.strategy import IStrategy, merge_informative_pair
from technical.indicators import ichimoku


class Ichimoku_v31(IStrategy):
    # ROI table:
    minimal_roi = {"0": 100}

    # Stoploss:
    stoploss = -0.99

    # Optimal timeframe for the strategy.
    timeframe = "1h"

    inf_tf = "4h"

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = True

    # These values can be overridden in the "exit_pricing" section in the config.
    use_exit_signal = True
    exit_profit_only = False
    ignore_roi_if_entry_signal = True

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count = 150

    # Optional order type mapping.
    order_types = {
        "entry": "market",
        "exit": "market",
        "stoploss": "market",
        "stoploss_on_exchange": False,
    }

    def informative_pairs(self):
        if not self.dp:
            # Don't do anything if DataProvider is not available.
            return []
        # Get access to all pairs available in whitelist.
        pairs = self.dp.current_whitelist()
        # Assign tf to each pair so they can be downloaded and cached for strategy.
        informative_pairs = [(pair, "4h") for pair in pairs]
        return informative_pairs

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        if not self.dp:
            # Don't do anything if DataProvider is not available.
            return dataframe

        dataframe_inf = self.dp.get_pair_dataframe(pair=metadata["pair"], timeframe=self.inf_tf)

        # Heiken Ashi Candlestick Data
        heikinashi = qtpylib.heikinashi(dataframe_inf)

        dataframe_inf["ha_open"] = heikinashi["open"]
        dataframe_inf["ha_close"] = heikinashi["close"]
        dataframe_inf["ha_high"] = heikinashi["high"]
        dataframe_inf["ha_low"] = heikinashi["low"]

        ha_ichi = ichimoku(
            heikinashi,
            conversion_line_period=20,
            base_line_periods=60,
            laggin_span=120,
            displacement=30,
        )

        # Required Ichi Parameters
        dataframe_inf["senkou_a"] = ha_ichi["senkou_span_a"]
        dataframe_inf["senkou_b"] = ha_ichi["senkou_span_b"]
        dataframe_inf["cloud_green"] = ha_ichi["cloud_green"]
        dataframe_inf["cloud_red"] = ha_ichi["cloud_red"]

        # Merge timeframes
        dataframe = merge_informative_pair(
            dataframe, dataframe_inf, self.timeframe, self.inf_tf, ffill=True
        )

        """
    Senkou Span A > Senkou Span B = Cloud Green
    Senkou Span B > Senkou Span A = Cloud Red
    """
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (
                    (dataframe["ha_close_4h"].crossed_above(dataframe["senkou_a_4h"]))
                    & (dataframe["ha_close_4h"].shift() < (dataframe["senkou_a_4h"]))
                    & (dataframe["cloud_green_4h"] is True)
                )
                | (
                    (dataframe["ha_close_4h"].crossed_above(dataframe["senkou_b_4h"]))
                    & (dataframe["ha_close_4h"].shift() < (dataframe["senkou_b_4h"]))
                    & (dataframe["cloud_red_4h"] is True)
                )
            ),
            "enter_long",
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe["ha_close_4h"] < dataframe["senkou_a_4h"])
                | (dataframe["ha_close_4h"] < dataframe["senkou_b_4h"])
            ),
            "exit_long",
        ] = 1
        return dataframe