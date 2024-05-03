import talib.abstract as ta
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
from datetime import datetime

# Custom imports to fetch API data


class INSIDEUP(IStrategy):
    INTERFACE_VERSION = 2

    # ROI table:
    minimal_roi = {"0": 0.237, "4195": 0.17, "7191": 0.053, "14695": 0}

    # Stoploss:
    stoploss = -0.99  # value loaded from strategy

    # Trailing stop:
    trailing_stop = True  # value loaded from strategy
    trailing_stop_positive = 0.011  # value loaded from strategy
    trailing_stop_positive_offset = 0.029  # value loaded from strategy
    trailing_only_offset_is_reached = True  # value loaded from strategy

    # Optimal timeframe for the strategy.
    timeframe = "1d"

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = True

    # These values can be overridden in the "exit_pricing" section in the config.
    use_exit_signal = False
    exit_profit_only = False
    ignore_roi_if_entry_signal = False

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Inputs:
        # # prices: ['open', 'high', 'low', 'close']

        # # Three Inside Up/Down: values [0, -100, 100]
        dataframe["CDL3INSIDE"] = ta.CDL3INSIDE(dataframe)  # values [-100, 0, 100]
        # # MORNINGDOJISTAR: values [0, 100]
        dataframe["CDLMORNINGDOJISTAR"] = ta.CDLMORNINGDOJISTAR(dataframe)  # values [0, 100]
        # # Piercing Line: values [0, 100]
        dataframe["CDLPIERCING"] = ta.CDLPIERCING(dataframe)  # values [0, 100]
        # # Three Black Crows: values [-100, 0, 100]
        dataframe["CDL3BLACKCROWS"] = ta.CDL3BLACKCROWS(dataframe)  # values [-100, 0, 100]

        # RSI
        dataframe["rsi_14"] = ta.RSI(dataframe, timeperiod=14)

        # ADX
        dataframe["adx"] = ta.ADX(dataframe)
        dataframe["slowadx"] = ta.ADX(dataframe, 35)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dateTime = datetime.now()

        dataframe.loc[
            # Check for downtrend movement
            ((dataframe["close"] < dataframe["close"].shift(2)) | (dataframe["rsi_14"] < 50))
            & (dataframe["adx"] > 13.0)
            &
            # Check for patterns
            (
                # the user should consider that a three inside up is significant
                # when it appears in a downtrend
                (dataframe["CDL3INSIDE"] >= 0).any()  # Bullish
            ),
            ["entry", "buy_tag"],
        ] = (1, "buy_3_inside")

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        no sell signal
        """
        dataframe.loc[:, "exit_long"] = 0
        return dataframe