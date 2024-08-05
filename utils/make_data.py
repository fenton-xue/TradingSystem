
# 计算数据
def calculate_k_line(row, point_number):
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
        'long': round(long, int(point_number))
    }
