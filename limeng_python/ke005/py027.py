# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:文件读写---ini，txt，excel
# 路径的问题os库
import os

print(__file__)
# 获取当前脚本的真实路径
cur_path = os.path.realpath(__file__)
print(cur_path)
# 获取脚本的名称
name = os.path.basename(cur_path)
print(name)
# 获取当前脚本的文件夹
file_path = os.path.dirname(cur_path)
print(file_path)
# 获取上一级文件夹
par_path = os.path.dirname(file_path)
print(par_path)
# 拼接文件路径
ta_path = os.path.join(par_path, "test001\\"+'20180603'+'testresult.html')  # join拼接，不局限与两个拼接，还可以使用多个拼接
print(ta_path)
# 获取其它文件夹
ta_path = os.path.join(par_path, "ke10")
print(ta_path)
# 判断文件夹是否存在
t = os.path.exists(ta_path)
print(t)
# 如果不存在就创建一个
if not t:
    os.mkdir(ta_path)

#获取当前文件夹下脚本的真实路径
path1 = os.path.dirname(os.path.realpath(__file__))
print(path1)
#获取Config.ini文件路径
path2 = os.path.join(path1,'Config.ini')
print(path2)