#module->It is a single python file consists of python code.
#'import' is a keyword used to import module.

'''def greetings(name):
    print("welcome",name)'''

'''a=10
b=20
print("Sum is",a+b)'''

'''a=int(input("a value:"))
b=int(input("b value:"))
print(a*b)'''

'''details={"idnos":[10,20,30],
            "names":["sowmya","sai","nanchi"],
            "marks":[70,80,90]}'''

'''if __name__=="__main__":
     a=[10,20,30,40]
     a.append("code")
     print(a)'''


'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''


#math module
'''import math
print(math.pi)
print(math.pi*5)
print(math.sqrt(8))
print(math.pow(5,4))
print(math.log(15))
print(math.cos(30))
print(math.tan(45))
print(math.ceil(4.3))
print(math.ceil(2,4))#error
print(math.floor(9.4))'''


'''from math import pi,log,sqrt,tan
print(pi,log(4),sqrt(13),tan(30))'''

#sys module
'''import sys
print(sys.path)

for i in sys.path:
    print(i)

print(sys.version)'''

#OS module
#It is a s/w that interacts with the system.
'''import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct5"))
#print(os.listdir())
#print(os.chdir("C:\\Users\\DELL\\Downloads"))
#print(os.listdir()) '''     

#random module->used to generate random numbers in python.

#sample  -->generate random numbers within given range.
'''import random
a=random.sample(range(5,50),8)
print(a)'''
#o/p:[18, 33, 36, 29, 28, 15, 42, 37]


#randint-->random number get generated including number.
'''import random
a=random.randint(5,12)
print(a)'''
#o/p:12

#choice -->random num generated within given list. 
'''import random
a=[10,20,30,40]
b=random.choice(a)
print(b)'''
#o/p:10


#TASK
'''while True:
    import random
    a=int(input("roll the dice:"))
    b=random.randint(1,6)
    print(b)
    option=input("enter the option:1.yes\n2.no")
    if option==1:
        continue
    elif option==2:
        break'''

#Calendar module
'''import calendar
year=2026
month=10
print(calendar.month(year,month))'''

'''import calendar
year=2028
print(calendar.calendar(year))'''

'''import calendar
a=int(input("enter the year:"))
b=int(input("enter the month:"))
print(calendar.month(a,b))'''

#Date & Time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a)#epoch time

#local time
b=time.localtime(a)
print(b)

#converting to human readable
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"today time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")

print(f"present day of the year is {b.tm_yday}")'''


#TASK
'''import random
import time
print("......generating a random number.........")
for i in range(10):
    a=random.randint(0,10)
    print(a)
    time.sleep(2)'''

#regular expression(regex) --> regex are powerful tools(module) embedded in python which is mainly used
#to find a pattern within a given string or statements or files ad mainly used for text manpulation.

'''a="codegnan is in vij"
print(a)

a="codegnan\nis\tin\nvij"
print(a)

a=r"codegnan\nis\tin\nvij"    
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces
\S->it represents non-white spaces'''

#compile()  #re:regular expression
import re
'''a="code map money cash cap maths cup cat mug mat"
b=re.compile(r"m\w\w\w\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall()
'''b=re.findall(r"m\w+",a)
print(b)

c=re.findall(r"c\w+",a)
print(c)'''

#split()
'''c=re.split(r"m",a)
print(c)

d=re.split(r"\s",a)'''

#sub()   sub:substitute(replace)
'''e=re.sub(r"maths","science",a)
print(e)'''

#TASK
'''a="hi there 123 come here"
b=re.findall(r"\d+",a)
print(b)

a="year 2026 month 10"
b=re.findall(r"\D+",a)
print(a)'''




















