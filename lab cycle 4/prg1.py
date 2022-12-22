class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length * self.breadth
        
    def peimeter(self):
        return 2*(self.length + self.breadth)
        

l1=int(input("Enter the length of rect1:"))
b1=int(input("Enter the breadth of rect1:"))
l2=int(input("Enter the length of rect2:"))
b2=int(input("Enter the breadth of rect2:"))
rect1=rectangle(l1,b1)
rect2=rectangle(l2,b2)

print("Area of first rectangle is ",rect1.area(),"\nArea of second rectangle is ",rect2.area())
print("Peimeter of first rectangle is ",rect1.peimeter(),"\nPeimeter of second rectangle is ",rect2.peimeter())
        
