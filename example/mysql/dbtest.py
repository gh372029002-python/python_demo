#!/usr/bin/python
#-*- coding:utf-8 -*-
import MySQLdb

db = MySQLdb.connect('127.0.0.1','root','gh7758521@#*','test')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cursor.execute(sql)


# START SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   #db.commit()
except MySQLdb.Error,e:
   print e
   # Rollback in case there is any error
   db.rollback()

# SQL 插入语句
sql = "SELECT * FROM EMPLOYEE"

cursor.execute(sql)

results = cursor.fetchall()

for row in results:
    print row[0]
    print row[1]
    print row[2]
    print row[3]
    print row[4]
    print row
# END SQL 插入语句 


# START SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                          WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   print 'SUCCESS UPDATE NUMBER %d' % cursor.rowcount
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# END 关闭数据库连接
db.close()



