# Topic - 5

"""
PYTHON PACKAGES

A package is a way of organizing related Python modules inside directories.

A package can contain:
1. Python modules (.py files).
2. Subpackages (nested packages).
3. An __init__.py file (commonly used to mark and
   initialize regular packages).

Packages help us:
1. Organize large Python projects.
2. Group related modules together.
3. Avoid naming conflicts.
4. Maintain reusable code.
"""


# 1. Understanding Packages

"""
Consider this project:

MyProject/
│
├── main.py
│
└── calculator/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py

Here:

calculator/       -> Package
addition.py       -> Module
subtraction.py    -> Module
__init__.py       -> Package initialization file
"""


# 2. Creating a Package

"""
Step 1: Create a directory named calculator.

Step 2: Inside it, create __init__.py.

Step 3: Create addition.py.

addition.py:

def add(a, b):
    return a + b

Step 4: Create subtraction.py.

subtraction.py:

def subtract(a, b):
    return a - b

The calculator directory now forms a regular package.
"""


# 3. Importing Modules from a Package

"""
Suppose main.py is outside the calculator package.

Method 1: Import the complete module.

import calculator.addition

print(calculator.addition.add(10, 5))


Method 2: Import a module using from.

from calculator import addition

print(addition.add(10, 5))


Method 3: Import a specific function.

from calculator.addition import add

print(add(10, 5))
"""


# 4. Importing Multiple Modules from a Package

"""
from calculator import addition, subtraction

print(addition.add(20, 10))
print(subtraction.subtract(20, 10))
"""


# 5. Understanding Nested Packages

"""
A package can contain another package.
Such packages are called nested packages.

Project Structure:

MyProject/
│
├── main.py
│
└── operations/
    ├── __init__.py
    │
    ├── arithmetic/
    │   ├── __init__.py
    │   ├── addition.py
    │   └── subtraction.py
    │
    └── geometry/
        ├── __init__.py
        ├── circle.py
        └── rectangle.py

Here:

operations       -> Main package
arithmetic       -> Subpackage
geometry         -> Subpackage
addition.py      -> Module
circle.py        -> Module
"""


# 6. Importing from Nested Packages

"""
We can import modules from nested packages.

from operations.arithmetic import addition

print(addition.add(10, 20))


We can also import a specific function.

from operations.arithmetic.addition import add

print(add(10, 20))
"""


# 7. Absolute Imports

"""
An absolute import specifies the complete path from the top-level package.

Example:

from operations.arithmetic.addition import add

print(add(10, 20))

Absolute imports make the module's location clear.
"""


# 8. Relative Imports

"""
Relative imports specify a module's location relative to the current package.

Suppose the structure is:

operations/
│
├── __init__.py
│
└── arithmetic/
    ├── __init__.py
    ├── addition.py
    └── subtraction.py

Inside subtraction.py:

from .addition import add

The single dot (.) refers to the current package.

Other relative import symbols:

.   -> Current package
..  -> Parent package
... -> Package two levels above

Relative imports are generally used inside packages.
They should be run as part of a package, not as
standalone scripts.
"""


# 9. Regular Packages vs Namespace Packages

"""
Regular Package:
- Commonly contains an __init__.py file.
- Can execute initialization code when imported.

Namespace Package:
- Does not require an __init__.py file.
- Can combine portions of a package located
  in different directories.

Most beginner projects use regular packages.
"""


# 10. Packages vs Modules

"""
Module:
- A single Python file.
- Contains reusable code.
- Example: addition.py

Package:
- Organizes related modules.
- Usually represented by a directory.
- Can contain subpackages.
- Example: calculator/

Remember:

A module is a file, whereas a package is a way
to organize modules into a directory structure.
"""


# 11. Important Notes

"""
1. Packages help organize large Python applications.
2. A package can contain multiple modules.
3. Packages can contain nested packages.
4. __init__.py is commonly used in regular packages.
5. Python supports both absolute and relative imports.
6. Python also supports namespace packages without
   an __init__.py file.
"""