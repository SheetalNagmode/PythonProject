# Global Variables Vs Local Variables:
# Variable created outside of a function
# are called Global Variables, Which can be accessed
# within the function and outside of the function.
# whereas variable created
# within a function is called Local Variables
# These variables we can access only with the function

global_var=10

def func():
    local_var=100
    print(local_var)
    print(global_var)

func()

print(global_var)
#print(local_var)  # not valid bcoz this is local variable inside the function

# Global variable behaviour within and outside the function:
# If changes are made to the global variable within the function,
# it will only reflect within the function.
# It will not affect the original value of the global variable outside the function.


xy=100

def cool():
    xy=200
    print(xy)

cool()
print(xy)


# Changing Global variable to local variable:
# in this case the global variable changed within the function
# will also reflect outside the function


t=1

def increment():
    #global t=100 # invalid
    global t
    t=100
    print(t)

increment()

print(t)


# There is no need to declare global variable outside the function
# you can declare them global inside the function

def foo():
    global x
    x=100
    print(x)


foo()

print(x)    #trying to print global variable outside of function

