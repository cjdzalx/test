# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:基础数据类型

a = 1   # 定义一个整形
b = 784327984723984723984792    # 定义一个长整形
c = 0.3287782317878312    # 定义一个浮点型
d = "anges"    # 定义一个字符串
e = 1 + 2j     # 定义一个复数

print(type(a))    # 内置函数type，可以查看变量的类型
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 涉及到运算符号，程序读取内容的时候，从上到下，从右往左

f = g = 9   # 多变量的赋值
print(f,g)

# 变量交换
m = 10
n = 20  # 预期结果  m=20 n=10
print(m,n)
m , n = n ,m   # =前面的内容，与后面的相对应
print(m,n)

o = m
m = n
n = o