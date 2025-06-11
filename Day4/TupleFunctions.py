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


# Example 4: Changing tuple items:
# by default tuple does not allow you change values because it is immutable
# but there is work around
# tuple--> list(modify)--> tuple

mytuple=("apple","banana","cherry")
mylist=list(mytuple)
mylist[0]="orange"

mytuple=tuple(mylist)
print(mytuple)

# Example 5: Reading tuple items using loop

mytuple=("orange","banana","cherry")
for i in mytuple:
    print(i)

# Example 6: Check if item Exits (Searching of item in tuple)

if "banana" in mytuple:
    print("Yes, banana is present")
else:
    print("No, banana is not present")

#Example 7: Tuple Functions:
# Functions like max, min, len, sum are also used with tuples

t1=(1,11,66,12,91)

print(min(t1))
print(max(t1))
print(sum(t1))
print(len(t1))

# Example 8: Add items to tuple-
# not possible becoz tuple is immutable -
# cannot change values/items

#mytuple=("apple","banana","cherry")
#mytuple[0]="orange"  #TypeError: 'tuple' object does not support item assignment
#print(mytuple)

# Example 9:  copy tuple
mytuple1=("apple","banana","cherry")
mytuple2= mytuple1
print(mytuple2)

# Example 10: Removing items from tuple -
# not possible becoz tuple is immutable
mytuple1=("apple","banana","cherry")
# mytuple.remove("apple")   # invalid / it is not possible

del mytuple
print(mytuple)      #NameError: name "mytuple" is not defined

