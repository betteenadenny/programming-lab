import math
l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))

def even():
    a=[]
    b=[]
    for i in range(l,u+1):
        k=i
        f=0
        while i>0:
            d=i%10
            if d%2!=0:
                f=1;
                break
            else:
                i=i//10
        if f==0:
            a.append(k)
    for j in a:
        s=(int(math.sqrt(j)))*(int(math.sqrt(j)))
        if s==j:
            b.append(j)
    print(b)    
            
if ((l>999 and l<10000) and (u>l and u<10000)):
    even()
else:
    print("Enter a valid 4-digit limit!")
