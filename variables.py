Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=10
print(a)
10
e=100
print(E)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(E)
NameError: name 'E' is not defined. Did you mean: 'e'?
print(e)
100
_a=21
print(_a)
21
first_name="sowmya"
print(first_name)
sowmya
city="vij"
print(city)
vij
Name="sowmya"
print(Name)
sowmya
NAME="SOWMYA"
print(NAME)
SOWMYA
if=23
SyntaxError: invalid syntax
del=22
SyntaxError: invalid syntax
a=3,b=4
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=4
print(a*b)
12
a,b=3,4
print(a+b)
7
 name="sowmya"
 
SyntaxError: unexpected indent
_name="sowmya"
>>> print(_name)
sowmya
>>> 3=9
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a3=5
>>> print(a3)
5
>>> del(a3)
>>> print(a3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a3)
NameError: name 'a3' is not defined. Did you mean: 'a'?
>>> a012345678=13
>>> print(a012345678)
13
>>> #unpacking
>>> a=(2,3,44,6,21)
>>> print(a)
(2, 3, 44, 6, 21)
>>> print("a")
a
>>> ,b,c=1,2,3
SyntaxError: invalid syntax
>>> a,b,c=5,6,7
>>> print(a,b,c)
5 6 7
>>> a,b,c=2,3,8,6,7,8
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c=2,3,8,6,7,8
ValueError: too many values to unpack (expected 3, got 6)
>>> #unpacking
>>> a,b,c=(4,5,6)
>>> print(a,b,c)
4 5 6
>>> fname="somwya"
>>> lname="potharlanka"
>>> print(fname+lname)
somwyapotharlanka
>>> print(fname,lname)
somwya potharlanka
>>> print(fname+""+lname)
somwyapotharlanka
>>> print(fname+" "+lname)
somwya potharlanka
