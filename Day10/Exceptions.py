# Example 1:
print("This is starting point of program")
print("This is starting point of program")
print("This is starting point of program")
print("This is starting point of program")
try:
    print(x)
except:
    print("Exception occured")

print("This is end of the program")
print("This is end of the program")
print("This is end of the program")

# Example 2:

print("This is starting of the program...")
print("Program in progress")
try:
    print(10/0)
except:
    print("Exception occurred... Handled..")

print("Program completed...")

# Example 3: Multiple except blocks : try, except, else, finally

try:
    num1, num2 = 10,0
    result=num1/num2
    print("result is:", result)
except ZeroDivisionError:
    print("Thrown ZeroDiviisonError exception..")
except SyntaxError:
    print("Thrown Syntax error exception...")
except:
    print("exception handled...")
else:
    print("No exceptions occurred..")
finally:
    print("Always execute...")


# Example 4: raising our own exception

def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("Even")
    else:
        print("Odd")

print("Checking number is even or odd by callng function..")
num=-1
try:
    enterage(num)
except ValueError:
    print("Value error exception occurred and handled..")
print("Program completed..")
