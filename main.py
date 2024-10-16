import AddEmployee 
import removeEmployee
import updateEmployee
import displayEmployee
import os
def main():
    print("Welcome to the Employee Mangement System")
    print("=================================================")
    while True:
        value=input("Please enter the operation which you want to perform , Add/remove/update/show/exit Employee")
        if value.lower()=="add":
            AddEmployee.addEmployee()
        elif value.lower()=="remove":
            removeEmployee.removeEmployee()
        elif value.lower()=="update":
            updateEmployee.updateEmployee()
        elif value.lower()=="show":
            displayEmployee.displayEmployee()
        else:
            os._exit(0)

main()