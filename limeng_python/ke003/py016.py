# -*- coding: utf-8 -*-
# @Time    : 2018/05/19
# @Author  : AngesZhu
# @File    : py016.py
# @desc:不定长参数 *args   **dictargs
def aaa(arg,*args):
	print(arg)
	print(args)  # 不定长参数，默认类型：元组
	print(type(args))
	# 打印不定长参数
	for i in args:
		print('other args:',i)

aaa(1,'aaa',True,111)
aaa(9)  # 不定长参数，不传参，默认为空元组

print('----------------------')
def bbb(*ag,**dictargs):
	print(bbb)
	print(dictargs)  # **不定长参数，默认类型是字典
	print(type(dictargs))
	for key in dictargs:
		print(key+':'+str(dictargs[key]))

bbb(name='anges',age=18,single=True)
# bbb(info='信息',{'name': 'anges', 'age': 18, 'single': True})
bbb(info='信息',ooo={'name': 'anges', 'age': 18, 'single': True})
bbb()
