# Types of Arguments:
# Positional and Keyword arguments:
# Argument with default values (positional)
# if there are two parameters and only one value is provided,
# by adding j=0, it will print zero as default value for j
# if only one value is mentioned it will go to the first variable
# and not to the 2nd one

#Example 1:

def func(i,j):
    print(i,j)

func(10,20)       # Positional arguments
func(j=20, i=10)       # Keyword arguments

#Example2: Default values assigned to Positional arguments

def func(i=0,j=0):      # Default values assigned
    print(i,j)

func(10)            # 20,0 # 0 is the default value of j
func(10,20)

#Example 3:  Keyword Argument (Named Argument):

def named_args(name, greeting):
    print(greeting+ " " + name)

named_args('Sheetal', 'Hi')
# in this normal way we need to keep in mind
# the order of the parameters

# keyword arguments:
# there is no need to keep in mind
# the order of parameter in keyword arguments:

named_args(name='Sheetal',greeting='Hi')
named_args(greeting='Hi',name='Sheetal')

# both ways are going to give same answer


# Mixing Positional and Keyword Arguments:
# Positional parameter must appear before keyword parameter
# Positional parameter always comes first
# followed by keyword parameter

def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30)

my_func(10,b=20,c=30)

my_func(10,c=30,b=20)

# my_func(b=20,c=30,10)   # this is invalid.
# Positional argument must appear before any keyword argument

