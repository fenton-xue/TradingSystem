from strategies.base_strategy import BaseStrategy


# 定义Pinbar策略类，继承自BaseStrategy
class DojiStrategy(BaseStrategy):

    def apply(self, data):

        def is_doji(row):
            k_line = calculate_k_line(row)
            is_doji = k_line['body'] / k_line['long'] < 0.15
            return is_doji

        # 应用is_doji函数，生成一个新的列'doji'，标记每行是否为doji形态
        data['doji'] = data.apply(is_doji, axis=1)
        # 返回所有标记为Pinbar形态的行
        return data[data['doji']]
