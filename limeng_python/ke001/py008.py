# coding=utf-8
# 布尔类型
a = None
b = ''
c = 0
# 非0为真，0为假，空字符，none都是假
print(bool(a))
print(bool(b))
print(bool(c))
d = 1
e = 4
f = 'klll'
print(bool(d))
print(bool(e))
print(bool(f))

print(bool(d > e))
'''
>  <  ==   !=
大于，小于，等于，不等于
and 条件1条件2条件3……所有的条件都满足，才为真
or 条件1条件2……所有的条件中只要有一个满足，就是真
not 条件，不满足这个条件，就是真
'''
