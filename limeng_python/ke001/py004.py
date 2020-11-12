# coding=utf-8
str = "hello world"
# 索引从0开始
print(str[0])
print(str[0:-1])
print(str[2:5])   # 第三个，到第六个
# 取值区间：等于前面这个，小于后面那个
# str[2] <= b < str[5] 3 4 5 第六个不显示
print(str)
print(str[2:])    # 第三个，到最后一个所有字符
print(str * 2)
print(str + "ooo")
print(str)
print(str[::-1]) #字符串翻转
print(str[7:3:-1])

# 不管用[]取值取哪个，取多少。原本的字符串、列表、元组，都是不变的。

# json格式处理，广泛应用
print(str.split("o"))   # 按照某个符号或者字符，切割字符串，返回的是一个list
b = "-hello-"
print(b)
print(b.strip("-"))  # 去掉前后的某个符号，返回字符串
c = "[ooooo]"
print(c)
print(c.strip("[]"))
