# Example 1: Writing data in to text file

file=open("C:/Demofiles/myfiles.txt", 'w')
file.write("This is my first statement...\n")
file.write("This is my second statement...\n")
file.write("This is my third statement...\n")
file.write("This is my fourth statement...\n")
file.write("This is my fifth statement...\n")
file.close()
print("Program Completed...")

# Example 2:  Reading data from text file

file=open("C:/Demofiles/myfiles.txt", 'r')
# print(file.read())      # reads whole data
print(file.readline())    # read only the first line
file.close()

# example 3: Appending data into the text file

file=open("C:/Demofiles/myfiles.txt", 'a')
file.write("This is my sixth line...\n")
file.write("This is my seventh line...\n")
file.close()
print("Program is Completed...")

