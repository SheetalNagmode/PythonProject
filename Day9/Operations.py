# first way to access the functions from another module

import Calculator

Calculator.add(100,200)
Calculator.mul(20,30)

# Approach 2

from Calculator import add, mul

add(100,200)
mul(10, 20)

# Approach 3:

from Calculator import *

# * imports all the functions from the module

add(100,200)
mul(10, 20)
