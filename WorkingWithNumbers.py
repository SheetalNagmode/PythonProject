# There are only two number types in python.
# Integer (without decimal) and Float (with Decimal)
# Number Types & Conversions:
# "type()" is a function which will return what type of variable it is
# max() and min() functions

x=10
print(type(x))
print(type(int(x)))
print(type(float(x)))

x=10
y="Welcome"
z=True
w=10.5

print(type(x))
print(type(y))
print(type(z))
print(type(w))

# for type conversion both should be same data type

print(type(float(x)))       # Valid int - float
print(type(int(w)))         # valid float - int
print(type(int(z)))         # valid boolean - int
print(type(float(z)))       # valid boolean - float

#print(type(int(y)))         # invalid string to int
#print(type(float(y)))       # invalid string to float

# max() method

print(max(10,50,20))

# min() method

print(min(10,50,20))

