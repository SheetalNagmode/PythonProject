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




# Retrieving, modifying and adding elements in the dictionary
# Retrieving specific value:

print(friends['jerry'])

# Add new data set in existing dictionary
friends['bob']='888-999-222'
print(friends)

# Modify existing value of tom

friends['tom']='999-888-777'
print(friends)

# Always put the key in [] and values in ''
# while operating on the data (modifying & adding)
# In the definition key and values should in {}

# Looping items in dictionary
# To extract only the values of the keys:

friends = {'a':'100',
           'b':'200',
           'c':'300',
           'd':'400'}

for x in friends:
    print(friends[x])

# to print key plus value of it use the follwing expression:

for x in friends:
    print(x, friends[x])

# Finding the length of dictionary

print(len(friends))

# Equality of dictionaries:
# Verifying if both dictionaries are same or not

d1 = {'mike': 41, "bob": 3}
d2 = {"bob":3, "mike":41}

print(d1==d2)       # True

d1 = {'mike': 41, "bob": 3}
d2 = {"bob":3, "mike":42}
print(d1==d2)       # False

print(d1!=d2)       # True


