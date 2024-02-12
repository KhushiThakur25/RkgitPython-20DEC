Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dicts = {"name":"Ram","roll no":32,"class":5}
type(dicts)
<class 'dict'>
a = {}
type(a)
<class 'dict'>
b = dict()
type(b)
<class 'dict'>
c = set()
type(c)
<class 'set'>
v= []
type(v)
<class 'list'>
dicts[0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dicts[0]
KeyError: 0
>>> dicts["name"]
'Ram'
>>> del dicts["class"]
>>> dicts
{'name': 'Ram', 'roll no': 32}
>>> len(dicts)
2
>>> dicts = {"name":"Ram","roll no":32,"class":5,"marks":65,"Fees":"clear"}
>>> dicts.get("marks")
65
>>> dicts.keys()
dict_keys(['name', 'roll no', 'class', 'marks', 'Fees'])
>>> dicts.values()
dict_values(['Ram', 32, 5, 65, 'clear'])
>>> dicts.items()
dict_items([('name', 'Ram'), ('roll no', 32), ('class', 5), ('marks', 65), ('Fees', 'clear')])
>>> dicts["id"] = "A025"
>>> dicts
{'name': 'Ram', 'roll no': 32, 'class': 5, 'marks': 65, 'Fees': 'clear', 'id': 'A025'}
>>> dicts["class"] = 5
>>> dicts
{'name': 'Ram', 'roll no': 32, 'class': 5, 'marks': 65, 'Fees': 'clear', 'id': 'A025'}
>>> dicts["class"] = 8
>>> dicts
{'name': 'Ram', 'roll no': 32, 'class': 8, 'marks': 65, 'Fees': 'clear', 'id': 'A025'}
