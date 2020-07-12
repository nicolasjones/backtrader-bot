import backtrader as bt
import ccxt
import time
import config
import binanceData
import exchange
from enums import ohlcv
import init
from emaCrossSt import EmaCross
import functions as func
import telepot
from pprint import pprint

exch = exchange.Exchange(init.EXCH)
exch.connect(config.binance.APIKEY, config.binance.SECRET)

ohlcv5 = exch.fetch_ohlcv(init.SYMBOL, init.PERIOD)
#ohlcv15 = func.ohlcv5to15(ohlcv5)

TelegramBot = telepot.Bot("1394250605:AAFXW2dQyIPB2DOhxT7oHsgylERctDIsgp8")
response = TelegramBot.getChatMembersCount("1250285981_15503845255433032185")
pprint (response)


def handle (msg):
    pprint(msg)

TelegramBot.message_loop(handle)

#chat = TelegramBot.getChatMembersCount("-1001250285981")
#print (chat)

#cerebro = bt.Cerebro()
#cerebro.addstrategy(EmaCross)
#data = bt.feeds.PandasData(dataname=dataframe)
#cerebro.adddata(data)

#cerebro.run()
#cerebro.plot()