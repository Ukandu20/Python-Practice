import mysql.connector
mydb =  mysql.connector.connect(
  hosts = "localhost",
  user= "root",
  password =   "root"
)
mycursor = mydb. cursor()
mycursor.execute("use student;")
str="insert into customer values(23, 'C5', 'xx8');
mycursor .execute(str)
mycursor.execute("select * from customer;")
ta = mycursor.fetchall()
print(data)
