
from Employee import Employeee as g 
from database import mydb
def addEmployee():
    name=input("Enter Yor Name")
    post=input("Enter Your Designation")
    salary=input("Enter Yor salary")
    mobile=input("Enter Your mobile Number")
    idName=name.split(" ")
    id=str(mobile)+"@"+idName[0].lower()
    mycursor = mydb.cursor()
    sql="select * from Employee where id=%s"
    mycursor.execute(sql,(id,))
    res=mycursor.fetchall()
    if len(res)==0:
        e=g(name,post,salary,mobile,id)
        print("Your Employee Id is : " + id)
        sql = "INSERT INTO Employee(name,post,salary,mobile,id) VALUES (%s, %s, %s, %s, %s)"
        values=(name,post,salary,mobile,id)
        mycursor.execute(sql, values)
        mydb.commit()
    else:
        print("Employee Already Exists !!! with employee id {}".format(id))
