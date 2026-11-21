# Topic - 4

"""
CUSTOM MODULES IN PYTHON

A custom module is a Python file created by a programmer.

We can store reusable functions, variables, and classes
inside one Python file and import them into another file.

This helps us:
1. Avoid repeating code.
2. Organize large programs.
3. Reuse functions across multiple files.
4. Maintain code more easily.
"""

# 1. Creating a Custom Module

"""
Create a file named calculator.py.

calculator.py:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

PI = 3.14159

This file is now a custom Python module.
"""


# 2. Importing a Custom Module

"""
Create another file named main.py in the same folder.

main.py:

import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.PI)

We access the functions and variables
using the module name.
"""


# 3. Importing Specific Functions

"""
Instead of importing the entire module,
we can import only the functions we need.

from calculator import add, multiply

print(add(10, 5))
print(multiply(10, 5))

The imported functions can be used directly.
"""


# 4. Importing with an Alias

"""
We can give a custom module a shorter name.

import calculator as calc

print(calc.add(20, 10))
print(calc.multiply(20, 10))

The alias is used instead of the original module name.
"""


# 5. Creating a Module with Variables and Functions

"""
Create a file named student.py.

student.py:

student_name = "Aman"
student_age = 20
student_marks = [85, 90, 78]

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_student():
    print("Name:", student_name)
    print("Age:", student_age)

Now import it into another file:

import student

student.display_student()

average = student.calculate_average(student.student_marks)
print("Average:", average)
"""


# 6. Creating a Module with a Class

"""
Create a file named employee.py.

employee.py:

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

Importing the class:

from employee import Employee

emp = Employee("Rahul", 50000)
emp.display()
"""


# 7. Using Multiple Custom Modules

"""
Project Structure:

MyProject/
│
├── main.py
├── calculator.py
├── student.py
└── employee.py

main.py can import and use all three modules.

import calculator
import student
import employee

Each module handles a separate responsibility.
"""


# 8. Important: Module Execution

"""
When a module is imported for the first time,
Python executes its top-level statements.

For example:

# calculator.py

print("Calculator module loaded")

def add(a, b):
    return a + b

When main.py imports calculator,
the message is displayed.

This is why we should avoid placing unnecessary
execution code directly at the top level of a module.
"""


# 9. Important Notes

"""
1. A Python file can be used as a custom module.
2. The filename becomes the module name.
3. Python modules normally use the .py extension.
4. Imported modules can contain functions, variables, and classes.
5. Modules in the same directory can generally be imported
   using their module names.
6. Avoid naming custom modules after standard library modules.
   For example, avoid naming a file math.py or random.py.
"""