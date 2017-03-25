name='ankit'
age=19
gender='male'
mob=7773017941
dr='shushil shukla'
suffer='fever'
a=[(name,age,mob,gender,suffer,dr)]
import sqlite3
con=sqlite3.Connection('lifeline Database')
cur=con.cursor()
#cur.execute("Drop table Patient_info")
#cur.execute('create table patient_info (pname varchar(25),age number,pmob number,pgender varchar(15),sufferings varchar(200),doc varchar(25));')
cur.executemany("insert into patient_info values(?,?,?,?,?,?)",a)
cur.executemany("insert into patient_info values(?,?,?,?,?,?)",a)
cur.execute("select * from patient_info where pmob==7773017941")
a=cur.fetchall()
print a
print a[0][0]
print a[0][2]
