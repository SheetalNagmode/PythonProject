#Example 1:  Creating Dictionary:
# Always use {} to pass the value
# always in key with values
# keys stay unique values can be same

friends = {'tom':'111-222-333',
           'Kim': '333-444-555',
           'jerry': '666-33-111'}
print(friends)

mydic={101:'x', 102:'y',103:'z'}
print(mydic)

# Example 2: Accessing items frm dictionary

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}

print(mydic["brand"])
print(mydic["model"])

# using get()  function:

x=mydic.get("brand")     # or
print(mydic.get("brand"))

# Retrieving, modifying and adding elements in the dictionary
# Retrieving specific value:

print(friends['jerry'])

# Add new data set in existing dictionary
friends['bob']='888-999-222'
print(friends)

# Example 3; Change/ Modify existing values in dictionary

friends['tom']='999-888-777'
print(friends)

mydic={"brand": "Hyundai",
    "model": "i10",
    "year": 2021}
mydic["year"]=2022
print(mydic)

# Always put the key in [] and values in ''
# while operating on the data (modifying & adding)
# In the definition key and values should in {}

# Example 4: reading items from dictionary using loop
# Looping items in dictionary
# To extract only the values of the keys:

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}

for i in mydic:
    print(i)     # prints only keys from dictionary

for i in mydic:
    print(mydic[i])   # print only values from dictionary

for x,y in mydic.items():
    print(x,y)       # print keys along with values

#2nd:
friends = {'a':'100',
           'b':'200',
           'c':'300',
           'd':'400'}

for x in friends:
    print(friends[x])

# to print key plus value of it use the following expression:

for x in friends:
    print(x, friends[x])

# Example: 5: Check key exist in dictionary or not

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
if "model" in mydic:
    print("exist")
else:
    print("not exist")

# Another way to find the item present in the dictionary in one line

print("model" in mydic)


# Example 6: Finding the length of dictionary
# Find the number of items in dictionary

print(len(mydic))

print(len(friends))

# Example 7: Adding items to dictionary

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
mydic["color"]="red"
print(mydic)

# Equality of dictionaries:
# Verifying if both dictionaries are same or not

d1 = {'mike': 41, "bob": 3}
d2 = {"bob":3, "mike":41}

print(d1==d2)       # True

d1 = {'mike': 41, "bob": 3}
d2 = {"bob":3, "mike":42}
print(d1==d2)       # False

print(d1!=d2)       # True


