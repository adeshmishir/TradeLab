from backtesting import Backtest, Strategy
from backtesting.test import GOOG, SMA
from backtesting.lib import crossover

class SmaCross(Strategy):
    def init(self):
        self.ma1 = self.I(SMA, self.data.Close, 10)
        self.ma2 = self.I(SMA, self.data.Close, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.position.close()
            self.buy(size=0.95)
        elif crossover(self.ma2, self.ma1):
            self.position.close()

bt = Backtest(
    GOOG,
    SmaCross,
    cash=10000,
    commission=0.002,
    exclusive_orders=True
)

stats = bt.run()
print(stats)

bt.plot()