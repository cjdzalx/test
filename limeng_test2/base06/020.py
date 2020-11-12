# -*- coding: utf-8 -*-
# python中的异常
# 所有异常的基类，BaseException
# Exception 常用异常的基类
# TypeError  类型错误/类型的无效操作
# SyntaxError Python语法错误
# IndexError 序列中没有这个索引
# KeyError 映射中没有这个键
# IndextationError 不适当的缩进
# TabError 不当的制表符和空格
# SystemError 通用解释器的系统错误
# ValueError 给定了无效的参数
# Unicode 编码有关系的异常
# NameError 变量相关的一个异常，没定义会出现

# try后面跟着except，这两个是异常处理try语句里面必须的两个
# else和finally不是必须要加的，这个看逻辑和需求
# try语句里面定义的变量，他的作用域包含else和finally
# except语句中定义的变量，只有他自己，和发生异常的时候执行的finally中可以使用。
class Error(Exception):
	pass

try:
	# print('a'+'b')
	print('a' + 1)
	b = 'ooo'
except Exception as a:
	# print(b)  # try里面定义的变量，except里面不可以使用
	# m = 'ppp'
	# print('类型错误')
	# print(a)
	print("如果出现异常，执行这里")
	raise Error("类型错误")
	# raise Exception   # 主动抛出异常，抛出异常之后后面的程序不会继续运行，所以，一般放在代码的最后一行
	# raise IOError
else:
	# print(m)
	print(b)
	print("如果没有异常，则执行这里")
finally:
	# print(m)
	# print(b)  # try里面定义的变量，finally里面不可以使用
	print("不管有没有异常，都执行")
