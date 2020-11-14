# coding:utf-8

# s = 'hello '
# a = 'world'
# print(s+' '+a)
# print(s*3)


# s1 = 'hello world!'
# print(s1[1:4] )  # 从1-4
# print (s1[4:])    # 从4开始往后切
# print (s1[:4])    # 从前面的开始切到4
# print (s1[4] )    # 这个是取对应第几个字符
# print (s1[::-1])  # 字符串反转
# print (s1[6:3:-1]) # 从6到3反着取
# print(len(s1)) # 计算字符串长度
# print(s1.count('l')) # 统计某个字符出现次数

# dict = {}
# dict['a'] = 'aaaaa'
# dict['b'] = 'bbbbb'
# print(dict)
# print(dict['a'])
# print(dict.keys())
# print(dict.values())


# age = 30
# if age > 30:
#     print('bbbbbb')
# elif age== 10:
#     print('cccccccc')
# else:
#     print('dddddd')


# a = 'hell0 world'
# for i in a:
#     print(i,end= '')


# s = 0
# for i in list(range(1,10,2)):
#     s+=i
# print(s)


# s = 0
# for i in range(100):
#     if i % 2 :   #奇数
#     #if i% 2==0:   #偶数
#         s+= i
#         if s > 1000 :
#             break
#     else:
#         continue
# print(s)


# s = 0
# i = 1
# while i < 100:
#     if i % 2:
#         s += i
#     else:
#         pass
#     i+=1
# print(s)

# 猜数字游戏
# import random
# a = 1
# b = 99
# key = random.randint(1,100)
# while 1 :
#     guess = int(input('请输入一个整数%d' % a + '到%d:' % b))
#     if guess < key and guess >a:
#         a = guess
#         print('请输入%d到'%a + '到%d'%b)
#     elif guess > key and guess < b :
#         b = guess
#         print('请输入%d到'%a + '到%d'%b)
#     elif guess <=1 or guess >=100 :
#         print('超出区间，请重新输入')
#     elif guess == key :
#         print('猜对了')
#         break
