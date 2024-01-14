# 2.3.1
# a1
# b2
# c1

# 2.3.2
class AccountPounds:
    Dollar2Pound_conversion = 2
    def __init__(self, ini):
        self.dollars = ini*self.Dollar2Pound_conversion

    def dd(self, depo):
        self.dollars += depo
        self.dollars = self._apply(self.dollars)
        return self.dollars

    def dp(self, dp):
        dollars = dp*self.Dollar2Pound_conversion
        return self.dp(dollars)

    def _apply(self, balance):
        return balance

x = AccountPounds(1)
# print(x.dp(3))
# print(x.dd(2))

# 2.3.4
# part 1
'''
分段函数表示
a,         if b = 0
f(a, b-1)  if b > 0

要写出递归函数，经可能先写出其分段函数表达式，这样就很简单了
'''
def add(a, b):
    if b == 0:
        return a
    else:
        return add(a, b-1) + 1
# part 2
# a can be any number and b must be a non-negative integr

# part 3
def sub(a,b):
    if b == 0:
        return a
    else:
        return sub(a-1, b-1)