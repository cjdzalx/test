# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:自定义异常
# 创建定制一个异常
class AError(Exception):# 创建定制异常类，必须继承Exception
	pass
class BError(Exception):
	pass
# raise 主动抛出一个异常
# raise AError('lllllllllll')
try:
	raise AError('aaaaa')
except AError as e:
	print(e)

raise AError('aaaa')   # 一个空异常类，表示一个异常，不可以同时写入
# raise AError('aaaa')