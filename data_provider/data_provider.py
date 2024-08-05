import ccxt
import pandas as pd
from datetime import timedelta

from utils.logger import subtract_hours_from_timestamp
from utils.make_data import calculate_k_line


# 定义数据提供类
class DataProvider:
    def __init__(self, symbol='BTC/USDT', timeframe='1h'):
        # self.exchange = getattr(ccxt, exchange_name)()  # 动态获取指定交易所的实例
        self.exchange = ccxt.binance()
        self.exchange.https_proxy = 'http://127.0.0.1:7890/'
        self.symbol = symbol  # 设置交易对
        self.timeframe = timeframe  # 设置时间框架

    # 定义方法，用于获取数据
    def fetch_data(self, start_time):
        # 从交易所获取数据
        data = self.exchange.fetch_ohlcv(self.symbol, self.timeframe, since=self.exchange.parse8601(start_time))
        # 将数据转换为pandas DataFrame
        df = pd.DataFrame(data, dtype=float)
        # 重命名
        df.rename(columns={0: 'MTS', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'}, inplace=True)
        # 整理时间
        df['candle_begin_time'] = pd.to_datetime(df['MTS'], unit='ms')
        # 北京时间
        df['candle_begin_time_GMT8'] = df['candle_begin_time'] + timedelta(hours=8)
        # 整理列的顺序
        df = df[['candle_begin_time_GMT8', 'open', 'high', 'low', 'close', 'volume']]
        return df

    # 定义方法，用于获取指定数据
    def fetch_single_data(self, start_time, point_number=2):
        # 时间先减去8
        start_time = subtract_hours_from_timestamp(start_time)
        # 从交易所获取数据
        data = self.exchange.fetch_ohlcv(
            self.symbol, self.timeframe, since=self.exchange.parse8601(start_time), limit=1
        )
        # 将数据转换为pandas DataFrame
        df = pd.DataFrame(data, dtype=float)
        # 重命名
        df.rename(columns={0: 'MTS', 1: 'open', 2: 'high', 3: 'low', 4: 'close'}, inplace=True)
        # 整理时间
        df['candle_begin_time'] = pd.to_datetime(df['MTS'], unit='ms')
        # 北京时间
        df['candle_begin_time_GMT8'] = df['candle_begin_time'] + timedelta(hours=8)
        # 整理列的顺序
        df = df[['candle_begin_time_GMT8', 'open', 'high', 'low', 'close']]
        df_dict = df.to_dict()
        kline_data1 = {
            'candle_begin_time_GMT8': f"{df_dict['candle_begin_time_GMT8'][0]}",
            'trading_target': self.symbol,
            'open': df_dict['open'][0],
            'high': df_dict['high'][0],
            'low': df_dict['low'][0],
            'close': df_dict['close'][0],
        }
        kline_data2 = calculate_k_line(kline_data1, point_number)
        return {**kline_data1, **kline_data2}



