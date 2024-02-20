Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Python312/roughRKGIT.py
11
>>> names = ["Amit","Aman","Ram","Hari","Yash"]
>>> ages = [45,22,52,19,23]
>>> zip(names,ages)
<zip object at 0x0000020F79E08980>
>>> list(zip(names,ages))
[('Amit', 45), ('Aman', 22), ('Ram', 52), ('Hari', 19), ('Yash', 23)]
>>> ages = [45,22,52,19,23,65,87]
>>> list(zip(names,ages))
[('Amit', 45), ('Aman', 22), ('Ram', 52), ('Hari', 19), ('Yash', 23)]
>>> dict(zip(names,ages))
{'Amit': 45, 'Aman': 22, 'Ram': 52, 'Hari': 19, 'Yash': 23}
>>> set(zip(names,ages))
{('Yash', 23), ('Hari', 19), ('Amit', 45), ('Aman', 22), ('Ram', 52)}
>>> for i in range(len(names)):
...     print(i,names[i])
... 
0 Amit
1 Aman
2 Ram
3 Hari
4 Yash
>>> enumerate(names)
<enumerate object at 0x0000020F7812A390>
list(enumerate(names))
[(0, 'Amit'), (1, 'Aman'), (2, 'Ram'), (3, 'Hari'), (4, 'Yash')]
list(enumerate(names,100))
[(100, 'Amit'), (101, 'Aman'), (102, 'Ram'), (103, 'Hari'), (104, 'Yash')]

====================== RESTART: C:/Python312/roughRKGIT.py =====================
11
<function <lambda> at 0x000001942FAAFD80>

====================== RESTART: C:/Python312/roughRKGIT.py =====================
11
BRAINMENTORS

======== RESTART: C:/Python312/roughRKGIT.py ========
11
BRAINMENTORS
a = [lambda x : x%2 == 0 , range(1,10)]
a
[<function <lambda> at 0x0000023D7D6EFEC0>, range(1, 10)]
a()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a()
TypeError: 'list' object is not callable
a = lambda x : x%2 == 0 , range(1,10)
a
(<function <lambda> at 0x0000023D7D708040>, range(1, 10))
a()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a()
TypeError: 'tuple' object is not callable
a = 2,3
type(a)
<class 'tuple'>
a = filter(lambda x : x%2 == 0 , range(1,10))
a
<filter object at 0x0000023D7D6D3040>
a()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a()
TypeError: 'filter' object is not callable
list(filter(lambda x : x%2 == 0 , range(1,10)))
[2, 4, 6, 8]
list(lambda x : x%2 == 0 , range(1,10))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(lambda x : x%2 == 0 , range(1,10))
TypeError: list expected at most 1 argument, got 2
