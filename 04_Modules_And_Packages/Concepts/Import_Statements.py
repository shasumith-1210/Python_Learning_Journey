# Topic - 2

"""
PYTHON IMPORT STATEMENTS

The import statement allows us to use code from other modules.

We can import:
1. An entire module.
2. Specific functions or variables.
3. A module using an alias.
4. Multiple modules together.
"""

# 1. Importing an Entire Module

import math

print(math.sqrt(25))
print(math.pi)
print(math.factorial(5))

# Syntax: module_name.function_name()


# 2. Importing Specific Functions

from math import sqrt, factorial

print(sqrt(36))
print(factorial(5))

# We can directly use the imported functions without writing the module name.


# 3. Importing a Specific Variable

from math import pi, e

print(pi)
print(e)


# 4. Importing a Module with an Alias

import math as m

print(m.sqrt(49))
print(m.pi)

# An alias gives a module a shorter name.


# 5. Importing Functions with an Alias

from math import factorial as fact

print(fact(6))


# 6. Importing Multiple Modules

import math
import random
import datetime

print(math.sqrt(64))
print(random.randint(1, 10))
print(datetime.date.today())


# 7. Importing Everything from a Module

from math import *

print(sqrt(81))
print(pi)
print(factorial(4))

# This imports all names exposed by the module.
# Avoid using this in larger projects because it can cause naming conflicts.


# 8. Importing User-Defined Modules

"""
Suppose we have two files in the same folder:

Project/
│
├── main.py
└── calculator.py

calculator.py:

def add(a, b):
    return a + b

PI = 3.14159

main.py:

import calculator

print(calculator.add(10, 20))
print(calculator.PI)

The main.py file can access the contents
of calculator.py using the module name.
"""


# 9. Importing Specific Items from a User-Defined Module

"""
Using the same calculator.py file:

from calculator import add, PI

print(add(10, 20))
print(PI)

We can directly access the imported items.
"""


# 10. Important Notes

"""
1. Python executes a module when it is imported
   for the first time in a running program.

2. Python caches imported modules in sys.modules.

3. Importing the same module again usually does not
   execute its code again.

4. Use aliases when they improve readability.

5. Avoid importing everything using * in large projects.
"""