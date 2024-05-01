import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="12345678",database="customers")
c=mydb.cursor()
login=False
aid=input("Enter Admin ID")
pwd=input("Enter Password")
c.execute("select * from Admin")
#To retrieve data
for row in c:
    if(aid==row[0] and pwd==row[1]):
        login=True
        break
if(login):
    print("Login Successful")
else:
    print("Incorrect ID or Password")