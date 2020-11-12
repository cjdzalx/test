# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:不定长参数和匿名函数

def add(*n):   # 任意几个数字，相加求和
	m = 0
	for i in n:   # n默认为元组类型
		m = m + i
	return m

print(add(1, 2,5,8,6,43,2,3))

def app(**n):# **   传入任意个数的键对值。  默认为字典类型
	print(n)
	print(type(n))
app(a='c',o='3',g='2')

mun = lambda a1,a2:a1+a2
print(mun(4,7))
