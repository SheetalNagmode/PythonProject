name, age, sal = "John", 26, 10000.5

#Approach 1st:
print(name, age, sal)

#Approach 2nd:
print("Name is:", name)         # comma is used to add the string
print("Age is:", age)
print("Salary is:", sal)

#Approach 3rd:
print("Name is: %s  age is:%d  sal is:%g" %(name, age,sal))
# %s where s is representing string,
# %d where d is for number(digit),
# %f or %g where g is for decimal number

# Approach 4:
print("Name:{}  age:{}  salary:{}" .format(name,age,sal))

# make sure the order of the variable name
# and the value should be in the same order
# otherwise it will print in the wrong format