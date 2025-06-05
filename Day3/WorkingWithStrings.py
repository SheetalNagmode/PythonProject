# Working with the Strings in Python
# Any alphabet in double or single quotation will be considered as a string
# char is also a string in python
# Syntax 1 to create the strings

name="John"
mychar='A'
print(name)
print(mychar)

print(type(name))
print(type(mychar))

# Syntax 2 to create the string

name1=str()         # empty string, no value
name2=str("welcome to Python")

print(name1)
print(name2)

# In Python Strings are immutable,
# new id is created everytime the value is changed

str1="Welcome"
str2="Welcome"

print(id(str1),id(str2))     #finding the id for the stored string

str2="Welcome123"

print(id(str1),id(str2))

# Using + and * with string
# concatenation and repetition can be achieved respectively
# Using + operator with the String Example

str3='Welcome'
print(str3+ "" + "to Python programming")

# Using * operator with the String example
# + and * with numbers give addition and multiplication respectively

print(str3 * 3)

