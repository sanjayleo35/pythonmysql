#connecting to DB
import mysql.connector as con
db=con.connect(host="localhost",user="root",password='Sanjay@3578',database="FirtDB")
print("connection created")

#creating new DB
cur=db.cursor()
'''cur.execute("create database FirtDB")
print("database created.......")
'''
#Using DB
cur.execute("use FirtDB")

#Creating Tables

'''cur.execute("create table student (roll_no int,name varchar(20))")
print("table created......")
cur.execute("desc student")
'''
#inserting values
'''query="insert into student values(%s,%s)"
list=[(1,"sanjayleo"),(2,"Rama"),(3,"sugu")]
cur.executemany(query,list)
db.commit()
print(cur.rowcount,"inserted.....")'''

#fetching form vsc
'''cur.execute("select * from student")
select=cur.fetchall()
print(select)'''

#updating
'''update="update student set name=%s where roll_no=%s"
value=("siva",3)
cur.execute(update,value)
db.commit()

cur.execute("select * from student")
select=cur.fetchall()
print(select)'''
 #deletion
'''delete="delete from student  where roll_no=%s"
value=(3,)
cur.execute(delete,value)
db.commit()

cur.execute("select * from student")
select=cur.fetchall()
print(select)'''





