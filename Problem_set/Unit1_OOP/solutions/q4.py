"""
二维向量是一个有两个分量的数学对象，通常表示为 [[x],[y]]
分别代表向量在 x 和 y 方向上的分量。

二维向量可以进行多种数学运算，比如加法、减法、数乘等。以下是用 Python 表示二维向量及其基本运算的示例代码
"""
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

# 创建两个二维向量
v1 = Vector2D(3, 4)
v2 = Vector2D(-1, 2)

# 向量加法
result_addition = v1 + v2
print("向量加法:", result_addition)  # 输出: (2, 6)

# 向量减法
result_subtraction = v1 - v2
print("向量减法:", result_subtraction)  # 输出: (4, 2)

# 数乘
scalar = 2
result_scalar_mul = v1 * scalar
print("数乘:", result_scalar_mul)  # 输出: (6, 8)
