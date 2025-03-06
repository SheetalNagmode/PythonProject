# Commonly used list methods
# for adding a number to the existing list:
#Adds an element x to the end of the list and returns none
# Method name:  append(x:object)

list = [2,3,4,1,30,4]
print(list)

list.append(20)            # Add new value into the list

print(list)

# Returns the number of times element x appears in the list
# Method name:  count(x:object)

print(list.count(4))       # prints how many times 4 is repeated in the list

# Appends all the elements in 1 to the list and returns None
# Method name: extend(1:list)

list1=[10,20,30]
list2=[40,50,60]

print(list1.extend(list2))

print(list1)    # same as print(list1+list2)

# Extracting a particular element/value at a specific index from the list
# method name:   index(x:object)

