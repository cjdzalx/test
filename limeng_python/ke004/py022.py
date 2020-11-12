# -*- coding: utf-8 -*-
# @Time    : 20180520
# @Author  : AngesZhu
# @File    : py022.py
# @desc:将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

n = num = 200
f = []

for i in range(int(num)):
	for j in range(2,n):
		t = n % j  # 数字能整出，需要分解的数字
		if t == 0:   # 能整出，代表j是一个质因数
			print(j)
			f.append(j)
			n = n//j   # 除以质因数后的数字，进行判断
			# break
if len(f) == 0:   # 如果一个质因数也没有
	print('该数字没有任何质因数')
else:
	f.append(n)   # n被某个质因数整除过，n就是最后一个质因数
	f.sort()
	print('%d=%d'%(num,f[0]),end='')
	for i in range(1,len(f)):
		print('*%d'%f[i],end='')
