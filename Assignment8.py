#Question 1
class circle():
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        print("Area:",3.14*r*r)
    def getCircumference(self):
        print("Circumference:",2*3.14*r)
r=int(input("enter the radius"))
c=circle(r)
c.getArea()
c.getCircumference()


#Question 2
class student():
    def __init__(self,r,n):
        self.roll_no=r
        self.name=n
    def age(self,a):
        self.age=a
    def display(self):
        print('Roll_no {}.\nName is {}.\nAge is {}.'.format(self.roll_no,self.name,self.age))
name=input("inter the name")
r=int(input("enter the rollno"))
stu=student(name,r)
a=int(input("Enter the age"))
stu.age(a)
stu.display()



#Question 3
class temp():
     def f_to_c(self,f):
        self.f=f
        c=(self.f-32)*5/9
        print(c)
     def c_to_f(self,c):
        self.c=c
        f=(self.c*9/5)+32
        print(f)
   
n=int(input("enter 1 for c to f and 2 for f to c"))
temp1=temp()
if(n==1):
    x=float(input("Enter temp\n"))
    temp1.c_to_f(x)
else:
    x=float(input("Enter temp\n"))
    temp1.f_to_c(x)


#Question 4
class movie():
    def __init__(self):
        self.artistname='NA'
        self.year='NA'
        self.rating='NA'
    def add_info(self,a,y,r):
        self.artist=a
        self.year=y
        self.rating=r
    def display(self):
        print("Artist : {}.\nRating : {}.\nYear : {}".format(self.artistname,self.year,self.rating))
a=input("enter the y to add details")
m1=movie()
if(a=='y'):
    name=input("Enter artist name")
    year=int(input("Enter year"))
    rating=int(input("Enter ratings"))
    m1.add_info(name,year,rating)
else:
    m1.display()



#Question 5
class Animals():
    def animal_attribute(self):
        print("base class")
class Tiger(Animals):
    pass
a=Tiger()
a.animal_attribute()


#Question 6
#Syntax Error(print)



#Question 7
class shape():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print("Area is ",self.length*self.breadth)
class square(shape):
    pass
class rectangle(shape):
    pass
l=int(input("Enter length"))
b=int(input("Enter breadth "))
if(l==b):
    obj=square(l,b)
    obj.area( )
else:
    obj=rectangle(l,b)
    obj.area( )

