# -*- coding: utf-8 -*-
# 1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数，都是多少
l = []
for i in range(1,5):
	for j in range(1,5):
		for n in range(1,5):
			if i!=j and j!=n and n!=i:
				a = str(i)+str(j)+str(n)
				l.append(int(a))
				# print("%d%d%d"%(i,j,n),end="|")
print(l)
print(len(l))
