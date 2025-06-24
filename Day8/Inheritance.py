# Types of inheritance in python
# Example 1: Single inheritance

class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")
# When A is put in brackets after B.
# B becomes the child class of A class.

bobj=B()
bobj.m1()
bobj.m2()

# Example 2: Another way single inheritance

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=200,100
    def m2(self):
        print(self.a-self.b)

bobj=B()
bobj.m1()
bobj.m2()

# Example 3: Multi Level Inheritance
# It's a combination of multiple single inheritances.

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a, b= 200, 100
    def m2(self):
        print(self.a-self.b)

class C(B):
    i, j= 5,2
    def m3(self):
        print(self.i * self.j)

cobj=C()
cobj.m1()
cobj.m2()
cobj.m3()

# Example 4: Hierarchy Inheritance.
# Only one parent class can have multiple child classes

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a, b= 200, 100
    def m2(self):
        print(self.a-self.b)

class C(A):
    i, j= 5,2
    def m3(self):
        print(self.i * self.j)

bobj=B()
bobj.m1()
bobj.m2()

cobj=C()
cobj.m1()
cobj.m3()

# Example 5: Multiple inheritance.
# In this two parent classes are needed for a child class

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B:
    a, b= 200, 100
    def m2(self):
        print(self.a-self.b)

class C(A,B):  # number of classes can be pacified
               # in the bracket separated by comma
    i, j= 5,2
    def m3(self):
        print(self.i * self.j)

cobj=C()
cobj.m1()
cobj.m2()
cobj.m3()


# Example 6: Over riding concept

class A:
    def m1(self):
        print("this is m1 method from class A")
class B(A):
    def m1(self):
        print("this is m1 method from class B")
        super().m1()
        # this will invoke the parent class method through the child class

bobj=B()
bobj.m1()   # Method created in parent class,
            # if same method is created in the child class,
            # is called the overriding concept
            # by default the method will be invoked from child class

# Example 7:

class A:
   a, b = 10, 20

class B(A):
    i, j=100, 200
    def m(self, x, y):
        print(x+y)  # local variables
        print(self.i+self.j)  # class variables
        print(self.a+self.b)  # class variables

bobj= B()
bobj.m(1000, 2000)

# Example 8: overriding variables

class Parent:
    name= "Scott"

class Child(Parent):
    name ="John"
    def test(self):
        print(super().name) # to access the parent class variable
                            # method is needed to be created

cobj = Child()
print(cobj.name)
cobj.test()


# Example 9: Overriding methods

class Bank:
    def rateofInterest(self):
        return 0

class XBank:
    def rateofInterest(self):
        return 10

class YBank:
    def rateofInterest(self):
        return 12

objx=XBank()
print(objx.rateofInterest())

objy=YBank()
print(objy.rateofInterest())

# Example 10: Overloading (polymorphism)

class Human:
    def sayhello(self, name=None):
        if name is not None:
            print("Hello"+" "+ name)
        else:
            print("Hello")

h=Human()
h.sayhello("Scott")
h.sayhello()

# Example 11: Overloading 2nd example

class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add()
calobj.add(10,20)
calobj.add(100,200,300)


