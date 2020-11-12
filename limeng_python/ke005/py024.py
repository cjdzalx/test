# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:# try 捕获异常，然后嗨可以做相应的处理

# a = 'bbb'
a = 4
try:
	b = a + 1
# 一个try，可以跟着多个except,except后面跟着的异常类型，不允许重复
# 指定类型的异常处理
except TypeError:
	print('a+1的运算，a不是数字')
# 所有类型的异常处理
except Exception as ex:  # as在程序里，是别名的意思
	print(ex)
except:   # 捕获没有指定的未知异常
	pass   # pass 只是一个占位符，不做任何操作，什么也不做的捕获所有异常的异常处理器
# 用try抓取处理异常，else要在finally前面
else:    # else 如果没有异常，就执行这里，执行顺序，是在except后，finally前
	print('运算后的结果：%d' % b)
finally:   # finally 不管有没有异常，都执行这里，执行顺序是在最后
	print(a)
# try 里面的作用域
# try里面的新增变量或者属性
# 只能作用于try和else里
# except和finally中，不可引用
