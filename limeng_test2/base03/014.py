# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:函数
import time

# print(dir(time))   # 查询某一个库里面的所有内容
# print(help(time.sleep))   #  查看某一个方法……
# print(help(time))

def add(a,b):
	c = a + b
	return c

def app():
	print("这是一个没有返回值，没有参数的函数")

def aoo(i=10):
	print(i)

print(add(1, 3))  # 有返回值，有参数的函数
app()
print(app())   # 输出函数返回值

aoo()   # 有参数默认值的函数
aoo(i=5)
