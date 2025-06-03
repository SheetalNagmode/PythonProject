#  Arithmetic Operators
from operator import truediv

a=5
b=2

print(a+b)      #addition
print(a-b)      #subtraction
print(a*b)      #multiplication

print(a/b)      #division operator- return decimal number
print(a//b)     #return Quotient value - division operator

print(a%b)      #return reminder  - modular division operator
print(a**b)     # exponent operator - 5 square = 25

# Relational Operators/ Comparison Operators
# > < >= <= != ==
# Relational Operators always return boolean values - true or false

x=5
y=10

print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)

# Logical Operators
# and or not
# Always returns a boolean value
# works between two different boolean variables

m=True
n=False

print(m and n)
print(m or n)
print( not m )