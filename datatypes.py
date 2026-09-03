Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=21
type(a)
<class 'int'>
b=2.88
type(b)
<class 'float'>
c='sonu'
type(c)
<class 'str'>
d="course"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
f=a+2j
type(f)
<class 'complex'>
g=2j+3j
type(g)
<class 'complex'>
h=True
type(h)
<class 'bool'>
i=False
type(i)
<class 'bool'>
#int
int(2)
2
int(1.3)
1
int("sowmya")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int("sowmya")
ValueError: invalid literal for int() with base 10: 'sowmya'
int(2+6j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(2+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(9)
9.0
float(0.21)
0.21
float("code")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float("code")
ValueError: could not convert string to float: 'code'
float(7+8j)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(7+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(2)
'2'
str(8.5)
'8.5'
str("codegnan")
'codegnan'
>>> str(3+4j)
'(3+4j)'
>>> str(True)
'True'
>>> str(Flase)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    str(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
>>> str(False)
'False'
>>> #complex
>>> comples(9)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    comples(9)
NameError: name 'comples' is not defined. Did you mean: 'complex'?
>>> complex(8)
(8+0j)
>>> complex(4.44)
(4.44+0j)
>>> complex("world")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex("world")
ValueError: complex() arg is a malformed string
>>> complex(6+7j)
(6+7j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #Boolean
>>> bool(21)
True
>>> bool(8.90)
True
>>> bool("red")
True
>>> bool(4+6j)
True
>>> bool(True)
True
>>> bool(False)
False
