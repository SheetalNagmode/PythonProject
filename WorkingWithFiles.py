# File handling can be used to read & write data to & from the file
# File Operations: Opening a file, closing a file, writing data in a file,
# reading data from a file, Appending data,
# Looping through the data using for loop

# Opening, Closing & writing the data into the Files:
# Choose a file saved on the computer & copy and paste the path here
# \n is used to get the data on separate lines

'''f = open('../../OneDrive/Desktop/Demofile.txt', 'w')
f.write("This is my first line...\n")
f.write("This is my second line...\n")
f.write("This is my third line...")

f.close()'''

# File Reading operations:
# read (read all the content from the file line by line) and
# readlines (read entire content in the form of list)
# readline (read the first line from a file)

#f = open('../../OneDrive/Desktop/Demofile.txt', 'r')
#print(f.read())

#print(f.readlines())

#print(f.readline())

#f.close()

# Append the data:
# Adding new data to the existing content in a file

'''f = open('../../OneDrive/Desktop/Demofile.txt', 'a')

f.write("This is fourth line....\n")
f.write("This is fifth line....")
f.close()'''

# Read data using for loop:

f = open('../../OneDrive/Desktop/Demofile.txt', 'r')

for l in f:
    print(l)

f.close()