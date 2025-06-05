# Testing Strings functions:
# Conditional functions always return in boolean (true & false)
# isalnum() = to test whether string is all numbers
# isalpha() = to test whether string is all alphabets
# isdigit() = to test whether string is all digit
# isidentifier() = test whether string is a valid python identifier
# islower() = test whether string is in lowercase
# isupper() = test whether string is in uppercase
# isspace() = test whether string is a whitespace string

s="Welcome to Python"

print(s.isalnum())
print("Welcome".isalpha())
print("2012".isdigit())
print("First Number".isidentifier())
print(s.islower())
print("WELCOME".isupper())
print("".isspace())


