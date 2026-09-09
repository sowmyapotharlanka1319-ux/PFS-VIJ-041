Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
a={'name':'sowmya','city':'vij'}
print(a)
{'name': 'sowmya', 'city': 'vij'}
type(a)
<class 'dict'>
b={'name','sowmya'}
type(b)
<class 'set'>
#methods
a={'year':2026,'month':'oct','date':21}
a.keys()
dict_keys(['year', 'month', 'date'])
a.values()
dict_values([2026, 'oct', 21])
a.items()
dict_items([('year', 2026), ('month', 'oct'), ('date', 21)])
a['month']
'oct'
a.get('month')
'oct'
a['oct']
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a['oct']
KeyError: 'oct'
#update
a={'name':'sowmya','year':2026}
a.update({'email':'sowmyapotharlanka@gmail.com'})
a
{'name': 'sowmya', 'year': 2026, 'email': 'sowmyapotharlanka@gmail.com'}
a.update({'time':6,'clg':'Aliet'})
a
{'name': 'sowmya', 'year': 2026, 'email': 'sowmyapotharlanka@gmail.com', 'time': 6, 'clg': 'Aliet'}
#set default
a={'hour':3,'min':13}
a.setdefault('sec',8)
8
a
{'hour': 3, 'min': 13, 'sec': 8}
#pop
a={'book':'The Hobbit','year':2012}
a.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop('book')
'The Hobbit'
a
{'year': 2012}
#popitem
a={'year':2013,'time':8,'sec':10}
a.popitem()
('sec', 10)
a
{'year': 2013, 'time': 8}
#len
a={'class':3,'course':'python','duration':250}
>>> len(a)
3
>>> a.count('course')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.count('course')
AttributeError: 'dict' object has no attribute 'count'
>>> a.index('class')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.index('class')
AttributeError: 'dict' object has no attribute 'index'
>>> a.copy()
{'class': 3, 'course': 'python', 'duration': 250}
>>> b=a.copy()
>>> b
{'class': 3, 'course': 'python', 'duration': 250}
>>> b.clear()
>>> b
{}
>>> a={'name':'sowmya','year':2026,'name':'sowmya'}
>>> print(a)
{'name': 'sowmya', 'year': 2026}
>>> a={'name':'sowmya','year':2026,'name':'sai'}
>>> print(a)
{'name': 'sai', 'year': 2026}
>>> a={'name':'sowmya','year':2026,'name1':'sowmya'}
>>> print(a)
{'name': 'sowmya', 'year': 2026, 'name1': 'sowmya'}
>>> #single key ,multiple values
>>> a={'idnos':[10,20,30],'names':['sowmya','hari','sai'],'places':['vij','hyd','viz']}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['sowmya', 'hari', 'sai'], 'places': ['vij', 'hyd', 'viz']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names', 'places'])
>>> a.values()
dict_values([[10, 20, 30], ['sowmya', 'hari', 'sai'], ['vij', 'hyd', 'viz']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sowmya', 'hari', 'sai']), ('places', ['vij', 'hyd', 'viz'])])
>>> #task
