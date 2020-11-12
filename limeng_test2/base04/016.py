# -*- coding: utf-8 -*-
# 类
# 类的定义：用来描述具有相同的属性和方法的对象的集合。它定义类该集合中每一个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 实例化：创建一个类的实例，类的具体对象
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
# 私有：默认两个'_'开头为：__
# 静态方法：主要是用来放一些方法，属于逻辑类，与类本身么没有多少交互的方法。放到类里，主要是可以更有一些组织性。
# 类方法：传递参数cls，表示类。

# 类定义
# self 代表的是类的实例，而非本身类。
# 类的方法和普通函数，有一个特别的区别，类的方法必须有一个额外的参数名，self。
# self 不是一个关键字，我们换成其他的也是可以的。
# cls 代表的是类本身。
class People:   # 可以添加小括号，表示继承，默认继承object，默认的时候，可以不添加小括号
	"这是一个基础类"
	def __init__(self,num):   # 初始状态，通过init来定义。定义一个类的参数
		# 这是一个特殊方法->构造方法
		# init，类的实例化操作，会自动调用init这个方法
		# 如果类需要有参数传递，那么参数也可以定义在init方法里
		self.a = 123
		self.num = num   # 接收类的参数
		self.__age = 18   # 定义一个私有属性
	i = "头发"   # 定义一个类的属性
	__name = "Anges"   # 定义一个私有属性
	def body(self):   # 定义一个类的方法
		return "这是一个身体"
	def p(self):
		self.i="头"   # 属性的内部调用
		print(self.i)
		print(self.body())   # 方法的内部调用
	def add(self):
		return self.num
	def pre(self):
		print(self)    # 类的实例化对象
		print(self.__class__)   # 类本身
	def m(ddd):   # self 非固定，只是一般写法
		print(ddd)
	def n(self):   # 调用私有属性和方法
		print(self.__name)
		print(self.__age)
		self.__ll()
		self.pp()
	def __ll(self):
		print("这是一个私有方法")
	@staticmethod   # 静态方法，用装饰器@staticmethod定义。静态方法，不需要传递任何类的东西
	def pp():
		print("这是一个静态方法")
	@classmethod    # 类方法，用装饰器@classmethod定义。定义类方法，需要传递参数cls
	def cc(cls):
		print(cls)
		print("这是一个类方法")
# 实例化类
a = People(9)
print(a)
# 外部访问类的属性和方法
print(a.i)
print(a.body())
a.p()
print(a.add())
a.pre()
a.m()
a.n()
# print(a.__name)  # 私有属性不可以外部访问
# print(a.__ll())  # 私有方法不可以外部访问
People.pp()  # 类名直接调用
a.pp()   # 实例名直接调用
People.cc()  # 类名直接调用
a.cc()   # 实例名直接调用