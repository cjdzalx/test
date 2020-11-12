# -*- coding: utf-8 -*-
# @Time    : 2018/05/19
# @Author  : AngesZhu
# @File    : py014.py
# @desc:函数
# 内建函数
l = [1,5,8,4,6,2]
print(sum(l))
import time
print(dir(time))   # dir内建函数，可以帮助我们查看库里面所有的变量和方法
print(help(time.sleep))  # help查看的时候，调用方法填写参数的()可以不用加
# help，可以查看方法的实例和帮助信息
print(len(l))
print(type(l))