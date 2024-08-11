from strategies.base_strategy import BaseStrategy
from utils.pattern_utils import check_pinbar, check_doji


class MovingAverageStrategy(BaseStrategy):
    @staticmethod
    def calculate_moving_average(data, point_number=2):
        """
        计算数据中的移动平均线。
        :param point_number:
        :param data: 包含K线数据的DataFrame
        :return: 添加了移动平均线的DataFrame
        """
        data['21EMA'] = round(data['close'].ewm(span=21, adjust=False).mean(), point_number)
        data['100MA'] = round(data['close'].rolling(window=100).mean(), point_number)
        # data['144EMA'] = round(data['close'].ewm(span=144, adjust=False).mean(), point_number)
        return data

    def apply(self, data):
        """
        应用移动平均策略，标记与Pinbar和Doji交叉的情况。
        :param data: 包含K线数据的DataFrame
        :return: 带有交叉标记的DataFrame
        """
        # 计算开盘价的小数点个数
        value_str = str(data['open'][0])
        if '.' in value_str:
            point_number = len(value_str.split('.')[1])
        else:
            point_number = 0  # 如果没有小数部分，返回0

        # 计算移动平均线
        data = self.calculate_moving_average(data, point_number)

        # 初始化交叉标记列
        # data['Pinbar_21EMA_Cross'] = False
        # data['Pinbar_100MA_Cross'] = False
        # data['Pinbar_144EMA_Cross'] = False
        #
        # data['Doji_21EMA_Cross'] = False
        # data['Doji_100MA_Cross'] = False
        # data['Doji_144EMA_Cross'] = False

        # 暂时不区分是Pinbar交叉还是Doji交叉
        data['21EMA_Cross'] = False
        data['100MA_Cross'] = False
        # data['144EMA_Cross'] = False

        # 遍历每一行，判断是否为Pinbar或Doji，以及是否与移动平均线交叉
        for index, row in data.iterrows():
            is_pinbar = check_pinbar(row)
            is_doji = check_doji(row)

            # 第一个大前提，必须是Pinbar或Doji才去计算
            if is_pinbar or is_doji:
                # 上影线长于下影线
                if row['upper_shadow'] >= row['lower_shadow']:
                    # 检查Pinbar和Doji与移动平均线交叉
                    if row['close'] <= row['21EMA'] <= row['high']:
                        data.at[index, '21EMA_Cross'] = True
                    # if row['close'] <= row['144EMA'] <= row['high']:
                    #     data.at[index, 'Pinbar_144EMA_Cross'] = True
                    #     data.at[index, 'Doji_144EMA_Cross'] = True
                    if row['close'] <= row['100MA'] <= row['high']:
                        data.at[index, '100MA_Cross'] = True
                else:
                    if row['low'] <= row['21EMA'] <= row['close']:
                        data.at[index, '21EMA_Cross'] = True
                    # if row['low'] <= row['144EMA'] <= row['close']:
                    #     data.at[index, 'Pinbar_144EMA_Cross'] = True
                    #     data.at[index, 'Doji_144EMA_Cross'] = True
                    if row['low'] <= row['100MA'] <= row['close']:
                        data.at[index, '100MA_Cross'] = True
            else:
                pass
        return data
#
# data.at[index, 'Pinbar_Cross'] = True 这一行代码的作用是将 data DataFrame 中指定位置的单元格的值设置为 True。具体来说，这一行代码做了以下事情：
#
# data: 是一个 pandas 的 DataFrame 对象，包含了你正在处理的K线数据，每一行代表一个时间点的价格数据，每一列代表不同的数据类型（如 open、high、low、close、移动平均线等）。
#
# at: 是 pandas DataFrame 提供的一种方法，用于访问和设置特定行和列的位置上的单个单元格。at 是一种基于标签的索引方式，它比 loc 更快且适合单个元素的操作。
#
# index: 是当前循环中的行索引（或行号）。在 for index, row in data.iterrows(): 这行代码中，index 是每次循环时的行索引值，用于标识当前处理的行。
#
# 'Pinbar_Cross': 是 data DataFrame 的一列名，这列用于存储是否发生了Pinbar与移动平均线的交叉情况。这个列是在代码中初始化的：data['Pinbar_Cross'] = False。
#
# True: 将 Pinbar_Cross 列中当前行的值设置为 True，表示在这一行数据对应的时间点上，Pinbar形态与移动平均线发生了交叉。
