
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="suva@1234",
  database="pdbc"
)

print(mydb)