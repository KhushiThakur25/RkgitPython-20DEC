class Employee:
    def __init__(self,emp_ID,emp_name):
        self.emp_ID = emp_ID
        self.emp_name = emp_name
    def show(self):
        print(f"Name of employee is {self.emp_name} , Id is {self.emp_ID}")

emp1 = Employee(101,"Rohit")
print(emp1.emp_name)
emp2 = Employee(102,"alia")
emp3 = Employee(103,"sana")
emp4 = Employee(104,"jiya")
print(emp3.emp_name)
emp3.show()
