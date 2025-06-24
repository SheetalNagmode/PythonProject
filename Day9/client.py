import sys
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/pack1")
# import sys first and than
# use sys.path.append(copy the path by right clicking on the package)
# make all the backward slash forward in the path address
# Approach 1:

import module1
import module2

module1.display()
module2.show()

# Approach 2:

from module1 import *
from module2 import *

display()
show()

