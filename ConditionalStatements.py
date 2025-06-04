#Conditional statements: if,  if...else and elif
#Syntax :
#if condition:
#   statements
#else:
#   statements
# indentation before the statements is very important and must
# No semicolon or comma needed at the end of statement.
# Colon at the end of if and else is needed.
# Multiple statements can be added for both.
# Either condition can be added after if or else or boolean values can be used(True, False)
# Comma is used inside the statement if needed to append any value.
# In python True= 1 and False= 0.
# Instead of true or false 1 or 0 can be used respectively

# Example 1:

a=50
if a>30:
    print("This is a true condition")
else:
    print("This is a false condition")

# Example 2:

if False:
    print('This is a true condition')
else:
    print('This is a false condition')

#Example 3:
if 0:
    print('This is a true condition')
else:
    print('This is a false condition')

# Example 4: Print a person is eligible for vote or not
# age>=18

age=15
if age>=18:
    print("Eligible for vote")
    # indentation is very impt in python
else:
    print("Not eligible for vote")
    # multiple statements can be added here or above

# Example 5: Find a number is even/odd
# num%2=0

num=10
if num%2==0:
    print("Given number is Even")
else:
    print("Given number is Odd")

# Example 6: If else - one statement in single line (ternary operator)

num1=10
print("Even number") if num1%2==0 else print("Odd number")

# Example 7: if else - Multiple statements in single line

x=20
{print("hello"), print("python")} if x>=10 else {print("hi"), print("java")}