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

#Continue Example:
for i in range(1,10):
    if i==5:
        continue
    print(i)

print("Program Exited")