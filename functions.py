from enums import ohlcv

def ohlcv5to15 (ohlcv5):

    ohlcv15 = []

    if len(ohlcv5) > 2:
        for i in range(0, len(ohlcv5) - 2, 3):
            highs = [ohlcv5[i + j][ohlcv.HIGH] for j in range(0, 3) if ohlcv5[i + j][ohlcv.HIGH]]
            lows = [ohlcv5[i + j][ohlcv.LOW] for j in range(0, 3) if ohlcv5[i + j][ohlcv.LOW]]
            volumes = [ohlcv5[i + j][ohlcv. VOLUME] for j in range(0, 3) if ohlcv5[i + j][ohlcv.VOLUME]]
            candle = [
                ohlcv5[i + 0][ohlcv.TIMESTAMP],
                ohlcv5[i + 0][ohlcv.OPEN],
                max(highs) if len(highs) else None,
                min(lows) if len(lows) else None,
                ohlcv5[i + 2][ohlcv.CLOSE],
                sum(volumes) if len(volumes) else None,
            ]
            ohlcv15.append(candle)
    else:
        raise Exception('Too few 5m candles')

    return ohlcv15