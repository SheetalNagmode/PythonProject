# Concatenation

# when + operator is used between
# numbers addition will be performed

print(10+10)            #Valid, perform addition of 2 numbers
print(10.5+10.5)        #Valid performs addition
print(10.5+10)          #Valid performs addition

# when operator + is used between number and
# string or str and str it performs the concatenation

print("Welcome" + "Python")   #Valid join strings
print(True+5)           #Valid True=1 and False=0
print(False+5)          #Valid
print(True+True)        #Valid

# Concatenation doesn't work for different data types

'''print(10+"Welcome")     #Invalid TypeError
print(10.5+"Welcome")   #Invalid
print(True+"Welcome")   #Invalid TypeError'''