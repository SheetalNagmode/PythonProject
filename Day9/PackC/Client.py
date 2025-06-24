import sys
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/PackA")
sys.path.append("C:/Users/sheet/PycharmProjects/PythonProject/Day9/PackB")

import emp
empobj=emp.Employee(101, "John", 120000)
empobj.displayemp()

import stu
stuobj=stu.Student(111, "Scott", "A")
stuobj.displaystu()


# Approach 2:

from emp import Employee
empobj=Employee(101, "John", 120000)
empobj.displayemp()

from stu import Student
stuobj=stu.Student(111, "Scott", "A")
stuobj.displaystu()
