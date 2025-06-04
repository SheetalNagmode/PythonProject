#Iterative Statements:
# for loop
# single parameter/argument

# Print 1 to 10 numbers using for loop

for i in range(10):
    print(i)            # this will give 0 to 9 numbers

for i in range(1, 11):
    print(i)            # if you want to print 1 to 10 exactly



# multiple parameters/arguments
# incrementation Example:
# Print only even numbers between 1 to 20

for i in range(2,21,2):         # will print even numbers
    print(i)                    #(2,4,6,8, 10, 12, 14, 16, 18, 20)

# Print only odd numbers between 1 to 20

for i in range(1,21,2):         # will print Odd numbers
    print(i)                    # (1,3,5,7,9, 11, 13, 15, 17, 19)

# Decremental Example:
# Print 1 to 10 numbers in descending order

for i in range(10, 0, -1):
    print(i)                    # (10,9,8,7,6,5,4,3,2,1)