# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:字典

a = {'name':'Anges','age':'18'}
# 字典中的value值，可以为数字、字符串、列表、元组、字典……
print(a)
print(type(a))
# 字典是无序的
print(a['name'])   # 根据key，输出value
print(a.values())   # 输出所有的value
print(a.keys())    # 输出所有的key
# a.clear()   # 清空字典
b = a.copy()   # 复制一个字典
print(b)
c=a.get('name')    # 根据key，输出value
print(c)
print(a.get('ppp'))    # 如果找不到，返回空
e=b.pop('name')   # 移除，整个键对
print(e)
print(b)
a['study']="good!"   # 字典中添加一个键对
print(a)
m = {'name':'Anges','age':{'age':'18'}}
o = m.get('age').get('age')
print(o)
print(m['age']['age'])
