Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Python312/QsDict.py
Enter your stringone
1
>>> di = {"name":["Ram","OM","Zoya","Muskaan"],"dept":["HR","Manager","intern"]}
>>> di["name"]
['Ram', 'OM', 'Zoya', 'Muskaan']
>>> di["name",2]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    di["name",2]
KeyError: ('name', 2)
>>> di["name"][2]
'Zoya'
>>> di = {"name":["Ram","OM","Zoya","Muskaan"],"dept":{"HR":1,"Manager":2,"intern":6}}
>>> di["dept"]
{'HR': 1, 'Manager': 2, 'intern': 6}
>>> di["dept"]["Manager"]
2
