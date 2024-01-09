Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = list()
li
[]
lists = [1,2,3,]
lists
[1, 2, 3]
lists[0] = 56
lists
[56, 2, 3]
lists.append(98)
lists
[56, 2, 3, 98]
lists.append("om")
lists
[56, 2, 3, 98, 'om']
lists.insert(5,4)
lists
[56, 2, 3, 98, 'om', 4]
lists.insert(2,74)
lists
[56, 2, 74, 3, 98, 'om', 4]
lists.append(5,3,6)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lists.append(5,3,6)
TypeError: list.append() takes exactly one argument (3 given)
lists.append([5,3,6])
lists
[56, 2, 74, 3, 98, 'om', 4, [5, 3, 6]]
lists[7,2]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    lists[7,2]
TypeError: list indices must be integers or slices, not tuple
lists[7,[2]]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    lists[7,[2]]
TypeError: list indices must be integers or slices, not tuple
lists[7]
[5, 3, 6]
lists.extend([5,3,6])
lists
[56, 2, 74, 3, 98, 'om', 4, [5, 3, 6], 5, 3, 6]
del lists[7]
lists
[56, 2, 74, 3, 98, 'om', 4, 5, 3, 6]
del lists[5]
lists
[56, 2, 74, 3, 98, 4, 5, 3, 6]
lists.sort()
lists
[2, 3, 3, 4, 5, 6, 56, 74, 98]
lists = [5,36,2,78,96,45,74,12,34]
lists.sort(reverse=True)
lists
[96, 78, 74, 45, 36, 34, 12, 5, 2]
lists.reverse()
lists
[2, 5, 12, 34, 36, 45, 74, 78, 96]
lists.pop()
96
m = lists
m
[2, 5, 12, 34, 36, 45, 74, 78]
lists
[2, 5, 12, 34, 36, 45, 74, 78]
m[0]= 65
m
[65, 5, 12, 34, 36, 45, 74, 78]
lists
[65, 5, 12, 34, 36, 45, 74, 78]
n = lists.copy()
n
[65, 5, 12, 34, 36, 45, 74, 78]
n[0] = 39
n
[39, 5, 12, 34, 36, 45, 74, 78]
lists
[65, 5, 12, 34, 36, 45, 74, 78]
a=2
b=3
a,b = b,a
a
3
b
2
n
[39, 5, 12, 34, 36, 45, 74, 78]
n[0],n[-1] = n[-1],n[0]
n
[78, 5, 12, 34, 36, 45, 74, 39]

========================= RESTART: C:/Python312/Swap.py ========================
[78, 1, 2, 3, 45, 69, 65]
for i in range(len(n)):
    print(n[i])

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    for i in range(len(n)):
NameError: name 'n' is not defined
>>> n = [78, 1, 2, 3, 45, 69, 65]
>>> for i in range(len(n)):
...     print(n[i])
... 
78
1
2
3
45
69
65
>>> for i in n:
...     print(i)
... 
78
1
2
3
45
69
65
>>> if 45 in n:
...     print("exist")
... 
exist
>>> n[::-1]
[65, 69, 45, 3, 2, 1, 78]
