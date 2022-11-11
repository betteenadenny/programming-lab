value=int(input("total number: "))
a=[]
for i in range(value):
    num=int(input("enter integers: "))
    if(num>100):
        num="over"
    a.append(num)
print(a)
