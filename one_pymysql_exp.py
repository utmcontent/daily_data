import pymysql.cursors
import sys,io 
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# Connect to the database
con = pymysql.connect(host='localhost', user='root', passwd='wwww', db='test', port=3306, charset='utf8')
cur = con.cursor()
cur.execute(' CREATE TABLE person (id int not null auto_increment primary key,name varchar(20),age int, sex varchar(2))')
data=('Alice',16,"f")
cur.execute('INSERT INTO person(name,age,sex) VALUES(%s,%s,%s)',data)
cur.executemany(' INSERT INTO person (name,age,sex) VALUES (%s,%s,%s)',[('sara',24,'女'),('开心麻花',30,'男')])
data=('dlice',16,"女")
cur.execute('INSERT INTO person(name,age,sex) VALUES(%s,%s,%s)',data)
con.commit()
cur.execute('SELECT * FROM person')
res = cur.fetchall()
print (res)
for line in res:
    print(line)









    # cur.execute('SELECT * FROM person')
    # res = cur.fetchone()
    # print(res)
# #     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)     
# finally:
#     connection.close()