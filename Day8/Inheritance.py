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

class C(B):
    i, j= 5,2
    def m3(self):
        print(self.i * self.j)

