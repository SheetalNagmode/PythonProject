name, age, sal = "John", 26, 10000.5

#Approach 1st:
print(name, age, sal)

#Approach 2nd:
print("Name is:", name)
print("Age is:", age)
print("Salary is:", sal)

#Approach 3rd:
print("Name: %s  age:%d  sal:%g" %(name, age,sal))
# %s is representing string, %d for number, %f or %g for decimal number

# Approach 4:
print("Name:{}  age:{}  salary:{}" .format(name,age,sal))

# make sure the order of the variable name and the value should be the same order otherwise it will be in the wrong format