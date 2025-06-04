# Range()  :  values between the range
# for a single parameter it will start default from zero
# and end in -1 of the maximum parameter.
# If first parameter/argument is mentioned
# it will start from the specified number and end -1 of the last number.
# if three parameters are provided
# it will follow the same for the first two numbers as above
# but third parameter will be either incrementation or decremental
#
print(range(10))                # range(0, 10)
print(list(range(10)))          #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5,10)))        #[5, 6, 7, 8, 9]

# print only odd numbers between 1 - 10
print(list(range(1,10,2)))      #[1, 3, 5, 7, 9]

# print only even numbers between 0 - 10
print(list(range(0,10,2)))      #[0, 2, 4, 6, 8]
print(list(range(2,10,2)))      #[0, 2, 4, 6, 8]

# print numbers 1 to 10 in descending order
print(list(range(10,1,-1)))     #[10, 9, 8, 7, 6, 5, 4, 3, 2]

print(list(range(-10, -5)))     #[-10, -9, -8, -7, -6]
print(list(range(-10, -5, 2)))  #[-10, -8, -6]


for x in range(10):
    print(x)

# Range function in list :

list1=[x for x in range(10)]
print(list1)

# To get 1 to 10 use following expression.

list2 = [x+1 for x in range(10)]

print(list2)

# To get the even number use following expression.

list3 = [x for x in range(10) if x%2 ==0]
print(list3)

# By changing the location of X % 2,
# One can return: True or False

list4 = [x % 2 ==0 for x in range(10)]
print(list4)

# To get Odd number use the following expression.

list5 = [x for x in range(10) if x%2==1]
print(list5)

# or

list6 = [x for x in range(10) if x%2!=0]
print(list6)
