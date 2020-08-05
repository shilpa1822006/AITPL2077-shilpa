import sqlite3
con=sqlite3.connect('db1.sqlite3')
c=con.cursor()
def create():
    c.execute('create table student(regno int primary key,name text)')
def insert():
    c.execute("insert into student values('01','amul')")
    c.execute("insert into student values('02','noor')")
    c.execute("insert into student values('03','ali')")
    c.execute("insert into student values('04','shree')")
    con.commit()
def select():
    c.execute('select * from student')
    data=c.fetchall()
    print(data)
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    c.close()
    con.close()
#create()
#insert()
select()