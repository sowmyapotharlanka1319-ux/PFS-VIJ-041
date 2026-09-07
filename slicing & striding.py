Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> b="vijayawada is a royal city"
>>> b[22:]
'city'
>>> b[:10]
'vijayawada'
>>> b[11:13]
'is'
>>> b[16:21]
'royal'
>>> c="Happy teachers day"
>>> c[:-13]
'Happy'
>>> c[-3:]
'day'
>>> c[-12:-5]
'teacher'
>>> d="vizag is a city of destiny"
>>> d[-26:-21]
'vizag'
>>> d[-15:-11]
'city'
>>> d[-7:]
'destiny'
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a[::3]
'dacn'
>>> a="Machine learning"
>>> a[::3]
'Mheeng'
>>> a[::9]
'Me'
a[3:11]
'hine lea'
a[5:]
'ne learning'
b="cloud computing"
b[2:13:3]
'o mt'
b[4:14:5]
'dp'
b[3:12:6]
'up'
b[:2:1]
'cl'
c="Python course"
c[-1:-9:-3]
'eu '
c[:-7:-2]
'ero'
a[-9:-5:-2]
''
a[::1]
'Machine learning'
c[::1]
'Python course'
c[::-1]
'esruoc nohtyP'
c[7:3:2]
''
c[-9:2:-4]
'o'
