# -*- coding: utf-8 -*-
# 面向对象
# 方法重写：如果从父类继承的方法，不能满足子类的需求，可以对其进行改写，这个过程，就叫做方法的覆盖(override),也可以称为方法的重写。
# 继承：即一个派生类(derived class)继承基类(base class)的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
# 面向对象：封装、继承、多态
# 1。子类上的动作完全等同于父类上的动作
# 2。子类上的动作完全覆盖了父类上的动作
# 3。子类上的动作部分替换了父类上的动作
# 继承，静态方法和类方法，都会被子类继承。也可以进行方法重写。
# 静态方法，主要用来存放逻辑性代码
class people:   # 类默认继承object，隐式继承
	name = ""
	age = 0
	__weight = 0
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print("%s 说：我 %d 岁。"%(self.name,self.age))
# 单继承
class student(people):   # 显示继承/显示覆盖
	grade = ""
	def __init__(self,n,a,w,g):
		people.__init__(self,n,a,w)   # 调用父类的构造
		self.grade = g
	# 方法重写，重写父类中的方法
	def speak(self):
		print("%s 说：我 %d 岁了，我在读 %d 年级。"%(self.name,self.age,self.grade))

s = student('jack',10,60,3)
s.speak()
super(student,s).speak()  # super函数，调用父类（超类）的方法。

# 另外一个类，多重继承
class speaker():
	topic = ""
	name = ""
	def __init__(self,n,t):
		self.name = n
		self.topic = t
	def speak(self):
		print("我叫 %s，我是一个演说家，我演讲的主题的是 %s"%(self.name,self.topic))

class sample(student,speaker):
	a = ''
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)

test = sample('Tim',25,80,4,"python")
test.speak()   # 方法如果同名，默认调用的是在括号中，排前的父类方法。

