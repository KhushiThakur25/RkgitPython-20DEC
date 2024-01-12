Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
tup = (1,2,3,4,5,6)
type(tup)
<class 'tuple'>
vi = 2,3,6,5,8
vi
(2, 3, 6, 5, 8)
ti = tuple()
ti
()
len(vi)
5
vi.count(3)
1
>>> vi.index(6)
2
>>> vi.append(9)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    vi.append(9)
AttributeError: 'tuple' object has no attribute 'append'
>>> vi[3] = 8
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    vi[3] = 8
TypeError: 'tuple' object does not support item assignment
>>> temp = list(vi)
>>> temp
[2, 3, 6, 5, 8]
>>> li = []
>>> for i in range(5):
...     el = int(input("enter element"))
...     li.append(el)
... 
enter element23
enter element65
enter element98
enter element74
enter element41
>>> li
[23, 65, 98, 74, 41]
