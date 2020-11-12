# -*- coding: utf-8 -*-
a = 1
b = '.....fdsfdsfa'
print(type(a))  # a的类型
print(str(a))   # a转换成字符串
print(type(str(a)))   # 转换后的类型
# int str相互转换，str必须为数字，int转换str没有任何要求

# 列表和字符串的转换
print(list(b))
# str 例如一个单独英文单词，单独字符串转换list，把每一个字符，都变成一个单独的元素存入列表
b = [111,444,3,6,3,0,8,'fdsfsd','hello',[3,2,7,4]]
c = str(b)
print(c)  # 列表转换成str之后，打括号[]并不是列表定义中的打括号，而是一个字符，'['或者']'
# 字符串转换成列表，符合列表格式的字符串
print(c)
print(type(c))
print(list(c))
print(type(list(c)))

# 字典，字典可以转换成字符串
# 列表和字典，不可以相互转换
# eval()  把字符串，强制转换成字典
# 如果字符串包含一下内容的时候，转换失败
# 内容：true，false，none……   关键字
