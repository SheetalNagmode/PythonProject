# Two types of methods we can define within a class:
# Instance Method: We can access these methods only through object
# Static Method: We can access these methods directly using class name
# annotation @staticmethod: This helps in making a static method
# which will be a common method for all the objects in a class
# when a static method is created 'self' is considered as a parameter
# but when an instance is created the 'self' is not considered as a parameter


class MyClass:
    def m1(self):
        print("Instance Method....")

    @staticmethod
    def m2(self):
        # print("Static Method....")
        print(self)

mc=MyClass()        #Calling Instance Method using object
mc.m1()

#MyClass.m2()        # Calling Static Method directly using class

MyClass.m2(100)     # Calling Static Method passing parameters
