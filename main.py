from data_provider.data_provider import DataProvider  # 导入数据提供类
from strategies.doji_strategy import DojiStrategy
from strategies.pinbar_strategy import PinbarStrategy  # 导入Pinbar策略类
from strategies.moving_average_strategy import MovingAverageStrategy  # 导入移动平均策略类
from utils.logger import get_logger, output_to_file  # 导入日志记录函数


# 获取日志记录器实例
logger = get_logger(__name__)


# 定义函数，用于执行策略
def execute_strategy(strategy, data):
    return strategy.apply(data)  # 应用策略


if __name__ == "__main__":
    data_provider = DataProvider("ATOM/USDT", "1h")  # 创建数据提供类实例
    data = data_provider.fetch_data('2024-07-15T00:00:00Z')  # 获取数据
    # data = data_provider.fetch_single_data('2024-08-04T10:00:00Z')  # 获取数据
    # output_to_file(data)
    # print(data)

    # 使用Pinbar策略
    # pinbar_strategy = PinbarStrategy()
    # pinbar_signals = execute_strategy(pinbar_strategy, data)

    # 使用Doji策略
    # doji_strategy = DojiStrategy()
    # doji_signals = execute_strategy(doji_strategy, data)

    # 使用移动平均策略
    ma_strategy = MovingAverageStrategy()  # 创建移动平均策略类实例
    pinbar_or_doji_intersect_ma = execute_strategy(ma_strategy, data)  # 执行移动平均策略

    # logger.info(f'此处有Pinbar/Doji和均线交叉: {pinbar_or_doji_intersect_ma}')  # 记录移动平均策略信号
    # 筛选 Pinbar_21EMA_Cross 或 Pinbar_144EMA_Cross 为 True 的行
    filtered_data = data[
        (data['21EMA_Cross'] == True) | (data['100MA_Cross'] == True)]
    # print(pinbar_or_doji_intersect_ma)
    output_to_file(filtered_data)
