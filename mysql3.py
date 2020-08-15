import mysql.connector
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table shilpa_employee(empid Integer(10),name varchar(20),salary integer(10))")
def insert_table():
    c.execute("insert into shilpa_employee values(600,'shilpa,'1000')")
    c.execute("insert into shilpa_employee values(100,'saara,'1100')")
    c.execute("insert into shilpa_employee values(200,'zameer,'1200')")
    c.execute("insert into shilpa_employee values(300,'jagu,'1300')")
    c.execute("insert into shilpa_employee values(400,'sham,'1400')")
    c.execute("insert into shilpa_employee values(500,'ali,'1500')")
    con.commit()
def select_table():
    c.execute('select * from shilpa_employee')
    data=c.fetchall()
    for row in data:
        print(row)
def update_table(id,name,salary):
    sql = '''UPDATE shilpa_employee set name VALUE = (?), salary  VALUE = (?) WHERE empid = ?'''
    c.execute(sql,[id],name,salary)
def delete_table():
    c.execute("delete from shilpa_employee where name=saara")
    data=c.fetchall()
    for row in data:
        print(row)
#create_table()
#insert_table()
#select_table()
c.close()
con.close()