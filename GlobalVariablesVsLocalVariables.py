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