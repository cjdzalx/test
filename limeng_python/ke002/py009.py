# -*- coding: utf-8 -*-
# @desc:控制流if

# if 如果
a = 1
b = 2
c = 3
if a == 1:   # 编程语言中的等于，符号是用==来表示，单=表示赋值
	print(a)
elif a == 2:   # else if  python：elif   else if，这种写法不存在python，java也不存在
	print(a)
else:
	print(3333)
# elif和else的区别：
# elif 后面跟的是跟if一样的条件，条件的结论，跟if一样，是一个bool类型的值
# else 后面不需要跟条件，不满足if和elif的条件，全部都走else
isinstance(a, (int,dict)) # 内置函数意义,判断某个变量，是否是某种类型，返回一个bool类型 false true

if a == 1:
	print(a)
if b == 2:
	print(b)
# 两个if同时存在的情况，是允许的。
# 但是这种情况，他存在，几个if，同时执行的情况。
# 如果程序里允许这样的操作，是可以允许这样写的。
# 如果程序里不允许，他们不说并列的关系，就需要用if elif else

if a == 1:
	if b==2:
		print(a+b)
# python程序里，大部分的语法，都可以嵌套。

# 如果 条件1，成立，为真，就执行XXXXXX   if
# 如果 条件1不成立，满足条件2，就执行xxxxxx    elif
# ……
# else，以上所有条件都不满足，就执行xxxxx
# 一个if中，else只允许有一个，elif允许有多个，一个if中，只有一个if存在
# if。。。。：
# elif。。。。
# elif。。。。
# ……
# else    else，可存在，也可以不存在，不是必须存在的条件




