def myfunc(n):
   return lambda a :a+n

myaddition = myfunc(25)

n=int(input("enter any number:"))
print(myaddition(n))
  
