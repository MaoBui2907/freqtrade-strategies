# Persia Strategy
# An strategy for combining formulas
# Author: @Mablue (Masoud Azizi)
# github: https://github.com/mablue/
# freqtrade hyperopt --hyperopt-loss SharpeHyperOptLoss --strategy Persia
# --- Do not remove these libs ---


from freqtrade.strategy.hyper import CategoricalParameter, IntParameter, DecimalParameter
from freqtrade.strategy.interface import IStrategy
from pandas import DataFrame
# --------------------------------

# Add your lib to import here
import talib.abstract as ta
# import freqtrade.vendor.qtpylib.indicators as qtpylib
from functools import reduce
import pandas as pd
import numpy as np
###################################### SETINGS ######################################

# INDICATORS
COSTUMEINDICATORSENABLED = True
COSTUMEINDICATORS = ['SMA', 'EMA', 'TEMA', 'DEMA']

# TIMEFRAMES
TIMEFRAMES = 10  # number of populated indicators
TFGAP = 3  # gap between each timeframe
COSTUMETFENABLED = True
COSTUMETF = [3, 7, 9, 21, 27, 63, 81, 189]

# REALS
REALSRANGE = [-2, 2]
DECIMALS = 1

# CONDITIONS
CONDITIONS = 3  # (max 100)

# FORMULAS
FORMULAS = [
    # '(A**2+B**2)>R**2',
    # '(A**2+B**2)<R**2',
    'A>B',
    'A<B',
    'A*R==B',
    'A==R',
    'A!=R',
    'A/B>R',
    'B/A>R',
    '0<=A<=1',
    '0<=B<=1',
    # 'A+R<B',
    # 'A-R>B',
    # '(R/(A+B))<A',
    # '(R/(A+B))<B',
    # '(R/(A+B))>A',
    # '(R/(A+B))>B',

    # 'A*(1+R)**2>5', # FV
    # 'A/(1+R)**2>5', # PV
    # '100-(100/(1+A/B))>70', # RSI
    # '100-(100/(1+A/B))<30', # RSI
]
#################################### END SETINGS ####################################


ta_funcs = ta.__TA_FUNCTION_NAMES__
ta_funcs.pop(107)
ta_funcs = [f for f in ta_funcs if not f.startswith('CDL')]
indicators = COSTUMEINDICATORS if COSTUMEINDICATORSENABLED else ta_funcs

tf_arr = np.arange(TIMEFRAMES)*TFGAP+TFGAP
# TODO: Not Costumized timeframes not work!
timeframes = COSTUMETF  # if COSTUMETFENABLED else np.delete(tf_arr,np.argwhere(tf_arr < 2))

reals = REALSRANGE

formulas = FORMULAS


class Persia(IStrategy):
    ###################### RESULT PLACE ######################
    buy_params = {
        "formula0": "A!=R",
        "formula1": "0<=B<=1",
        "formula2": "B/A>R",
        "indicator0": "TEMA",
        "indicator1": "DEMA",
        "indicator2": "DEMA",
        "timeframe0": 9,
        "timeframe1": 3,
        "timeframe2": 27,
        "crossed0": "TEMA",
        "crossed1": "EMA",
        "crossed2": "DEMA",
        "crossed_timeframe0": 81,
        "crossed_timeframe1": 27,
        "crossed_timeframe2": 63,
        "real0": 0.5,
        "real1": 1.8,
        "real2": -1.4,
    }
    sell_params = {
        "sell_formula0": "A==R",
        "sell_formula1": "B/A>R",
        "sell_formula2": "A!=R",
        "sell_indicator0": "EMA",
        "sell_indicator1": "DEMA",
        "sell_indicator2": "TEMA",
        "sell_timeframe0": 21,
        "sell_timeframe1": 21,
        "sell_timeframe2": 3,
        "sell_crossed0": "SMA",
        "sell_crossed1": "TEMA",
        "sell_crossed2": "EMA",
        "sell_crossed_timeframe0": 27,
        "sell_crossed_timeframe1": 27,
        "sell_crossed_timeframe2": 3,
        "sell_real0": 1.5,
        "sell_real1": 1.4,
        "sell_real2": 1.6,
    }

    # ROI table:
    minimal_roi = {
        "0": 0.273,
        "26": 0.084,
        "79": 0.033,
        "187": 0
    }

    # Stoploss:
    stoploss = -0.19

    timeframe = '5m'
    # #################### END OF RESULT PLACE ####################

    ###############################################################
    # BUY HYPEROPTABLE PARAMS:
    formula0 = CategoricalParameter(
        formulas, default=formulas[0], optimize=0 < CONDITIONS, space='entry')
    formula1 = CategoricalParameter(
        formulas, default=formulas[0], optimize=1 < CONDITIONS, space='entry')
    formula2 = CategoricalParameter(
        formulas, default=formulas[0], optimize=2 < CONDITIONS, space='entry')
    formula3 = CategoricalParameter(
        formulas, default=formulas[0], optimize=3 < CONDITIONS, space='entry')
    formula4 = CategoricalParameter(
        formulas, default=formulas[0], optimize=4 < CONDITIONS, space='entry')
    formula5 = CategoricalParameter(
        formulas, default=formulas[0], optimize=5 < CONDITIONS, space='entry')
    formula6 = CategoricalParameter(
        formulas, default=formulas[0], optimize=6 < CONDITIONS, space='entry')
    formula7 = CategoricalParameter(
        formulas, default=formulas[0], optimize=7 < CONDITIONS, space='entry')
    formula8 = CategoricalParameter(
        formulas, default=formulas[0], optimize=8 < CONDITIONS, space='entry')
    formula9 = CategoricalParameter(
        formulas, default=formulas[0], optimize=9 < CONDITIONS, space='entry')
    formula10 = CategoricalParameter(
        formulas, default=formulas[0], optimize=10 < CONDITIONS, space='entry')
    formula11 = CategoricalParameter(
        formulas, default=formulas[0], optimize=11 < CONDITIONS, space='entry')
    formula12 = CategoricalParameter(
        formulas, default=formulas[0], optimize=12 < CONDITIONS, space='entry')
    formula13 = CategoricalParameter(
        formulas, default=formulas[0], optimize=13 < CONDITIONS, space='entry')
    formula14 = CategoricalParameter(
        formulas, default=formulas[0], optimize=14 < CONDITIONS, space='entry')
    formula15 = CategoricalParameter(
        formulas, default=formulas[0], optimize=15 < CONDITIONS, space='entry')
    formula16 = CategoricalParameter(
        formulas, default=formulas[0], optimize=16 < CONDITIONS, space='entry')
    formula17 = CategoricalParameter(
        formulas, default=formulas[0], optimize=17 < CONDITIONS, space='entry')
    formula18 = CategoricalParameter(
        formulas, default=formulas[0], optimize=18 < CONDITIONS, space='entry')
    formula19 = CategoricalParameter(
        formulas, default=formulas[0], optimize=19 < CONDITIONS, space='entry')
    formula20 = CategoricalParameter(
        formulas, default=formulas[0], optimize=20 < CONDITIONS, space='entry')
    formula21 = CategoricalParameter(
        formulas, default=formulas[0], optimize=21 < CONDITIONS, space='entry')
    formula22 = CategoricalParameter(
        formulas, default=formulas[0], optimize=22 < CONDITIONS, space='entry')
    formula23 = CategoricalParameter(
        formulas, default=formulas[0], optimize=23 < CONDITIONS, space='entry')
    formula24 = CategoricalParameter(
        formulas, default=formulas[0], optimize=24 < CONDITIONS, space='entry')
    formula25 = CategoricalParameter(
        formulas, default=formulas[0], optimize=25 < CONDITIONS, space='entry')
    formula26 = CategoricalParameter(
        formulas, default=formulas[0], optimize=26 < CONDITIONS, space='entry')
    formula27 = CategoricalParameter(
        formulas, default=formulas[0], optimize=27 < CONDITIONS, space='entry')
    formula28 = CategoricalParameter(
        formulas, default=formulas[0], optimize=28 < CONDITIONS, space='entry')
    formula29 = CategoricalParameter(
        formulas, default=formulas[0], optimize=29 < CONDITIONS, space='entry')
    formula30 = CategoricalParameter(
        formulas, default=formulas[0], optimize=30 < CONDITIONS, space='entry')
    formula31 = CategoricalParameter(
        formulas, default=formulas[0], optimize=31 < CONDITIONS, space='entry')
    formula32 = CategoricalParameter(
        formulas, default=formulas[0], optimize=32 < CONDITIONS, space='entry')
    formula33 = CategoricalParameter(
        formulas, default=formulas[0], optimize=33 < CONDITIONS, space='entry')
    formula34 = CategoricalParameter(
        formulas, default=formulas[0], optimize=34 < CONDITIONS, space='entry')
    formula35 = CategoricalParameter(
        formulas, default=formulas[0], optimize=35 < CONDITIONS, space='entry')
    formula36 = CategoricalParameter(
        formulas, default=formulas[0], optimize=36 < CONDITIONS, space='entry')
    formula37 = CategoricalParameter(
        formulas, default=formulas[0], optimize=37 < CONDITIONS, space='entry')
    formula38 = CategoricalParameter(
        formulas, default=formulas[0], optimize=38 < CONDITIONS, space='entry')
    formula39 = CategoricalParameter(
        formulas, default=formulas[0], optimize=39 < CONDITIONS, space='entry')
    formula40 = CategoricalParameter(
        formulas, default=formulas[0], optimize=40 < CONDITIONS, space='entry')
    formula41 = CategoricalParameter(
        formulas, default=formulas[0], optimize=41 < CONDITIONS, space='entry')
    formula42 = CategoricalParameter(
        formulas, default=formulas[0], optimize=42 < CONDITIONS, space='entry')
    formula43 = CategoricalParameter(
        formulas, default=formulas[0], optimize=43 < CONDITIONS, space='entry')
    formula44 = CategoricalParameter(
        formulas, default=formulas[0], optimize=44 < CONDITIONS, space='entry')
    formula45 = CategoricalParameter(
        formulas, default=formulas[0], optimize=45 < CONDITIONS, space='entry')
    formula46 = CategoricalParameter(
        formulas, default=formulas[0], optimize=46 < CONDITIONS, space='entry')
    formula47 = CategoricalParameter(
        formulas, default=formulas[0], optimize=47 < CONDITIONS, space='entry')
    formula48 = CategoricalParameter(
        formulas, default=formulas[0], optimize=48 < CONDITIONS, space='entry')
    formula49 = CategoricalParameter(
        formulas, default=formulas[0], optimize=49 < CONDITIONS, space='entry')
    formula50 = CategoricalParameter(
        formulas, default=formulas[0], optimize=50 < CONDITIONS, space='entry')
    formula51 = CategoricalParameter(
        formulas, default=formulas[0], optimize=51 < CONDITIONS, space='entry')
    formula52 = CategoricalParameter(
        formulas, default=formulas[0], optimize=52 < CONDITIONS, space='entry')
    formula53 = CategoricalParameter(
        formulas, default=formulas[0], optimize=53 < CONDITIONS, space='entry')
    formula54 = CategoricalParameter(
        formulas, default=formulas[0], optimize=54 < CONDITIONS, space='entry')
    formula55 = CategoricalParameter(
        formulas, default=formulas[0], optimize=55 < CONDITIONS, space='entry')
    formula56 = CategoricalParameter(
        formulas, default=formulas[0], optimize=56 < CONDITIONS, space='entry')
    formula57 = CategoricalParameter(
        formulas, default=formulas[0], optimize=57 < CONDITIONS, space='entry')
    formula58 = CategoricalParameter(
        formulas, default=formulas[0], optimize=58 < CONDITIONS, space='entry')
    formula59 = CategoricalParameter(
        formulas, default=formulas[0], optimize=59 < CONDITIONS, space='entry')
    formula60 = CategoricalParameter(
        formulas, default=formulas[0], optimize=60 < CONDITIONS, space='entry')
    formula61 = CategoricalParameter(
        formulas, default=formulas[0], optimize=61 < CONDITIONS, space='entry')
    formula62 = CategoricalParameter(
        formulas, default=formulas[0], optimize=62 < CONDITIONS, space='entry')
    formula63 = CategoricalParameter(
        formulas, default=formulas[0], optimize=63 < CONDITIONS, space='entry')
    formula64 = CategoricalParameter(
        formulas, default=formulas[0], optimize=64 < CONDITIONS, space='entry')
    formula65 = CategoricalParameter(
        formulas, default=formulas[0], optimize=65 < CONDITIONS, space='entry')
    formula66 = CategoricalParameter(
        formulas, default=formulas[0], optimize=66 < CONDITIONS, space='entry')
    formula67 = CategoricalParameter(
        formulas, default=formulas[0], optimize=67 < CONDITIONS, space='entry')
    formula68 = CategoricalParameter(
        formulas, default=formulas[0], optimize=68 < CONDITIONS, space='entry')
    formula69 = CategoricalParameter(
        formulas, default=formulas[0], optimize=69 < CONDITIONS, space='entry')
    formula70 = CategoricalParameter(
        formulas, default=formulas[0], optimize=70 < CONDITIONS, space='entry')
    formula71 = CategoricalParameter(
        formulas, default=formulas[0], optimize=71 < CONDITIONS, space='entry')
    formula72 = CategoricalParameter(
        formulas, default=formulas[0], optimize=72 < CONDITIONS, space='entry')
    formula73 = CategoricalParameter(
        formulas, default=formulas[0], optimize=73 < CONDITIONS, space='entry')
    formula74 = CategoricalParameter(
        formulas, default=formulas[0], optimize=74 < CONDITIONS, space='entry')
    formula75 = CategoricalParameter(
        formulas, default=formulas[0], optimize=75 < CONDITIONS, space='entry')
    formula76 = CategoricalParameter(
        formulas, default=formulas[0], optimize=76 < CONDITIONS, space='entry')
    formula77 = CategoricalParameter(
        formulas, default=formulas[0], optimize=77 < CONDITIONS, space='entry')
    formula78 = CategoricalParameter(
        formulas, default=formulas[0], optimize=78 < CONDITIONS, space='entry')
    formula79 = CategoricalParameter(
        formulas, default=formulas[0], optimize=79 < CONDITIONS, space='entry')
    formula80 = CategoricalParameter(
        formulas, default=formulas[0], optimize=80 < CONDITIONS, space='entry')
    formula81 = CategoricalParameter(
        formulas, default=formulas[0], optimize=81 < CONDITIONS, space='entry')
    formula82 = CategoricalParameter(
        formulas, default=formulas[0], optimize=82 < CONDITIONS, space='entry')
    formula83 = CategoricalParameter(
        formulas, default=formulas[0], optimize=83 < CONDITIONS, space='entry')
    formula84 = CategoricalParameter(
        formulas, default=formulas[0], optimize=84 < CONDITIONS, space='entry')
    formula85 = CategoricalParameter(
        formulas, default=formulas[0], optimize=85 < CONDITIONS, space='entry')
    formula86 = CategoricalParameter(
        formulas, default=formulas[0], optimize=86 < CONDITIONS, space='entry')
    formula87 = CategoricalParameter(
        formulas, default=formulas[0], optimize=87 < CONDITIONS, space='entry')
    formula88 = CategoricalParameter(
        formulas, default=formulas[0], optimize=88 < CONDITIONS, space='entry')
    formula89 = CategoricalParameter(
        formulas, default=formulas[0], optimize=89 < CONDITIONS, space='entry')
    formula90 = CategoricalParameter(
        formulas, default=formulas[0], optimize=90 < CONDITIONS, space='entry')
    formula91 = CategoricalParameter(
        formulas, default=formulas[0], optimize=91 < CONDITIONS, space='entry')
    formula92 = CategoricalParameter(
        formulas, default=formulas[0], optimize=92 < CONDITIONS, space='entry')
    formula93 = CategoricalParameter(
        formulas, default=formulas[0], optimize=93 < CONDITIONS, space='entry')
    formula94 = CategoricalParameter(
        formulas, default=formulas[0], optimize=94 < CONDITIONS, space='entry')
    formula95 = CategoricalParameter(
        formulas, default=formulas[0], optimize=95 < CONDITIONS, space='entry')
    formula96 = CategoricalParameter(
        formulas, default=formulas[0], optimize=96 < CONDITIONS, space='entry')
    formula97 = CategoricalParameter(
        formulas, default=formulas[0], optimize=97 < CONDITIONS, space='entry')
    formula98 = CategoricalParameter(
        formulas, default=formulas[0], optimize=98 < CONDITIONS, space='entry')
    formula99 = CategoricalParameter(
        formulas, default=formulas[0], optimize=99 < CONDITIONS, space='entry')

    indicator0 = CategoricalParameter(
        indicators, default=indicators[0], optimize=0 < CONDITIONS, space='entry')
    indicator1 = CategoricalParameter(
        indicators, default=indicators[0], optimize=1 < CONDITIONS, space='entry')
    indicator2 = CategoricalParameter(
        indicators, default=indicators[0], optimize=2 < CONDITIONS, space='entry')
    indicator3 = CategoricalParameter(
        indicators, default=indicators[0], optimize=3 < CONDITIONS, space='entry')
    indicator4 = CategoricalParameter(
        indicators, default=indicators[0], optimize=4 < CONDITIONS, space='entry')
    indicator5 = CategoricalParameter(
        indicators, default=indicators[0], optimize=5 < CONDITIONS, space='entry')
    indicator6 = CategoricalParameter(
        indicators, default=indicators[0], optimize=6 < CONDITIONS, space='entry')
    indicator7 = CategoricalParameter(
        indicators, default=indicators[0], optimize=7 < CONDITIONS, space='entry')
    indicator8 = CategoricalParameter(
        indicators, default=indicators[0], optimize=8 < CONDITIONS, space='entry')
    indicator9 = CategoricalParameter(
        indicators, default=indicators[0], optimize=9 < CONDITIONS, space='entry')
    indicator10 = CategoricalParameter(
        indicators, default=indicators[0], optimize=10 < CONDITIONS, space='entry')
    indicator11 = CategoricalParameter(
        indicators, default=indicators[0], optimize=11 < CONDITIONS, space='entry')
    indicator12 = CategoricalParameter(
        indicators, default=indicators[0], optimize=12 < CONDITIONS, space='entry')
    indicator13 = CategoricalParameter(
        indicators, default=indicators[0], optimize=13 < CONDITIONS, space='entry')
    indicator14 = CategoricalParameter(
        indicators, default=indicators[0], optimize=14 < CONDITIONS, space='entry')
    indicator15 = CategoricalParameter(
        indicators, default=indicators[0], optimize=15 < CONDITIONS, space='entry')
    indicator16 = CategoricalParameter(
        indicators, default=indicators[0], optimize=16 < CONDITIONS, space='entry')
    indicator17 = CategoricalParameter(
        indicators, default=indicators[0], optimize=17 < CONDITIONS, space='entry')
    indicator18 = CategoricalParameter(
        indicators, default=indicators[0], optimize=18 < CONDITIONS, space='entry')
    indicator19 = CategoricalParameter(
        indicators, default=indicators[0], optimize=19 < CONDITIONS, space='entry')
    indicator20 = CategoricalParameter(
        indicators, default=indicators[0], optimize=20 < CONDITIONS, space='entry')
    indicator21 = CategoricalParameter(
        indicators, default=indicators[0], optimize=21 < CONDITIONS, space='entry')
    indicator22 = CategoricalParameter(
        indicators, default=indicators[0], optimize=22 < CONDITIONS, space='entry')
    indicator23 = CategoricalParameter(
        indicators, default=indicators[0], optimize=23 < CONDITIONS, space='entry')
    indicator24 = CategoricalParameter(
        indicators, default=indicators[0], optimize=24 < CONDITIONS, space='entry')
    indicator25 = CategoricalParameter(
        indicators, default=indicators[0], optimize=25 < CONDITIONS, space='entry')
    indicator26 = CategoricalParameter(
        indicators, default=indicators[0], optimize=26 < CONDITIONS, space='entry')
    indicator27 = CategoricalParameter(
        indicators, default=indicators[0], optimize=27 < CONDITIONS, space='entry')
    indicator28 = CategoricalParameter(
        indicators, default=indicators[0], optimize=28 < CONDITIONS, space='entry')
    indicator29 = CategoricalParameter(
        indicators, default=indicators[0], optimize=29 < CONDITIONS, space='entry')
    indicator30 = CategoricalParameter(
        indicators, default=indicators[0], optimize=30 < CONDITIONS, space='entry')
    indicator31 = CategoricalParameter(
        indicators, default=indicators[0], optimize=31 < CONDITIONS, space='entry')
    indicator32 = CategoricalParameter(
        indicators, default=indicators[0], optimize=32 < CONDITIONS, space='entry')
    indicator33 = CategoricalParameter(
        indicators, default=indicators[0], optimize=33 < CONDITIONS, space='entry')
    indicator34 = CategoricalParameter(
        indicators, default=indicators[0], optimize=34 < CONDITIONS, space='entry')
    indicator35 = CategoricalParameter(
        indicators, default=indicators[0], optimize=35 < CONDITIONS, space='entry')
    indicator36 = CategoricalParameter(
        indicators, default=indicators[0], optimize=36 < CONDITIONS, space='entry')
    indicator37 = CategoricalParameter(
        indicators, default=indicators[0], optimize=37 < CONDITIONS, space='entry')
    indicator38 = CategoricalParameter(
        indicators, default=indicators[0], optimize=38 < CONDITIONS, space='entry')
    indicator39 = CategoricalParameter(
        indicators, default=indicators[0], optimize=39 < CONDITIONS, space='entry')
    indicator40 = CategoricalParameter(
        indicators, default=indicators[0], optimize=40 < CONDITIONS, space='entry')
    indicator41 = CategoricalParameter(
        indicators, default=indicators[0], optimize=41 < CONDITIONS, space='entry')
    indicator42 = CategoricalParameter(
        indicators, default=indicators[0], optimize=42 < CONDITIONS, space='entry')
    indicator43 = CategoricalParameter(
        indicators, default=indicators[0], optimize=43 < CONDITIONS, space='entry')
    indicator44 = CategoricalParameter(
        indicators, default=indicators[0], optimize=44 < CONDITIONS, space='entry')
    indicator45 = CategoricalParameter(
        indicators, default=indicators[0], optimize=45 < CONDITIONS, space='entry')
    indicator46 = CategoricalParameter(
        indicators, default=indicators[0], optimize=46 < CONDITIONS, space='entry')
    indicator47 = CategoricalParameter(
        indicators, default=indicators[0], optimize=47 < CONDITIONS, space='entry')
    indicator48 = CategoricalParameter(
        indicators, default=indicators[0], optimize=48 < CONDITIONS, space='entry')
    indicator49 = CategoricalParameter(
        indicators, default=indicators[0], optimize=49 < CONDITIONS, space='entry')
    indicator50 = CategoricalParameter(
        indicators, default=indicators[0], optimize=50 < CONDITIONS, space='entry')
    indicator51 = CategoricalParameter(
        indicators, default=indicators[0], optimize=51 < CONDITIONS, space='entry')
    indicator52 = CategoricalParameter(
        indicators, default=indicators[0], optimize=52 < CONDITIONS, space='entry')
    indicator53 = CategoricalParameter(
        indicators, default=indicators[0], optimize=53 < CONDITIONS, space='entry')
    indicator54 = CategoricalParameter(
        indicators, default=indicators[0], optimize=54 < CONDITIONS, space='entry')
    indicator55 = CategoricalParameter(
        indicators, default=indicators[0], optimize=55 < CONDITIONS, space='entry')
    indicator56 = CategoricalParameter(
        indicators, default=indicators[0], optimize=56 < CONDITIONS, space='entry')
    indicator57 = CategoricalParameter(
        indicators, default=indicators[0], optimize=57 < CONDITIONS, space='entry')
    indicator58 = CategoricalParameter(
        indicators, default=indicators[0], optimize=58 < CONDITIONS, space='entry')
    indicator59 = CategoricalParameter(
        indicators, default=indicators[0], optimize=59 < CONDITIONS, space='entry')
    indicator60 = CategoricalParameter(
        indicators, default=indicators[0], optimize=60 < CONDITIONS, space='entry')
    indicator61 = CategoricalParameter(
        indicators, default=indicators[0], optimize=61 < CONDITIONS, space='entry')
    indicator62 = CategoricalParameter(
        indicators, default=indicators[0], optimize=62 < CONDITIONS, space='entry')
    indicator63 = CategoricalParameter(
        indicators, default=indicators[0], optimize=63 < CONDITIONS, space='entry')
    indicator64 = CategoricalParameter(
        indicators, default=indicators[0], optimize=64 < CONDITIONS, space='entry')
    indicator65 = CategoricalParameter(
        indicators, default=indicators[0], optimize=65 < CONDITIONS, space='entry')
    indicator66 = CategoricalParameter(
        indicators, default=indicators[0], optimize=66 < CONDITIONS, space='entry')
    indicator67 = CategoricalParameter(
        indicators, default=indicators[0], optimize=67 < CONDITIONS, space='entry')
    indicator68 = CategoricalParameter(
        indicators, default=indicators[0], optimize=68 < CONDITIONS, space='entry')
    indicator69 = CategoricalParameter(
        indicators, default=indicators[0], optimize=69 < CONDITIONS, space='entry')
    indicator70 = CategoricalParameter(
        indicators, default=indicators[0], optimize=70 < CONDITIONS, space='entry')
    indicator71 = CategoricalParameter(
        indicators, default=indicators[0], optimize=71 < CONDITIONS, space='entry')
    indicator72 = CategoricalParameter(
        indicators, default=indicators[0], optimize=72 < CONDITIONS, space='entry')
    indicator73 = CategoricalParameter(
        indicators, default=indicators[0], optimize=73 < CONDITIONS, space='entry')
    indicator74 = CategoricalParameter(
        indicators, default=indicators[0], optimize=74 < CONDITIONS, space='entry')
    indicator75 = CategoricalParameter(
        indicators, default=indicators[0], optimize=75 < CONDITIONS, space='entry')
    indicator76 = CategoricalParameter(
        indicators, default=indicators[0], optimize=76 < CONDITIONS, space='entry')
    indicator77 = CategoricalParameter(
        indicators, default=indicators[0], optimize=77 < CONDITIONS, space='entry')
    indicator78 = CategoricalParameter(
        indicators, default=indicators[0], optimize=78 < CONDITIONS, space='entry')
    indicator79 = CategoricalParameter(
        indicators, default=indicators[0], optimize=79 < CONDITIONS, space='entry')
    indicator80 = CategoricalParameter(
        indicators, default=indicators[0], optimize=80 < CONDITIONS, space='entry')
    indicator81 = CategoricalParameter(
        indicators, default=indicators[0], optimize=81 < CONDITIONS, space='entry')
    indicator82 = CategoricalParameter(
        indicators, default=indicators[0], optimize=82 < CONDITIONS, space='entry')
    indicator83 = CategoricalParameter(
        indicators, default=indicators[0], optimize=83 < CONDITIONS, space='entry')
    indicator84 = CategoricalParameter(
        indicators, default=indicators[0], optimize=84 < CONDITIONS, space='entry')
    indicator85 = CategoricalParameter(
        indicators, default=indicators[0], optimize=85 < CONDITIONS, space='entry')
    indicator86 = CategoricalParameter(
        indicators, default=indicators[0], optimize=86 < CONDITIONS, space='entry')
    indicator87 = CategoricalParameter(
        indicators, default=indicators[0], optimize=87 < CONDITIONS, space='entry')
    indicator88 = CategoricalParameter(
        indicators, default=indicators[0], optimize=88 < CONDITIONS, space='entry')
    indicator89 = CategoricalParameter(
        indicators, default=indicators[0], optimize=89 < CONDITIONS, space='entry')
    indicator90 = CategoricalParameter(
        indicators, default=indicators[0], optimize=90 < CONDITIONS, space='entry')
    indicator91 = CategoricalParameter(
        indicators, default=indicators[0], optimize=91 < CONDITIONS, space='entry')
    indicator92 = CategoricalParameter(
        indicators, default=indicators[0], optimize=92 < CONDITIONS, space='entry')
    indicator93 = CategoricalParameter(
        indicators, default=indicators[0], optimize=93 < CONDITIONS, space='entry')
    indicator94 = CategoricalParameter(
        indicators, default=indicators[0], optimize=94 < CONDITIONS, space='entry')
    indicator95 = CategoricalParameter(
        indicators, default=indicators[0], optimize=95 < CONDITIONS, space='entry')
    indicator96 = CategoricalParameter(
        indicators, default=indicators[0], optimize=96 < CONDITIONS, space='entry')
    indicator97 = CategoricalParameter(
        indicators, default=indicators[0], optimize=97 < CONDITIONS, space='entry')
    indicator98 = CategoricalParameter(
        indicators, default=indicators[0], optimize=98 < CONDITIONS, space='entry')
    indicator99 = CategoricalParameter(
        indicators, default=indicators[0], optimize=99 < CONDITIONS, space='entry')

    crossed0 = CategoricalParameter(
        indicators, default=indicators[0], optimize=0 < CONDITIONS, space='entry')
    crossed1 = CategoricalParameter(
        indicators, default=indicators[0], optimize=1 < CONDITIONS, space='entry')
    crossed2 = CategoricalParameter(
        indicators, default=indicators[0], optimize=2 < CONDITIONS, space='entry')
    crossed3 = CategoricalParameter(
        indicators, default=indicators[0], optimize=3 < CONDITIONS, space='entry')
    crossed4 = CategoricalParameter(
        indicators, default=indicators[0], optimize=4 < CONDITIONS, space='entry')
    crossed5 = CategoricalParameter(
        indicators, default=indicators[0], optimize=5 < CONDITIONS, space='entry')
    crossed6 = CategoricalParameter(
        indicators, default=indicators[0], optimize=6 < CONDITIONS, space='entry')
    crossed7 = CategoricalParameter(
        indicators, default=indicators[0], optimize=7 < CONDITIONS, space='entry')
    crossed8 = CategoricalParameter(
        indicators, default=indicators[0], optimize=8 < CONDITIONS, space='entry')
    crossed9 = CategoricalParameter(
        indicators, default=indicators[0], optimize=9 < CONDITIONS, space='entry')
    crossed10 = CategoricalParameter(
        indicators, default=indicators[0], optimize=10 < CONDITIONS, space='entry')
    crossed11 = CategoricalParameter(
        indicators, default=indicators[0], optimize=11 < CONDITIONS, space='entry')
    crossed12 = CategoricalParameter(
        indicators, default=indicators[0], optimize=12 < CONDITIONS, space='entry')
    crossed13 = CategoricalParameter(
        indicators, default=indicators[0], optimize=13 < CONDITIONS, space='entry')
    crossed14 = CategoricalParameter(
        indicators, default=indicators[0], optimize=14 < CONDITIONS, space='entry')
    crossed15 = CategoricalParameter(
        indicators, default=indicators[0], optimize=15 < CONDITIONS, space='entry')
    crossed16 = CategoricalParameter(
        indicators, default=indicators[0], optimize=16 < CONDITIONS, space='entry')
    crossed17 = CategoricalParameter(
        indicators, default=indicators[0], optimize=17 < CONDITIONS, space='entry')
    crossed18 = CategoricalParameter(
        indicators, default=indicators[0], optimize=18 < CONDITIONS, space='entry')
    crossed19 = CategoricalParameter(
        indicators, default=indicators[0], optimize=19 < CONDITIONS, space='entry')
    crossed20 = CategoricalParameter(
        indicators, default=indicators[0], optimize=20 < CONDITIONS, space='entry')
    crossed21 = CategoricalParameter(
        indicators, default=indicators[0], optimize=21 < CONDITIONS, space='entry')
    crossed22 = CategoricalParameter(
        indicators, default=indicators[0], optimize=22 < CONDITIONS, space='entry')
    crossed23 = CategoricalParameter(
        indicators, default=indicators[0], optimize=23 < CONDITIONS, space='entry')
    crossed24 = CategoricalParameter(
        indicators, default=indicators[0], optimize=24 < CONDITIONS, space='entry')
    crossed25 = CategoricalParameter(
        indicators, default=indicators[0], optimize=25 < CONDITIONS, space='entry')
    crossed26 = CategoricalParameter(
        indicators, default=indicators[0], optimize=26 < CONDITIONS, space='entry')
    crossed27 = CategoricalParameter(
        indicators, default=indicators[0], optimize=27 < CONDITIONS, space='entry')
    crossed28 = CategoricalParameter(
        indicators, default=indicators[0], optimize=28 < CONDITIONS, space='entry')
    crossed29 = CategoricalParameter(
        indicators, default=indicators[0], optimize=29 < CONDITIONS, space='entry')
    crossed30 = CategoricalParameter(
        indicators, default=indicators[0], optimize=30 < CONDITIONS, space='entry')
    crossed31 = CategoricalParameter(
        indicators, default=indicators[0], optimize=31 < CONDITIONS, space='entry')
    crossed32 = CategoricalParameter(
        indicators, default=indicators[0], optimize=32 < CONDITIONS, space='entry')
    crossed33 = CategoricalParameter(
        indicators, default=indicators[0], optimize=33 < CONDITIONS, space='entry')
    crossed34 = CategoricalParameter(
        indicators, default=indicators[0], optimize=34 < CONDITIONS, space='entry')
    crossed35 = CategoricalParameter(
        indicators, default=indicators[0], optimize=35 < CONDITIONS, space='entry')
    crossed36 = CategoricalParameter(
        indicators, default=indicators[0], optimize=36 < CONDITIONS, space='entry')
    crossed37 = CategoricalParameter(
        indicators, default=indicators[0], optimize=37 < CONDITIONS, space='entry')
    crossed38 = CategoricalParameter(
        indicators, default=indicators[0], optimize=38 < CONDITIONS, space='entry')
    crossed39 = CategoricalParameter(
        indicators, default=indicators[0], optimize=39 < CONDITIONS, space='entry')
    crossed40 = CategoricalParameter(
        indicators, default=indicators[0], optimize=40 < CONDITIONS, space='entry')
    crossed41 = CategoricalParameter(
        indicators, default=indicators[0], optimize=41 < CONDITIONS, space='entry')
    crossed42 = CategoricalParameter(
        indicators, default=indicators[0], optimize=42 < CONDITIONS, space='entry')
    crossed43 = CategoricalParameter(
        indicators, default=indicators[0], optimize=43 < CONDITIONS, space='entry')
    crossed44 = CategoricalParameter(
        indicators, default=indicators[0], optimize=44 < CONDITIONS, space='entry')
    crossed45 = CategoricalParameter(
        indicators, default=indicators[0], optimize=45 < CONDITIONS, space='entry')
    crossed46 = CategoricalParameter(
        indicators, default=indicators[0], optimize=46 < CONDITIONS, space='entry')
    crossed47 = CategoricalParameter(
        indicators, default=indicators[0], optimize=47 < CONDITIONS, space='entry')
    crossed48 = CategoricalParameter(
        indicators, default=indicators[0], optimize=48 < CONDITIONS, space='entry')
    crossed49 = CategoricalParameter(
        indicators, default=indicators[0], optimize=49 < CONDITIONS, space='entry')
    crossed50 = CategoricalParameter(
        indicators, default=indicators[0], optimize=50 < CONDITIONS, space='entry')
    crossed51 = CategoricalParameter(
        indicators, default=indicators[0], optimize=51 < CONDITIONS, space='entry')
    crossed52 = CategoricalParameter(
        indicators, default=indicators[0], optimize=52 < CONDITIONS, space='entry')
    crossed53 = CategoricalParameter(
        indicators, default=indicators[0], optimize=53 < CONDITIONS, space='entry')
    crossed54 = CategoricalParameter(
        indicators, default=indicators[0], optimize=54 < CONDITIONS, space='entry')
    crossed55 = CategoricalParameter(
        indicators, default=indicators[0], optimize=55 < CONDITIONS, space='entry')
    crossed56 = CategoricalParameter(
        indicators, default=indicators[0], optimize=56 < CONDITIONS, space='entry')
    crossed57 = CategoricalParameter(
        indicators, default=indicators[0], optimize=57 < CONDITIONS, space='entry')
    crossed58 = CategoricalParameter(
        indicators, default=indicators[0], optimize=58 < CONDITIONS, space='entry')
    crossed59 = CategoricalParameter(
        indicators, default=indicators[0], optimize=59 < CONDITIONS, space='entry')
    crossed60 = CategoricalParameter(
        indicators, default=indicators[0], optimize=60 < CONDITIONS, space='entry')
    crossed61 = CategoricalParameter(
        indicators, default=indicators[0], optimize=61 < CONDITIONS, space='entry')
    crossed62 = CategoricalParameter(
        indicators, default=indicators[0], optimize=62 < CONDITIONS, space='entry')
    crossed63 = CategoricalParameter(
        indicators, default=indicators[0], optimize=63 < CONDITIONS, space='entry')
    crossed64 = CategoricalParameter(
        indicators, default=indicators[0], optimize=64 < CONDITIONS, space='entry')
    crossed65 = CategoricalParameter(
        indicators, default=indicators[0], optimize=65 < CONDITIONS, space='entry')
    crossed66 = CategoricalParameter(
        indicators, default=indicators[0], optimize=66 < CONDITIONS, space='entry')
    crossed67 = CategoricalParameter(
        indicators, default=indicators[0], optimize=67 < CONDITIONS, space='entry')
    crossed68 = CategoricalParameter(
        indicators, default=indicators[0], optimize=68 < CONDITIONS, space='entry')
    crossed69 = CategoricalParameter(
        indicators, default=indicators[0], optimize=69 < CONDITIONS, space='entry')
    crossed70 = CategoricalParameter(
        indicators, default=indicators[0], optimize=70 < CONDITIONS, space='entry')
    crossed71 = CategoricalParameter(
        indicators, default=indicators[0], optimize=71 < CONDITIONS, space='entry')
    crossed72 = CategoricalParameter(
        indicators, default=indicators[0], optimize=72 < CONDITIONS, space='entry')
    crossed73 = CategoricalParameter(
        indicators, default=indicators[0], optimize=73 < CONDITIONS, space='entry')
    crossed74 = CategoricalParameter(
        indicators, default=indicators[0], optimize=74 < CONDITIONS, space='entry')
    crossed75 = CategoricalParameter(
        indicators, default=indicators[0], optimize=75 < CONDITIONS, space='entry')
    crossed76 = CategoricalParameter(
        indicators, default=indicators[0], optimize=76 < CONDITIONS, space='entry')
    crossed77 = CategoricalParameter(
        indicators, default=indicators[0], optimize=77 < CONDITIONS, space='entry')
    crossed78 = CategoricalParameter(
        indicators, default=indicators[0], optimize=78 < CONDITIONS, space='entry')
    crossed79 = CategoricalParameter(
        indicators, default=indicators[0], optimize=79 < CONDITIONS, space='entry')
    crossed80 = CategoricalParameter(
        indicators, default=indicators[0], optimize=80 < CONDITIONS, space='entry')
    crossed81 = CategoricalParameter(
        indicators, default=indicators[0], optimize=81 < CONDITIONS, space='entry')
    crossed82 = CategoricalParameter(
        indicators, default=indicators[0], optimize=82 < CONDITIONS, space='entry')
    crossed83 = CategoricalParameter(
        indicators, default=indicators[0], optimize=83 < CONDITIONS, space='entry')
    crossed84 = CategoricalParameter(
        indicators, default=indicators[0], optimize=84 < CONDITIONS, space='entry')
    crossed85 = CategoricalParameter(
        indicators, default=indicators[0], optimize=85 < CONDITIONS, space='entry')
    crossed86 = CategoricalParameter(
        indicators, default=indicators[0], optimize=86 < CONDITIONS, space='entry')
    crossed87 = CategoricalParameter(
        indicators, default=indicators[0], optimize=87 < CONDITIONS, space='entry')
    crossed88 = CategoricalParameter(
        indicators, default=indicators[0], optimize=88 < CONDITIONS, space='entry')
    crossed89 = CategoricalParameter(
        indicators, default=indicators[0], optimize=89 < CONDITIONS, space='entry')
    crossed90 = CategoricalParameter(
        indicators, default=indicators[0], optimize=90 < CONDITIONS, space='entry')
    crossed91 = CategoricalParameter(
        indicators, default=indicators[0], optimize=91 < CONDITIONS, space='entry')
    crossed92 = CategoricalParameter(
        indicators, default=indicators[0], optimize=92 < CONDITIONS, space='entry')
    crossed93 = CategoricalParameter(
        indicators, default=indicators[0], optimize=93 < CONDITIONS, space='entry')
    crossed94 = CategoricalParameter(
        indicators, default=indicators[0], optimize=94 < CONDITIONS, space='entry')
    crossed95 = CategoricalParameter(
        indicators, default=indicators[0], optimize=95 < CONDITIONS, space='entry')
    crossed96 = CategoricalParameter(
        indicators, default=indicators[0], optimize=96 < CONDITIONS, space='entry')
    crossed97 = CategoricalParameter(
        indicators, default=indicators[0], optimize=97 < CONDITIONS, space='entry')
    crossed98 = CategoricalParameter(
        indicators, default=indicators[0], optimize=98 < CONDITIONS, space='entry')
    crossed99 = CategoricalParameter(
        indicators, default=indicators[0], optimize=99 < CONDITIONS, space='entry')

    timeframe0 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=0 < CONDITIONS, space='entry')
    timeframe1 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=1 < CONDITIONS, space='entry')
    timeframe2 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=2 < CONDITIONS, space='entry')
    timeframe3 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=3 < CONDITIONS, space='entry')
    timeframe4 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=4 < CONDITIONS, space='entry')
    timeframe5 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=5 < CONDITIONS, space='entry')
    timeframe6 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=6 < CONDITIONS, space='entry')
    timeframe7 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=7 < CONDITIONS, space='entry')
    timeframe8 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=8 < CONDITIONS, space='entry')
    timeframe9 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=9 < CONDITIONS, space='entry')
    timeframe10 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=10 < CONDITIONS, space='entry')
    timeframe11 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=11 < CONDITIONS, space='entry')
    timeframe12 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=12 < CONDITIONS, space='entry')
    timeframe13 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=13 < CONDITIONS, space='entry')
    timeframe14 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=14 < CONDITIONS, space='entry')
    timeframe15 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=15 < CONDITIONS, space='entry')
    timeframe16 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=16 < CONDITIONS, space='entry')
    timeframe17 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=17 < CONDITIONS, space='entry')
    timeframe18 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=18 < CONDITIONS, space='entry')
    timeframe19 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=19 < CONDITIONS, space='entry')
    timeframe20 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=20 < CONDITIONS, space='entry')
    timeframe21 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=21 < CONDITIONS, space='entry')
    timeframe22 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=22 < CONDITIONS, space='entry')
    timeframe23 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=23 < CONDITIONS, space='entry')
    timeframe24 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=24 < CONDITIONS, space='entry')
    timeframe25 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=25 < CONDITIONS, space='entry')
    timeframe26 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=26 < CONDITIONS, space='entry')
    timeframe27 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=27 < CONDITIONS, space='entry')
    timeframe28 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=28 < CONDITIONS, space='entry')
    timeframe29 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=29 < CONDITIONS, space='entry')
    timeframe30 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=30 < CONDITIONS, space='entry')
    timeframe31 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=31 < CONDITIONS, space='entry')
    timeframe32 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=32 < CONDITIONS, space='entry')
    timeframe33 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=33 < CONDITIONS, space='entry')
    timeframe34 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=34 < CONDITIONS, space='entry')
    timeframe35 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=35 < CONDITIONS, space='entry')
    timeframe36 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=36 < CONDITIONS, space='entry')
    timeframe37 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=37 < CONDITIONS, space='entry')
    timeframe38 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=38 < CONDITIONS, space='entry')
    timeframe39 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=39 < CONDITIONS, space='entry')
    timeframe40 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=40 < CONDITIONS, space='entry')
    timeframe41 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=41 < CONDITIONS, space='entry')
    timeframe42 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=42 < CONDITIONS, space='entry')
    timeframe43 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=43 < CONDITIONS, space='entry')
    timeframe44 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=44 < CONDITIONS, space='entry')
    timeframe45 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=45 < CONDITIONS, space='entry')
    timeframe46 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=46 < CONDITIONS, space='entry')
    timeframe47 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=47 < CONDITIONS, space='entry')
    timeframe48 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=48 < CONDITIONS, space='entry')
    timeframe49 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=49 < CONDITIONS, space='entry')
    timeframe50 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=50 < CONDITIONS, space='entry')
    timeframe51 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=51 < CONDITIONS, space='entry')
    timeframe52 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=52 < CONDITIONS, space='entry')
    timeframe53 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=53 < CONDITIONS, space='entry')
    timeframe54 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=54 < CONDITIONS, space='entry')
    timeframe55 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=55 < CONDITIONS, space='entry')
    timeframe56 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=56 < CONDITIONS, space='entry')
    timeframe57 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=57 < CONDITIONS, space='entry')
    timeframe58 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=58 < CONDITIONS, space='entry')
    timeframe59 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=59 < CONDITIONS, space='entry')
    timeframe60 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=60 < CONDITIONS, space='entry')
    timeframe61 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=61 < CONDITIONS, space='entry')
    timeframe62 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=62 < CONDITIONS, space='entry')
    timeframe63 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=63 < CONDITIONS, space='entry')
    timeframe64 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=64 < CONDITIONS, space='entry')
    timeframe65 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=65 < CONDITIONS, space='entry')
    timeframe66 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=66 < CONDITIONS, space='entry')
    timeframe67 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=67 < CONDITIONS, space='entry')
    timeframe68 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=68 < CONDITIONS, space='entry')
    timeframe69 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=69 < CONDITIONS, space='entry')
    timeframe70 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=70 < CONDITIONS, space='entry')
    timeframe71 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=71 < CONDITIONS, space='entry')
    timeframe72 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=72 < CONDITIONS, space='entry')
    timeframe73 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=73 < CONDITIONS, space='entry')
    timeframe74 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=74 < CONDITIONS, space='entry')
    timeframe75 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=75 < CONDITIONS, space='entry')
    timeframe76 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=76 < CONDITIONS, space='entry')
    timeframe77 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=77 < CONDITIONS, space='entry')
    timeframe78 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=78 < CONDITIONS, space='entry')
    timeframe79 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=79 < CONDITIONS, space='entry')
    timeframe80 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=80 < CONDITIONS, space='entry')
    timeframe81 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=81 < CONDITIONS, space='entry')
    timeframe82 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=82 < CONDITIONS, space='entry')
    timeframe83 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=83 < CONDITIONS, space='entry')
    timeframe84 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=84 < CONDITIONS, space='entry')
    timeframe85 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=85 < CONDITIONS, space='entry')
    timeframe86 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=86 < CONDITIONS, space='entry')
    timeframe87 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=87 < CONDITIONS, space='entry')
    timeframe88 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=88 < CONDITIONS, space='entry')
    timeframe89 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=89 < CONDITIONS, space='entry')
    timeframe90 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=90 < CONDITIONS, space='entry')
    timeframe91 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=91 < CONDITIONS, space='entry')
    timeframe92 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=92 < CONDITIONS, space='entry')
    timeframe93 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=93 < CONDITIONS, space='entry')
    timeframe94 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=94 < CONDITIONS, space='entry')
    timeframe95 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=95 < CONDITIONS, space='entry')
    timeframe96 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=96 < CONDITIONS, space='entry')
    timeframe97 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=97 < CONDITIONS, space='entry')
    timeframe98 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=98 < CONDITIONS, space='entry')
    timeframe99 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=99 < CONDITIONS, space='entry')

    crossed_timeframe0 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=0 < CONDITIONS, space='entry')
    crossed_timeframe1 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=1 < CONDITIONS, space='entry')
    crossed_timeframe2 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=2 < CONDITIONS, space='entry')
    crossed_timeframe3 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=3 < CONDITIONS, space='entry')
    crossed_timeframe4 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=4 < CONDITIONS, space='entry')
    crossed_timeframe5 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=5 < CONDITIONS, space='entry')
    crossed_timeframe6 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=6 < CONDITIONS, space='entry')
    crossed_timeframe7 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=7 < CONDITIONS, space='entry')
    crossed_timeframe8 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=8 < CONDITIONS, space='entry')
    crossed_timeframe9 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=9 < CONDITIONS, space='entry')
    crossed_timeframe10 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=10 < CONDITIONS, space='entry')
    crossed_timeframe11 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=11 < CONDITIONS, space='entry')
    crossed_timeframe12 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=12 < CONDITIONS, space='entry')
    crossed_timeframe13 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=13 < CONDITIONS, space='entry')
    crossed_timeframe14 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=14 < CONDITIONS, space='entry')
    crossed_timeframe15 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=15 < CONDITIONS, space='entry')
    crossed_timeframe16 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=16 < CONDITIONS, space='entry')
    crossed_timeframe17 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=17 < CONDITIONS, space='entry')
    crossed_timeframe18 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=18 < CONDITIONS, space='entry')
    crossed_timeframe19 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=19 < CONDITIONS, space='entry')
    crossed_timeframe20 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=20 < CONDITIONS, space='entry')
    crossed_timeframe21 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=21 < CONDITIONS, space='entry')
    crossed_timeframe22 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=22 < CONDITIONS, space='entry')
    crossed_timeframe23 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=23 < CONDITIONS, space='entry')
    crossed_timeframe24 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=24 < CONDITIONS, space='entry')
    crossed_timeframe25 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=25 < CONDITIONS, space='entry')
    crossed_timeframe26 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=26 < CONDITIONS, space='entry')
    crossed_timeframe27 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=27 < CONDITIONS, space='entry')
    crossed_timeframe28 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=28 < CONDITIONS, space='entry')
    crossed_timeframe29 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=29 < CONDITIONS, space='entry')
    crossed_timeframe30 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=30 < CONDITIONS, space='entry')
    crossed_timeframe31 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=31 < CONDITIONS, space='entry')
    crossed_timeframe32 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=32 < CONDITIONS, space='entry')
    crossed_timeframe33 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=33 < CONDITIONS, space='entry')
    crossed_timeframe34 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=34 < CONDITIONS, space='entry')
    crossed_timeframe35 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=35 < CONDITIONS, space='entry')
    crossed_timeframe36 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=36 < CONDITIONS, space='entry')
    crossed_timeframe37 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=37 < CONDITIONS, space='entry')
    crossed_timeframe38 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=38 < CONDITIONS, space='entry')
    crossed_timeframe39 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=39 < CONDITIONS, space='entry')
    crossed_timeframe40 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=40 < CONDITIONS, space='entry')
    crossed_timeframe41 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=41 < CONDITIONS, space='entry')
    crossed_timeframe42 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=42 < CONDITIONS, space='entry')
    crossed_timeframe43 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=43 < CONDITIONS, space='entry')
    crossed_timeframe44 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=44 < CONDITIONS, space='entry')
    crossed_timeframe45 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=45 < CONDITIONS, space='entry')
    crossed_timeframe46 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=46 < CONDITIONS, space='entry')
    crossed_timeframe47 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=47 < CONDITIONS, space='entry')
    crossed_timeframe48 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=48 < CONDITIONS, space='entry')
    crossed_timeframe49 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=49 < CONDITIONS, space='entry')
    crossed_timeframe50 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=50 < CONDITIONS, space='entry')
    crossed_timeframe51 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=51 < CONDITIONS, space='entry')
    crossed_timeframe52 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=52 < CONDITIONS, space='entry')
    crossed_timeframe53 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=53 < CONDITIONS, space='entry')
    crossed_timeframe54 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=54 < CONDITIONS, space='entry')
    crossed_timeframe55 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=55 < CONDITIONS, space='entry')
    crossed_timeframe56 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=56 < CONDITIONS, space='entry')
    crossed_timeframe57 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=57 < CONDITIONS, space='entry')
    crossed_timeframe58 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=58 < CONDITIONS, space='entry')
    crossed_timeframe59 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=59 < CONDITIONS, space='entry')
    crossed_timeframe60 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=60 < CONDITIONS, space='entry')
    crossed_timeframe61 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=61 < CONDITIONS, space='entry')
    crossed_timeframe62 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=62 < CONDITIONS, space='entry')
    crossed_timeframe63 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=63 < CONDITIONS, space='entry')
    crossed_timeframe64 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=64 < CONDITIONS, space='entry')
    crossed_timeframe65 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=65 < CONDITIONS, space='entry')
    crossed_timeframe66 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=66 < CONDITIONS, space='entry')
    crossed_timeframe67 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=67 < CONDITIONS, space='entry')
    crossed_timeframe68 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=68 < CONDITIONS, space='entry')
    crossed_timeframe69 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=69 < CONDITIONS, space='entry')
    crossed_timeframe70 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=70 < CONDITIONS, space='entry')
    crossed_timeframe71 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=71 < CONDITIONS, space='entry')
    crossed_timeframe72 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=72 < CONDITIONS, space='entry')
    crossed_timeframe73 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=73 < CONDITIONS, space='entry')
    crossed_timeframe74 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=74 < CONDITIONS, space='entry')
    crossed_timeframe75 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=75 < CONDITIONS, space='entry')
    crossed_timeframe76 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=76 < CONDITIONS, space='entry')
    crossed_timeframe77 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=77 < CONDITIONS, space='entry')
    crossed_timeframe78 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=78 < CONDITIONS, space='entry')
    crossed_timeframe79 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=79 < CONDITIONS, space='entry')
    crossed_timeframe80 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=80 < CONDITIONS, space='entry')
    crossed_timeframe81 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=81 < CONDITIONS, space='entry')
    crossed_timeframe82 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=82 < CONDITIONS, space='entry')
    crossed_timeframe83 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=83 < CONDITIONS, space='entry')
    crossed_timeframe84 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=84 < CONDITIONS, space='entry')
    crossed_timeframe85 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=85 < CONDITIONS, space='entry')
    crossed_timeframe86 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=86 < CONDITIONS, space='entry')
    crossed_timeframe87 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=87 < CONDITIONS, space='entry')
    crossed_timeframe88 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=88 < CONDITIONS, space='entry')
    crossed_timeframe89 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=89 < CONDITIONS, space='entry')
    crossed_timeframe90 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=90 < CONDITIONS, space='entry')
    crossed_timeframe91 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=91 < CONDITIONS, space='entry')
    crossed_timeframe92 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=92 < CONDITIONS, space='entry')
    crossed_timeframe93 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=93 < CONDITIONS, space='entry')
    crossed_timeframe94 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=94 < CONDITIONS, space='entry')
    crossed_timeframe95 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=95 < CONDITIONS, space='entry')
    crossed_timeframe96 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=96 < CONDITIONS, space='entry')
    crossed_timeframe97 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=97 < CONDITIONS, space='entry')
    crossed_timeframe98 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=98 < CONDITIONS, space='entry')
    crossed_timeframe99 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='entry')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=99 < CONDITIONS, space='entry')

    real0 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=0 < CONDITIONS, space='entry')
    real1 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=1 < CONDITIONS, space='entry')
    real2 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=2 < CONDITIONS, space='entry')
    real3 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=3 < CONDITIONS, space='entry')
    real4 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=4 < CONDITIONS, space='entry')
    real5 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=5 < CONDITIONS, space='entry')
    real6 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=6 < CONDITIONS, space='entry')
    real7 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=7 < CONDITIONS, space='entry')
    real8 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=8 < CONDITIONS, space='entry')
    real9 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                             decimals=DECIMALS, optimize=9 < CONDITIONS, space='entry')
    real10 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=10 < CONDITIONS, space='entry')
    real11 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=11 < CONDITIONS, space='entry')
    real12 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=12 < CONDITIONS, space='entry')
    real13 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=13 < CONDITIONS, space='entry')
    real14 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=14 < CONDITIONS, space='entry')
    real15 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=15 < CONDITIONS, space='entry')
    real16 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=16 < CONDITIONS, space='entry')
    real17 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=17 < CONDITIONS, space='entry')
    real18 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=18 < CONDITIONS, space='entry')
    real19 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=19 < CONDITIONS, space='entry')
    real20 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=20 < CONDITIONS, space='entry')
    real21 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=21 < CONDITIONS, space='entry')
    real22 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=22 < CONDITIONS, space='entry')
    real23 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=23 < CONDITIONS, space='entry')
    real24 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=24 < CONDITIONS, space='entry')
    real25 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=25 < CONDITIONS, space='entry')
    real26 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=26 < CONDITIONS, space='entry')
    real27 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=27 < CONDITIONS, space='entry')
    real28 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=28 < CONDITIONS, space='entry')
    real29 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=29 < CONDITIONS, space='entry')
    real30 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=30 < CONDITIONS, space='entry')
    real31 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=31 < CONDITIONS, space='entry')
    real32 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=32 < CONDITIONS, space='entry')
    real33 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=33 < CONDITIONS, space='entry')
    real34 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=34 < CONDITIONS, space='entry')
    real35 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=35 < CONDITIONS, space='entry')
    real36 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=36 < CONDITIONS, space='entry')
    real37 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=37 < CONDITIONS, space='entry')
    real38 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=38 < CONDITIONS, space='entry')
    real39 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=39 < CONDITIONS, space='entry')
    real40 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=40 < CONDITIONS, space='entry')
    real41 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=41 < CONDITIONS, space='entry')
    real42 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=42 < CONDITIONS, space='entry')
    real43 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=43 < CONDITIONS, space='entry')
    real44 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=44 < CONDITIONS, space='entry')
    real45 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=45 < CONDITIONS, space='entry')
    real46 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=46 < CONDITIONS, space='entry')
    real47 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=47 < CONDITIONS, space='entry')
    real48 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=48 < CONDITIONS, space='entry')
    real49 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=49 < CONDITIONS, space='entry')
    real50 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=50 < CONDITIONS, space='entry')
    real51 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=51 < CONDITIONS, space='entry')
    real52 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=52 < CONDITIONS, space='entry')
    real53 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=53 < CONDITIONS, space='entry')
    real54 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=54 < CONDITIONS, space='entry')
    real55 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=55 < CONDITIONS, space='entry')
    real56 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=56 < CONDITIONS, space='entry')
    real57 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=57 < CONDITIONS, space='entry')
    real58 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=58 < CONDITIONS, space='entry')
    real59 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=59 < CONDITIONS, space='entry')
    real60 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=60 < CONDITIONS, space='entry')
    real61 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=61 < CONDITIONS, space='entry')
    real62 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=62 < CONDITIONS, space='entry')
    real63 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=63 < CONDITIONS, space='entry')
    real64 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=64 < CONDITIONS, space='entry')
    real65 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=65 < CONDITIONS, space='entry')
    real66 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=66 < CONDITIONS, space='entry')
    real67 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=67 < CONDITIONS, space='entry')
    real68 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=68 < CONDITIONS, space='entry')
    real69 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=69 < CONDITIONS, space='entry')
    real70 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=70 < CONDITIONS, space='entry')
    real71 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=71 < CONDITIONS, space='entry')
    real72 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=72 < CONDITIONS, space='entry')
    real73 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=73 < CONDITIONS, space='entry')
    real74 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=74 < CONDITIONS, space='entry')
    real75 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=75 < CONDITIONS, space='entry')
    real76 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=76 < CONDITIONS, space='entry')
    real77 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=77 < CONDITIONS, space='entry')
    real78 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=78 < CONDITIONS, space='entry')
    real79 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=79 < CONDITIONS, space='entry')
    real80 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=80 < CONDITIONS, space='entry')
    real81 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=81 < CONDITIONS, space='entry')
    real82 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=82 < CONDITIONS, space='entry')
    real83 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=83 < CONDITIONS, space='entry')
    real84 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=84 < CONDITIONS, space='entry')
    real85 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=85 < CONDITIONS, space='entry')
    real86 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=86 < CONDITIONS, space='entry')
    real87 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=87 < CONDITIONS, space='entry')
    real88 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=88 < CONDITIONS, space='entry')
    real89 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=89 < CONDITIONS, space='entry')
    real90 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=90 < CONDITIONS, space='entry')
    real91 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=91 < CONDITIONS, space='entry')
    real92 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=92 < CONDITIONS, space='entry')
    real93 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=93 < CONDITIONS, space='entry')
    real94 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=94 < CONDITIONS, space='entry')
    real95 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=95 < CONDITIONS, space='entry')
    real96 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=96 < CONDITIONS, space='entry')
    real97 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=97 < CONDITIONS, space='entry')
    real98 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=98 < CONDITIONS, space='entry')
    real99 = DecimalParameter(reals[0], reals[-1], default=reals[0],
                              decimals=DECIMALS, optimize=99 < CONDITIONS, space='entry')

    # SELL HYPEROPTABLE PARAMS:
    sell_formula0 = CategoricalParameter(
        formulas, default=formulas[0], optimize=0 < CONDITIONS, space='exit')
    sell_formula1 = CategoricalParameter(
        formulas, default=formulas[0], optimize=1 < CONDITIONS, space='exit')
    sell_formula2 = CategoricalParameter(
        formulas, default=formulas[0], optimize=2 < CONDITIONS, space='exit')
    sell_formula3 = CategoricalParameter(
        formulas, default=formulas[0], optimize=3 < CONDITIONS, space='exit')
    sell_formula4 = CategoricalParameter(
        formulas, default=formulas[0], optimize=4 < CONDITIONS, space='exit')
    sell_formula5 = CategoricalParameter(
        formulas, default=formulas[0], optimize=5 < CONDITIONS, space='exit')
    sell_formula6 = CategoricalParameter(
        formulas, default=formulas[0], optimize=6 < CONDITIONS, space='exit')
    sell_formula7 = CategoricalParameter(
        formulas, default=formulas[0], optimize=7 < CONDITIONS, space='exit')
    sell_formula8 = CategoricalParameter(
        formulas, default=formulas[0], optimize=8 < CONDITIONS, space='exit')
    sell_formula9 = CategoricalParameter(
        formulas, default=formulas[0], optimize=9 < CONDITIONS, space='exit')
    sell_formula10 = CategoricalParameter(
        formulas, default=formulas[0], optimize=10 < CONDITIONS, space='exit')
    sell_formula11 = CategoricalParameter(
        formulas, default=formulas[0], optimize=11 < CONDITIONS, space='exit')
    sell_formula12 = CategoricalParameter(
        formulas, default=formulas[0], optimize=12 < CONDITIONS, space='exit')
    sell_formula13 = CategoricalParameter(
        formulas, default=formulas[0], optimize=13 < CONDITIONS, space='exit')
    sell_formula14 = CategoricalParameter(
        formulas, default=formulas[0], optimize=14 < CONDITIONS, space='exit')
    sell_formula15 = CategoricalParameter(
        formulas, default=formulas[0], optimize=15 < CONDITIONS, space='exit')
    sell_formula16 = CategoricalParameter(
        formulas, default=formulas[0], optimize=16 < CONDITIONS, space='exit')
    sell_formula17 = CategoricalParameter(
        formulas, default=formulas[0], optimize=17 < CONDITIONS, space='exit')
    sell_formula18 = CategoricalParameter(
        formulas, default=formulas[0], optimize=18 < CONDITIONS, space='exit')
    sell_formula19 = CategoricalParameter(
        formulas, default=formulas[0], optimize=19 < CONDITIONS, space='exit')
    sell_formula20 = CategoricalParameter(
        formulas, default=formulas[0], optimize=20 < CONDITIONS, space='exit')
    sell_formula21 = CategoricalParameter(
        formulas, default=formulas[0], optimize=21 < CONDITIONS, space='exit')
    sell_formula22 = CategoricalParameter(
        formulas, default=formulas[0], optimize=22 < CONDITIONS, space='exit')
    sell_formula23 = CategoricalParameter(
        formulas, default=formulas[0], optimize=23 < CONDITIONS, space='exit')
    sell_formula24 = CategoricalParameter(
        formulas, default=formulas[0], optimize=24 < CONDITIONS, space='exit')
    sell_formula25 = CategoricalParameter(
        formulas, default=formulas[0], optimize=25 < CONDITIONS, space='exit')
    sell_formula26 = CategoricalParameter(
        formulas, default=formulas[0], optimize=26 < CONDITIONS, space='exit')
    sell_formula27 = CategoricalParameter(
        formulas, default=formulas[0], optimize=27 < CONDITIONS, space='exit')
    sell_formula28 = CategoricalParameter(
        formulas, default=formulas[0], optimize=28 < CONDITIONS, space='exit')
    sell_formula29 = CategoricalParameter(
        formulas, default=formulas[0], optimize=29 < CONDITIONS, space='exit')
    sell_formula30 = CategoricalParameter(
        formulas, default=formulas[0], optimize=30 < CONDITIONS, space='exit')
    sell_formula31 = CategoricalParameter(
        formulas, default=formulas[0], optimize=31 < CONDITIONS, space='exit')
    sell_formula32 = CategoricalParameter(
        formulas, default=formulas[0], optimize=32 < CONDITIONS, space='exit')
    sell_formula33 = CategoricalParameter(
        formulas, default=formulas[0], optimize=33 < CONDITIONS, space='exit')
    sell_formula34 = CategoricalParameter(
        formulas, default=formulas[0], optimize=34 < CONDITIONS, space='exit')
    sell_formula35 = CategoricalParameter(
        formulas, default=formulas[0], optimize=35 < CONDITIONS, space='exit')
    sell_formula36 = CategoricalParameter(
        formulas, default=formulas[0], optimize=36 < CONDITIONS, space='exit')
    sell_formula37 = CategoricalParameter(
        formulas, default=formulas[0], optimize=37 < CONDITIONS, space='exit')
    sell_formula38 = CategoricalParameter(
        formulas, default=formulas[0], optimize=38 < CONDITIONS, space='exit')
    sell_formula39 = CategoricalParameter(
        formulas, default=formulas[0], optimize=39 < CONDITIONS, space='exit')
    sell_formula40 = CategoricalParameter(
        formulas, default=formulas[0], optimize=40 < CONDITIONS, space='exit')
    sell_formula41 = CategoricalParameter(
        formulas, default=formulas[0], optimize=41 < CONDITIONS, space='exit')
    sell_formula42 = CategoricalParameter(
        formulas, default=formulas[0], optimize=42 < CONDITIONS, space='exit')
    sell_formula43 = CategoricalParameter(
        formulas, default=formulas[0], optimize=43 < CONDITIONS, space='exit')
    sell_formula44 = CategoricalParameter(
        formulas, default=formulas[0], optimize=44 < CONDITIONS, space='exit')
    sell_formula45 = CategoricalParameter(
        formulas, default=formulas[0], optimize=45 < CONDITIONS, space='exit')
    sell_formula46 = CategoricalParameter(
        formulas, default=formulas[0], optimize=46 < CONDITIONS, space='exit')
    sell_formula47 = CategoricalParameter(
        formulas, default=formulas[0], optimize=47 < CONDITIONS, space='exit')
    sell_formula48 = CategoricalParameter(
        formulas, default=formulas[0], optimize=48 < CONDITIONS, space='exit')
    sell_formula49 = CategoricalParameter(
        formulas, default=formulas[0], optimize=49 < CONDITIONS, space='exit')
    sell_formula50 = CategoricalParameter(
        formulas, default=formulas[0], optimize=50 < CONDITIONS, space='exit')
    sell_formula51 = CategoricalParameter(
        formulas, default=formulas[0], optimize=51 < CONDITIONS, space='exit')
    sell_formula52 = CategoricalParameter(
        formulas, default=formulas[0], optimize=52 < CONDITIONS, space='exit')
    sell_formula53 = CategoricalParameter(
        formulas, default=formulas[0], optimize=53 < CONDITIONS, space='exit')
    sell_formula54 = CategoricalParameter(
        formulas, default=formulas[0], optimize=54 < CONDITIONS, space='exit')
    sell_formula55 = CategoricalParameter(
        formulas, default=formulas[0], optimize=55 < CONDITIONS, space='exit')
    sell_formula56 = CategoricalParameter(
        formulas, default=formulas[0], optimize=56 < CONDITIONS, space='exit')
    sell_formula57 = CategoricalParameter(
        formulas, default=formulas[0], optimize=57 < CONDITIONS, space='exit')
    sell_formula58 = CategoricalParameter(
        formulas, default=formulas[0], optimize=58 < CONDITIONS, space='exit')
    sell_formula59 = CategoricalParameter(
        formulas, default=formulas[0], optimize=59 < CONDITIONS, space='exit')
    sell_formula60 = CategoricalParameter(
        formulas, default=formulas[0], optimize=60 < CONDITIONS, space='exit')
    sell_formula61 = CategoricalParameter(
        formulas, default=formulas[0], optimize=61 < CONDITIONS, space='exit')
    sell_formula62 = CategoricalParameter(
        formulas, default=formulas[0], optimize=62 < CONDITIONS, space='exit')
    sell_formula63 = CategoricalParameter(
        formulas, default=formulas[0], optimize=63 < CONDITIONS, space='exit')
    sell_formula64 = CategoricalParameter(
        formulas, default=formulas[0], optimize=64 < CONDITIONS, space='exit')
    sell_formula65 = CategoricalParameter(
        formulas, default=formulas[0], optimize=65 < CONDITIONS, space='exit')
    sell_formula66 = CategoricalParameter(
        formulas, default=formulas[0], optimize=66 < CONDITIONS, space='exit')
    sell_formula67 = CategoricalParameter(
        formulas, default=formulas[0], optimize=67 < CONDITIONS, space='exit')
    sell_formula68 = CategoricalParameter(
        formulas, default=formulas[0], optimize=68 < CONDITIONS, space='exit')
    sell_formula69 = CategoricalParameter(
        formulas, default=formulas[0], optimize=69 < CONDITIONS, space='exit')
    sell_formula70 = CategoricalParameter(
        formulas, default=formulas[0], optimize=70 < CONDITIONS, space='exit')
    sell_formula71 = CategoricalParameter(
        formulas, default=formulas[0], optimize=71 < CONDITIONS, space='exit')
    sell_formula72 = CategoricalParameter(
        formulas, default=formulas[0], optimize=72 < CONDITIONS, space='exit')
    sell_formula73 = CategoricalParameter(
        formulas, default=formulas[0], optimize=73 < CONDITIONS, space='exit')
    sell_formula74 = CategoricalParameter(
        formulas, default=formulas[0], optimize=74 < CONDITIONS, space='exit')
    sell_formula75 = CategoricalParameter(
        formulas, default=formulas[0], optimize=75 < CONDITIONS, space='exit')
    sell_formula76 = CategoricalParameter(
        formulas, default=formulas[0], optimize=76 < CONDITIONS, space='exit')
    sell_formula77 = CategoricalParameter(
        formulas, default=formulas[0], optimize=77 < CONDITIONS, space='exit')
    sell_formula78 = CategoricalParameter(
        formulas, default=formulas[0], optimize=78 < CONDITIONS, space='exit')
    sell_formula79 = CategoricalParameter(
        formulas, default=formulas[0], optimize=79 < CONDITIONS, space='exit')
    sell_formula80 = CategoricalParameter(
        formulas, default=formulas[0], optimize=80 < CONDITIONS, space='exit')
    sell_formula81 = CategoricalParameter(
        formulas, default=formulas[0], optimize=81 < CONDITIONS, space='exit')
    sell_formula82 = CategoricalParameter(
        formulas, default=formulas[0], optimize=82 < CONDITIONS, space='exit')
    sell_formula83 = CategoricalParameter(
        formulas, default=formulas[0], optimize=83 < CONDITIONS, space='exit')
    sell_formula84 = CategoricalParameter(
        formulas, default=formulas[0], optimize=84 < CONDITIONS, space='exit')
    sell_formula85 = CategoricalParameter(
        formulas, default=formulas[0], optimize=85 < CONDITIONS, space='exit')
    sell_formula86 = CategoricalParameter(
        formulas, default=formulas[0], optimize=86 < CONDITIONS, space='exit')
    sell_formula87 = CategoricalParameter(
        formulas, default=formulas[0], optimize=87 < CONDITIONS, space='exit')
    sell_formula88 = CategoricalParameter(
        formulas, default=formulas[0], optimize=88 < CONDITIONS, space='exit')
    sell_formula89 = CategoricalParameter(
        formulas, default=formulas[0], optimize=89 < CONDITIONS, space='exit')
    sell_formula90 = CategoricalParameter(
        formulas, default=formulas[0], optimize=90 < CONDITIONS, space='exit')
    sell_formula91 = CategoricalParameter(
        formulas, default=formulas[0], optimize=91 < CONDITIONS, space='exit')
    sell_formula92 = CategoricalParameter(
        formulas, default=formulas[0], optimize=92 < CONDITIONS, space='exit')
    sell_formula93 = CategoricalParameter(
        formulas, default=formulas[0], optimize=93 < CONDITIONS, space='exit')
    sell_formula94 = CategoricalParameter(
        formulas, default=formulas[0], optimize=94 < CONDITIONS, space='exit')
    sell_formula95 = CategoricalParameter(
        formulas, default=formulas[0], optimize=95 < CONDITIONS, space='exit')
    sell_formula96 = CategoricalParameter(
        formulas, default=formulas[0], optimize=96 < CONDITIONS, space='exit')
    sell_formula97 = CategoricalParameter(
        formulas, default=formulas[0], optimize=97 < CONDITIONS, space='exit')
    sell_formula98 = CategoricalParameter(
        formulas, default=formulas[0], optimize=98 < CONDITIONS, space='exit')
    sell_formula99 = CategoricalParameter(
        formulas, default=formulas[0], optimize=99 < CONDITIONS, space='exit')

    sell_indicator0 = CategoricalParameter(
        indicators, default=indicators[0], optimize=0 < CONDITIONS, space='exit')
    sell_indicator1 = CategoricalParameter(
        indicators, default=indicators[0], optimize=1 < CONDITIONS, space='exit')
    sell_indicator2 = CategoricalParameter(
        indicators, default=indicators[0], optimize=2 < CONDITIONS, space='exit')
    sell_indicator3 = CategoricalParameter(
        indicators, default=indicators[0], optimize=3 < CONDITIONS, space='exit')
    sell_indicator4 = CategoricalParameter(
        indicators, default=indicators[0], optimize=4 < CONDITIONS, space='exit')
    sell_indicator5 = CategoricalParameter(
        indicators, default=indicators[0], optimize=5 < CONDITIONS, space='exit')
    sell_indicator6 = CategoricalParameter(
        indicators, default=indicators[0], optimize=6 < CONDITIONS, space='exit')
    sell_indicator7 = CategoricalParameter(
        indicators, default=indicators[0], optimize=7 < CONDITIONS, space='exit')
    sell_indicator8 = CategoricalParameter(
        indicators, default=indicators[0], optimize=8 < CONDITIONS, space='exit')
    sell_indicator9 = CategoricalParameter(
        indicators, default=indicators[0], optimize=9 < CONDITIONS, space='exit')
    sell_indicator10 = CategoricalParameter(
        indicators, default=indicators[0], optimize=10 < CONDITIONS, space='exit')
    sell_indicator11 = CategoricalParameter(
        indicators, default=indicators[0], optimize=11 < CONDITIONS, space='exit')
    sell_indicator12 = CategoricalParameter(
        indicators, default=indicators[0], optimize=12 < CONDITIONS, space='exit')
    sell_indicator13 = CategoricalParameter(
        indicators, default=indicators[0], optimize=13 < CONDITIONS, space='exit')
    sell_indicator14 = CategoricalParameter(
        indicators, default=indicators[0], optimize=14 < CONDITIONS, space='exit')
    sell_indicator15 = CategoricalParameter(
        indicators, default=indicators[0], optimize=15 < CONDITIONS, space='exit')
    sell_indicator16 = CategoricalParameter(
        indicators, default=indicators[0], optimize=16 < CONDITIONS, space='exit')
    sell_indicator17 = CategoricalParameter(
        indicators, default=indicators[0], optimize=17 < CONDITIONS, space='exit')
    sell_indicator18 = CategoricalParameter(
        indicators, default=indicators[0], optimize=18 < CONDITIONS, space='exit')
    sell_indicator19 = CategoricalParameter(
        indicators, default=indicators[0], optimize=19 < CONDITIONS, space='exit')
    sell_indicator20 = CategoricalParameter(
        indicators, default=indicators[0], optimize=20 < CONDITIONS, space='exit')
    sell_indicator21 = CategoricalParameter(
        indicators, default=indicators[0], optimize=21 < CONDITIONS, space='exit')
    sell_indicator22 = CategoricalParameter(
        indicators, default=indicators[0], optimize=22 < CONDITIONS, space='exit')
    sell_indicator23 = CategoricalParameter(
        indicators, default=indicators[0], optimize=23 < CONDITIONS, space='exit')
    sell_indicator24 = CategoricalParameter(
        indicators, default=indicators[0], optimize=24 < CONDITIONS, space='exit')
    sell_indicator25 = CategoricalParameter(
        indicators, default=indicators[0], optimize=25 < CONDITIONS, space='exit')
    sell_indicator26 = CategoricalParameter(
        indicators, default=indicators[0], optimize=26 < CONDITIONS, space='exit')
    sell_indicator27 = CategoricalParameter(
        indicators, default=indicators[0], optimize=27 < CONDITIONS, space='exit')
    sell_indicator28 = CategoricalParameter(
        indicators, default=indicators[0], optimize=28 < CONDITIONS, space='exit')
    sell_indicator29 = CategoricalParameter(
        indicators, default=indicators[0], optimize=29 < CONDITIONS, space='exit')
    sell_indicator30 = CategoricalParameter(
        indicators, default=indicators[0], optimize=30 < CONDITIONS, space='exit')
    sell_indicator31 = CategoricalParameter(
        indicators, default=indicators[0], optimize=31 < CONDITIONS, space='exit')
    sell_indicator32 = CategoricalParameter(
        indicators, default=indicators[0], optimize=32 < CONDITIONS, space='exit')
    sell_indicator33 = CategoricalParameter(
        indicators, default=indicators[0], optimize=33 < CONDITIONS, space='exit')
    sell_indicator34 = CategoricalParameter(
        indicators, default=indicators[0], optimize=34 < CONDITIONS, space='exit')
    sell_indicator35 = CategoricalParameter(
        indicators, default=indicators[0], optimize=35 < CONDITIONS, space='exit')
    sell_indicator36 = CategoricalParameter(
        indicators, default=indicators[0], optimize=36 < CONDITIONS, space='exit')
    sell_indicator37 = CategoricalParameter(
        indicators, default=indicators[0], optimize=37 < CONDITIONS, space='exit')
    sell_indicator38 = CategoricalParameter(
        indicators, default=indicators[0], optimize=38 < CONDITIONS, space='exit')
    sell_indicator39 = CategoricalParameter(
        indicators, default=indicators[0], optimize=39 < CONDITIONS, space='exit')
    sell_indicator40 = CategoricalParameter(
        indicators, default=indicators[0], optimize=40 < CONDITIONS, space='exit')
    sell_indicator41 = CategoricalParameter(
        indicators, default=indicators[0], optimize=41 < CONDITIONS, space='exit')
    sell_indicator42 = CategoricalParameter(
        indicators, default=indicators[0], optimize=42 < CONDITIONS, space='exit')
    sell_indicator43 = CategoricalParameter(
        indicators, default=indicators[0], optimize=43 < CONDITIONS, space='exit')
    sell_indicator44 = CategoricalParameter(
        indicators, default=indicators[0], optimize=44 < CONDITIONS, space='exit')
    sell_indicator45 = CategoricalParameter(
        indicators, default=indicators[0], optimize=45 < CONDITIONS, space='exit')
    sell_indicator46 = CategoricalParameter(
        indicators, default=indicators[0], optimize=46 < CONDITIONS, space='exit')
    sell_indicator47 = CategoricalParameter(
        indicators, default=indicators[0], optimize=47 < CONDITIONS, space='exit')
    sell_indicator48 = CategoricalParameter(
        indicators, default=indicators[0], optimize=48 < CONDITIONS, space='exit')
    sell_indicator49 = CategoricalParameter(
        indicators, default=indicators[0], optimize=49 < CONDITIONS, space='exit')
    sell_indicator50 = CategoricalParameter(
        indicators, default=indicators[0], optimize=50 < CONDITIONS, space='exit')
    sell_indicator51 = CategoricalParameter(
        indicators, default=indicators[0], optimize=51 < CONDITIONS, space='exit')
    sell_indicator52 = CategoricalParameter(
        indicators, default=indicators[0], optimize=52 < CONDITIONS, space='exit')
    sell_indicator53 = CategoricalParameter(
        indicators, default=indicators[0], optimize=53 < CONDITIONS, space='exit')
    sell_indicator54 = CategoricalParameter(
        indicators, default=indicators[0], optimize=54 < CONDITIONS, space='exit')
    sell_indicator55 = CategoricalParameter(
        indicators, default=indicators[0], optimize=55 < CONDITIONS, space='exit')
    sell_indicator56 = CategoricalParameter(
        indicators, default=indicators[0], optimize=56 < CONDITIONS, space='exit')
    sell_indicator57 = CategoricalParameter(
        indicators, default=indicators[0], optimize=57 < CONDITIONS, space='exit')
    sell_indicator58 = CategoricalParameter(
        indicators, default=indicators[0], optimize=58 < CONDITIONS, space='exit')
    sell_indicator59 = CategoricalParameter(
        indicators, default=indicators[0], optimize=59 < CONDITIONS, space='exit')
    sell_indicator60 = CategoricalParameter(
        indicators, default=indicators[0], optimize=60 < CONDITIONS, space='exit')
    sell_indicator61 = CategoricalParameter(
        indicators, default=indicators[0], optimize=61 < CONDITIONS, space='exit')
    sell_indicator62 = CategoricalParameter(
        indicators, default=indicators[0], optimize=62 < CONDITIONS, space='exit')
    sell_indicator63 = CategoricalParameter(
        indicators, default=indicators[0], optimize=63 < CONDITIONS, space='exit')
    sell_indicator64 = CategoricalParameter(
        indicators, default=indicators[0], optimize=64 < CONDITIONS, space='exit')
    sell_indicator65 = CategoricalParameter(
        indicators, default=indicators[0], optimize=65 < CONDITIONS, space='exit')
    sell_indicator66 = CategoricalParameter(
        indicators, default=indicators[0], optimize=66 < CONDITIONS, space='exit')
    sell_indicator67 = CategoricalParameter(
        indicators, default=indicators[0], optimize=67 < CONDITIONS, space='exit')
    sell_indicator68 = CategoricalParameter(
        indicators, default=indicators[0], optimize=68 < CONDITIONS, space='exit')
    sell_indicator69 = CategoricalParameter(
        indicators, default=indicators[0], optimize=69 < CONDITIONS, space='exit')
    sell_indicator70 = CategoricalParameter(
        indicators, default=indicators[0], optimize=70 < CONDITIONS, space='exit')
    sell_indicator71 = CategoricalParameter(
        indicators, default=indicators[0], optimize=71 < CONDITIONS, space='exit')
    sell_indicator72 = CategoricalParameter(
        indicators, default=indicators[0], optimize=72 < CONDITIONS, space='exit')
    sell_indicator73 = CategoricalParameter(
        indicators, default=indicators[0], optimize=73 < CONDITIONS, space='exit')
    sell_indicator74 = CategoricalParameter(
        indicators, default=indicators[0], optimize=74 < CONDITIONS, space='exit')
    sell_indicator75 = CategoricalParameter(
        indicators, default=indicators[0], optimize=75 < CONDITIONS, space='exit')
    sell_indicator76 = CategoricalParameter(
        indicators, default=indicators[0], optimize=76 < CONDITIONS, space='exit')
    sell_indicator77 = CategoricalParameter(
        indicators, default=indicators[0], optimize=77 < CONDITIONS, space='exit')
    sell_indicator78 = CategoricalParameter(
        indicators, default=indicators[0], optimize=78 < CONDITIONS, space='exit')
    sell_indicator79 = CategoricalParameter(
        indicators, default=indicators[0], optimize=79 < CONDITIONS, space='exit')
    sell_indicator80 = CategoricalParameter(
        indicators, default=indicators[0], optimize=80 < CONDITIONS, space='exit')
    sell_indicator81 = CategoricalParameter(
        indicators, default=indicators[0], optimize=81 < CONDITIONS, space='exit')
    sell_indicator82 = CategoricalParameter(
        indicators, default=indicators[0], optimize=82 < CONDITIONS, space='exit')
    sell_indicator83 = CategoricalParameter(
        indicators, default=indicators[0], optimize=83 < CONDITIONS, space='exit')
    sell_indicator84 = CategoricalParameter(
        indicators, default=indicators[0], optimize=84 < CONDITIONS, space='exit')
    sell_indicator85 = CategoricalParameter(
        indicators, default=indicators[0], optimize=85 < CONDITIONS, space='exit')
    sell_indicator86 = CategoricalParameter(
        indicators, default=indicators[0], optimize=86 < CONDITIONS, space='exit')
    sell_indicator87 = CategoricalParameter(
        indicators, default=indicators[0], optimize=87 < CONDITIONS, space='exit')
    sell_indicator88 = CategoricalParameter(
        indicators, default=indicators[0], optimize=88 < CONDITIONS, space='exit')
    sell_indicator89 = CategoricalParameter(
        indicators, default=indicators[0], optimize=89 < CONDITIONS, space='exit')
    sell_indicator90 = CategoricalParameter(
        indicators, default=indicators[0], optimize=90 < CONDITIONS, space='exit')
    sell_indicator91 = CategoricalParameter(
        indicators, default=indicators[0], optimize=91 < CONDITIONS, space='exit')
    sell_indicator92 = CategoricalParameter(
        indicators, default=indicators[0], optimize=92 < CONDITIONS, space='exit')
    sell_indicator93 = CategoricalParameter(
        indicators, default=indicators[0], optimize=93 < CONDITIONS, space='exit')
    sell_indicator94 = CategoricalParameter(
        indicators, default=indicators[0], optimize=94 < CONDITIONS, space='exit')
    sell_indicator95 = CategoricalParameter(
        indicators, default=indicators[0], optimize=95 < CONDITIONS, space='exit')
    sell_indicator96 = CategoricalParameter(
        indicators, default=indicators[0], optimize=96 < CONDITIONS, space='exit')
    sell_indicator97 = CategoricalParameter(
        indicators, default=indicators[0], optimize=97 < CONDITIONS, space='exit')
    sell_indicator98 = CategoricalParameter(
        indicators, default=indicators[0], optimize=98 < CONDITIONS, space='exit')
    sell_indicator99 = CategoricalParameter(
        indicators, default=indicators[0], optimize=99 < CONDITIONS, space='exit')

    sell_crossed0 = CategoricalParameter(
        indicators, default=indicators[0], optimize=0 < CONDITIONS, space='exit')
    sell_crossed1 = CategoricalParameter(
        indicators, default=indicators[0], optimize=1 < CONDITIONS, space='exit')
    sell_crossed2 = CategoricalParameter(
        indicators, default=indicators[0], optimize=2 < CONDITIONS, space='exit')
    sell_crossed3 = CategoricalParameter(
        indicators, default=indicators[0], optimize=3 < CONDITIONS, space='exit')
    sell_crossed4 = CategoricalParameter(
        indicators, default=indicators[0], optimize=4 < CONDITIONS, space='exit')
    sell_crossed5 = CategoricalParameter(
        indicators, default=indicators[0], optimize=5 < CONDITIONS, space='exit')
    sell_crossed6 = CategoricalParameter(
        indicators, default=indicators[0], optimize=6 < CONDITIONS, space='exit')
    sell_crossed7 = CategoricalParameter(
        indicators, default=indicators[0], optimize=7 < CONDITIONS, space='exit')
    sell_crossed8 = CategoricalParameter(
        indicators, default=indicators[0], optimize=8 < CONDITIONS, space='exit')
    sell_crossed9 = CategoricalParameter(
        indicators, default=indicators[0], optimize=9 < CONDITIONS, space='exit')
    sell_crossed10 = CategoricalParameter(
        indicators, default=indicators[0], optimize=10 < CONDITIONS, space='exit')
    sell_crossed11 = CategoricalParameter(
        indicators, default=indicators[0], optimize=11 < CONDITIONS, space='exit')
    sell_crossed12 = CategoricalParameter(
        indicators, default=indicators[0], optimize=12 < CONDITIONS, space='exit')
    sell_crossed13 = CategoricalParameter(
        indicators, default=indicators[0], optimize=13 < CONDITIONS, space='exit')
    sell_crossed14 = CategoricalParameter(
        indicators, default=indicators[0], optimize=14 < CONDITIONS, space='exit')
    sell_crossed15 = CategoricalParameter(
        indicators, default=indicators[0], optimize=15 < CONDITIONS, space='exit')
    sell_crossed16 = CategoricalParameter(
        indicators, default=indicators[0], optimize=16 < CONDITIONS, space='exit')
    sell_crossed17 = CategoricalParameter(
        indicators, default=indicators[0], optimize=17 < CONDITIONS, space='exit')
    sell_crossed18 = CategoricalParameter(
        indicators, default=indicators[0], optimize=18 < CONDITIONS, space='exit')
    sell_crossed19 = CategoricalParameter(
        indicators, default=indicators[0], optimize=19 < CONDITIONS, space='exit')
    sell_crossed20 = CategoricalParameter(
        indicators, default=indicators[0], optimize=20 < CONDITIONS, space='exit')
    sell_crossed21 = CategoricalParameter(
        indicators, default=indicators[0], optimize=21 < CONDITIONS, space='exit')
    sell_crossed22 = CategoricalParameter(
        indicators, default=indicators[0], optimize=22 < CONDITIONS, space='exit')
    sell_crossed23 = CategoricalParameter(
        indicators, default=indicators[0], optimize=23 < CONDITIONS, space='exit')
    sell_crossed24 = CategoricalParameter(
        indicators, default=indicators[0], optimize=24 < CONDITIONS, space='exit')
    sell_crossed25 = CategoricalParameter(
        indicators, default=indicators[0], optimize=25 < CONDITIONS, space='exit')
    sell_crossed26 = CategoricalParameter(
        indicators, default=indicators[0], optimize=26 < CONDITIONS, space='exit')
    sell_crossed27 = CategoricalParameter(
        indicators, default=indicators[0], optimize=27 < CONDITIONS, space='exit')
    sell_crossed28 = CategoricalParameter(
        indicators, default=indicators[0], optimize=28 < CONDITIONS, space='exit')
    sell_crossed29 = CategoricalParameter(
        indicators, default=indicators[0], optimize=29 < CONDITIONS, space='exit')
    sell_crossed30 = CategoricalParameter(
        indicators, default=indicators[0], optimize=30 < CONDITIONS, space='exit')
    sell_crossed31 = CategoricalParameter(
        indicators, default=indicators[0], optimize=31 < CONDITIONS, space='exit')
    sell_crossed32 = CategoricalParameter(
        indicators, default=indicators[0], optimize=32 < CONDITIONS, space='exit')
    sell_crossed33 = CategoricalParameter(
        indicators, default=indicators[0], optimize=33 < CONDITIONS, space='exit')
    sell_crossed34 = CategoricalParameter(
        indicators, default=indicators[0], optimize=34 < CONDITIONS, space='exit')
    sell_crossed35 = CategoricalParameter(
        indicators, default=indicators[0], optimize=35 < CONDITIONS, space='exit')
    sell_crossed36 = CategoricalParameter(
        indicators, default=indicators[0], optimize=36 < CONDITIONS, space='exit')
    sell_crossed37 = CategoricalParameter(
        indicators, default=indicators[0], optimize=37 < CONDITIONS, space='exit')
    sell_crossed38 = CategoricalParameter(
        indicators, default=indicators[0], optimize=38 < CONDITIONS, space='exit')
    sell_crossed39 = CategoricalParameter(
        indicators, default=indicators[0], optimize=39 < CONDITIONS, space='exit')
    sell_crossed40 = CategoricalParameter(
        indicators, default=indicators[0], optimize=40 < CONDITIONS, space='exit')
    sell_crossed41 = CategoricalParameter(
        indicators, default=indicators[0], optimize=41 < CONDITIONS, space='exit')
    sell_crossed42 = CategoricalParameter(
        indicators, default=indicators[0], optimize=42 < CONDITIONS, space='exit')
    sell_crossed43 = CategoricalParameter(
        indicators, default=indicators[0], optimize=43 < CONDITIONS, space='exit')
    sell_crossed44 = CategoricalParameter(
        indicators, default=indicators[0], optimize=44 < CONDITIONS, space='exit')
    sell_crossed45 = CategoricalParameter(
        indicators, default=indicators[0], optimize=45 < CONDITIONS, space='exit')
    sell_crossed46 = CategoricalParameter(
        indicators, default=indicators[0], optimize=46 < CONDITIONS, space='exit')
    sell_crossed47 = CategoricalParameter(
        indicators, default=indicators[0], optimize=47 < CONDITIONS, space='exit')
    sell_crossed48 = CategoricalParameter(
        indicators, default=indicators[0], optimize=48 < CONDITIONS, space='exit')
    sell_crossed49 = CategoricalParameter(
        indicators, default=indicators[0], optimize=49 < CONDITIONS, space='exit')
    sell_crossed50 = CategoricalParameter(
        indicators, default=indicators[0], optimize=50 < CONDITIONS, space='exit')
    sell_crossed51 = CategoricalParameter(
        indicators, default=indicators[0], optimize=51 < CONDITIONS, space='exit')
    sell_crossed52 = CategoricalParameter(
        indicators, default=indicators[0], optimize=52 < CONDITIONS, space='exit')
    sell_crossed53 = CategoricalParameter(
        indicators, default=indicators[0], optimize=53 < CONDITIONS, space='exit')
    sell_crossed54 = CategoricalParameter(
        indicators, default=indicators[0], optimize=54 < CONDITIONS, space='exit')
    sell_crossed55 = CategoricalParameter(
        indicators, default=indicators[0], optimize=55 < CONDITIONS, space='exit')
    sell_crossed56 = CategoricalParameter(
        indicators, default=indicators[0], optimize=56 < CONDITIONS, space='exit')
    sell_crossed57 = CategoricalParameter(
        indicators, default=indicators[0], optimize=57 < CONDITIONS, space='exit')
    sell_crossed58 = CategoricalParameter(
        indicators, default=indicators[0], optimize=58 < CONDITIONS, space='exit')
    sell_crossed59 = CategoricalParameter(
        indicators, default=indicators[0], optimize=59 < CONDITIONS, space='exit')
    sell_crossed60 = CategoricalParameter(
        indicators, default=indicators[0], optimize=60 < CONDITIONS, space='exit')
    sell_crossed61 = CategoricalParameter(
        indicators, default=indicators[0], optimize=61 < CONDITIONS, space='exit')
    sell_crossed62 = CategoricalParameter(
        indicators, default=indicators[0], optimize=62 < CONDITIONS, space='exit')
    sell_crossed63 = CategoricalParameter(
        indicators, default=indicators[0], optimize=63 < CONDITIONS, space='exit')
    sell_crossed64 = CategoricalParameter(
        indicators, default=indicators[0], optimize=64 < CONDITIONS, space='exit')
    sell_crossed65 = CategoricalParameter(
        indicators, default=indicators[0], optimize=65 < CONDITIONS, space='exit')
    sell_crossed66 = CategoricalParameter(
        indicators, default=indicators[0], optimize=66 < CONDITIONS, space='exit')
    sell_crossed67 = CategoricalParameter(
        indicators, default=indicators[0], optimize=67 < CONDITIONS, space='exit')
    sell_crossed68 = CategoricalParameter(
        indicators, default=indicators[0], optimize=68 < CONDITIONS, space='exit')
    sell_crossed69 = CategoricalParameter(
        indicators, default=indicators[0], optimize=69 < CONDITIONS, space='exit')
    sell_crossed70 = CategoricalParameter(
        indicators, default=indicators[0], optimize=70 < CONDITIONS, space='exit')
    sell_crossed71 = CategoricalParameter(
        indicators, default=indicators[0], optimize=71 < CONDITIONS, space='exit')
    sell_crossed72 = CategoricalParameter(
        indicators, default=indicators[0], optimize=72 < CONDITIONS, space='exit')
    sell_crossed73 = CategoricalParameter(
        indicators, default=indicators[0], optimize=73 < CONDITIONS, space='exit')
    sell_crossed74 = CategoricalParameter(
        indicators, default=indicators[0], optimize=74 < CONDITIONS, space='exit')
    sell_crossed75 = CategoricalParameter(
        indicators, default=indicators[0], optimize=75 < CONDITIONS, space='exit')
    sell_crossed76 = CategoricalParameter(
        indicators, default=indicators[0], optimize=76 < CONDITIONS, space='exit')
    sell_crossed77 = CategoricalParameter(
        indicators, default=indicators[0], optimize=77 < CONDITIONS, space='exit')
    sell_crossed78 = CategoricalParameter(
        indicators, default=indicators[0], optimize=78 < CONDITIONS, space='exit')
    sell_crossed79 = CategoricalParameter(
        indicators, default=indicators[0], optimize=79 < CONDITIONS, space='exit')
    sell_crossed80 = CategoricalParameter(
        indicators, default=indicators[0], optimize=80 < CONDITIONS, space='exit')
    sell_crossed81 = CategoricalParameter(
        indicators, default=indicators[0], optimize=81 < CONDITIONS, space='exit')
    sell_crossed82 = CategoricalParameter(
        indicators, default=indicators[0], optimize=82 < CONDITIONS, space='exit')
    sell_crossed83 = CategoricalParameter(
        indicators, default=indicators[0], optimize=83 < CONDITIONS, space='exit')
    sell_crossed84 = CategoricalParameter(
        indicators, default=indicators[0], optimize=84 < CONDITIONS, space='exit')
    sell_crossed85 = CategoricalParameter(
        indicators, default=indicators[0], optimize=85 < CONDITIONS, space='exit')
    sell_crossed86 = CategoricalParameter(
        indicators, default=indicators[0], optimize=86 < CONDITIONS, space='exit')
    sell_crossed87 = CategoricalParameter(
        indicators, default=indicators[0], optimize=87 < CONDITIONS, space='exit')
    sell_crossed88 = CategoricalParameter(
        indicators, default=indicators[0], optimize=88 < CONDITIONS, space='exit')
    sell_crossed89 = CategoricalParameter(
        indicators, default=indicators[0], optimize=89 < CONDITIONS, space='exit')
    sell_crossed90 = CategoricalParameter(
        indicators, default=indicators[0], optimize=90 < CONDITIONS, space='exit')
    sell_crossed91 = CategoricalParameter(
        indicators, default=indicators[0], optimize=91 < CONDITIONS, space='exit')
    sell_crossed92 = CategoricalParameter(
        indicators, default=indicators[0], optimize=92 < CONDITIONS, space='exit')
    sell_crossed93 = CategoricalParameter(
        indicators, default=indicators[0], optimize=93 < CONDITIONS, space='exit')
    sell_crossed94 = CategoricalParameter(
        indicators, default=indicators[0], optimize=94 < CONDITIONS, space='exit')
    sell_crossed95 = CategoricalParameter(
        indicators, default=indicators[0], optimize=95 < CONDITIONS, space='exit')
    sell_crossed96 = CategoricalParameter(
        indicators, default=indicators[0], optimize=96 < CONDITIONS, space='exit')
    sell_crossed97 = CategoricalParameter(
        indicators, default=indicators[0], optimize=97 < CONDITIONS, space='exit')
    sell_crossed98 = CategoricalParameter(
        indicators, default=indicators[0], optimize=98 < CONDITIONS, space='exit')
    sell_crossed99 = CategoricalParameter(
        indicators, default=indicators[0], optimize=99 < CONDITIONS, space='exit')

    sell_timeframe0 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=0 < CONDITIONS, space='exit')
    sell_timeframe1 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=1 < CONDITIONS, space='exit')
    sell_timeframe2 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=2 < CONDITIONS, space='exit')
    sell_timeframe3 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=3 < CONDITIONS, space='exit')
    sell_timeframe4 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=4 < CONDITIONS, space='exit')
    sell_timeframe5 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=5 < CONDITIONS, space='exit')
    sell_timeframe6 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=6 < CONDITIONS, space='exit')
    sell_timeframe7 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=7 < CONDITIONS, space='exit')
    sell_timeframe8 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=8 < CONDITIONS, space='exit')
    sell_timeframe9 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=9 < CONDITIONS, space='exit')
    sell_timeframe10 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=10 < CONDITIONS, space='exit')
    sell_timeframe11 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=11 < CONDITIONS, space='exit')
    sell_timeframe12 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=12 < CONDITIONS, space='exit')
    sell_timeframe13 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=13 < CONDITIONS, space='exit')
    sell_timeframe14 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=14 < CONDITIONS, space='exit')
    sell_timeframe15 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=15 < CONDITIONS, space='exit')
    sell_timeframe16 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=16 < CONDITIONS, space='exit')
    sell_timeframe17 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=17 < CONDITIONS, space='exit')
    sell_timeframe18 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=18 < CONDITIONS, space='exit')
    sell_timeframe19 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=19 < CONDITIONS, space='exit')
    sell_timeframe20 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=20 < CONDITIONS, space='exit')
    sell_timeframe21 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=21 < CONDITIONS, space='exit')
    sell_timeframe22 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=22 < CONDITIONS, space='exit')
    sell_timeframe23 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=23 < CONDITIONS, space='exit')
    sell_timeframe24 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=24 < CONDITIONS, space='exit')
    sell_timeframe25 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=25 < CONDITIONS, space='exit')
    sell_timeframe26 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=26 < CONDITIONS, space='exit')
    sell_timeframe27 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=27 < CONDITIONS, space='exit')
    sell_timeframe28 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=28 < CONDITIONS, space='exit')
    sell_timeframe29 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=29 < CONDITIONS, space='exit')
    sell_timeframe30 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=30 < CONDITIONS, space='exit')
    sell_timeframe31 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=31 < CONDITIONS, space='exit')
    sell_timeframe32 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=32 < CONDITIONS, space='exit')
    sell_timeframe33 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=33 < CONDITIONS, space='exit')
    sell_timeframe34 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=34 < CONDITIONS, space='exit')
    sell_timeframe35 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=35 < CONDITIONS, space='exit')
    sell_timeframe36 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=36 < CONDITIONS, space='exit')
    sell_timeframe37 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=37 < CONDITIONS, space='exit')
    sell_timeframe38 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=38 < CONDITIONS, space='exit')
    sell_timeframe39 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=39 < CONDITIONS, space='exit')
    sell_timeframe40 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=40 < CONDITIONS, space='exit')
    sell_timeframe41 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=41 < CONDITIONS, space='exit')
    sell_timeframe42 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=42 < CONDITIONS, space='exit')
    sell_timeframe43 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=43 < CONDITIONS, space='exit')
    sell_timeframe44 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=44 < CONDITIONS, space='exit')
    sell_timeframe45 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=45 < CONDITIONS, space='exit')
    sell_timeframe46 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=46 < CONDITIONS, space='exit')
    sell_timeframe47 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=47 < CONDITIONS, space='exit')
    sell_timeframe48 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=48 < CONDITIONS, space='exit')
    sell_timeframe49 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=49 < CONDITIONS, space='exit')
    sell_timeframe50 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=50 < CONDITIONS, space='exit')
    sell_timeframe51 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=51 < CONDITIONS, space='exit')
    sell_timeframe52 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=52 < CONDITIONS, space='exit')
    sell_timeframe53 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=53 < CONDITIONS, space='exit')
    sell_timeframe54 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=54 < CONDITIONS, space='exit')
    sell_timeframe55 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=55 < CONDITIONS, space='exit')
    sell_timeframe56 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=56 < CONDITIONS, space='exit')
    sell_timeframe57 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=57 < CONDITIONS, space='exit')
    sell_timeframe58 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=58 < CONDITIONS, space='exit')
    sell_timeframe59 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=59 < CONDITIONS, space='exit')
    sell_timeframe60 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=60 < CONDITIONS, space='exit')
    sell_timeframe61 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=61 < CONDITIONS, space='exit')
    sell_timeframe62 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=62 < CONDITIONS, space='exit')
    sell_timeframe63 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=63 < CONDITIONS, space='exit')
    sell_timeframe64 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=64 < CONDITIONS, space='exit')
    sell_timeframe65 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=65 < CONDITIONS, space='exit')
    sell_timeframe66 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=66 < CONDITIONS, space='exit')
    sell_timeframe67 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=67 < CONDITIONS, space='exit')
    sell_timeframe68 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=68 < CONDITIONS, space='exit')
    sell_timeframe69 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=69 < CONDITIONS, space='exit')
    sell_timeframe70 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=70 < CONDITIONS, space='exit')
    sell_timeframe71 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=71 < CONDITIONS, space='exit')
    sell_timeframe72 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=72 < CONDITIONS, space='exit')
    sell_timeframe73 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=73 < CONDITIONS, space='exit')
    sell_timeframe74 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=74 < CONDITIONS, space='exit')
    sell_timeframe75 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=75 < CONDITIONS, space='exit')
    sell_timeframe76 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=76 < CONDITIONS, space='exit')
    sell_timeframe77 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=77 < CONDITIONS, space='exit')
    sell_timeframe78 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=78 < CONDITIONS, space='exit')
    sell_timeframe79 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=79 < CONDITIONS, space='exit')
    sell_timeframe80 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=80 < CONDITIONS, space='exit')
    sell_timeframe81 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=81 < CONDITIONS, space='exit')
    sell_timeframe82 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=82 < CONDITIONS, space='exit')
    sell_timeframe83 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=83 < CONDITIONS, space='exit')
    sell_timeframe84 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=84 < CONDITIONS, space='exit')
    sell_timeframe85 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=85 < CONDITIONS, space='exit')
    sell_timeframe86 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=86 < CONDITIONS, space='exit')
    sell_timeframe87 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=87 < CONDITIONS, space='exit')
    sell_timeframe88 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=88 < CONDITIONS, space='exit')
    sell_timeframe89 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=89 < CONDITIONS, space='exit')
    sell_timeframe90 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=90 < CONDITIONS, space='exit')
    sell_timeframe91 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=91 < CONDITIONS, space='exit')
    sell_timeframe92 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=92 < CONDITIONS, space='exit')
    sell_timeframe93 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=93 < CONDITIONS, space='exit')
    sell_timeframe94 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=94 < CONDITIONS, space='exit')
    sell_timeframe95 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=95 < CONDITIONS, space='exit')
    sell_timeframe96 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=96 < CONDITIONS, space='exit')
    sell_timeframe97 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=97 < CONDITIONS, space='exit')
    sell_timeframe98 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=98 < CONDITIONS, space='exit')
    sell_timeframe99 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=99 < CONDITIONS, space='exit')

    sell_crossed_timeframe0 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=0 < CONDITIONS, space='exit')
    sell_crossed_timeframe1 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=1 < CONDITIONS, space='exit')
    sell_crossed_timeframe2 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=2 < CONDITIONS, space='exit')
    sell_crossed_timeframe3 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=3 < CONDITIONS, space='exit')
    sell_crossed_timeframe4 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=4 < CONDITIONS, space='exit')
    sell_crossed_timeframe5 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=5 < CONDITIONS, space='exit')
    sell_crossed_timeframe6 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=6 < CONDITIONS, space='exit')
    sell_crossed_timeframe7 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=7 < CONDITIONS, space='exit')
    sell_crossed_timeframe8 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=8 < CONDITIONS, space='exit')
    sell_crossed_timeframe9 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=9 < CONDITIONS, space='exit')
    sell_crossed_timeframe10 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=10 < CONDITIONS, space='exit')
    sell_crossed_timeframe11 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=11 < CONDITIONS, space='exit')
    sell_crossed_timeframe12 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=12 < CONDITIONS, space='exit')
    sell_crossed_timeframe13 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=13 < CONDITIONS, space='exit')
    sell_crossed_timeframe14 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=14 < CONDITIONS, space='exit')
    sell_crossed_timeframe15 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=15 < CONDITIONS, space='exit')
    sell_crossed_timeframe16 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=16 < CONDITIONS, space='exit')
    sell_crossed_timeframe17 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=17 < CONDITIONS, space='exit')
    sell_crossed_timeframe18 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=18 < CONDITIONS, space='exit')
    sell_crossed_timeframe19 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=19 < CONDITIONS, space='exit')
    sell_crossed_timeframe20 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=20 < CONDITIONS, space='exit')
    sell_crossed_timeframe21 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=21 < CONDITIONS, space='exit')
    sell_crossed_timeframe22 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=22 < CONDITIONS, space='exit')
    sell_crossed_timeframe23 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=23 < CONDITIONS, space='exit')
    sell_crossed_timeframe24 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=24 < CONDITIONS, space='exit')
    sell_crossed_timeframe25 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=25 < CONDITIONS, space='exit')
    sell_crossed_timeframe26 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=26 < CONDITIONS, space='exit')
    sell_crossed_timeframe27 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=27 < CONDITIONS, space='exit')
    sell_crossed_timeframe28 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=28 < CONDITIONS, space='exit')
    sell_crossed_timeframe29 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=29 < CONDITIONS, space='exit')
    sell_crossed_timeframe30 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=30 < CONDITIONS, space='exit')
    sell_crossed_timeframe31 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=31 < CONDITIONS, space='exit')
    sell_crossed_timeframe32 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=32 < CONDITIONS, space='exit')
    sell_crossed_timeframe33 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=33 < CONDITIONS, space='exit')
    sell_crossed_timeframe34 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=34 < CONDITIONS, space='exit')
    sell_crossed_timeframe35 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=35 < CONDITIONS, space='exit')
    sell_crossed_timeframe36 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=36 < CONDITIONS, space='exit')
    sell_crossed_timeframe37 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=37 < CONDITIONS, space='exit')
    sell_crossed_timeframe38 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=38 < CONDITIONS, space='exit')
    sell_crossed_timeframe39 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=39 < CONDITIONS, space='exit')
    sell_crossed_timeframe40 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=40 < CONDITIONS, space='exit')
    sell_crossed_timeframe41 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=41 < CONDITIONS, space='exit')
    sell_crossed_timeframe42 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=42 < CONDITIONS, space='exit')
    sell_crossed_timeframe43 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=43 < CONDITIONS, space='exit')
    sell_crossed_timeframe44 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=44 < CONDITIONS, space='exit')
    sell_crossed_timeframe45 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=45 < CONDITIONS, space='exit')
    sell_crossed_timeframe46 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=46 < CONDITIONS, space='exit')
    sell_crossed_timeframe47 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=47 < CONDITIONS, space='exit')
    sell_crossed_timeframe48 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=48 < CONDITIONS, space='exit')
    sell_crossed_timeframe49 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=49 < CONDITIONS, space='exit')
    sell_crossed_timeframe50 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=50 < CONDITIONS, space='exit')
    sell_crossed_timeframe51 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=51 < CONDITIONS, space='exit')
    sell_crossed_timeframe52 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=52 < CONDITIONS, space='exit')
    sell_crossed_timeframe53 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=53 < CONDITIONS, space='exit')
    sell_crossed_timeframe54 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=54 < CONDITIONS, space='exit')
    sell_crossed_timeframe55 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=55 < CONDITIONS, space='exit')
    sell_crossed_timeframe56 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=56 < CONDITIONS, space='exit')
    sell_crossed_timeframe57 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=57 < CONDITIONS, space='exit')
    sell_crossed_timeframe58 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=58 < CONDITIONS, space='exit')
    sell_crossed_timeframe59 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=59 < CONDITIONS, space='exit')
    sell_crossed_timeframe60 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=60 < CONDITIONS, space='exit')
    sell_crossed_timeframe61 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=61 < CONDITIONS, space='exit')
    sell_crossed_timeframe62 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=62 < CONDITIONS, space='exit')
    sell_crossed_timeframe63 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=63 < CONDITIONS, space='exit')
    sell_crossed_timeframe64 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=64 < CONDITIONS, space='exit')
    sell_crossed_timeframe65 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=65 < CONDITIONS, space='exit')
    sell_crossed_timeframe66 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=66 < CONDITIONS, space='exit')
    sell_crossed_timeframe67 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=67 < CONDITIONS, space='exit')
    sell_crossed_timeframe68 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=68 < CONDITIONS, space='exit')
    sell_crossed_timeframe69 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=69 < CONDITIONS, space='exit')
    sell_crossed_timeframe70 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=70 < CONDITIONS, space='exit')
    sell_crossed_timeframe71 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=71 < CONDITIONS, space='exit')
    sell_crossed_timeframe72 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=72 < CONDITIONS, space='exit')
    sell_crossed_timeframe73 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=73 < CONDITIONS, space='exit')
    sell_crossed_timeframe74 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=74 < CONDITIONS, space='exit')
    sell_crossed_timeframe75 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=75 < CONDITIONS, space='exit')
    sell_crossed_timeframe76 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=76 < CONDITIONS, space='exit')
    sell_crossed_timeframe77 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=77 < CONDITIONS, space='exit')
    sell_crossed_timeframe78 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=78 < CONDITIONS, space='exit')
    sell_crossed_timeframe79 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=79 < CONDITIONS, space='exit')
    sell_crossed_timeframe80 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=80 < CONDITIONS, space='exit')
    sell_crossed_timeframe81 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=81 < CONDITIONS, space='exit')
    sell_crossed_timeframe82 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=82 < CONDITIONS, space='exit')
    sell_crossed_timeframe83 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=83 < CONDITIONS, space='exit')
    sell_crossed_timeframe84 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=84 < CONDITIONS, space='exit')
    sell_crossed_timeframe85 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=85 < CONDITIONS, space='exit')
    sell_crossed_timeframe86 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=86 < CONDITIONS, space='exit')
    sell_crossed_timeframe87 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=87 < CONDITIONS, space='exit')
    sell_crossed_timeframe88 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=88 < CONDITIONS, space='exit')
    sell_crossed_timeframe89 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=89 < CONDITIONS, space='exit')
    sell_crossed_timeframe90 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=90 < CONDITIONS, space='exit')
    sell_crossed_timeframe91 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=91 < CONDITIONS, space='exit')
    sell_crossed_timeframe92 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=92 < CONDITIONS, space='exit')
    sell_crossed_timeframe93 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=93 < CONDITIONS, space='exit')
    sell_crossed_timeframe94 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=94 < CONDITIONS, space='exit')
    sell_crossed_timeframe95 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=95 < CONDITIONS, space='exit')
    sell_crossed_timeframe96 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=96 < CONDITIONS, space='exit')
    sell_crossed_timeframe97 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=97 < CONDITIONS, space='exit')
    sell_crossed_timeframe98 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=98 < CONDITIONS, space='exit')
    sell_crossed_timeframe99 = CategoricalParameter(timeframes, default=timeframes[0], optimize=0 < CONDITIONS, space='exit')if COSTUMETFENABLED else IntParameter(
        timeframes[0], timeframes[-1], default=timeframes[0], optimize=99 < CONDITIONS, space='exit')

    sell_real0 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=0 < CONDITIONS, space='exit')
    sell_real1 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=1 < CONDITIONS, space='exit')
    sell_real2 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=2 < CONDITIONS, space='exit')
    sell_real3 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=3 < CONDITIONS, space='exit')
    sell_real4 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=4 < CONDITIONS, space='exit')
    sell_real5 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=5 < CONDITIONS, space='exit')
    sell_real6 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=6 < CONDITIONS, space='exit')
    sell_real7 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=7 < CONDITIONS, space='exit')
    sell_real8 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=8 < CONDITIONS, space='exit')
    sell_real9 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=9 < CONDITIONS, space='exit')
    sell_real10 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=10 < CONDITIONS, space='exit')
    sell_real11 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=11 < CONDITIONS, space='exit')
    sell_real12 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=12 < CONDITIONS, space='exit')
    sell_real13 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=13 < CONDITIONS, space='exit')
    sell_real14 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=14 < CONDITIONS, space='exit')
    sell_real15 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=15 < CONDITIONS, space='exit')
    sell_real16 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=16 < CONDITIONS, space='exit')
    sell_real17 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=17 < CONDITIONS, space='exit')
    sell_real18 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=18 < CONDITIONS, space='exit')
    sell_real19 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=19 < CONDITIONS, space='exit')
    sell_real20 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=20 < CONDITIONS, space='exit')
    sell_real21 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=21 < CONDITIONS, space='exit')
    sell_real22 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=22 < CONDITIONS, space='exit')
    sell_real23 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=23 < CONDITIONS, space='exit')
    sell_real24 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=24 < CONDITIONS, space='exit')
    sell_real25 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=25 < CONDITIONS, space='exit')
    sell_real26 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=26 < CONDITIONS, space='exit')
    sell_real27 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=27 < CONDITIONS, space='exit')
    sell_real28 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=28 < CONDITIONS, space='exit')
    sell_real29 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=29 < CONDITIONS, space='exit')
    sell_real30 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=30 < CONDITIONS, space='exit')
    sell_real31 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=31 < CONDITIONS, space='exit')
    sell_real32 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=32 < CONDITIONS, space='exit')
    sell_real33 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=33 < CONDITIONS, space='exit')
    sell_real34 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=34 < CONDITIONS, space='exit')
    sell_real35 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=35 < CONDITIONS, space='exit')
    sell_real36 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=36 < CONDITIONS, space='exit')
    sell_real37 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=37 < CONDITIONS, space='exit')
    sell_real38 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=38 < CONDITIONS, space='exit')
    sell_real39 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=39 < CONDITIONS, space='exit')
    sell_real40 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=40 < CONDITIONS, space='exit')
    sell_real41 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=41 < CONDITIONS, space='exit')
    sell_real42 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=42 < CONDITIONS, space='exit')
    sell_real43 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=43 < CONDITIONS, space='exit')
    sell_real44 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=44 < CONDITIONS, space='exit')
    sell_real45 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=45 < CONDITIONS, space='exit')
    sell_real46 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=46 < CONDITIONS, space='exit')
    sell_real47 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=47 < CONDITIONS, space='exit')
    sell_real48 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=48 < CONDITIONS, space='exit')
    sell_real49 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=49 < CONDITIONS, space='exit')
    sell_real50 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=50 < CONDITIONS, space='exit')
    sell_real51 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=51 < CONDITIONS, space='exit')
    sell_real52 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=52 < CONDITIONS, space='exit')
    sell_real53 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=53 < CONDITIONS, space='exit')
    sell_real54 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=54 < CONDITIONS, space='exit')
    sell_real55 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=55 < CONDITIONS, space='exit')
    sell_real56 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=56 < CONDITIONS, space='exit')
    sell_real57 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=57 < CONDITIONS, space='exit')
    sell_real58 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=58 < CONDITIONS, space='exit')
    sell_real59 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=59 < CONDITIONS, space='exit')
    sell_real60 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=60 < CONDITIONS, space='exit')
    sell_real61 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=61 < CONDITIONS, space='exit')
    sell_real62 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=62 < CONDITIONS, space='exit')
    sell_real63 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=63 < CONDITIONS, space='exit')
    sell_real64 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=64 < CONDITIONS, space='exit')
    sell_real65 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=65 < CONDITIONS, space='exit')
    sell_real66 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=66 < CONDITIONS, space='exit')
    sell_real67 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=67 < CONDITIONS, space='exit')
    sell_real68 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=68 < CONDITIONS, space='exit')
    sell_real69 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=69 < CONDITIONS, space='exit')
    sell_real70 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=70 < CONDITIONS, space='exit')
    sell_real71 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=71 < CONDITIONS, space='exit')
    sell_real72 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=72 < CONDITIONS, space='exit')
    sell_real73 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=73 < CONDITIONS, space='exit')
    sell_real74 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=74 < CONDITIONS, space='exit')
    sell_real75 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=75 < CONDITIONS, space='exit')
    sell_real76 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=76 < CONDITIONS, space='exit')
    sell_real77 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=77 < CONDITIONS, space='exit')
    sell_real78 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=78 < CONDITIONS, space='exit')
    sell_real79 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=79 < CONDITIONS, space='exit')
    sell_real80 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=80 < CONDITIONS, space='exit')
    sell_real81 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=81 < CONDITIONS, space='exit')
    sell_real82 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=82 < CONDITIONS, space='exit')
    sell_real83 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=83 < CONDITIONS, space='exit')
    sell_real84 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=84 < CONDITIONS, space='exit')
    sell_real85 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=85 < CONDITIONS, space='exit')
    sell_real86 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=86 < CONDITIONS, space='exit')
    sell_real87 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=87 < CONDITIONS, space='exit')
    sell_real88 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=88 < CONDITIONS, space='exit')
    sell_real89 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=89 < CONDITIONS, space='exit')
    sell_real90 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=90 < CONDITIONS, space='exit')
    sell_real91 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=91 < CONDITIONS, space='exit')
    sell_real92 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=92 < CONDITIONS, space='exit')
    sell_real93 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=93 < CONDITIONS, space='exit')
    sell_real94 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=94 < CONDITIONS, space='exit')
    sell_real95 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=95 < CONDITIONS, space='exit')
    sell_real96 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=96 < CONDITIONS, space='exit')
    sell_real97 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=97 < CONDITIONS, space='exit')
    sell_real98 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=98 < CONDITIONS, space='exit')
    sell_real99 = DecimalParameter(
        reals[0], reals[-1], default=reals[0], decimals=DECIMALS, optimize=99 < CONDITIONS, space='exit')
    ###############################################################

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe1 = dataframe.shift(1)
        # print(timeframes)
        for indicator in indicators:
            for tf_idx in timeframes:
                tf_idx = int(tf_idx)
                try:
                    dataframe[f'{indicator}-{tf_idx}'] = getattr(
                        ta, indicator)(dataframe1, timeperiod=tf_idx)
                except:
                    try:
                        dataframe[f'{indicator}-{tf_idx}'] = getattr(
                            ta, indicator)(dataframe1, timeperiod=float(tf_idx))
                    except:
                        try:
                            dataframe[f'{indicator}-{tf_idx}'] = getattr(ta, indicator)(
                                dataframe1,  timeperiod=tf_idx).iloc[:, 0]
                        except:
                            raise
        # print(dataframe.keys())
        # print("\t",metadata['pair'],end="\h")
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions = []

        for i in range(CONDITIONS):
            i = str(i)
            indicator = f'{getattr(self,"indicator"+i).value}'
            crossed = f'{getattr(self,"crossed"+i).value}'
            timeframe = f'{getattr(self,"timeframe"+i).value}'
            crossed_timeframe = f'{getattr(self,"crossed_timeframe"+i).value}'
            formula = f'{getattr(self,"formula"+i).value}'

            A = dataframe[f'{indicator}-{timeframe}']
            B = dataframe[f'{crossed}-{crossed_timeframe}']
            R = pd.Series([float(f'{getattr(self,"real"+i).value}')]*len(A))
            df = pd.DataFrame({'A': A, 'B': A, 'R': R})

            conditions.append(df.eval(formula))

        if conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'entry']=1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        conditions = []

        formula = []
        max_loop = CONDITIONS
        i = 0
        last_df = pd.DataFrame
        last_opr = None
        for i in range(CONDITIONS):
            i = str(i)
            indicator = f'{getattr(self,"sell_indicator"+i).value}'
            crossed = f'{getattr(self,"sell_crossed"+i).value}'
            tf_idx = f'{getattr(self,"sell_timeframe"+i).value}'
            crossed_timeframe_idx = f'{getattr(self,"sell_crossed_timeframe"+i).value}'
            formula = f'{getattr(self,"sell_formula"+i).value}'

            A = dataframe[f'{indicator}-{tf_idx}']
            B = dataframe[f'{crossed}-{crossed_timeframe_idx}']
            R = pd.Series([float(f'{getattr(self,"sell_real"+i).value}')]*len(A))
            df = pd.DataFrame({'A': A, 'B': A, 'R': R})

            conditions.append(df.eval(formula))

        if conditions:
            dataframe.loc[
                reduce(lambda x, y: x & y, conditions),
                'exit_long']=1

        return dataframe

