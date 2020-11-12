# -*- coding: utf-8 -*-
# @desc:while for
# while，满足的条件，满足条件之后，才会继续执行。
a = 1
while a < 10:   # 满足条件的，一个循环,条件一定上true，否则不执行
	# print(a)
	a = a + 1   # a+=1
# for 循环范围，遍历
b = [111,444,3,6,3,0,8,'fdsfsd','hello',[3,2,7,4]]
for i in b:   # 在一个条件中，循环
	print(i,end=',')  # 列表的遍历，适用于元组，字典无序所以不能用遍历
print('')
for j in range(0,10):  # range随机函数，跟index取值方式一样。0<=j<10
	print(j,end=',')
print('')
for m in range(0,10,2):   # step步长，人上楼梯，一步迈几个台阶
	print(m,end=',')
print('')
