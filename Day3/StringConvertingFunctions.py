# Converting String Functions:
# capitalize()  = Capitalizes the string(1st letter of the first word is capitalized )
# title() = Every word in the sentence will start with capital letter
# lower() = All the characters in the string will be converted to lowercase
# upper() = All the characters in the string will be converted to uppercase
# swapcase() = will convert upper into lower case and vice versa
# replace("","") = replace single or multiple characters in a string with suggested new characters
# Examples of the functions:

s="String in PYTHON"

s1= s.capitalize()
print(s1)

s2 = s.title()
print(s2)

s3 = s.lower()
print(s3)

s4 = s.upper()
print(s4)

s5 = s.swapcase()
print(s5)

s6 = s.replace("in","on")
print(s6)

print(s)

# Reverse a string
# Method1:
s="welcome"
rev_str=""
for i in s:
    rev_str=i+rev_str
print("reversed string is:", rev_str)

# Method 2:

s="welcome"
rev_str=s[::-1]     # s[0:7:-1]
print(rev_str)

