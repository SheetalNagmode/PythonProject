# Slicing In python:
# It means extracting some portion (characters) from a string
# str[starting index:ending index]
#  0 1 2 3 4 5 6   = starting index, always starts with '0'
#  W e l c o m e
#  1 2 3 4 5 6 7   = ending index, always starts with '1'

str="Welcome"
print(str[1:3])
print(str[2:4])
print(str[2:6])
print(str[1:4])

# When the starting and ending index are not specified
# it will consider by default 0 and 1 respectively

print(str[:6])
print(str[0:6])             # both are same

print(str[2:])
print(str[2:7])             # both are same

# If the ending index is a negative number.
# Those many characters will be terminated from the end
# And the remaining characters will return

print(str[1:-1])
print(str[1:-2])
print(str[2:-3])

# ord() and chr()

print(ord('A'))     # returns the ASCII code of the character.
print(chr(65))      # returns character represented by a ASCII number.