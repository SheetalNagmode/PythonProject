# Dictionary Methods:
# Example 1: remove item from dictionary
# popitem() : returns specific selected item from dictionary
# and also remove selected item.

mydic={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
mydic.pop("year")
print(mydic)


#2nd:

friends = {'tom':'111-222-333',
           'bob': '333-444-555',
           'jerry': '666-33-111'}

print(friends.popitem())
# popitem() : returns randomly selected item from dictionary
print(friends)

print(friends.pop("bob"))
print(friends)

# Example 2: Using del() function
# this will delete the items and the dictionary completely

# del mydic["year"]
# print(mydic)     # NameError: name 'mydic' is not defined


# Example 3: clear() : Delete all items from the dictionary
# this will only delete the items in the dic
# but the dictionary variable will still be there

print(friends)
friends.clear()
print(friends)

# Example4: Copying dictionary
# Approach 1: without using copy() function

mydic1={
    "brand": "Hyundai",
    "model": "i10",
    "year": 2021
}
mydic2=mydic1
print(mydic2)

# Approach 2: Using copy() function

mydic2=mydic1.copy()
print(mydic2)


# Example5:
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
