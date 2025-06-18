# Example 1: Single inheritance

class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m2(self):
        print("This is m2 method from class B")

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