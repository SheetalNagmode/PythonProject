#Conditional Statements:
# Even or Odd Numbers
# Example 3:

a=11
if a%2==0:
    print("Even Number")
else:
    print("Odd Number")

# Multiple statements in one block

if True:
    print("statement1")
    print("statement1")
    print("statement1")
else:
    print("statement2")
    print("statement2")
    print("statement2")

# Single line
#syntax:
#  statement/s if condition else statement/s
#Example:

print("statement1") if True else print("statement2")

a=20
print("Even Number") if a%2==0 else print("Odd Number")

# Multiple statements with condition in single line

{print("statement1"),print("statement2")} if True else {print("statement3"), print("statement4")}


