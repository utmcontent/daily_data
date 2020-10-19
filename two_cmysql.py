import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="wwww",charset="utf8")

import sys,io 

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# print(con)

cursor_instance=con.cursor()
# cur.execute("create database awesome character set utf8;")
cursor_instance.execute("USE student IF EXISTS studen;");

cursor_instance.execute("DROP TABLE IF EXISTS student")
# cursor.execute("DROP TABLE IF EXISTS awesome")
sql = """create table student(id int not null,name char(10),age int,address char(20),create_time datetime)"""
try:
    # 执行SQL语句
    cursor_instance.execute(sql)
    print("创建数据库成功")
except Exception as e:
    print("创建数据库失败：case%s"%e)
finally:
    cursor_instance.close()
    con.close()


# cur.execute("create table blogs(id char(20),user_id char(20),name char(20),)character set utf8;")