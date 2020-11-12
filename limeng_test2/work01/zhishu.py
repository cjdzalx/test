# -*- coding: utf-8 -*-
# 100以内质数
# 质数：只能被自己和1整除的数字
num = []
mun = True
for i in range(2,101):
	for j in range(2,i-1):
		if i % j == 0:
			mun = False
			break
		else:
			mun = True
	if mun:
			num.append(i)
print(num)
