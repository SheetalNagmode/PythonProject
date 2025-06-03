# Named Object & Nameless Object:

class MyClass:
    def display(self):
        print("This is display method....")

obj1=MyClass()          # obj1 is Named object
obj1.display()

MyClass().display()     # Nameless object

# No variable is required for a nameless object


# Assigning an object to another variable

class MyClass:
    def m1(self):
        pass
c1=MyClass()
c2=c1

print(id(c1))
print(id(c2))

c3=MyClass()
print(id(c3))