Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Python312/ChatAppRKGIT.py
Enter the message..hello
Traceback (most recent call last):
  File "C:/Python312/ChatAppRKGIT.py", line 8, in <module>
    print(random.choice(greetingIntent,"user"))
TypeError: Random.choice() takes 2 positional arguments but 3 were given

===================== RESTART: C:/Python312/ChatAppRKGIT.py ====================
Enter the message..hello
hello there user
Enter the message..hy
hey there user
Enter the message..bye
ok Bye
import datetime
datetime.datetime
<class 'datetime.datetime'>
datetime.datetime.now()
datetime.datetime(2024, 1, 12, 17, 34, 38, 771665)
datetime.datetime.now().date
<built-in method date of datetime.datetime object at 0x000001B430864C30>
datetime.datetime.now().date()
datetime.date(2024, 1, 12)
>>> datetime.datetime.now().time()
datetime.time(17, 36, 4, 957559)
>>> from datetime import datetime as dt
>>> dt
<class 'datetime.datetime'>
>>> date  =dt.now().date()
>>> date
datetime.date(2024, 1, 12)
>>> time = dt.now().time()
>>> print(time)
17:37:58.630812
>>> print(date)
2024-01-12
>>> date.strftime("%d/%m/%y")
'12/01/24'
>>> date.strftime("%d-%m-%y")
'12-01-24'
>>> date.strftime("%d/%m/%y,%a")
'12/01/24,Fri'
>>> date.strftime("%d/%m/%y,%A")
'12/01/24,Friday'
>>> date.strftime("%d/%b/%y,%a")
'12/Jan/24,Fri'
>>> date.strftime("%d/%B/%y,%a")
'12/January/24,Fri'
>>> date.strftime("%d/%m/%Y,%a")
'12/01/2024,Fri'
time.strftime("%H:%M:%S")
'17:37:58'
time.strftime("%H:%M:%S,%p")
'17:37:58,PM'
