# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:while,for
a = 1
while a<20:   # while 后面的语句为真，则执行while里面的内容
	a = a + 1
	print(a,end=',')
print()   # 打一个回车，换行

for i in range(10,20):   # range 随机函数  前闭后开
	print(i,end=',')
print()
b = [3,'bb',0.314,'hello']
f = {'name':'Anges','age':18}
for j in b:print(j,end=',')   # 遍历list
print()
for n in f.values():print(n,end=',')   # 遍历dict value
print()
for n in f:print(n,end=',')   # 遍历dict key
print()
for n in f.keys():print(n,end=',')   # 遍历dict key
print()

# python中的所属关系——缩进
# 缩进  tab 不能用空格代替，要缩进，就用tab，按一下一个缩进

# 控制流的嵌套，嵌套个数任意
# if 套 if
# if 套 for，while
# while 套 while
# while 套 if和for
# for 套 for
# for 套 if和while

# break和continue
print('----------------------------------')
for i in range(0,20):
	print(i,end=',')
	if i==12:
		break    # 跳出循环
print()
print('----------------------------------')
m = 30
for i in range(0,20):
	print('i=%s'%i,end=',')
	print('m=%s'%m,end=',')
	if i==12:
		continue    # 跳出当前，继续下一个循环
	m = m - 1
