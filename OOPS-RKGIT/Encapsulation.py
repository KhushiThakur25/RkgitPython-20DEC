# Public Member: Accessible anywhere from outside class , different.
# Private Member: Accessible within the class
# Protected Member: Accessible within the class and its subclass ,package.

#Private Members:
'''class Employee:
    def __init__(self,emp_ID,emp_name,salary):
        self.emp_ID = emp_ID
        self.emp_name = emp_name
        self.__salary = salary
    def show(self):
        print(f"Name of employee is {self.emp_name} , Id is {self.emp_ID} , salary is {self.__salary}")

emp = Employee(101,"Jasika",10000)
emp.show()
# print(emp.emp_name)
print(emp._Employee__salary)
'''

#Protected Members

class Company:
    def __init__(self):
        self._project = "NLP"
class Employee(Company):
    def __init__(self,name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name:",self.name)
        print("Working on project:",self._project)
    
obj = Employee("Riya")
obj.show()

print("Project:",obj._project)

#getter and setter

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
st1 = Student("siya",14)
print("Name:",st1.name,st1.get_age())
st1.set_age(16)
print("Name:",st1.name,st1.get_age())

