# -*- coding: utf-8 -*-
# 装饰器
def outer(x):
	# x = 1
	def inner():
		# print(x)
		return x
	return inner   # 作为一个函数被返回，保存在变量里。
foo1 = outer(1)  # outer返回的是一个函数
foo2 = outer(2)
# print(outer(4))
# print(foo1())
# print(foo2())

def star(func):
	def inner(*args,**kwargs):
		print("*" * 30)
		func(*args,**kwargs)
		print("*"*30)
	return inner

def percent(func):
	def inner(*args,**kwargs):
		print("%" * 30)
		func(*args,**kwargs)
		print("%"*30)
	return inner

# @star
# @percent
# def printer(msg):
# 	print(msg)
# printer("hello")
@percent
def printer():
	print("hello")
printer()

# 带参数的装饰器
def smart_divide(func):
	def inner(a,b):
		print("I am going to divide",a,"and",b)
		if b==0:
			print("11111")
			return
	return inner

@smart_divide
def divide(a,b): # 装饰器里面嵌套的inner函数的参数，和其装饰的函数参数是一样的。
	return a/b
# divide(2,0)

# @smart_divide
# def ddd(a): # 装饰器里面嵌套的inner函数的参数，和其装饰的函数参数是一样的。
# 	return a
# ddd(2)