"""
多项式（Polynomial）是代数学中的一个重要概念，它是由变量和常数通过加法、减法以及乘法运算得到的表达式。
一个多项式通常被表示为单个变量的项的和，每一项包括一个系数乘以变量的幂。
见 https://www.notion.so/OPP-4afe672140744fca83853cc411403389?pvs=4#e94693ff5609444fa94ded52ed1767e9

coefficients（系数）：存储多项式的各项系数，可能是一个数组或者列表。
degree（次数）：存储多项式的最高次数。

3 1 0
1 0
3 1 0
4 2 1 0
4 2 1
3 1 0
？
"""
# 多项式类:
# 多项式类是一种在编程中用来表示和操作多项式的数据结构。它通常包含多项式的系数和次数，并提供用于多项式运算的方法，比如加法、减法、乘法、求导等。


class Polynomial:
    def __init__(self, coefficients):   # 初始化方法，用来创建一个多项式对象，可能需要传入系数列表或者其他参数。
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1  # 最高次数

    def add(self, other):
        # 实现多项式加法
        pass

    def subtract(self, other):
        # 实现多项式减法
        pass

    def multiply(self, other):
        # 实现多项式乘法
        pass

    def differentiate(self):
        # 实现多项式求导
        pass

    def evaluate(self, x):
        # 计算多项式在给定值 x 处的值
        pass
