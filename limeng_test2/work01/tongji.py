# -*- coding: utf-8 -*-
# 输入一个字符串，统计他的字母、数字、空格、以及其他字符的个数
s = input("输入一行字符：")

str_count = 0
num_count = 0
spac_num = 0
else_num = 0

for strs in s:
	if strs.isalpha():
		str_count += 1
	elif strs.isdigit():
		num_count += 1
	elif strs == " ":
		spac_num += 1
	else:
		else_num += 1
print("字符有%d个"%str_count)
print("数字有%d个"%num_count)
print("空格有%d个"%spac_num)
print("其他字符有%d个"%else_num)