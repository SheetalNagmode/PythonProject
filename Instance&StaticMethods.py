# Instance Method: We can access these methods only through object
# Static Method: We can access these methods directly using class


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
