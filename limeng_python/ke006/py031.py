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
result = cursor.fetchone()
print(result)
# 执行的sql语句，对应的是多少条数据。
# 不知道多少条的时候，就用获取多条数据的方法
# 插入
s1 = "INSERT INTO `tb_emp` (id,Name,sex,age,address,email) VALUES(6,'aaa',0,18,'杭州市','11111@126.com');"
cursor.execute(s1)
con.commit()   # 提交
s2 = "select * from tb_emp"
r1 = cursor.fetchall()
cursor.execute(s2)
r2 = cursor.fetchall()
print(r1)
print(r2)
# 获取是跟着查询走
s3 = "update tb_emp set sex=1"
try:
	cursor.execute(s3)
	con.commit()
except:
	print("更新异常")
r3 = cursor.fetchall()
print(r3)
# 插入和更新，都要查询后获取
# 参数化sql查询
id = 4
s4 = "select * from tb_emp where id = %d"%id  # 参数化sql，跟格式化输出类似
# cursor.execute("select * from tb_emp where id = %d"%id)
cursor.execute(s4)
r4 = cursor.fetchall()
print(r4)

cursor.close()