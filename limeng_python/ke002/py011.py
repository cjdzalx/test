# -*- coding: utf-8 -*-
# break

for i in range(0,100):
	if i == 66:
		print(i)
		break   # 跳出当前循环
	print(i,end=',')
print('------------------')
for i in range(0,100):
	if i == 66:
		print(i)
		continue   # 继续当前循环
	print(i,end=',')   # continue之后的内容，就不执行了。
