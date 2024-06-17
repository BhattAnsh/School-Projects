import mysql.connector as sq
mydb = sq.connect(host = "localhost", user= "root", passwd = "password")
mycursor = mydb.cursor()
mycursor.execute()#Statement 1 to create the database 
mycursor.execute()#Statement 2 to open the database
mycursor.execute()#Statement 3 to create teh tabel STUDENT
mycursor.execute("delete from student;")
mycursor.execute("insert into student values('123, 'arjun', 25);")
mycursor.execute("insert into student values('124', 'bala', 65);")
mycursor.execute("insert into student values('125', 'charu', 98);")
query ="select * from student where mark>50;"
mycursor.execute(query)
result = mycursor.fetchall()
for row in result:
    print(row)
mydb.commit()
