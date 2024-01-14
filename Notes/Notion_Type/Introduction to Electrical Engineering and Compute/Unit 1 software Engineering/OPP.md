# OPP

Owner: Kasen Jones

[第 1 节讲义：面向对象编程 (PDF)](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/resources/mit6_01scs11_ses01/)

reading chapters:

- [第 1 章：课程概述 (PDF)](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/resources/mit6_01scs11_chap01/)
- [第 2 章：学习使用 Python 编程 (PDF)](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/resources/mit6_01scs11_chap02/)
- [第 3 章：程序和数据 (PDF - 1.6MB)](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/resources/mit6_01scs11_chap03/)

---

# Lecture  Notes  讲义笔记

主旨：

- Primitives lead to combinations via composition（Primitives）
通过组合不同的原语来创建另外的组合（功能和算法等）。
- 如果一种特定的组合频繁出现，它就可以被认作一种新的模式
- 如果我们想与模式进行交互，而不是与原语或者组合交互，我们创建一个抽象。一个程序就是这种抽象的例子。
- 环境：在最局限的范围内查找给定变量的绑定。如果找到，返回绑定，否则，检查副作用域。如此重复直到找到一个赋值，或者到达全局作用域。
- 类和实例都是环境
- pat.saluatation() 和 staff601.salutation() 完全相同。

 

这周都是关于编程的:原语，表达式，赋值，函数，环境，OOP和继承。

## Vocabulary:

**Theory**

- [PCAP](OPP%204afe672140744fca83853cc411403389.md) 原始组合抽象模式 （*primitive-combinationabstraction-pattern*）
- Interpreter (versus Compiler) [解释器](https://zh.wikipedia.org/zh-cn/%E7%9B%B4%E8%AD%AF%E5%99%A8)
- Expression 表达式
- Variable 变量
- Structured Data 结构化数据
- Mutation 突变：在程序执行过程中修改变量的值
- Aliasing 别名：多个名称（引用）指向昂相同的内存位置或者资源。
- Procedures and Procedure Calls 过程和过程调用

![Untitled](OPP%204afe672140744fca83853cc411403389/Untitled.png)

- Non-Local Reference  非局部引用：程序引用不属于当前作用域上下文的变量或者数据。
- Environments 环境：是数据结构，是程序执行时存储变量、函数和其他绑定（Blindings）的地方
Bindings:  指将名称（变量或标识符等）和特定实体（内存中的值、函数和其他数据）关联起来的过程
- Functions as First-Class Objects 一等对象：将函数视为一等对象（First-Class Objects）意味着函数可以像其他数据类型一样被操作、传递和使用
- Object Oriented Programming OOP: 将程序中的数据（对象）和操作数据的行为（方法或函数）组织成为单个实体，即“对象”
- Class 类
- Instance 实例
- Method 方法：类中的函数称为方法
- Object 对象 ：类的实例
- Inheritance 继承：允许一个类（子类）继承另一个类（父类）的属性和方法
- Recursion 递归：函数直接或间接地调用自身的过程

# Lecture Note 讲座笔记

EECS : 电气工程和计算机科学

机器人转向

多项式（Polynomial）是代数学中的一个重要概念，它是由变量和常数通过加法、减法以及乘法运算得到的表达式。一个多项式通常被表示为单个变量的项的和，每一项包括一个系数乘以变量的幂。

一个一元多项式的一般形式可以写作：

![Untitled](OPP%204afe672140744fca83853cc411403389/Untitled%201.png)

P(x) 表示多项式函数，an,an-1,…..,a1,a0,是常数系数，x是变量，n是多项式的最高次数

![Untitled](OPP%204afe672140744fca83853cc411403389/Untitled%202.png)

自然语言：
        自然语言是人类使用的基于语音或书面形式的交流工具。它是一种复杂的沟通系统，由词汇、语法、语义和语用学组成，用于传达思想、情感和信息。自然语言不是由人为设计或规划的，而是随着时间、文化和社会的演变而形成的

def : associates a name with an expression

使程序、数据结构等与名称相关联

定义类后使用类来定义实例，实例继承了所以类的结构

```jsx
class Student:
	school = "MIT"
	def calculateFinalGrade():
		..........
		return theFinalGrade
mary = Student()  # marry 为Student类的实例
marry.section()  # section方法
john = Student()
john.select = 4
```

[.] dot, 点符号，[环境].[变量] 

在类 class 中可以通过”__str__“方法返回一个字符串，该字符串提供Thing类的实例的信息。

```jsx
class Thing:
    def set(self, v):
        self.x = v

    def get(self):
        return self.x

    def clone(self):
        new_thing = Thing()
        new_thing.set(self.get())
        return new_thing

    def __str__(self):
        return f"This is a Thing with value {self.get()}"

a = Thing()
a.set(3)
print(a)  # 输出: This is a Thing with value 3
```

## Chapter 1 notes 绪论

我们通常可以通过限制可能的设计空间，并通过标准化：

1、原始组件的基础集，使设计工作更容易；

2、组合原始组件制作更复杂系统的方法；

3、“包装”或抽象设计片段的方法，以便它们可以重用（本质上创建新的“原语”）；

4、以及捕获常见抽象模式的方法（本质上，抽象我们的抽象）。

使用这种原始组合抽象模式（PCAP）方法，非常复杂的设计问题可以变得容易处理

关于抽象模型的一个要点：一旦我们修复了抽象，通常就可以使用各种不同的底层底层来实现它

关于抽象模型的一个非常重要的事情是，一旦我们修复了抽象，通常就可以使用各种不同的底层底层来实现它

组合电路元件的方法是将它们的端子和导体（导线，crimps，solder，etc.) 连接起来，这一过程称为布线（wiring）。我们这里的抽象方法是描述电路元件对其所连接的端子的电流和电压施加的约束。

电路中电压输入和输出关系：

![Untitled](OPP%204afe672140744fca83853cc411403389/Untitled%203.png)

如果RA = RB，那么Vout = Vin/2。或者，在我们的例子中，如果RA实际上随着照射在它上面的光的量而变化，那么Vout也会随着光的量而变化。

![Untitled](OPP%204afe672140744fca83853cc411403389/Untitled%204.png)

我们可以用一些额外的组件来增加我们的模拟电路工具箱，这些组件允许我们设计具有模块化行为的组件;它们“缓冲”或“隔离”电路的一部分与另一部分，使我们能够更容易地组合这些部分。

好的模块在使用模块和如何构造模块的内部细节之间保留了抽象障碍（abstraction barriers）。

### Chapter 2  and Chapter 3

 [https://docs.python.org](https://docs.python.org/zh-cn/3/tutorial/index.html) 

任意Python教程

PCAP

Primitives, Composition, Abstraction, and Patterns、

原语， 组合，抽象， 模式