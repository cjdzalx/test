# -*- coding: utf-8 -*-
# 猜数字游戏
# 数字范围0～100
# 输入对数字，跟正确的比较
# 比较结果如果是失败，那么继续循环
import random   # 生成随机数

print("猜数字游戏开始！")
print("生成一个目标数字")
guessnum = random.randint(1,100)
print("初始化猜数字游戏数字范围")
startnum = 0
endnum = 100
print("初始化猜数字次数")
count = 1
while True:
	# num = input("输入您猜测的数字：")
	num = input("输入%d到%d之间的数字："%(startnum,endnum))
	# input获取之后的内容类型，自动识别为str
	if num.isdigit():
		m = int(num)
		if m < startnum:
			print("您输入的数字小了！")
			count+=1   # count = count + 1
		elif m > endnum:
			print("您输入的数字大了！")
			count += 1  # count = count + 1
		elif startnum <= m <= endnum:
			if m == guessnum:
				print("恭喜你猜对了！")
				print("您猜测次数，使用了%d次"%count)
				break
			elif startnum <=m <guessnum:
				print("小了")
				startnum = m
				count+=1
			elif guessnum < m <=endnum:
				print("大了")
				endnum = m
				count+=1
	else:
		print("您输入的内容不是数字，请重新输入")
