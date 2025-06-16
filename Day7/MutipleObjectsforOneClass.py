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

# Example 2: Method & constructor

