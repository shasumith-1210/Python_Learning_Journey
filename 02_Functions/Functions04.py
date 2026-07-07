# Function Annotations

# Function annotations are optional hints that describe
# the expected data types of parameters and return values.
# They improve code readability and documentation.

def multiply(num1: int, num2: int) -> int:
    return num1 * num2

print(multiply(5, 4))

# 20


# Docstrings

# A docstring is a string written inside a function
# to describe its purpose.
# It can be accessed using the __doc__ attribute.

def greet_docstring():
    """Prints a welcome message."""
    print("Welcome!")

print(greet_docstring.__doc__)

# Prints a welcome message.


# Function Aliasing

# A function can be assigned to another variable.
# Both names will refer to the same function.

def hello():
    print("Hello!")

welcome_message = hello

welcome_message()

# Hello!

hello()

# Hello!


# Built-in Functions

# Python provides many built-in functions that
# can be used directly.

numbers = [10, 20, 30, 40]

print(len(numbers))
# 4

print(max(numbers))
# 40

print(min(numbers))
# 10

print(sum(numbers))
# 100

print(sorted(numbers))
# [10, 20, 30, 40]

print(sorted(numbers, reverse=True))
# [40, 30, 20, 10]

print(abs(-15))
# 15

print(round(3.14159265, 2))
# 3.14

print(pow(2, 5))
# 32

print(type(numbers))
# <class 'list'>

print(bin(10))
# 0b1010

print(oct(10))
# 0o12

print(hex(255))
# 0xff

print(any([False, False, True]))
# True

print(all([True, True, True]))
# True

print(list(reversed(numbers)))
# [40, 30, 20, 10]


# enumerate()

# enumerate() returns both the index and value
# while iterating over an iterable.

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 0 Apple
# 1 Banana
# 2 Mango


# zip()

# zip() combines multiple iterables
# into a single iterable.

names = ["Rahul", "Aman", "Priya"]
marks = [85, 90, 95]

result = list(zip(names, marks))

print(result)

# [('Rahul', 85), ('Aman', 90), ('Priya', 95)]


# map()

# map() applies a function to every element
# of an iterable.
# It returns a map object.

def square(number):
    return number * number

numbers = [1, 2, 3, 4, 5]

result = list(map(square, numbers))

print(result)

# [1, 4, 9, 16, 25]


# map() using Lambda Function

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda number: number * number, numbers))

print(result)

# [1, 4, 9, 16, 25]


# filter()

# filter() selects only those elements
# that satisfy a condition.
# It returns a filter object.

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(is_even, numbers))

print(result)

# [2, 4, 6]


# filter() using Lambda Function

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda number: number % 2 == 0, numbers))

print(result)

# [2, 4, 6]


# reduce()

# reduce() repeatedly applies a function
# to reduce an iterable to a single value.
# It is available in the functools module.

from functools import reduce

def add(num1, num2):
    return num1 + num2

numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)

print(result)

# 15


# reduce() using Lambda Function

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda num1, num2: num1 + num2, numbers)

print(result)

# 15


# pass Statement

# pass is used as a placeholder.
# It allows us to define an empty function
# without causing an error.

def future_function():
    pass

print("Function Created Successfully")

# Function Created Successfully


# Functions Returning None

# If a function does not explicitly return a value,
# Python automatically returns None.

def display():
    print("Hello!")

result = display()

print(result)

# Hello!
# None


# Quick Revision

# Functions are reusable blocks of code.
# Parameters receive values.
# Arguments pass values to functions.
# return sends values back to the caller.
# Default arguments provide fallback values.
# Positional arguments depend on order.
# Keyword arguments use parameter names.
# *args stores positional arguments as a tuple.
# **kwargs stores keyword arguments as a dictionary.
# Lambda functions are anonymous functions.
# Recursive functions call themselves.
# Local variables exist inside functions.
# Global variables exist outside functions.
# global modifies global variables.
# nonlocal modifies enclosing variables.
# Python follows the LEGB rule for variable lookup.
# Function annotations improve readability.
# Docstrings document functions.
# Functions can be assigned to variables (aliasing).
# map(), filter() and reduce() simplify data processing.
# Functions without an explicit return statement return None.

# Common Mistakes

# Forgetting to call a function.
# Forgetting the return statement.
# Confusing parameters with arguments.
# Using mutable objects as default arguments.
# Infinite recursion due to a missing base case.
# Trying to modify a global variable without using the global keyword.
# Accessing a local variable outside its function.