# empty Tuple:
# Example: creating Tuple

mytuple=("apple","banana","cherry")
print(mytuple)

# Example 2: Access tuple items:
# index starts with zero

mytuple=("apple","banana","cherry")
print(mytuple[1])
print(mytuple[-1])

# Example3: Range of indexes:

mytuple=("apple","banana","cherry", "orange","kiwi","melon","mango")
mytuple[2:5]
mytuple[-4:-1]

# Tuple Functions:
# Functions like max, min, len, sum are also used with tuples

t1=(1,11,66,12,91)

print(min(t1))
print(max(t1))
print(sum(t1))
print(len(t1))

# Extracting values from the tuple using for loop:
# index cannot be used because tuple is immutable

for i in t1:
    print(i)

# Example 4: Changing tuple items:
# by default tuple does not allow you change values because it is immutable
# but there is work around
# tuple--> list(modify)--> tuple

mytuple=("apple","banana","cherry")
mylist=list(mytuple)
mylist[0]="orange"

mytuple=tuple(mylist)
print(mytuple)
