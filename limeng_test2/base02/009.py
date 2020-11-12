# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:布尔

# 布尔值的判断，非0非空为真
a = None
b = ''
c = 0
d = 1
e = -1
f = '0'
print(bool(a))   # 输出一个元素的布尔值bool
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

# 逻辑运算符
# 与 and
# 或 or
# 非 not
# and or，均可以跟2个以上的表达式
q = 1
w = 2
print(bool(q>w))   # 大于
print(bool(q<w))   # 小于
print(bool(q==w))   # 等于
print(bool(q!=w))   # 不等于

print(bool(q<w and q!=w))
# and两边的条件都为true，整个表达式，也就是true，只要有一个为false，那么整个表达式就是false
print(bool(q<w or q==w))
# or两边的条件，只要有一个为true，那么整个表达式就是true
print(bool(not q==w))
print(bool(not q<w))
# not 表达式的结果，相反的结果是true，整个表达式就是true