# Approach 1: Importing modules from 2 different packages

import sys
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/Package1")
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/Package1/Package2")

import module1
import module2

module1.display()
module2.show()

# Approach 2:

import sys
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/Package1")
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/Package1/Package2")

from module1 import *
from module2 import *

display()
show()
