# -*- coding: utf-8 -*-
# @Time    : 20180520
# @Author  : AngesZhu
# @File    : py021.py
# @desc:模块，模块导入
# import  from
# 1。import 可以直接导入，系统或标准库中的模块。
# 2。from
from ke003.py016 import *
aaa(888)
# from 文件夹名.文件名 import 所有：* 或者是函数和类
from ke004.py020 import A
aa = A()
print(aa.add(b=40))
# 一个模块只能被导入一次
import sys,time
# 导入多个模块的时候，模块来源，要添加
from ke004.py019 import A,B,C
# 导入全部模块，使用*


# __name__ 存放要执行的内容
if __name__ == '__main__':
	a = 1