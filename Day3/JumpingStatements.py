#Flow Control Statements:
# Jumping Statements (Transfer Statement)
# Break , continue are the keywords used to exit(break), skip(continue) from the program
# Most of the time they are used with the looping statements

#break Example:

for i in range(1,10):
    if i==5:
        break
    print(i)
print("Program Exited")

# Print 5 to 100 with 5 increment:
for i in range(5, 101, 5):
     print(i)

#Continue Example:
for i in range(1,10):
    if i==5:
        continue
    print(i)
print("Program Exited")

# skip with multiple values using 'or' keyword:

for i in range(1,10):
    if i==3 or i==5 or i==7:
        continue
    print(i)
print("Program Exited")