import pandas as pd
import ccxt
from datetime import timedelta

exchange = ccxt.binance()
exchange.https_proxy = 'http://127.0.0.1:7890'

symbol = 'BTC/USDT'
time_inteval = '15m'
bar_num = 100

ohlcv = exchange.fetch_ohlcv(symbol=symbol, timeframe=time_inteval, limit=bar_num)
# print(ohlcv)

# --整理数据
# 将数据转换为dataframe
df = pd.DataFrame(ohlcv, dtype=float)
# 重命名
df.rename(columns={0: 'MTS', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'}, inplace=True)
# 整理时间
df['candle_begin_time'] = pd.to_datetime(df['MTS'], unit='ms')
# 北京时间
df['candle_begin_time_GMT8'] = df['candle_begin_time'] + timedelta(hours=8)
# 整理列的顺序
df = df[['candle_begin_time_GMT8', 'open', 'high', 'low', 'close', 'volume']]

print(df)
