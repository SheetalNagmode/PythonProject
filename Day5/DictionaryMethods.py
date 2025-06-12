# Dictionary Methods:
# Example 1: remove item from dictionary


friends = {'tom':'111-222-333',
           'bob': '333-444-555',
           'jerry': '666-33-111'}

# popitem() : returns randomly selected item from dictionary
# and also remove selected item.
print(friends.popitem())

print(friends)

# pop() : returns specific selected item from dictionary
# and also remove selected item

print(friends.pop("bob"))
print(friends)

# clear() : Delete all items from the dictionary

print(friends)
friends.clear()
print(friends)


# keys() :Extract only keys. Return keys in dictionary as tuples
# value(): extract only values

friends = {'tom':'111-222-333',
           'bob': '333-444-555',
           'jerry': '666-33-111'}

print(friends.keys())
print(friends.values())
print(friends)

# get() : Extract the value of specific key

print(friends.get('jerry'))
