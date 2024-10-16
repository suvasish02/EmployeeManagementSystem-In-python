from database import mydb
def displayEmployee():
    id=input("Please Enter the Employee Id which You want to See the Details :")
    mycursor = mydb.cursor()
    sql="select * from Employee where id=%s"
    mycursor.execute(sql,(id,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("Sorry !!! But the Employee Is not available.")
    else:
        query="select * from Employee where id=%s"
        mycursor.execute(query,(id,))
        result=mycursor.fetchall()
        for x in result:
            print("Name of the Employee is : {}".format(x[0]))
            print("Designation Of the Employee is : {}".format(x[1]))
            print("Salary Of the Employee is : {}".format(x[2]))
            print("Mobile Number of the Employee is : {}".format(x[3]))