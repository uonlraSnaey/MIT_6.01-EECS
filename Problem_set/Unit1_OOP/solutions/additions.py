# 1.4.2
# part 1
c = [[[4]], [1], [[2, [-5]]], -2]

# part 2
a = [1, 2, 3]
# b = [[a[0]],a[0]]
b = [1, 1]

# part 3
a = [3, [1, 2]]
b = [a]


# 1.4.3
# part 1
# 创建一个 ‘evenSquare' 函数，接受一个数字列表作为输入，并返回该列表中的偶数值平方所组成的列表
# 使用列表推导式
def evenSquare(n):
    square = [x ** 2 for x in n if x % 2 == 0]
    return square


# part 2
# 使用列表推导式定义一个函数，接受两个输入列表，返回两个列表中每对数字的乘积累的绝对值的和
def sumAbsLst(lst1=None, lst2=None):
    if lst2 is None:
        lst2 = [2, 3]
    if lst1 is None:
        lst1 = [1, 2]
    return sum(abs(x * y) for x, y in zip(lst1, lst2))

# 1.4.4
# part 1
"""
1.6
2.对象地址 class Thing()
3.7
4.对象地址 class Thing()
5.7
6.7
7.-6
8.error
9.a
10.True
11.True
12.True
"""

# part 2
"""
6
True
class
4
error
"""
# part 3
# 在 Thing 类中添加一个 mangle 方法，与 part 2 相同
class Thing3:
    def set(self, v):
        self.x = v
    def get(self):
        return self.x
    def mangle(self):
        self.set(self.get()+1)
        self.hasBeenMangled = True

# part 4
def mangle(z):
    nt = Thing3()
    nt.set(z)
    nt.managle()
    return nt

# 1.4.5
class Thing4:
    def set(self, v):
        self.x = v

    def get(self):
        return self.x

    def clone(self):
        new_thing = Thing4()      # Create a new instance of Thing
        new_thing.set(self.get())  # Set its 'x' value to the current 'x' value
        return new_thing         # Return the new instance

# part 2
class Thing5:
    def set(self, v):
        self.x = v

    def get(self):
        return self.x

    def clone(self):
        new_thing = Thing5()
        new_thing.set(self.get())
        return new_thing

    def __str__(self):
        return f"output value is {self.get()}"
"""
a = Thing5()
a.set(3)
print(a)
"""


