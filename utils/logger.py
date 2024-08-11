import logging  # 导入logging库，用于日志记录
import pandas as pd
from datetime import datetime, timedelta

# 定义函数，用于获取日志记录器
def get_logger(name):
    logger = logging.getLogger(name)  # 获取日志记录器实例
    if not logger.hasHandlers():  # 检查日志记录器是否已有处理器
        handler = logging.StreamHandler()  # 创建流处理器
        # 创建日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)  # 设置处理器的格式
        logger.addHandler(handler)  # 将处理器添加到日志记录器
        logger.setLevel(logging.INFO)  # 设置日志记录级别
    return logger  # 返回日志记录器实例


# 输出结果到文件
def output_to_file(data):
    # 获取当前时间并格式化
    now = datetime.now()
    current_time = now.strftime("%Y%m%dT%H：%M：%S")
    # 文件名
    filepath = f"E:\\WorkSpace\\PythonCode\\TradingSystem\\TradingSystem\\output\\{current_time}.log"

    # 使用with语句打开文件并写入内容
    with open(filepath, 'w', encoding='utf-8') as file:
        if isinstance(data, pd.DataFrame):
            # 如果data是DataFrame，使用to_string()方法转换为字符串
            file.write(data.to_string())
        else:
            # 否则直接写入字符串内容
            file.write(str(data))
    print(f"内容已写入到文件：{filepath}")


def subtract_hours_from_timestamp(timestamp_str, hours=8):
    """
    将给定的时间字符串减去指定的小时数。

    :param timestamp_str: 时间字符串，格式为'YYYY-MM-DDTHH:MM:SSZ'
    :param hours: 需要减去的小时数
    :return: 新的时间字符串，格式为'YYYY-MM-DDTHH:MM:SSZ'
    """
    # 将字符串转换为datetime对象
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%SZ')

    # 减去指定的小时数
    new_timestamp = timestamp - timedelta(hours=hours)

    # 将datetime对象转换为字符串
    new_timestamp_str = new_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

    return new_timestamp_str


if __name__ == '__main__':
    # output_to_file("1")
    print(subtract_hours_from_timestamp("2023-07-01T07:00:00Z"))
