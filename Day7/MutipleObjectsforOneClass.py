# Creating multiple objects for single Class:
# Example 1:
class MyClass:
    def display(self, name):
        print("This is display method....")
        print(name)

obj1=MyClass()
obj1.display("John")

obj2=MyClass()
obj2.display("Scott")

print(id(obj1))
print(id(obj2))

# Method & constructor difference:
# Method:
# Give any name
# Return the values
# Method can take arguments/parameters
# We have to use an object to invoke the method
# Constructor:
# Constructor name is fixed: def  __init__(self)
# Constructor will not return any value
# Constructor can also take arguments/ parameters
# Constructor will be called at the time of object creation itself.

# Example 2: Constructor example

class MyClass:
    def __init__(self):
        print("This is constructor..")
    def m1(self):
        print("hello..")
    def m2(self, x,y):
        return(x+y)

mc=MyClass()  # this statement invoke constructor automatically
mc.m1()   # method we have call explicitly by using object
res=mc.m2(10,20)
print(res)    # using a variable to store the returned value and print it
# or
print(mc.m2(10,20))  # directly print the value


