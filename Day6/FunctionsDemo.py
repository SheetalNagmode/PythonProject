# Creating Functions:
# Empty Function do nothing

def myfunc():
   pass

def myfun():
    print("hello")

# this will not print anything.
# Becoz this is only creating a function.
# To call a function it needs to be mentioned:

myfun()    # Calling the function

# Example 2: Function takes arguments/parameters and do something

def myfun(name):
    print("Hello",name)
myfun("Smith")


# Example3:

def cal(a,b):
    return(a+b)

sum= cal(100,200)
print(sum)
#  or
print(cal(100,200))

def sum1(start, end):
    result = 0
    for i in range(start, end+1):
        result=result+i
        print(result)

# Function takes arguments and return the output:

def sum2(start, end):
    result = 0
    for i in range(start, end+1):
        result=result+i
        return result
myfunc()
sum1(5,10)

res=sum2(10,20)
print(res)

# You can also use the return statement without a return value.

def sum3(start, end):
    if start>end:
        print("Starting value should be less than ending value")
        return
    result=0
    for i in range(start,end+1):
        result=result+i
        return result

s=sum3(1,5)
print(s)

