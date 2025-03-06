# String Searching Functions
# Always returns in boolean(true and false)
# endswith(char)= shows the ending of the string
# startswith(char) = gives the start of the string
# find(char) = This will return which position the character started in the string
# find(char) = If the given string is not found in the main string then it returns minus
# count(char) = It will return how many times the character is repeated in the main string


s="Welcome to Python"

print(s.endswith('thon'))
print(s.startswith("good"))
print(s.find("come"))
print(s.find("become"))      # not in the main string so returns minus
print(s.count("o"))

