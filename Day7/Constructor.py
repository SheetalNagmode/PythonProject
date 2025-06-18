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

