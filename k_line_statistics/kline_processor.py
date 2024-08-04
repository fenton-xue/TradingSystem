class KlineProcessor:
    @staticmethod
    def calculate_kline_info(kline):
        open_price = float(kline[1])
        high_price = float(kline[2])
        low_price = float(kline[3])
        close_price = float(kline[4])
        upper_shadow = high_price - max(open_price, close_price)
        lower_shadow = min(open_price, close_price) - low_price
        long_shadow = max(upper_shadow, lower_shadow)
        short_shadow = min(upper_shadow, lower_shadow)
        entity = abs(close_price - open_price)
        total_length = high_price - low_price
        return open_price, high_price, low_price, close_price, long_shadow, short_shadow, entity, total_length
