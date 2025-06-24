# Approach 1:

import Animal
import Bird

Animal.fly()
Animal.color()

Bird.fly()
Bird.color()

# Approach 2:

from Animal import *
from Bird import *

fly()
color()

# there is a issue in this approach, only the latest imported module will be called
# by default the functions will call the Bird module and not the Animal module
# to solve this issue we will need to import the Animal module call the functions
# than impost the Bird module and call the functions

from Animal import *

fly()
color()

from Bird import *

fly()
color()


