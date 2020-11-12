# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:控制流 if
a = 1
if a==1:    # 如果语句为真，则执行if下面的内容
	print('11111')
elif a==2:    # 如果if后面的语句为假，但是elif语句为真，则执行
	print('22222')
else:   # 上面所有的条件都不满足，执行这里
	print('33333')
# 一个if语句，有一个if，一个else，elif可以有多个
if True:pass
if True:pass
# ……   多个if，他们的执行是顺序的。