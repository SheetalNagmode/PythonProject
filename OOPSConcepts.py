# Creating Basic class and object which include methods:

class MyClass:
    def myfunc(self):
        pass

    def display(self,name):
        print("Name is:",name)

mc=MyClass()            #Object creation
mc.myfunc()
mc.display("John")