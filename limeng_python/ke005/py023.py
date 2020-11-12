# -*- coding: utf-8 -*-
# @Time    : 20180603 09：00
# @Author  : AngesZhu
# @File    : py023.py
# @desc:异常处理
import random   # 随机数的库

print('猜数字游戏开始')
print('生成一个要猜的数字')
guessnum = random.randint(1,100)
print('初始化猜数字游戏的数字范围')
startnum = 0   # 猜数字的范围，小
endnum = 100   # 猜数字的范围，大
print('初始化猜数字次数')
count = 1
# count = 'aaa'
while True:  # 缩进 tab
	# num = input('请输入您猜测的数字：')  # 输入内容
	num = input('请输入%d和%d之间的数字：'% (startnum,endnum))
	# input输入之后获取的内容类型,自动识别为str
	if num.isdigit():  # num的内容全部为数字
		m = int(num)
		if m < startnum:
			print('您输入的数字不在范围内！')
			count += 1
		elif m > endnum:
			print('您输入的数字不在范围内！')
			count += 1
		elif startnum <= m <= endnum:
			if m == guessnum:
				print("恭喜您，猜对了！")
				print('您完成猜数字游戏的次数为%d'%count)
				break
			elif startnum <= m < guessnum:
				print('您猜的数字小了！')
				startnum = m
				count += 1
			elif guessnum < m <=endnum:
				print('您猜的数字大了！')
				endnum = m
				count += 1
	else:
		print('您输入的内容不是数字，请重新输入！')

# TypeError 类型错误，运算的时候类型错误，比较的时候等……
# try 捕获异常，然后嗨可以做相应的处理
