from strategies.base_strategy import BaseStrategy
from utils.pattern_utils import calculate_k_line


# 定义Pinbar策略类，继承自BaseStrategy
class PinbarStrategy(BaseStrategy):
    @staticmethod
    def check_pinbar(row):
        k_line = calculate_k_line(row)
        # 判断Pinbar 和 Doji
        # 1、短影线不超过实体的60%，并且，长影线大于实体
        is_pinbar = k_line['body'] * 0.6 >= k_line['short_shadow'] and k_line['long_shadow'] > k_line['body']
        # 判断是否满足Pinbar形态的条件
        return is_pinbar

    def apply(self, data):
        # 应用is_pinbar函数，生成一个新的列'pinbar'，标记每行是否为Pinbar形态
        data['pinbar'] = data.apply(self.check_pinbar, axis=1)
        # 返回所有标记为Pinbar形态的行
        return data[data['pinbar']]
