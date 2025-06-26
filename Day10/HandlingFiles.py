# Example 1: Writing data in to text file

file=open("C:/Demofiles/myfiles.txt", 'w')
file.write("This is my first statement...\n")
file.write("This is my second statement...\n")
file.write("This is my third statement...\n")
file.write("This is my fourth statement...\n")
file.write("This is my fifth statement...\n")
file.close()
print("Program Completed...")