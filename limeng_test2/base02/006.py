# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:列表list

a = 10
b = [1,3,92,46,76,33]
l = [1,"a","bbbb",88888,999,a,b,1,1,1]
print(l)
# 列表定义：1。数字、2。字符串、3。变量、4。列表、5。元组……
# 列表的元素，类型并不局限
# 列表和字符串一样，都可以运用索引，[]前闭后开  包含前面的，不包含后面的
l.append(666)   # 在列表的最后，添加一个元素
# del l[1]   # 删除某一个位置的元素
# l.remove(999)   # 移除某一个元素，参数是元素
# l.clear()  # 清除所有的元素
print(l.count(1))   # 统计，某一个元素，在列表中出现的次数
print(l.remove(999))
print(l.pop(2))   # 移除某一个元素，参数是索引
# pop和remove的区别
# 1。pop有返回值，remove没有返回值
# 2。pop参数是索引，remove参数是元素
l[1]="aaa"   # 给制定索引位置的元素，重新赋值
print(len(l))  # 内置函数len，用来统计长度
b.sort()  # 把一个列表，从小到大排序。列表必须全部元素都是数字
print(b)
print(l.index(1))   # 返回一个元素的索引
l.insert(2,"ooo")    # 在索引位置，插入一个元素
b.reverse()   # 倒序排列一个列表。列表必须全部元素都是数字
print(b)
l.extend(['a','b','c'])   # 把一个列表，添加到当前列表中
print(l)
m = l.copy()   # 复制一个一模一样的列表出来
print(m)
