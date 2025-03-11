# Creating Functions:
# Empty Function do nothing

def myfunc():
   pass


# Function takes arguments/parameters and do something

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

