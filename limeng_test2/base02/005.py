# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:字符串操作
s = "hello python!"
# 字符串索引
print(s)
print(s[4])  # 输出索引对应的字符串元素，索引，从0开始计算，-符号代表的是倒序,-1又右开始的下标
print(s[0:-1])   # 输出第一个，到最后一个字符串元素
print(s[1:5])    # 大于第一个，小于等于第二个，前闭后开
print(s[3:])    # 输出索引往后所有的字符串元素
print(s[4:1:-1])  # 从4到1，反着取  步长=1
print(s[8:5:-2])  # 步长=2
print(s[6:9:2])   # 从6到9 正着取，步长=2
print(s[6:9])
# 所有的步长，默认都是1

print(s*4)
print(s + " "+"world")
print(s + "\n"+"world")
print(s)

# 字符串索引，只是一个查看，不会改变字符串的原有内容。