# Topic - 6

"""
PYTHON __INIT__.PY FILE

The __init__.py file is used to initialize a regular Python package.

It can contain:
1. Initialization code.
2. Package-level variables.
3. Imports from other modules.
4. Package metadata.
5. The __all__ variable.

It is commonly placed inside a package directory.
"""


# 1. Basic Package Structure

"""
MyProject/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py

The __init__.py file makes calculator a regular package.
"""


# 2. Writing Code Inside __init__.py

"""
calculator/__init__.py:

print("Calculator package initialized")

PI = 3.14159

When we import the package:

import calculator

The initialization message is displayed.

We can also access the package variable:

print(calculator.PI)
"""


# 3. Importing Modules Through __init__.py

"""
Suppose addition.py contains:

def add(a, b):
    return a + b


And subtraction.py contains:

def subtract(a, b):
    return a - b


Inside calculator/__init__.py:

from .addition import add
from .subtraction import subtract

Now main.py can directly use:

import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))

The dot (.) indicates a relative import
from the current package.
"""


# 4. Importing Specific Functions from a Package

"""
We can also import functions directly:

from calculator import add, subtract

print(add(20, 10))
print(subtract(20, 10))

These functions are available because
they were imported in __init__.py.
"""


# 5. Understanding __all__

"""
The __all__ variable defines which names are exposed
when someone uses a wildcard import.

Suppose calculator/__init__.py contains:

from .addition import add
from .subtraction import subtract
from .multiplication import multiply

__all__ = ["add", "subtract"]

Now another file uses:

from calculator import *

Only add and subtract are imported through
this wildcard import.

multiply is not included.
"""


# 6. Package Metadata

"""
We can also define package-level information.

Inside calculator/__init__.py:

__version__ = "1.0.0"
__author__ = "Python Developer"

These variables can be accessed using:

import calculator

print(calculator.__version__)
print(calculator.__author__)
"""


# 7. Complete Practical Example

"""
Project Structure:

MyProject/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── addition.py
    └── multiplication.py


addition.py:

def add(a, b):
    return a + b


multiplication.py:

def multiply(a, b):
    return a * b


__init__.py:

from .addition import add
from .multiplication import multiply

__version__ = "1.0.0"

__all__ = ["add", "multiply"]


main.py:

import calculator

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))
print(calculator.__version__)


Output:

30
20
1.0.0
"""


# 8. Does Every Package Need __init__.py?

"""
No.

Python also supports namespace packages,
which do not require an __init__.py file.

However, regular packages commonly include it.

For beginner projects, including __init__.py
makes package organization easier to understand.
"""


# 9. Important Notes

"""
1. __init__.py is associated with regular packages.
2. It runs when the package is imported for the first time
   in a running Python process.
3. It can contain package-level variables and imports.
4. Relative imports can be used inside it.
5. __all__ controls names included in wildcard imports.
6. Namespace packages do not require __init__.py.
"""