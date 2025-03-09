# Creating Dictionary:
# Always use {} to pass the value

friends = {'tom':'111-222-333',
           'Kim': '333-444-555',
           'jerry': '666-33-111'}
print(friends)

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