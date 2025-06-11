# Example 1: Creating set

myset={"apple","banana","cherry"}
print(myset)  # the order will be changed
# as set is unordered

# Example 2: Accessing items or values from the set

myset={"apple","banana","cherry"}

for i in myset:
    print(i)

# Example 3: Value exists in set or not
#Using in operator and loop

myset={"apple","banana","cherry"}

print("banana" in myset)         # returns in true or false
print("banana2" in myset)

if "apple" in myset:
    print("Yes, apple in the set")
else:
    print("No, apple not in the set")

# Example 4: Adding items to set
# add()- add single item
# update()- add multiple items to set  functions

myset={"apple","banana","cherry"}
myset.add("orange")
print(myset)

myset={"apple","banana","cherry"}
myset.update(["mango","grapes"])
print(myset)

# Example 5: find number of items in a set or
# finding the length of the set
# len()

myset={"apple","banana","cherry"}
print(len(myset))

# Example 6: Remove items from the set
# remove()   discard()

myset={"apple","banana","cherry"}
myset.remove("banana")
print(myset)
# myset.remove("xyz")  # KeyError
# Trying to remove the item which is not available will return KeyError

myset.discard("banana")
print(myset)
myset.discard("xyz")  # this will not throw any error

# both functions will try to remove the item from the set
# but discard() will not throw the error for not available items

# Example 7: Clear all the items from set

myset={"apple","banana","cherry"}
myset.clear()
print(myset)   # this will clear the items but the set will still be present

# to delete the whole set use del() function

del myset
# print(myset)
# this will give error
# NameError: name 'myset' is not defined

# Example 8: Joining two sets :  union()
set1 = {"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

# update()  function to join sets

set1 = {"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)




