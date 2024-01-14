"""
# 编写一个状态机类 Delay2Machine，它继承自 sm.SM 类。
# 这个状态机类会将输入延迟两个时间步骤，即在时间 i 时刻的输出是时间 i-2 时刻的输入。
# 类应该接受两个参数，它们将是机器在时间0和1时刻的输出。
"""
class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = (val0, val1)

    def getNextValues(self, state, inp):
        val0, val1 = state
        return ((val1, inp), val0)

# 示例实例化
sm = Delay2Machine(100, 10)

# 测试
for i in range(5):
    input_value = i * 10
    (state, output) = sm.getNextValues(sm.startState, input_value)
    print(f"Input: {input_value}, Output: {output}")
