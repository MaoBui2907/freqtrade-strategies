# --- Do not remove these libs ---
from freqtrade.strategy.interface import IStrategy
from functools import reduce
from pandas import DataFrame

# --------------------------------
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import datetime
from datetime import datetime, timedelta
from freqtrade.persistence import Trade
from freqtrade.strategy import DecimalParameter, IntParameter


def EWO(dataframe, ema_length=5, ema2_length=35):
    df = dataframe.copy()
    ema1 = ta.EMA(df, timeperiod=ema_length)
    ema2 = ta.EMA(df, timeperiod=ema2_length)
    emadif = (ema1 - ema2) / df["close"] * 100
    return emadif


class ElliotV5HOMod2(IStrategy):
    INTERFACE_VERSION = 2

    # Buy hyperspace params:
    buy_params = {
        "base_nb_candles_buy": 17,
        "ewo_high": 3.34,
        "ewo_low": -17.457,
        "low_offset": 0.978,
        "rsi_buy": 60,
    }

    # Sell hyperspace params:
    sell_params = {"base_nb_candles_sell": 39, "high_offset": 1.011, "high_offset_2": 0.997}

    # ROI table:
    minimal_roi = {"0": 0.05, "40": 0.04, "201": 0.03}

    # Stoploss:
    stoploss = -0.99

    # SMAOffset
    base_nb_candles_buy = IntParameter(
        5, 80, default=buy_params["base_nb_candles_buy"], space="entry", optimize=True
    )
    base_nb_candles_sell = IntParameter(
        5, 80, default=sell_params["base_nb_candles_sell"], space="exit", optimize=True
    )
    low_offset = DecimalParameter(
        0.9, 0.99, default=buy_params["low_offset"], space="entry", optimize=True
    )
    high_offset = DecimalParameter(
        0.99, 1.1, default=sell_params["high_offset"], space="exit", optimize=True
    )
    high_offset_2 = DecimalParameter(
        0.99, 1.5, default=sell_params["high_offset_2"], space="sell", optimize=True
    )

    # Protection
    fast_ewo = 50
    slow_ewo = 200
    ewo_low = DecimalParameter(
        -20.0, -8.0, default=buy_params["ewo_low"], space="entry", optimize=True
    )
    ewo_high = DecimalParameter(
        2.0, 12.0, default=buy_params["ewo_high"], space="entry", optimize=True
    )
    rsi_buy = IntParameter(30, 70, default=buy_params["rsi_buy"], space="entry", optimize=True)

    # Trailing stop:
    trailing_stop = True
    trailing_stop_positive = 0.005
    trailing_stop_positive_offset = 0.03
    trailing_only_offset_is_reached = True

    # Sell signal
    use_exit_signal = True
    exit_profit_only = True
    exit_profit_offset = 0.01
    ignore_roi_if_entry_signal = True

    order_types = {
        "entry": "limit",
        "exit": "limit",
        "stoploss": "market",
        "stoploss_on_exchange": False,
    }

    # Optional order time in force.
    order_time_in_force = {"entry": "gtc", "exit": "gtc"}

    # Optimal timeframe for the strategy
    timeframe = "5m"
    informative_timeframe = "1h"

    process_only_new_candles = True
    startup_candle_count = 79

    plot_config = {
        "main_plot": {
            f"ma_buy_{base_nb_candles_buy.value}": {"color": "orange"},
            f"ma_sell_{base_nb_candles_sell.value}": {"color": "green"},
        },
    }

    use_custom_stoploss = False

    def informative_pairs(self):
        pairs = self.dp.current_whitelist()
        informative_pairs = [(pair, self.informative_timeframe) for pair in pairs]

        return informative_pairs

    def get_informative_indicators(self, metadata: dict):
        dataframe = self.dp.get_pair_dataframe(
            pair=metadata["pair"], timeframe=self.informative_timeframe
        )

        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        if self.config["runmode"].value == "hyperopt":
            # Calculate all ma_buy values
            for val in self.base_nb_candles_buy.range:
                dataframe[f"ma_buy_{val}"] = ta.EMA(dataframe, timeperiod=val)

            # Calculate all ma_sell values
            for val in self.base_nb_candles_sell.range:
                dataframe[f"ma_sell_{val}"] = ta.EMA(dataframe, timeperiod=val)

        else:
            dataframe[f"ma_buy_{self.base_nb_candles_buy.value}"] = ta.EMA(
                dataframe, timeperiod=self.base_nb_candles_buy.value
            )

            dataframe[f"ma_sell_{self.base_nb_candles_sell.value}"] = ta.EMA(
                dataframe, timeperiod=self.base_nb_candles_sell.value
            )

        dataframe["hma_50"] = qtpylib.hull_moving_average(dataframe["close"], window=50)

        # Elliot
        dataframe["EWO"] = EWO(dataframe, self.fast_ewo, self.slow_ewo)

        # RSI
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        dataframe["rsi_fast"] = ta.RSI(dataframe, timeperiod=4)
        dataframe["rsi_slow"] = ta.RSI(dataframe, timeperiod=20)

        dataframe["hma_50"] = qtpylib.hull_moving_average(dataframe["close"], window=50)

        dataframe["rsi_fast"] = ta.RSI(dataframe, timeperiod=4)
        dataframe["rsi_slow"] = ta.RSI(dataframe, timeperiod=20)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions = []

        conditions.append(
            (
                (
                    dataframe["close"]
                    < (
                        dataframe[f"ma_buy_{self.base_nb_candles_buy.value}"]
                        * self.low_offset.value
                    )
                )
                & (dataframe["EWO"] > self.ewo_high.value)
                & (dataframe["rsi"] < self.rsi_buy.value)
                & (dataframe["volume"] > 0)
            )
        )

        conditions.append(
            (
                (
                    dataframe["close"]
                    < (
                        dataframe[f"ma_buy_{self.base_nb_candles_buy.value}"]
                        * self.low_offset.value
                    )
                )
                & (dataframe["EWO"] < self.ewo_low.value)
                & (dataframe["rsi"] < self.rsi_buy.value)
                & (dataframe["volume"] > 0)
            )
        )

        if conditions:
            dataframe.loc[reduce(lambda x, y: x | y, conditions), "entry"] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions = []

        conditions.append(
            (
                (
                    dataframe["close"]
                    > (
                        dataframe[f"ma_sell_{self.base_nb_candles_sell.value}"]
                        * self.high_offset.value
                    )
                )
                & (dataframe["volume"] > 0)
            )
        )

        if conditions:
            dataframe.loc[reduce(lambda x, y: x | y, conditions), "exit"] = 1

        return dataframe

    def custom_stoploss(
        self,
        pair: str,
        trade: Trade,
        current_time: datetime,
        current_rate: float,
        current_profit: float,
        **kwargs,
    ) -> float:
        df, _ = self.dp.get_analyzed_dataframe(pair, self.timeframe)
        candle = df.iloc[-1].squeeze()

        if current_profit < 0.001 and current_time - timedelta(minutes=140) > trade.open_date_utc:
            return -0.005

        return 1