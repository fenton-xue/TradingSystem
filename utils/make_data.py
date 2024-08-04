
# 计算数据
def calculate_k_line(row):
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
        'body': round(body, 2),
        'long_shadow': round(long_shadow, 2),
        'short_shadow': round(short_shadow, 2),
        'long': round(long, 2)
    }
