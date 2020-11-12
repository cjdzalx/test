# Author:Alex Li
'''
count = 0
while True:
    print("count:",count)
    count = count +1  #count +=1
    if count == 1000:
        break

for i in range(0,10):
    if i <3:
        print("loop ",i)
    else :
        continue
    print("hehe...")

for i in range(10):
    print('----------', i)
    for j in range(10):
        print(j)
        if j > 5:
            break





var = 10  # 第二个实例
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)

'''
# list=[1,2,3,4]
# # it = iter(list)    # 创建迭代器对象
# # for x in it:
# #     print (x, end=' ')
# #

import urllib3

urllib3.disable_warnings()

