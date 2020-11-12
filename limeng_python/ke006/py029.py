# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:
import pymysql

# 连接mysq数据库
connection = pymysql.connect(host='47.98.214.128',
                             port=3306,
                             user='test',
                             password='test123',
                             db='test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
# 实例化——创建数据库游标
cursor = connection.cursor()

# 使用execute方法执行SQL语句
id = 1
i = cursor.execute("select * from tb_emp where id = %d"%id)
print(i)
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

sql = cursor.execute("select * from tb_emp")
# 使用 fetchall() 方法获取多条数据
a = cursor.fetchall()
for i in a:
    print(i)

print("Database version : %s " % data)
print(type(data))
# 关闭数据库连接
cursor.close()
