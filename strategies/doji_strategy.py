from strategies.base_strategy import BaseStrategy
from utils.pattern_utils import calculate_k_line


# 定义Pinbar策略类，继承自BaseStrategy
class DojiStrategy(BaseStrategy):
    @staticmethod
    def check_doji(row):
        """
        检查给定行数据是否符合Doji形态。
        :param row: 单行数据（Series）
        :return: True 如果是Doji形态，否则为False
        """
        k_line = calculate_k_line(row)  # 计算K线指标
        # 判断是否为Doji形态，通常是实体(body)与影线(long)的比例较小
        return k_line['body'] / k_line['long'] < 0.15

    def apply(self, data):
        """
        应用策略到数据，标记Doji形态。
        :param data: 包含K线数据的DataFrame
        :return: 只包含Doji形态的行的DataFrame
        """
        # 应用check_doji函数，生成一个新的列'doji'，标记每行是否为Doji形态
        data['doji'] = data.apply(self.check_doji, axis=1)
        # 返回所有标记为Doji形态的行
        return data[data['doji']]
