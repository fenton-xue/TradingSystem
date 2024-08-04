import requests


class BinanceKlineFetcher:
    def __init__(self):
        self.api_url = 'https://api.binance.com/api/v3/klines'
        self.proxies = {
            'http': 'http://127.0.0.1:7890/',
            'https': 'http://127.0.0.1:7890/'
        }

    def fetch_kline(self, symbol, interval, start_time):
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': int(start_time.timestamp() * 1000),
            'endTime': int((start_time.timestamp() + 3600) * 1000) - 1
        }
        response = requests.get(self.api_url, params=params, proxies=self.proxies)
        if response.status_code == 200:
            kline = response.json()
            if kline:
                return kline[0]
        return None
