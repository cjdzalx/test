# coding=utf-8
# 列表list
l = ['fffff', 21211, "oooo"]
print(type(l))
o = [l, ["ooo", 8888, 'hello'], 183736]

# 列表操作
l.append("good") # 添加一个元素
print(l)
l.remove("fffff") # 移除一个元素
print(l)
print(l.count("oooo"))    # 数数，计算某个元素在列表中出现的次数
# print(l.pop(1))    # 把列表中的某个元素取出，索引
p = l.pop(1)
print(p)
print(l)
li = [1, 5, 333, 12, 6783, 445]
li.sort()
print(li)
print(len(li))  # 计算列表的长度，一共有多少个元素