#ERROR HANDLING
'''1.syntax error->compile error eg:indendation error
2.Run-time error->during execution it will happens eg:value,name,zerodivisionerror
3.logical error->error in logic(it can't be visible) eg:no o/p or empty''' 

#Syntax error
'''for i in range(10)
print(i)'''

#runtime error
'''Print(4+8)'''
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''

#logical error
'''a=10
b=20
print(a-b)

a=4
b=8
if a<b:
    print("less")

a=4
b=8
if a>b:
    print("less")'''  


#Exception handling
#It consists of 4 blocks: try,except,finally,else
'''while True:
     try:
         a=int(input("a value"))
         b=int(input("b value"))
         c=a//b
         print(c)
     except:
         print("exception is raised")
     else:
         print("no exceptions")
     finally:
         print("program ends")'''


#File handling
'''a=open("sonu.txt","w")
a.write("python full stack")
a.close()'''

'''a=open("sonu.txt","w")
a.write("vijayawada")
a.close()'''

#append()
'''a=open("sonu.txt","a")
a.write("\tbanglore")
a.close()'''

#task
#insert content into file in runtime
'''a=open("sonu.txt","a")
a.write(input("enter content:"))
a.close()'''

'''a=open("sonu.txt","w")
b=input("enter the content:")
a.write(b)
a.close()'''

#read()
#a=open("sonu.txt")
#print(a.read())#display entire content
#print(a.readline())#display first line
#print(a.readlines())#display with \n(new line)
#print(a.read(15))#display no.of characters/read up to that number

#writelines()-->it makes every object side by side
'''a=open("python.txt","w")
b=["priya","sowmya","bhavika","uma","himaja"]
a.writelines(b)
a.close()'''

'''a=open("python.txt","w")
b=["priya","sowmya","bhavika","uma","himaja"]
a.writelines("\n".join(b))
a.close()'''


'''a=open("list.py")
print(a.read())'''


'''a=open("C:\\Users\\DELL\\OneDrive\\Documents\\Desktop\\PFS-041\\variable len arguments.py")
print(a.read())'''














 













