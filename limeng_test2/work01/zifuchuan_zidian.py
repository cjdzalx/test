# -*- coding: utf-8 -*-
# 字符串-字典
a = "k:1|k1:2|k2:3|k3:4"
a_list=a.split('|')   # 按照指定字符串分割字符串，返回一个list
print(a_list)
d = {}
for i in a_list:
	key,value=i.split(":")
	d[key]=value
print(d)

# print(eval(a)) eval直接转对象类型的时候
a = "{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}"
print(type(a))
print(eval(a))
print(type(eval(a)))