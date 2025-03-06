# String Functions
# len() = How many characters in the string
# max(0 = Which one is the maximum character in the string
# min() = which one is the minimum character in the string

print(len("Hello"))
print(max("ABC"))
print(min("ABC"))

# String Comparison
# Using relational operators to compare strings
# Relational operators are always in Boolean(True & False)
# Every character has a number (Asking number)
# ord()  & chr(num)

print("tim"=="tie")
print("free"!= "freedom")
print("arrow">"aron")
print("right">="left")
print("teeth"<"tee")
print("yellow"<="fellow")
print("abc">"")

print(ord('A'))             # Asking characters
print(chr(65))

# Strings with the loop

s="Hello"

for i in s:
    #print(i)       # every character will be printed on new line
    #print(s)       # whole string will be printed on new line times the length
    #print(s,end="\n")  #same as print(s)
    print(s,end="")    #everything will be printed on the same line
    print(s,end="John") #it will append "John" with the main string

