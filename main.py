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
    data_provider = DataProvider()  # 创建数据提供类实例
    # data = data_provider.fetch_data('2024-08-02T00:00:00Z')  # 获取数据
    data = data_provider.fetch_single_data('2024-08-04T10:00:00Z')  # 获取数据
    # output_to_file(data)
    print(data)

    # 使用Pinbar策略
    # pinbar_strategy = PinbarStrategy()  # 创建Pinbar策略类实例
    # pinbar_signals = execute_strategy(pinbar_strategy, data)  # 执行Pinbar策略
    # doji_strategy = DojiStrategy()
    # doji_signals = execute_strategy(doji_strategy, data)
    # logger.info(f'\nPinbar signals: \n{pinbar_signals}')  # 记录Pinbar策略信号
    # logger.info(f'\ndoji signals: \n{doji_signals}')  # 记录Pinbar策略信号
    #
    # # 使用移动平均策略
    # ma_strategy = MovingAverageStrategy()  # 创建移动平均策略类实例
    # ma_signals = execute_strategy(ma_strategy, data)  # 执行移动平均策略
    # logger.info(f'Moving Average signals: {ma_signals}')  # 记录移动平均策略信号
