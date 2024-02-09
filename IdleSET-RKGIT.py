Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = {1,2,2,3,4}
>>> st
{1, 2, 3, 4}
>>> type(st)
<class 'set'>
>>> a = set()
>>> a
set()
>>> a.add(5)
>>> a
{5}
>>> st_1 = {1,2,3,4,5}
>>> st_2 = {6,7,8,2,3}
>>> st_1.union(st_2)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> st_1
{1, 2, 3, 4, 5}
>>> st_2
{2, 3, 6, 7, 8}
>>> st_1 = st_1.union(st_2)
>>> st_1
{1, 2, 3, 4, 5, 6, 7, 8}
>>> st_2
{2, 3, 6, 7, 8}
>>> st_3 = {2,56,3,8,9}
st_3.update(st_2)
st_3
{2, 3, 6, 7, 8, 9, 56}
st_1.intersection(st_3)
{2, 3, 6, 7, 8}
st_1
{1, 2, 3, 4, 5, 6, 7, 8}
st_1.intersection_update(st_3)
st_1
{2, 3, 6, 7, 8}
st_1 = {1,2,3,4,8}
st_2 = {2,3,7,9}
st_1 - st_2
{8, 1, 4}
st_1.difference(st_2)
{8, 1, 4}
st_1.isdisjoint(st_2)
False
st_1.clear()
st_1
set()
del st_1
st_1
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    st_1
NameError: name 'st_1' is not defined. Did you mean: 'st_2'?
st_1.issuperset(st_2)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    st_1.issuperset(st_2)
NameError: name 'st_1' is not defined. Did you mean: 'st_2'?
st_1 = {1,2,3,4,8}
st_1.issuperset(st_2)
False
st_1.issubset(st_2)
False
st_1.pop()
1
st_1
{2, 3, 4, 8}
st_1.remove(3)
st_1
{2, 4, 8}
st_1.remove(9)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    st_1.remove(9)
KeyError: 9
st_1.discard(9)
