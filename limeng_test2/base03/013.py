# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:
"""s 代表的是字符串
s.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
s.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。
s.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。
s.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
s.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。
s.istitle()      所有单词都是首字母大写，为真返回 Ture，否则返回 False。
s.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False
"""
s = "hello"
o = "HelLo"
p = "1ohd9ems7"
l = '44444'
if s.isalnum():print(True)
print('1---------------------')
if p.isalpha():print(True)
else:print(False)
print('2---------------------')
if l.isdigit():print(True)
print('3---------------------')
