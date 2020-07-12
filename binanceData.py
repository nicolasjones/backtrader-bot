import backtrader.feed as btFeed
from enums import ohlcv

class PandasData(btFeed.DataBase):
    params = (
        ('datetime', ohlcv.TIMESTAMP),
        ('open', ohlcv.OPEN),
        ('high', ohlcv.HIGH),
        ('low', ohlcv.LOW),
        ('close', ohlcv.CLOSE),
        ('volume', ohlcv.VOLUME),
)