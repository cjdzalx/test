# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:数据转换

a = 111
b = [3,'bb',0.314,'hello']
print(a,type(a))
print(str(a),type(str(a)))   # 转换为字符串   str()  int->str
print(type(b))
print(str(b),type(str(b)))   # list->str
c = str(a)
print(int(c),type(int(c)))   # str->int
# print(int(b),type(int(b)))   # 类型错误 list->int 数据不匹配
# 特定类型转换，需要被转换的内容，与目标类型，相匹配   TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
d = "hello world"
print(list(d))  # str->list
print(d)
e = tuple(b)
print(e)  # list->tuple
print(list(e))   # tuple->list

f = {'name':'Anges','age':18}
print(type(f))
print(str(f))   # dict->str
print(list(f))   # dict->list   ['name', 'age']  内容不全
print(list(f.values()))   # ['Anges', 18]
# print(dict(b))   # list->dict  不可以
print(eval(str(f)))  # 转换成对象
print(type(eval(str(f))))
# eval 转换失败  null  ture flase……   如果被转换的内容中，含有某些特定的关键字，eval就会转换失败
