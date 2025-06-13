# Local Variables, Class Variables & Global Variables:
# Local Variables: Within the method
# Class Variables: within the class
#Global Variables: Outside of the class

i, j= 15,25         # Global Variables

class MyClass:          # Class Variables
    a,b=10,20

    def add(self, x,y):         # Local Variables
        print(x+y)
        print(self.a+ self.b)   # Class Variables
        print(i+j)              # Global Variable

cal=MyClass()
cal.add(100,200)


# if all the variable(local, Class & Global) have same name:

a, b= 15,25                     # Global Variables

class MyClass:
    a,b=10,20                   # Class Variables

    def add(self, a,b):         # Local Variables
        print(a+b)              #accessing local variable
        print(self.a+ self.b)   # accessing Class Variables
        print(globals()['a']+globals()['b'])

# Accessing Global Variable:
# Use the syntax globals()['']

cal=MyClass()
cal.add(100,200)