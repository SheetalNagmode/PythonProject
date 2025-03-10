# Tuple Functions:
# Functions like max, min, len, sum are also used with tuples

t1=(1,11,66,12,91)

print(min(t1))
print(max(t1))
print(sum(t1))
print(len(t1))

# Extracting values from the tuple using for loop:
# index cannot be used because tuple is immutable

for i in t1:
    print(i)

