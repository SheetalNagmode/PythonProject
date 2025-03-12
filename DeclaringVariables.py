# Declaring Variables inside the class:

class MyClass:
    a,b=10,20

    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a * self.b)

cal=MyClass()

cal.add()
cal.mul()

