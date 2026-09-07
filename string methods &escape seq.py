Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> a="python course"
>>> len(a)
13
>>> b=""
>>> len(b)
0
>>> c=" "
>>> len(c)
1
>>> #2.count()
>>> a="twinkle twinkle little star"
>>> a.count("t")
5
>>> a.count("twinkle")
2
>>> #find a string
>>> a="natural disaster"
>>> a[1]
'a'
>>> a.find("s")
10
>>> a.find("3")
-1
>>> a.find("u")
3
>>> #escape sequence
>>> a="idno\nname\tmobileno\nbranch\tcollege"
>>> print(a)
idno
name	mobileno
branch	college
>>> a
'idno\nname\tmobileno\nbranch\tcollege'
>>> b="idno:059\nname:sowmya\tmobileno:9999456744\nbranch:cse\ncollage:ALIET"
>>> print(b)
idno:059
name:sowmya	mobileno:9999456744
branch:cse
collage:ALIET
