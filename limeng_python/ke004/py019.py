# -*- coding: utf-8 -*-
# @Time    : 20180520
# @Author  : AngesZhu
# @File    : py020.py
# @desc:面向对象
# 面向对象，它可以理解为定制
# 根据客户要求编写指定的功能
# 重写，添加，修改，等内容
# *面向对象：封装、继承、多态
# 封装：把流水账一样的代码，封装成一个代码块
# 继承：
# 多态：

# 定义一个父类
class A(object):   # 所有的类，如果没有指定的继承，那么，默认继承的是object

	def add(self,a,b):
		return a+b
a = A()
print(a.add(6,3))

# 定义一个子类
class B(A):
	def bcc(self,a,b):
		return a-b

b = B()
print(b.bcc(12,7))   # 子类，拥有父类中所有的属性和方法
print(b.add(3,7))    # 子类的实例化对象，可以调用父类中的属性和方法
# 子类，可以添加，方法
# 父类，不包含子类的所有属性和方法
# 父类和子类，是一个包含关系

class C(A):
	def mmn(self,a):
		return a**3

	def add(self,a,b,c):   # 方法重写  ——多态
		return a+b+c
c = C()
# 一个子类，可以拥有多个父类
print(c.add(3,4,5))

# 态，状态
# 多态，就是多状态
# 之前，父类中的方法和属性，可以在子类中，重写或者是修改
