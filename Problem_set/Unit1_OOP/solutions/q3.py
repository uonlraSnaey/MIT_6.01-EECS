class Car:
    weight = 1000

    def __init__(self, weight, driver):
        self.weight = weight
        self.driver = driver


class Person:
    """
    >>> Person.weight
    100
    >>> p = Person(150) # p 为Person实例
    >>> p
    instance
    >>> c = Car(2000, p)
    >>> Car.weight

    """
    weight = 100

    def __init__(self, weight):
        self.weight = weight


print(Person)  # <class 'q3.Person'> 表明Person类属于'q3'这个python模块
# 创建一个Person实例，对Person进行实例化，并传入‘150’参数
p = Person(150)
print(p)
c = Car(2000, p)
print(Car.weight)
print(c.weight)
print(c.driver.weight)  # c.drive->p, p.weight = 150
