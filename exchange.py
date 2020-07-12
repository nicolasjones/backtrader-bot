import enums
import ccxt

class Exchange:
    __exchange = ""
    __cctx = None

    def __init__(self, ex): 
        self.__exchange = ex

    def connect(self, apiKey, secret): 
        account = {'exchange_id': self.__exchange, 
                'params': 
                        {'id': self.__exchange, 
                        'apiKey': apiKey, 
                        'secret': secret
                        }
                    }
        try:
            exchange_class = getattr(ccxt, account['exchange_id'])
            self.__cctx = exchange_class(account['params'])
        except:
            print("An exception occurred") 

    def fetch_ohlcv(self, SYMBOL, PERIOD):
        return self.__cctx.fetch_ohlcv(SYMBOL, PERIOD)

    def order (self):
        #A desarrollar
        return 0