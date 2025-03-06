# Creating Lists

list1 = list()              # Empty list
list2 = list([10,20,30])    #list contains some values
list3 = [10,20,30]          # list contains the values

list4 = ["John","Mary","Scott"]

print(list1)
print(list2)
print(list3)
print(list4)

# Accessing elements from list
# There is an index number associated with every element in list

l= [1,2,3,4,5,6]

print(l[1])      # index number starts with 0
print(l[5])

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

