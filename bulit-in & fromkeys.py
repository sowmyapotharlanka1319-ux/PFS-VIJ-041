#built-in function
#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"sowmya")
print(c)

c["g"]="java"
print(c)'''

#eval()
'''while True:
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)'''                

'''while True:
    a=float(input("a value:"))
    b=float(input("b value:"))
    print(a+b)'''

'''while True:
    a=input("a value:")
    b=input("b value:")
    print(a+b)'''

'''while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

#zip()->we can combine multiple collections into one collection.
'''a=[10,20,30,40,50]
names=["sonu","uma","bhavika","ashri","sana"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)'''

#enumerate()->we can give counter to the collection
'''names=["sonu","uma","bhavika","ashri","sana"]
for i in range(len(names)):
    print(i,names[i])

b=list(enumerate(names))
print(b)

b=list(enumerate(names,15))
print(b)

b=tuple(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)

b=dict(enumerate(names))
print(b)'''

#annonymous functions()->they are nameless func() and use keyword 'lambda'.
#syntax: a=lambda argument:expression

#write a func to cal 2*x+5 where x=5
'''def cal(x):
    print(2*x+5)
cal(5)    

def f():
    x=int(input("enter value:"))
    print(2*x+5)
f()'''    


#a=lambda arg:expr
'''a= lambda x:2*x+5
print(a(5))

a=int(input("enter value:"))
b=lambda x:2*x+5
print(b(a))'''

#TASKS
'''a= lambda x,y:x*y
print(a(2,3))

a=int(input("enter value:"))
b=int(input("enter value:"))
c=lambda a,b:a*b
print(c(a,b))'''

'''a="python"
b=lambda a:a.upper()
print(b(a))'''

'''fname=input("enter first name:")
lname=input("enter last name:")
full=lambda fname,lname:fname+" "+lname
print(full(fname,lname))'''

'''a,b=[x for x in input("enter names:").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()->only remains what we need and discard the rest data.
a=[2,6,7,9,10,12,15,20,40,55,60,80]
'''if a%2==0:
    print(a)'''#error

'''for i in a:
    if i%2==0:
        print(i)
        
b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),set(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c=set()
print(type(c))

d={}
print(type(d))'''

'''a=[[],(),set(),{},"",None,3,8.9,"python",6+3j,True,False]
b=list(filter(None,a))
print(b)'''

#map->each object from a collection and forms a new collection

'''a=[2,4,5,6,7,8,9,22,25]
b=[1,5,8,4,8,9,30,60,65]
c=list(map(max,a,b))
print(c)
#o/p:[2, 5, 8, 6, 8, 9, 30, 60, 65]

d=list(map(min,a,b))
print(d)
#o/p:[1, 4, 5, 4, 7, 8, 9, 22, 25]'''

#runtime-input()
'''a=int(input("a value:"))
b=int(input("b value:"))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b)'''#error

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=input("data1")
b=input("data2:")
print(a+b)'''

'''a,b=[ x for x in input("data").split(",")]
print(a+b)

a,b=input("data").split(",")
print(a+b)'''

'''a,b=map(str,input("data").split(","))
print(a+b)'''

'''a=list(map(int,input("data").split(","))
print(a)'''

'''a=tuple(map(int,input("data").split(","))
print(a)'''

'''a=set(map(int,input("data").split(","))
print(a)'''


'''a=list(map(str,input("data").split(","))
print(a)'''

'''a=list(map(eval,input("data").split(","))
print(a)'''

#dict
'''a=input("enter the key value pairs:")
b=dict(i.split(":")for i in a.split(","))
print(b)'''














































                     






















