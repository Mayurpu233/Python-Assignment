a=[]
size=int(input("How many elements you want to enter?"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
even=0
odd=0
for i in range(size):
    if (a[i]%2==0):
        even=even+1
    else:
         odd=odd+1
print("Total Even=",even,"Total odd=",odd)
