# Two types of methods we can define within a class:
# Instance Method: We can access these methods only through object
# Static Method: We can access these methods directly using class name
# annotation @staticmethod: This helps in making a static method
# which will be a common method for all the objects in a class
# when a static method is created 'self' is considered as a parameter
# but when an instance is created the 'self' is not considered as a parameter


# Example1:

class MyClass:
    def myfun(self):
        pass
    def display(self,name):
        print("John")

mc1=MyClass()
mc1.myfun()
mc1.display("Scott")


# Example 2:

class MyClass:
    def m1(self):
        print("This is Instance Method....")

    @staticmethod
    def m2(self,num):
        # print("This is Static Method....")
        print(self,num)

mc=MyClass()     #Calling Instance Method using object
mc.m1()
mc.m2(100,200)

MyClass.m2(10,20)  # Calling Static Method directly using class

MyClass.m2(100,200)  # Calling Static Method passing parameters

# Example 3:  Class variables:

class MyClass:
    a,b=10,20   # class variable
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=MyClass()
mc.add()
mc.mul()

# Example4:
i,j= 15,25   # global variables
class MyClass:
    a,b=10,20  # Class variables
    def add(self,x,y):
        print(x+y)  #    local variable
        print(self.a+self.b)   # a, b are class variables
        print(i + j)      # i, j are global variables

mc=MyClass()
mc.add(100,200)


# Example 5:  when the global, class and local variables are the same,
# we need to use globals()[] to access the global variables

a,b= 15,25   # global variables
class MyClass:
    a,b=10,20  # Class variables
    def add(self,a,b):
        print(a+b)  #   local variables
        print(self.a+self.b)   # a, b are class variables
        print(globals()['a'] + globals()['b'])      # a, b are global variables

mc=MyClass()
mc.add(100,200)