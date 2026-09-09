Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[21,3.05,"python",(4+5j),True,False]
print(a)
[21, 3.05, 'python', (4+5j), True, False]
a=1.3
type(a)
<class 'float'>
a=[21.19]
type(a)
<class 'list'>
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#extend
a.extend(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai'], 'ml', 'ai']
>>> b=['ds','c++']
>>> b.extend(['ai','ml'])
>>> b
['ds', 'c++', 'ai', 'ml']
>>> #insert
>>> a=['black','white']
>>> a.insert(1,'pink')
>>> a
['black', 'pink', 'white']
>>> #index
>>> a=['apple','banana','grapes']
>>> a.index('banana')
1
>>> a.index('apple')
0
>>> #copy
>>> a.copy()
['apple', 'banana', 'grapes']
>>> b=a.copy()
>>> b
['apple', 'banana', 'grapes']
>>> a=['hi','hello','how','are,'you']
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> #pop
...    
>>> a=['hi','hello','how','are']
...    
>>> a.pop()
...    
'are'
>>> a
...    
['hi', 'hello', 'how']
>>> a=['hi','hello','how']
...    
>>> a.remove("hello")
...    
>>> a
...    
['hi', 'how']
