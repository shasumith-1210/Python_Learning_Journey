# Topic - 7

"""
PYTHON MAIN GUARD

The main guard is used to control which code executes
when a Python file is run directly or imported into another file.

Syntax:

if __name__ == "__main__":
    # Code to execute only when this file runs directly

It prevents certain statements from executing
automatically when the module is imported.
"""


# 1. Understanding __name__

"""
Every Python module has a special variable called __name__.

When a Python file is executed directly:

__name__ = "__main__"

When the same file is imported into another module:

__name__ = "module_name"
"""


# 2. Example Without Main Guard

"""
Create a file named calculator.py:

print("Calculator module loaded")

def add(a, b):
    return a + b

print(add(10, 20))


Now create main.py:

import calculator

print("Main program started")

When main.py runs, the output is:

Calculator module loaded
30
Main program started

Why?

Because Python executes the top-level statements
of calculator.py when it is imported.
"""


# 3. Example With Main Guard

"""
Update calculator.py:

print("Calculator module loaded")

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))


Now import it in main.py:

import calculator

print("Main program started")

Output:

Calculator module loaded
Main program started

The add() function is defined, but the function call
inside the main guard is not executed during import.
"""


# 4. Checking __name__ Directly

print("Current Module Name:", __name__)

if __name__ == "__main__":
    print("This file is running directly.")
else:
    print("This file has been imported.")


# 5. Practical Example

"""
Create a file named student.py:

def calculate_average(marks):
    return sum(marks) / len(marks)

def display_result(name, marks):
    average = calculate_average(marks)

    print("Student:", name)
    print("Average:", average)

if __name__ == "__main__":
    marks = [85, 90, 78]
    display_result("Aman", marks)


Now create main.py:

from student import display_result

display_result("Riya", [92, 88, 95])


When student.py is imported:
- The functions are made available.
- The example execution inside the main guard is skipped.

When student.py is run directly:
- The example student result is displayed.
"""


# 6. Why Use the Main Guard?

"""
1. Prevents unwanted code execution during imports.
2. Makes modules reusable.
3. Separates reusable logic from program execution.
4. Makes testing and debugging easier.
5. Provides a clear entry point for a Python program.
"""


# 7. Main Guard in Real Projects

"""
project/
│
├── main.py
│
├── calculator.py
│
└── student.py


main.py:

from calculator import add
from student import calculate_average

def main():
    print(add(10, 20))
    print(calculate_average([80, 90, 100]))

if __name__ == "__main__":
    main()


The main() function contains the main program logic.

The main guard ensures that main() runs only
when main.py is executed directly.
"""


# 8. Important Notes

"""
1. __name__ is a special module attribute.
2. Its value is "__main__" when the file runs directly.
3. When imported, it normally contains the module's name.
4. The main guard prevents its indented code from running
   during a normal import.
5. Functions and classes outside the main guard can
   still be imported and reused.
6. The main guard is a convention, not a compulsory
   requirement for every Python file.
"""