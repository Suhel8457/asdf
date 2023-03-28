import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='pythontest'
 
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers WHERE address ='hyderabad'")
result=mycursor.fetchone()
print(result)
for x in result:
    print(x)