Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sort
a=['vij','hyd','chennai','viz']
a.sort()
a
['chennai', 'hyd', 'vij', 'viz']
b=['1,2,5,9,3,8,99,82']
b.sort()
b
['1,2,5,9,3,8,99,82']
#pop
a.pop()
'viz'
a
['chennai', 'hyd', 'vij']
b.pop()
'1,2,5,9,3,8,99,82'
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.pop(3)
IndexError: pop index out of range
a.pop(0)
'chennai'
#remove
a.remove('hyd')
a
['vij']
#reverse
a=['mango','banana','apple']
a.reverse()
a
['apple', 'banana', 'mango']
a=['c','c++','java']
#len
len(a)
3
b='java'
len(b)
4
len(a)
3
len(b)
4
a.count('a')
0
a.count('c')
1
b.count('a')
2
#clear
a=['python','c','c++','java']
a.clear()
a
[]
a.append['sonu']
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.append['sonu']
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append("sonu")
a
['sonu']
#tuple
a=(5,2.7,'sonu',2+9j,True,False)
print(a)
(5, 2.7, 'sonu', (2+9j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.count(2+9j)
1
a.index(2.7)
1
#sets{}
a={13,4.89,'sonu',7+6j,True,False}
print(a)
{False, True, 4.89, (7+6j), 'sonu', 13}
type(a)
<class 'set'>
b={1,0,8,3,9,8,6,8}
print(b)
{0, 1, 3, 6, 8, 9}
#add
a={4,6,8,9,2}
a.add(10)
a
{2, 4, 6, 8, 9, 10}
#issubset
a={2,6,7,8,9}
b={2,8,9}
b.issubset(a)
True
a.issubset(b)
False
#superset
a={4,5,7,8,9}
b={5,7,8}
a.superset(b)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
True
b.issuperset(a)
False
#union
a.union(b)
{4, 5, 7, 8, 9}
b.union(a)
{4, 5, 7, 8, 9}
#intersection
a.intersection(b)
{8, 5, 7}
#update
a.update(b)
a
{4, 5, 7, 8, 9}
b.update(a)
b
{4, 5, 7, 8, 9}
a={7,8,9,13,52,66,72}
b={10,12,22,21}
a.update(b)
a
{66, 7, 8, 9, 72, 10, 12, 13, 52, 21, 22}
b.update(a)
b
{66, 7, 8, 9, 10, 72, 12, 13, 52, 21, 22}
#difference
a.difference(b)
set()
a={4,8,9,6,5}
b={6,7,8,9,5,1}
a.difference(b)
{4}
b.difference(a)
{1, 7}
#symmeteric difference
a={1,2,5,6,8,9}
b={6,8,5,10,12,13,15}
a.symmetric_difference(b)
{1, 2, 9, 10, 12, 13, 15}
#difference_update
a={2,3,4,7,8,6}
b={2,5,6,12,16}
a.difference_update(b)
a
{3, 4, 7, 8}
b.difference_update(a)
b
{16, 2, 5, 6, 12}
#intersection_update
a={3,4,5,6,7,8}
b={9,8,2,3,6,7}
a.intersection_update(b)
a
{8, 3, 6, 7}
b.intersection_update(a)
b
{8, 3, 6, 7}
#symmetric_difference_update
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15}
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 13, 14, 15}
b.symmetric_difference_update(a)
b
{6, 7, 8, 9, 10, 11, 12}
#pop
a={10,20,30,40}
a.pop()
40
a.remove(10)
a
{20, 30}
a.pop(20)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a.pop(20)
TypeError: set.pop() takes no arguments (1 given)
#discard
a={4,5,7,8,9}
a.discard(5)
a
{4, 7, 8, 9}
a.discard()
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.discard()
TypeError: set.discard() takes exactly one argument (0 given)
a.copy()
{8, 9, 4, 7}
>>> b=a.copy()
>>> b
{8, 9, 4, 7}
>>> #clear and add
>>> a={3,5,8,9,4}
>>> a.clear()
>>> a
set()
>>> a.add(12)
>>> a
{12}
>>> #methods not included
>>> a={5,8,7,9}
>>> len(a)
4
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> a={1,2,4,5,7,2,1}
>>> a.count(1)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
>>> #disjoint
>>> a={12,17,19,20,21}
>>> b={12,15,20,15}
>>> a.isdisjoint(b)
False
>>> a={6,7,8,9}
>>> b=(12,11,14,13}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> b={12,11,14,13}
>>> a.isdisjoint(b)
True
