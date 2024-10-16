from database import mydb
def updateEmployee():
    id=input("Please Enter the Employee Id which You want to Update :")
    mycursor = mydb.cursor()
    sql="select * from Employee where id=%s"
    mycursor.execute(sql,(id,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("Sorry !!! But the Employee Is not available.")
    else:
        op=input("What do yu want to update name,post,salary,mobile")
        if op.lower()=="name":
            newname=input("Enter the nEw name :")
            q = "UPDATE Employee SET name = %s WHERE id = %s"
            mycursor.execute(q,(newname,id))
            mydb.commit()
            if mycursor.rowcount==1:
                print("Employee Name Updated Succesfully!!")
        elif op.lower()=="post":
            newpost=input("Enter the nEw post :")
            q = "UPDATE Employee SET post = %s WHERE id = %s"
            mycursor.execute(q,(newpost,id))
            mydb.commit()
            if mycursor.rowcount==1:
                print("Employee Post Updated Succesfully!!")
        elif op.lower()=="salary":
            newsalary=input("Enter the nEw Salary :")
            q = "UPDATE Employee SET salary = %s WHERE id = %s"
            mycursor.execute(q,(newsalary,id))
            mydb.commit()
            if mycursor.rowcount==1:
                print("Employee Salary Updated Succesfully!!")
        else:
            newsalary=input("Enter the nEw Salary :")
            q = "UPDATE Employee SET salary = %s WHERE id = %s"
            mycursor.execute(q,(newsalary,id))
            mydb.commit()
            if mycursor.rowcount==1:
                print("Employee Salary Updated Succesfully!!")