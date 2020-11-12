# -*- coding: utf-8 -*-
# 水仙花
# 一个数字的每一位取幂，幂等于位数，取每一位相加的和，等于本身。
def flower(num):
	b = 0  # 储存相加的和
	a = len(str(num))
	for n in range(a):
		c = int(str(num)[n]) ** a
		b = c + b
	return b

n = 3
num_edd = []
for i in range(1,10000):
	if len(str(i))==n:
		if i == flower(i):
			num_edd.append(i)
print(num_edd)
