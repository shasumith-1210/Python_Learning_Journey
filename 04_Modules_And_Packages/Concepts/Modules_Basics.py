# Topic - 1

"""
PYTHON MODULES - BASICS

A module is a Python file containing code such as variables,
functions, and classes that can be reused in other Python files.

Modules help us:
1. Organize code into separate files.
2. Reuse code instead of writing it repeatedly.
3. Make large programs easier to manage.
4. Maintain and debug code more easily.
"""

# 1. Understanding a Module

# Every Python (.py) file can act as a module.

# For example, a file named calculator.py can contain:

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


PI = 3.14159


# The file containing these definitions is itself a module.
# Other Python files can reuse its functions and variables.


# 2. Types of Python Modules

"""
Python modules can be broadly classified into three types:

1. Built-in Modules:
   Modules provided by Python.
   Examples: math, random, os, datetime.

2. User-Defined Modules:
   Modules created by programmers.
   Example: calculator.py

3. Third-Party Modules:
   Modules developed by external contributors.
   Examples: numpy, pandas, requests.
"""


# 3. Module Attributes

# Python provides special attributes for modules.

print("Module Name:", __name__)
print("Module File:", __file__)


# __name__ stores the name of the current module.
# When a file runs directly, its __name__ is "__main__".
# When imported into another file, it uses its module name.


# 4. Example: Organizing Code into Modules

"""
Suppose we have the following project:

MyProject/
│
├── main.py
└── calculator.py

calculator.py contains reusable functions:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

main.py can use these functions instead of
writing the same logic again.

We will learn how to import these functions
in the next concept file.
"""


# 5. Why Use Modules?

"""
Without modules:
- All code is written in one large file.
- Reusing code becomes difficult.
- Maintaining the program becomes harder.

With modules:
- Code is divided into smaller files.
- Functions and variables can be reused.
- Projects become easier to understand and maintain.
"""
