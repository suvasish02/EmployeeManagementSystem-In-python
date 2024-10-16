from database import mydb
def removeEmployee():
    id=input("Please Enter the Employee Id which You want to remove :")
    mycursor = mydb.cursor()
    sql="select * from Employee where id=%s"
    mycursor.execute(sql,(id,))
    res=mycursor.fetchall()
    if len(res)==0:
        print("Sorry !!! But the Employee Id Is not available.")
    else:
        query="DELETE FROM Employee WHERE id = %s"
        mycursor.execute(query, (id,))
        mydb.commit()
        if mycursor.rowcount==1:
            print("Employee Deleted Succesfully!!")