# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : py025.py
# @desc:从'sys'了解异常
import sys
try:
	1/0
except:
	err = sys.exc_info()  # 当前处理的异常的有关信息
	# 返回一个元组，元组里面有两个值，第一个：指示异常的类型；第二个：详细描述异常的值；第三个：包含一个回溯跟踪的对象
	for e in err:
		print(e)
a = 'qqq'
try:
	a = a + 1
except:
	err = sys.exc_info()  # 当前处理的异常的有关信息
	# 返回一个元组，元组里面有两个值，第一个：指示异常的类型；第二个：详细描述异常的值；第三个：包含一个回溯跟踪的对象
	for e in err:
		print(e)