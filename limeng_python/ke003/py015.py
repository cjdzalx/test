# -*- coding: utf-8 -*-
# @Time    : 2018/05/19
# @Author  : AngesZhu
# @File    : py015.py
# @desc:自定义函数

def add():
	print(1111)
add()   # 自定义函数的调用
print(add())    # 调用函数外，还可以输出函数返回值内容

print('------------------------------')
# 有返回值的函数
def bbb():
	return '2222'
bbb()
print(bbb())   # 先调用，后输出

print('------------------------------')
# 带参数的函数
def ccc(a):
	return a
# ccc()   # 右半边括号颜色异常，一般表示你的函数参数异常(缺少参数，多参数，参数写错……)
ccc('aaaa')
print(ccc('aaaa'))
print(ccc(a='mmmm'))   # 给指定的函数参数传参

print('------------------------------')
# 有参数默认值的函数
def ddd(a=1,b=2):
	return a+b
print(ddd())   # 参数有默认值的函数，在调用时，可以不给参数传参，不传参时，参数为默认值
print(ddd(a=2))  # 有参数默认值的函数，调用时，可以给部分参数传参
print(ddd(a=3,b=6))  # 可以部分传参，也可以全部传参

