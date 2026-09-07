Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #replace
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> b="python java1"
>>> b.replace("java1","c")
'python c'
>>> #upper
>>> a="java"
>>> a.upper()
'JAVA'
>>> #lower()
>>> b="PRECIOUS"
>>> b.lower()
'precious'
>>> #capitalize()
>>> 
>>> c="python"
>>> c[0].upper()
'P'
>>> c.capitalize()
'Python'
>>> #title()
>>> d="i am in the class"
>>> d.title()
'I Am In The Class'
>>> #conditions
>>> a="python"
>>> a.startswith(p)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.startswith(p)
NameError: name 'p' is not defined
>>> a="hello world"
>>> a.startswith("h")
True
>>> a.endswith("d")
True
>>> a.isalpha()
False
>>> b="helloworld"
b.isalpha()
True
c=1234
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="1234"
c.isdigit()
True
c.isalnum()
True
b.isalnum()
True
#strip
a="         sowmya     "
a.strip()
'sowmya'
a.lstrip()
'sowmya     '
a.rstrip()
'         sowmya'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
#example
fname="sowmya"
lname="p"
print(fname+lname)
sowmyap
print(fname+" "+lname)
sowmya p
print((fname+" "+lname).title())
Sowmya P
#split
a="i am learning python fullstack"
a.split()
['i', 'am', 'learning', 'python', 'fullstack']
b="be consistent"
b.split()
['be', 'consistent']
b.join()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b.join()
TypeError: str.join() takes exactly one argument (0 given)
#join
b="python","java","c++"
"".join(b)
'pythonjavac++'
"c".join(b)
'pythoncjavacc++'
#formatting
a=5
b=8
print(a+b)
13
print("the sum is"a+b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("the sum is",a+b)
the sum is 13
city="vij"
print("the city is",city)
the city is vij
#format method
a="motu"
b="pathulu"
print("hello {}{}",format(a,b))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print("hello {}{}",format(a,b))
ValueError: Invalid format specifier 'pathulu' for object of type 'str'
print("hello {}{}".format(a,b))
hello motupathulu
print("hello {} {}".format(a,b))
hello motu pathulu
print("hello {} hello {}".format(a,b))
hello motu hello pathulu
#fstring
a="virat"
b="kohli"
print(f"hello {a}{b}")
hello viratkohli
print(f"hello{a} {b}")
hellovirat kohli
print(f"hello {a} hello {b}")
hello virat hello kohli
#example
fname="sowmya"
lname="potharlanka"
print("hello {} {}".formaat(fname,lname))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print("hello {} {}".formaat(fname,lname))
AttributeError: 'str' object has no attribute 'formaat'. Did you mean: 'format'?
print("hello {}{}".format(fname,lname))
hello sowmyapotharlanka
print("hello {} {}".format(fname,lname))
hello sowmya potharlanka
print(f"hello {fname} (lname}")
SyntaxError: f-string: single '}' is not allowed
print(f"hello {fname} {lname}")
hello sowmya potharlanka
print(f"hello{fname} hello{lname}")
hellosowmya hellopotharlanka
print(f"hello {fname} hello {lanme}")
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    print(f"hello {fname} hello {lanme}")
NameError: name 'lanme' is not defined. Did you mean: 'lname'?
print(f"hello {fname} hello {lname}")
hello sowmya hello potharlanka
a=9
b=4
print("the sum is {} {}".format(a,b))
the sum is 9 4
print("the sum is {} ".format(a,b))
the sum is 9 
print(f"the sum is {a+b}")
the sum is 13
print("the sum is {}".format(a+b))
the sum is 13
