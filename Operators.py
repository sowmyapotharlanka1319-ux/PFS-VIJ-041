Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arthimetic Operators
a=21
b=13
print(a+b)
34
print(a-b)
8
print(a*b)
273
print(a//b)
1
print(a/b)
1.6153846153846154
print(a**b)
154472377739119461
print(a%b)
8
#Assignment
a=6
b=7
a+=b
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
20
a-=3
a
17
a*=2
a
34
a//=4
a
8
a**=5
a
32768
a%=6
a
2
a%=2
a
0
a%=3
a
0
b+=3
b
10
b-=4
b
6
b//=2
b
3
b%=8
b
3
b**=2
b
9
#Comparision
a=19
b=16
a<b
False
b>a
False
a>b
True
a!=b
True
a>=b
True
b>=a
False
a<=b
False
B<=a
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    B<=a
NameError: name 'B' is not defined. Did you mean: 'b'?
b<=a
True
#Logical
a=12
b=23
a<b and b>a
True
a>b and b<a
False
a!=b and a==b
False
a<=b and b==a
False
a>b or b<a
False
a>b or b==a
False
a!=b or b>a
True
a<b or a!=b
True
#identify
a=4
typea(a) is int
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    typea(a) is int
NameError: name 'typea' is not defined. Did you mean: 'type'?
type(a)is int
True
>>> type (a) is not in float
SyntaxError: invalid syntax
>>> type(a) is not float
True
>>> #membership
>>> a=2,4,5,8,9
>>> 8 in a
True
>>> 3 not in a
True
>>> 4 not in a
False
>>> #Bitwise
>>> a=2
>>> b=6
>>> bin(a)
'0b10'
>>> a&b
2
>>> a|b
6
>>> a=9
>>> ~a
-10
>>> -(a+1)
-10
>>> a=-3
>>> ~a
2
>>> a=6
>>> b=8
>>> a^b
14
>>> a=3
>>> b=5
>>> a^b
6
>>> a=9
>>> a<<2
36
>>> a>>2
2
>>> a=3
>>> a>>2
0
