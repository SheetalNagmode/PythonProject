# Example 1:

class MyClass:
    def __init__(self):
        print("This is constructor")
    def m1(self):
        print("Hello..")
    def m2(self,x,y):
        return(x+y)

mc=MyClass()         # invoke constructor automatically
mc.m1()              # Method we have to call explicitly by using object
print(mc.m2(10,20))

# Example 2:

class MyClass:
    name="John"
    def __init__(self,name):
        # constructor expecting one argument
        print(name)
        print(self.name)

mc=MyClass("David")    # Passing parameter to the constructor


# Example 3:
# requirements: Employee class
# constructor: eid, ename, sal
# diplay(): print eid, ename & sal

class Emp:

    def __init__(self, eid, ename, sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid, self.ename,self.sal)

e1=Emp(101, "John", 120000)
e1.display()

e2=Emp(102,"Scott",80000)
e2.display()

# Example 4:
# requirements: Employee class
# constructor: eid, ename, sal
# constructor : print eid, ename & sal

class Emp:

    def __init__(self, eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def __str__(self):      # returns only a string
        return (self.ename)

e1=Emp(101, "John", 120000)
print(e1)