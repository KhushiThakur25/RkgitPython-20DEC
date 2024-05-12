#single inheritance--
class Parent:
    def show(self):
        print("I'm a parent class")
    
class Child(Parent):
    def display(self):
        print("I'm child class")

Ram = Child()
Ram.display()
Ram.show()

#Multiple inheritance
class Base1:
    def func1(self):
        print("I'm a parent class 1")
class Base2:
    def func2(self):
        print("I'm a parent class 2")
class Derived(Base1,Base2):
    def show(self):
        print("I'm derived class")
jay = Derived()
jay.func1()
jay.func2()
jay.show()

#Multilevel inheritance
class GrandParent:
    def func1(self):
        print("I'm grand parent")
class Parent(GrandParent):
    def func2(self):
        print("I'm a parent ")
class Child(Parent):
    def func3(self):
        print("I'm a child class")

Rahul = Child()
Rahul.func1()
Rahul.func2()
Rahul.func3()




