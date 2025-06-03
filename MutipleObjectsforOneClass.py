# Creating multiple objects for single Class:

class MyClass:
    def display(self):
        print("This is display method....")

obj1=MyClass()
obj1.display()

obj2=MyClass()
obj2.display()

print(id(obj1))
print(id(obj2))

