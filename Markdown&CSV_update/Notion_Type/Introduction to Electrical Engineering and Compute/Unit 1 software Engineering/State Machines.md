# State Machines

Owner: Kasen Jones

状态机对具有功能也具有内存的系统进行建模。

讲义：

• [第 2 节讲义：状态机 (PDF)](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/resources/mit6_01scs11_ses02/)

课本：

• [第 4 章笔记：状态机 (PDF)](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/resources/mit6_01scs11_chap04/) 

# 讲义笔记：

**总体思想**：

- 程序的结构对其模块化有重要的影响。
- 递归是可表达的
- 状态机使用内存进行计算
- 输出和下一个状态取决于输入和当前状态
- 有一种特殊的状态机，他说SM的子类
- 有种特殊的状态机，他是自己子类的实例
- 状态机可以用来表示系统的控制
- 状态机可以用来分析和预测一个系统的行为

## 术语

### 概念：

Imperative Programming
Functional Programming
Functions as First-Class Objects
Recursion
Object Oriented Programming
Abstraction and Modularity
State Machine ：

一个计算模型，描述系统中可能的状态集合和状态之间的转移规则。
State Transition Diagram：状态转移图，描述状态机的可视化图形表示。
Transition Table：过度表，描述状态机中转移状态的一种表格形式
Cascade, Parallel, Select, Feedback：级联，并行，选择，反馈
Controller：在控制系统中的一个组件或者模块。
Plant :在控制系统上下文中，被监控或者控制的设备，进程或者系统。 

# 课本笔记：

状态机在不同系统的作用：

- 用户界面，包括打字输入，鼠标点击等
- 例如，在对话中，单词 ‘it’ 的含义取决于它所代表的事物的历史。
- 航天器的状态，包含某些属性值的开合，燃油和氧气的水平量等
- DNA的序列模式，以及它们分别表示了什么

连续时间模型：

在连续时间模型中，我们通常假设输入和输出的值范围为连续空间，并使用微分方程来描述系统的动力学。

间接时间模型：

模型的输入和输出是由特定时间增量决定，并且他们与这些特定的时间样本同步。

在状态机方法中，我们试图找到系统的一些状态集，这些状态集捕获了输入历史的基本属性，并用于确定系统的当前输出及其下一个状态。寻找具有正确状态集的良好状态机模型是一个有趣的建模问题，有时也很困难;

状态机中一个很有趣并且很重要的是关于状态机模型是由多少方法供我们使用。在这种情况下，我们可以在下面三种情况下使用：

1. **综合性的: (Synthetically)：**
状态机可以为机器人或世界上嵌入的其他系统指定一个“程序”，输入是传感器读数，输出是控制命令。
2. **分析性的：(Analytically)**
    
    状态机可以描述控制系统和它所控制的环境的组合行为。输入总的来说是对整个系统的一个简单指令，输出是对系统状态的简单度量。
    
    这里的目标是分析耦合系统的全局特性，比如它是否会收敛到一个稳态，或者会振荡，或者会发散
    
3. **预测性的：(Predictively)** 
    
    状态机可以描述环境的工作方式。输入是控制命令，输出是外部世界的状态。
    

我们将定义一组原始机器(在这种情况下，是无限类原始机器)，然后定义一组组合子（collection） ，这些组合子允许我们将原始机器组合在一起，以制造更复杂的机器，这些机器本身可以被抽象和组合，以制造更复杂的机器.

## Primitive state machines 元素状态机器

我们可以指定一个传感器(一个过程，它接受一系列值作为状态机的输入，并为每个输入返回机器的输出集合)作为状态机(SM)，通过一系列的指定。

# 讲座笔记：

### PCAP框架：

Python 具有模块性化编程的特性

- def 将操作组合成一个过程，并将其绑定给一个名称
- list 为数据提供了灵活的分层结构
- valuable 将名称与数据相关联
- class 将数据（属性）和（过程）关联起来

| PCAP | procddures | date |
| --- | --- | --- |
| Primitives | +, -, *, ==. !=,  | numbers, booleans, strings |
| Combination | if, while, f(g(x)) | lists, dictionaries, objects |
| Abstraction | def | classes |
| Patterns | higher-order-procedures | super-classes, sub-classes |

### 构建程序的三种不同方法

1、Imperative 命令式，编写程序的最基本方法

注重按步骤地构建程序

使用结构化条件和循环来组织程序

2、Function 函数式

注重模拟数学函数的程序，根据 输入 来生成没有副作用的 输出

函数是数据结构中的第一类对象对象，程序中的参数可以由程序返回

- first-class object 第一类对象
    
    **第一类对象不一定是指面向对象程序设计中所指的对象，而是指程序中的所有实体**(比如：变量、函数、队列、字典等等)。一般第一类对象具有一下特征：
    
    1. 可以被存入变量或其他结构
    2. 可以被作为参数传递给其他方法/函数
    3. 可以被作为方法/函数的返回值
    4. 可以在执行期被创建，而无需在设计期全部写出
    5. 有固定身份
    
    固有身份”是指实体有内部表示，而不是根据名字来识别，比如匿名函数，还可以通过赋值叫任何名字
    

3、Object-oriented 面向对象

注重相关程序和数据间的联系

将程序和类组织为相关类和实例的层次结构

```python
def apply(oplist, arg):
		if len(oplist) == 0:
			return arg
		else:
		# 这里的oplist列表中全是函数
		# oplist[0](arg) 是将 arg 变量传递给oplist[0] 这个函数。
			return apply(oplist[:1], oplist[0](arg))

def addLevel(opList, fctList):
		return [x + [y] for y in facList for x in opList]
```

![Untitled](State%20Machines%20f468c14824f744a6b8349519bc949915/Untitled.png)

```python
def recursion_fb(b, n):
		if n == 0:
				return 1
		else:
			return b*recurrsion(b, n-1) 
		# 2*2*2*2*2 直到n=0,
```

![Untitled](State%20Machines%20f468c14824f744a6b8349519bc949915/Untitled%201.png)