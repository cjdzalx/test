# -*- coding: utf-8 -*-
# @Time    : 20180520
# @Author  : AngesZhu
# @File    : py018.py
# @desc:类、方法
# 创建一个类
# python中，没有关键字去指定属性或方法，是私有，还是公共等……
# 默认的就是公开的属性和方法
class Add:

	a = 1111  # 类其中的属性

	def __init__(self):   # 类的初始化
		self.b = 2222  # 类其中的属性
	# 每次实例化后，默认执行

	def ccc(self):
		return self.a+self.b   # self.a==a

	def bbb(self, c, b):   # 类的方法
		return c+b
	# 类的方法与函数相同，返回值、参数……
	# self，类的方法中，都有一个默认参数，代表这个方法是属于这个类，这个参数，就叫做self

	def ddd(self, o): # 拿o的值跟ccc方法的返回值做对比
		i = self.ccc()   # 内部调用，主要是指在类里面，对方法或者变量，进行的调用
		if i>o:
			print('o比ccc的返回值小')
		elif i==o:
			print('o和ccc的返回值一样大')
		else:
			print('o比ccc的返回值大')


	# 私有变量和私有方法
	__d = 5555

	def __eee(self):
		return self.a + self.b

	def fff(self):
		n = self.__d + self.__eee()   # self.__d 内部调用属性
		# self.__eee()   内部调用方法
		return n

q = Add()    # 类的实例化  变量名 = 类名()
# 外部调用，是在类外面调用的
print(q.a)   # 调用类里面的属性
print(q.bbb(c=2,b=6))   # 调用类里面的方法
print(q.ccc())   # 类实例化之后，默认先执行init中的内容
# 类中，调用一个方法，是需要在方法名后面加()；如果调用的是一个属性，只需要写属性名

# print(q)
# p = Add()   # 一个类，可以有多个实例化对象
# print(p)

# 内里面调用的
print(q.ddd(4000))  # 内部调用

# 私有变量、私有方法——这个方法和这个变量，只存在与当前类
# # 私有变量和私有方法的调用
# print(q.__d)  # 私有变量不能使用外部调用方式调用
# print(q.__eee())   # 私有方法不能使用外部调用方式调用

print(q.fff())