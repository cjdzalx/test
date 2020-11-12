# -*- coding: utf-8 -*-
# @Time    : 2018/05/19
# @Author  : AngesZhu
# @File    : py017.py
# @desc:匿名函数

add = lambda a,b:a+b
print(add(1,5))
# add 匿名函数名，  a，b变量名。"："后面的，是表达式，也就是执行逻辑

# bbb = lambda i:for j in i:print(i)
# 不能加控制流相关表达式

ccc = lambda b,c,d:add(b,c)-d
print(ccc(5,4,1))
# 匿名函数，可以嵌套使用
# 这个嵌套，并不局限与匿名函数，也可以与自定义函数，进行嵌套


ddd = lambda p,q:p-q
try:
	print(ddd(1,'a'))
except:
	print('1111')
