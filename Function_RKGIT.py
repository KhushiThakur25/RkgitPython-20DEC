Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def calc():
    x = 12
    y = 4
    z = x+y
    print("Sum is:",z)

calc()
Sum is: 16
x
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = 56
def calc():
    x = 12
    y = 4
    z = x+y
    print("Sum is:",z)

calc()
Sum is: 16
x
56
def calc():
    y = 4
    z = x + y
    print("Sum is:",z)

calc()
Sum is: 60
def calc():
    x = 12
    y = 4
    z = x+y
    print("Sum is:",z)

def calc():
    x = 1
    x = x + 5
    y = 4
    z = x+y
    print("Sum is:",z)

calc()
Sum is: 10
z
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    z
NameError: name 'z' is not defined
def calc():
    x = 1
    x = x + 5
    y = 4
    global z
    z = x+y
    print("Sum is:",z)

calc()
Sum is: 10
z
10
def calc():
    d = a+b+c
    print(d)


def calc(a,b,c):
    d = a+b+c
    print(d)

calc(5,6,7)
18
calc(5,6)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    calc(5,6)
TypeError: calc() missing 1 required positional argument: 'c'
def calc(a,b,c):
    d = a+b+c
    print(d)

calc(a = 2,b = 5,c = 6)
13
calc(b = 5,c = 6,a = 2)
13
calc(x = 2,y = 5, z = 6)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    calc(x = 2,y = 5, z = 6)
TypeError: calc() got an unexpected keyword argument 'x'
def calc(a = 2,b = 5,c = 6):
    d = a+b+c
    print(d)

calc()
13
calc(7)
18
calc(x = 6,y = 2,z = 1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    calc(x = 6,y = 2,z = 1)
TypeError: calc() got an unexpected keyword argument 'x'
calc(2,3,6,5)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    calc(2,3,6,5)
TypeError: calc() takes from 0 to 3 positional arguments but 4 were given
calc(a = 3,b=9)
18
calc(a = 6, 5)
SyntaxError: positional argument follows keyword argument
calc(5,b = 8)
19
def calc(*args):
    s = sum()x
    
SyntaxError: incomplete input
def calc(*args):
    s = sum(args)
    print("Sum is:",s)

calc(5,6,8,9,2,3)
Sum is: 33
def calc(*args):
    print(args)
... 
>>> calc(5,6,1,2)
(5, 6, 1, 2)
>>> calc()
()
>>> calc(x = 5)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    calc(x = 5)
TypeError: calc() got an unexpected keyword argument 'x'
>>> def details(name,age,sal,*address):
...     print(name)
...     print(age)
...     print(sal)
...     print(address)
... 
>>> details("Ram",45,45600,"Delhi","Chennai","Pune")
Ram
45
45600
('Delhi', 'Chennai', 'Pune')
>>> def person(**details):
...     print(details)
... 
>>> person(name = "Amit",age = 45, sal = 45000)
{'name': 'Amit', 'age': 45, 'sal': 45000}
