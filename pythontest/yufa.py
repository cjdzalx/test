#coding = utf-8
import time
# if __name__ == '__main__':
# 这里解释下上面__main__的含义：
# 意思就是说让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行
# 如果你不写if __name__ == '__main__':,那么这个代码中的max（）方法只能被
# 别的类导入后，进行调用，但是不能被该模块自己执行max()
# 先尝试了解下，接下来介绍模块的导入，你可以试试练习，体会下



# def fuction(a ,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# fuction(5, 8)

# a = 1
# while a<10:
#     print(a)
#     a+=1

#获取1~100相加的和
# sum = 0
# a = 1
# while a < 101:
#     sum+=a
#     a=a+1
# print(sum)

# x = 6
# def fucation():
#     y = 7
#     z = 8
#     print(y+z)
#     print(x)
# fucation()
# print(x)

#报错Unicode错误(复制来的链接C:\Users/cjdza\Desktop是"\"转义字符，需变为C:/Users/cjdza/Desktop)
# 把text的内容写入文件当中
# text = 'Sample Text to Save \nNew Line'
# save_file = open('C:/Users/cjdza/Desktop/testfile.txt','w')
# save_file.write(text)
# save_file.close()

#读取txt文件在中的内容
# read_me = open('C:/Users/cjdza/Desktop/testfile.txt').read()
# print(read_me)


#在当前文件的内容后加入append_text中内容
# append_text = '\nAppend new line for testing.'
# save_file = open('C:/Users/cjdza/Desktop/testfile.txt','a')
# save_file.write(append_text)
# save_file.close()

# 键盘输入
# x = input('what is your name?')
# print('my name is', x)

#打印当前时间
# timenow = time.localtime()
# print(time.strftime('%Y-%M-%D %H:%M:%S',timenow))

#
# x = [5,6,2,1,6,7,2,7,9]
# x.append(2)
# print(x)
# x.insert(0,99)
# print(x)
# x.remove(2)
# print(x)
# x.remove(x[0])
# print(x)
# x.pop()
# print(x)
# print(x[0:3])
# # print(x.index(1))
# # print(x.count(2))
# x.sort()
# print(x)

# y = ['Janet','Jessy','Anthony','Tom','Alice','Bob']
# y.sort()
# print(y)