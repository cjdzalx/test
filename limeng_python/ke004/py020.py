# -*- coding: utf-8 -*-
# @Time    : 20180520
# @Author  : AngesZhu
# @File    : py020.py
# @desc:变量作用域

# 块级作用域，针对代码块if、for之类的代码块，python中没有块级别的作用域，java中，存在块级作用域
# for i in range(10):
# 	age = i
# print(age)

a = 10  # 从此行往下的所有代码都有效，这个有效，指的并不是类和方法中的参数有效

class A(object):   # 所有的类，如果没有指定的继承，那么，默认继承的是object

	# a = 'mmmm'
	b = 20  # 当前类中，从此行往下的所有代码

	# 方法或函数中的参数，参数名与变量名相同时，二者不等同

	def add(self,b):  # 局部作用域，方法和函数中的参数
		self.d = 60   # 带self的变量，作用域在它所在的类中
		c = 30
		return a+b+c  # 40+30+10
	# 只要是在方法中出现的参数，没有带self或者其他代表全局变量的关键字
	# 它的作用域，只存在与当前方法或者函数
	# 参数名不带self等，它跟之前定义的全局变量，或者作用域大于当前函数或方法的变量，不等同

	def abb(self):
		return self.d   # 等同于22行的self.d


aa = A()
# a=999  同一个作用域中，不能存在两个一模一样变量名的变量
print(aa.add(b=40))
# print(b)   # 没有定义NameError: name 'b' is not defined
