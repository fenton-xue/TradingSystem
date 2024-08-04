from abc import ABC, abstractmethod


# 定义一个抽象基类，用于所有策略类的基类
class BaseStrategy(ABC):
    @abstractmethod         # 抽象方法装饰器，要求子类必须实现该方法
    def apply(self, data):  # 定义一个抽象方法apply，用于应用策略
        pass
