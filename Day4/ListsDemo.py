# Creating Lists: List can be created using
# square brackets [] or the list() constructor

list1 = list()              # Empty list
list2 = list([10,20,30])    #list of integers 1st method
list3 = [10,20,30]          #list of integers 2nd method
list4 = ["Apple","Banana", "Orange"]    # List of strings
list7 = ["Apple", 10, "Banana", 20]     # Mixed Data type


print(list1)
print(list2)
print(list3)
print(list4)
print(list7)

# Accessing elements/items from list
# There is an index number associated with every element in list
# index number starts with 0

mylist=["Apple", "Banana", "Cherry"]
#           0           1        2    # index starts with zero
#          -3          -2       -1    # negative index starts with -1 from end

print(mylist[0])
print(mylist[2])
print(mylist[-1])
print(mylist[-2])
# negative index is also allowed.
# -1 means it will start the count from the end
# In this case -1 will be "Cherry"

l= [1,2,3,4,5,6]

print(l[1])
print(l[5])

# Range of indexes

mylist=["Apple","Banana","Cherry","Orange","Kiwi","Melon","Mango"]
print(mylist[2:5])
print(mylist[-4:-1])   # will be count from end (-4 = orange) and -1 = mango.
# but the last will not be displayed. Ans=orange, kiwi, melon

# Common operations in list
# returns in boolean (true/false)

list1=[2,3,4,1,32]

print(2 in list1)
print(100 in list1)

# len(list) = returns number of elements/values in the list
# max(list) = maximum value present in the list
# min(list) = minimum value present in the list
# sum(list) = sum of all the elements in the list

print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))

# Slicing in list

list2= [11,22,44,55,77,66]

print(list2[0:5])

print(list2[2:])
print(list2[2:6])      # both are same

print(list2[:5])
print(list2[0:5])      # both are same

# + and * operators with list

list1=[10,20]
list2=[5,15]

list3=list1+list2
print(list3)

list4 = [1,2,3,4]

list5 = list4*3

print(list5)          # instead of new list use print(list4*3)

# 'in'& 'not in' operators:
# these operators help to verify
# whether certain elements are in the list or not

list6 = [10,20,30,40,50,60,100]

print(40 in list6)
print(150 in list6)

print(15 not in list6)
print(100 not in list6)

# Traversing List using for loop:
# extracting each and every element from the list and
# printing them in the console output

for i in list6:
    print(i)

# Check if the item exist in the list or not
# using if..else statement

mylist=["apple","banana","orange"]

if "apple" in mylist:
    print("Yes. Apple is present")
else:
    print("No. Apple is not present")

# Add items:  append()  insert()
#when you use append() the item is always added at the end of the list

mylist1= ["apple", "banana", "cherry"]
mylist1.append("orange")
print(mylist1)

# to insert an item in the middle of the list use insert() function
# mention the index where the new item will be added and the item name

mylist1.insert(1, "kiwi")
print(mylist1)

# remove item from the list
#pop()   del   clear()

mylist1= ["apple", "banana", "cherry"]
mylist1.pop(0)
print(mylist1)

# del : using del keyword

mylist1= ["apple", "banana", "cherry"]
del mylist1[2]      #here del command removes single item based on the index
print(mylist1)

# clear()  : removes all the items from the list

mylist1= ["apple", "banana", "cherry"]
mylist1.clear()
print(mylist1)

# Copy list:  2 methods

mylist1= ["apple", "banana", "cherry"]
mylist2=list(mylist1)
print(mylist1)
print(mylist2)

# copy() function

mylist1= ["apple", "banana", "cherry"]
mylist2=mylist1.copy()
print(mylist2)

# Combine/ join lists
# using + operator
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)

# using for loop

for i in list2:
    list1.append(i)
print(list1)

# Using extend() function

list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)

# List comparison:

list1=[1,2,3]
list2=[1,2,3]

if list1==list2:
    print("List are equal")
else:
    print("List are not equal")

