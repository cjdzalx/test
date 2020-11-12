# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:读取和写入ini文件
import os
import configparser
conf = configparser.ConfigParser()
path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(path,'Config.ini')
print(path)
conf.read(path)   # 读取ini文件
s = conf.sections()   # 获取所有的sections,返回值：一个列表
print(s)
o = conf.options(s[0])  # 获取传入的section下面的所有option，返回一个列表
print(o)
v = conf.get(s[0],o[1])  # 获取指定的section 下面option对应的值，获取之后的内容是str字符串
print(v)
print(type(v))  # get方法获取的内容，是字符串类型
i = conf.getint(s[0],o[0])  # 获取之后的内容，是int类型
print(i)
print(type(i))
print(conf.getfloat(s[0],o[0]))  # 返回的是浮点型
# conf.set(section='qqnum',option='age',value='18')
conf.set(section='qqnum',option='age',value='20')# 在原有的section中，添加或更新，内容

print(conf.items(s[0]))   # 返回指定section中的键对值
conf.add_section('info')   # 添加一个section
conf.set(section='info',option='age',value='18')
conf.set('info','name','Anges')

# 删除option
conf.remove_option('info','age')
# 删除section，无论当前要删除的section中是否有内容，都直接一起删除
conf.remove_section('info')

conf.write(open(path, "w"))   # 写入文件，跟在更新或者添加后面