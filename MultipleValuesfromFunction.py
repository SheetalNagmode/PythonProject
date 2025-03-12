# finding the largest of two numbers:
# returning multiple values from function,
# default return type is tuple

def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a

s=bigger(100,200)
print(s)

print(type(s))

