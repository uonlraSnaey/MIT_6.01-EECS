#斐波那契 F(n)=F(n−1)+F(n−2)。其中，
def fib(n):
    if n < 0:
        return "Error inputs"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(11):
    print(f"第{i}项为：{fib(i)}")