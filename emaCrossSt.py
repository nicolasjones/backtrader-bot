from backtrader import Strategy
from backtrader.indicators import (CrossOver, EMA)

class EmaCross(Strategy):
    params = (
        ('fast', 10),
        ('slow', 30),
    )
    crossover = 0.0

    def __init__(self):
        emaFast = EMA(period=self.p.fast)
        emaSlow = EMA(period=self.p.slow)
        self.crossover = CrossOver(emaFast, emaSlow)

    def next(self):
       
        if self.crossover >= 1.0:
            #self.order_target_size(target=1)
            #print("Buy {} shares".format(self.data.close[0]))
            print("OK")