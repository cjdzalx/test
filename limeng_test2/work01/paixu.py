# -*- coding: utf-8 -*-
# 排序
def paixu(list):
	for i in range(len(list)-1):
		for j in range(len(list)-1-i):
			if list[j]>list[j+1]:
				list[j],list[j+1]=list[j+1],list[j]
	return list

a = [4,2,6,2,99,6,5,4,55,33,20,17,58]
print(a)
num = input("输入一个数字:")
if num.isdigit():
	if int(num)>0:
		a.append(int(num))
		print(a)
		print(paixu(a))
		print(set(paixu(a)))   # 去除list中的重复元素

l = [-2,1,3,-6]
l.sort(key=abs)
print(l)

