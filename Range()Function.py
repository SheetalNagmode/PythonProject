# Range()
# for a single parameter it will start default from zero
# and end in -1 of the maximum parameter.
# If first parameter/argument is mentioned it will start from the specified number and end -1 of the last number.
# if three parameters are provided it will follow the same for the first two numbers as above
# but third parameter will be either incrementation or decremental
#
print(range(10))                # range(0, 10)
print(list(range(10)))          #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5,10)))        #[5, 6, 7, 8, 9]

print(list(range(1,10,2)))      #[1, 3, 5, 7, 9]
print(list(range(0,10,2)))      #[0, 2, 4, 6, 8]
print(list(range(10,1,-1)))     #[10, 9, 8, 7, 6, 5, 4, 3, 2]

