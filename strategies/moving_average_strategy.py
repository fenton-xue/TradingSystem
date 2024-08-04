from strategies.base_strategy import BaseStrategy


# 定义移动平均策略类，继承自BaseStrategy
class MovingAverageStrategy(BaseStrategy):
    def apply(self, data):
        # 计算短期移动平均线
        data['ma_short'] = data['close'].rolling(window=20).mean()
        # 计算长期移动平均线
        data['ma_long'] = data['close'].rolling(window=50).mean()
        # 判断短期均线是否大于长期均线，生成信号
        data['signal'] = data['ma_short'] > data['ma_long']
        # 返回所有信号为真的行
        return data[data['signal']]
