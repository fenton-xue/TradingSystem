# 计算数据
def calculate_k_line(row, point_number=2):
    # 计算实体长度
    body = abs(row['close'] - row['open'])
    # 计算上影线长度
    upper_shadow = row['high'] - max(row['close'], row['open'])
    # 计算下影线长度
    lower_shadow = min(row['close'], row['open']) - row['low']
    # 定义长影线
    long_shadow = max(upper_shadow, lower_shadow)
    # 定义短影线
    short_shadow = min(upper_shadow, lower_shadow)
    # 定义总长
    long = row['high'] - row['low']
    return {
        'body': round(body, int(point_number)),
        'long_shadow': round(long_shadow, int(point_number)),
        'short_shadow': round(short_shadow, int(point_number)),
        'long': round(long, int(point_number)),
        'upper_shadow': round(upper_shadow, int(point_number)),
        'lower_shadow': round(lower_shadow, int(point_number))
    }


def check_pinbar(row):
    """
    判断给定的K线是否为Pinbar形态。
    :param row: 单行数据（Series）
    :return: True 如果是Pinbar形态，否则为False
    """
    k_line = calculate_k_line(row)
    is_pinbar = k_line['body'] * 0.6 >= k_line['short_shadow'] and k_line['long_shadow'] > k_line['body']
    return is_pinbar


def check_doji(row):
    """
    判断给定的K线是否为Doji形态。
    :param row: 单行数据（Series）
    :return: True 如果是Doji形态，否则为False
    """
    k_line = calculate_k_line(row)
    return k_line['body'] / k_line['long'] < 0.15
