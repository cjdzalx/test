# -*- coding: utf-8 -*-
# 变量作用域

# 程序执行顺序，从上到下。
a = 1  # 作用域，就是整个文件

# while和if中定义的变量，不是局部变量，全局变量
while True:
	b = 0  # 作用于此行往后
	if a==1:
		b = 0  # 作用于第一个if往后
		# print(a)
		break
	else:
		# b = 0  # 作用于else往后
		for i in range(0,10):
			c = 8  # 只作用于本循环
			b = b + i
		break

# print(b)
# print(c)

def add(a,b):   # a,b不等同于上面定义过的ab，且函数定义过的ab，只作用于此函数。函数参数
	# print(a,b)
	return a+b

# add(2,5)

def aaa():
	print(a+b)  # 这里的ab，是整个文件的ab，也就是说5行和8行，定义的ab

aaa()

# nonlocal 用来在函数或其他作用域中使用外层(非全局)变量。
def mmm():
	count = 0
	def ccc():
		nonlocal count  # 外层全局中有一个变量，用nonlocal声明之后，在声明的范围内算作使用
		count +=1
		return count
	print(count)
	return ccc

# aaa = mmm()
# print(aaa())

class p:

	q = 3  # 定义的变量，在类里使用的时候，要加self，作用，也是类全局
	def __init__(self):
		self.pp = 1   # 带self的变量，类全局，在类里面使用。
	@classmethod
	def w(cls):
		cls.ii = 2    # 带cls的变量，类全局，在类里面使用。
		print(cls.ii)
		# print(cls.pp)  # 类方法中不可以调用self开头定义的属性
	def o(self,c,d):
		r = 9    # 作用于定义的方法
		print(self.pp)
		return c+d
	def u(self):
		print(self.q)   # 调用
		print(self.ii)    # 普通方法中，可以用self.的形式，去调用类方法中定义的属性
		self.ii = 99   # 重新赋值，普通方法里的都改变了。
		print(self.ii)
		# print(r)
	def mm(self):
		print(self.ii)
		print(a+b)
	# @classmethod
	# def nn(cls):
	# 	print(cls.ii)   # 类方法跟类方法直接，也没有关系

# h = p()
# p.w()
# h.u()
# h.w()
# h.mm()

hehe = 6
def bb():
	# hehe = 9
	global hehe
	print(hehe)   # 局部变量hehe = 9
	hehe = 9
bb()
print(hehe)   # 全局变量hehe = 6
