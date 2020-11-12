# -*- coding: utf-8 -*-
# @Time    : now()
# @Author  : AngesZhu
# @File    : .py
# @desc:
import pymysql
# 创建数据库连接
con = pymysql.connect(host='47.98.214.128',
                             port=3306,
                             user='test',
                             password='test123',
                             db='test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
# 实例化——创建数据库游标
cursor = con.cursor()
sql = "select * from tb_emp"
# 执行一条sql语句
cursor.execute(sql)
# 获取多条数据
result = cursor.fetchall()
print(type(result)) # 查看返回数据的类型，方便处理
print(result)
for i in result:
	print(type(i))
	print(i)
sql1 = "select * from tb_emp where id=4"
cursor.execute(sql1)
# result1 = cursor.fetchone()  # 获取一条数据
result1 = cursor.fetchall()
print(result1)