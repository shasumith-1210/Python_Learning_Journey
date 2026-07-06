"""
Functions

Definition:
A function is a reusable block of code that performs a specific task.
Functions help organize code, reduce repetition, and improve readability.

Why Learn Functions?
• Avoid writing the same code repeatedly.
• Improve code readability.
• Make programs modular and easier to maintain.
• Simplify debugging and testing.

Syntax:

def function_name(parameters):
    # Function Body
    return value

Types of Functions:
• Built-in Functions
• User-defined Functions
• Lambda Functions
• Recursive Functions

Advantages:
• Code Reusability
• Better Readability
• Easier Debugging
• Modular Programming
"""


# Function Definition

# A function is created using the def keyword.
# The function body executes only when the function is called.

def greet():
    print("Welcome to Python!")

greet()

# Welcome to Python!


# Function with Parameters

# Parameters allow a function to receive values from the caller.

def greet_user(name):
    print("Hello,", name)

greet_user("Shasumith")

# Hello, Shasumith


# Function with Multiple Parameters

# A function can accept multiple parameters.

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(10, 20)

# 30


# Function Returning a Value

# The return statement sends a value back to the caller.

def square(number):
    return number * number

result = square(5)

print(result)

# 25


# Returning Multiple Values

# A function can return multiple values separated by commas.
# Python automatically packs them into a tuple.

def calculate(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2

addition, subtraction, multiplication = calculate(10, 5)

print(addition)
# 15

print(subtraction)
# 5

print(multiplication)
# 50


# Default Arguments

# Default arguments let you assign a fallback value to a parameter directly
# in the function definition.
# If the caller does not provide that argument,
# Python uses the default value.

def greet_with_default(name="Guest"):
    print("Hello,", name)

greet_with_default()

# Hello, Guest

greet_with_default("Rahul")

# Hello, Rahul


# Positional Arguments

# Positional arguments are matched based on their position.
# The order of arguments must match the order of parameters.

def employee(name, department):
    print(name, department)

employee("Aman", "HR")

# Aman HR


# Keyword Arguments

# Keyword arguments are passed using the parameter name.
# The order of arguments does not matter.

def student(name, age):
    print(name, age)

student(age=19, name="Shasumith")

# Shasumith 19


# Positional-Only Arguments (/)

# Parameters before / must be passed positionally.

def subtract_numbers(num1, num2, /):
    print(num1 - num2)

subtract_numbers(20, 5)

# 15


# Keyword-Only Arguments (*)

# Parameters after * must be passed using their names.

def create_account(name, *, age):
    print(name, age)

create_account("Shasumith", age=19)

# Shasumith 19


# Arbitrary Arguments (*args)

# *args allows a function to accept any number of positional arguments.
# Python stores all the arguments as a tuple.

def find_total(*numbers):

    print(numbers)
    # (10, 20, 30)

    print(sum(numbers))
    # 60

find_total(10, 20, 30)

find_total(5, 10, 15, 20)

# (5, 10, 15, 20)
# 50


# Keyword Arbitrary Arguments (**kwargs)

# **kwargs allows a function to accept any number of keyword arguments.
# Python stores all the arguments as a dictionary.

def display_profile(**details):

    print(details)

    print(details["name"])

    print(details["age"])

profile = {
    "name": "Shasumith",
    "age": 19,
    "city": "Mumbai"
}

display_profile(**profile)

# {'name': 'Shasumith', 'age': 19, 'city': 'Mumbai'}
# Shasumith
# 19

# Lambda Functions

# A lambda function is a small anonymous function.
# It can have any number of arguments but only one expression.
# Lambda functions are commonly used for short and simple operations.

square_lambda = lambda number: number * number

print(square_lambda(5))

# 25


add_lambda = lambda num1, num2: num1 + num2

print(add_lambda(10, 20))

# 30


numbers = [1, 2, 3, 4, 5]

double_numbers = list(map(lambda number: number * 2, numbers))

print(double_numbers)

# [2, 4, 6, 8, 10]


# Calling One Function from Another

# A function can call another function just like any other statement.
# This helps divide a large problem into smaller reusable functions.

def greet():
    print("Hello!")

def welcome():
    greet()
    print("Welcome to Python!")

welcome()

# Hello!
# Welcome to Python!


# Recursive Functions

# A recursive function is a function that calls itself.
# Every recursive function must have a base condition
# to stop infinite recursion.

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))

# 120


# Local Variables

# A local variable is created inside a function.
# It can only be accessed within that function.

def display_message():

    message = "Local Variable"

    print(message)

display_message()

# Local Variable


# Global Variables

# A global variable is declared outside all functions.
# It can be accessed from anywhere in the program.

language = "Python"

def display_language():

    print(language)

display_language()

# Python

print(language)

# Python


# global Keyword

# The global keyword allows a function to modify
# a global variable.
# Without using global, Python creates a local variable.

count = 0

def increment():

    global count

    count += 1

increment()

print(count)

# 1


# Nested Functions

# A function defined inside another function
# is called a nested function.
# Nested functions help organize helper functions.

def outer_function():

    def inner_function():
        print("Inside Inner Function")

    inner_function()

    print("Inside Outer Function")

outer_function()

# Inside Inner Function
# Inside Outer Function


# nonlocal Keyword

# The nonlocal keyword allows an inner function
# to modify a variable from the enclosing function.

def outer_nonlocal():

    count = 0

    def inner():

        nonlocal count

        count += 1

        print(count)

    inner()
    inner()

outer_nonlocal()

# 1
# 2


# Variable Scope (LEGB Rule)

# Python searches for variables in the following order:
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in


# Local Scope

# Variables declared inside a function belong
# to the local scope.

def local_scope():

    message = "Local Variable"

    print(message)

local_scope()

# Local Variable


# Enclosing Scope

# An enclosing scope exists when one function
# is defined inside another function.

def enclosing_scope():

    message = "Enclosing Variable"

    def inner():
        print(message)

    inner()

enclosing_scope()

# Enclosing Variable


# Global Scope

# Variables declared outside all functions
# belong to the global scope.

message = "Global Variable"

def global_scope():

    print(message)

global_scope()

# Global Variable


# Built-in Scope

# Built-in names are predefined by Python.

numbers = [10, 20, 30]

print(len(numbers))

# 3

print(max(numbers))

# 30

print(min(numbers))

# 10

print(sum(numbers))

# 60


# LEGB Example 1

# Python first searches for the variable in:
# Local → Enclosing → Global → Built-in

message = "Global"

def outer_local():

    message = "Enclosing"

    def inner():

        message = "Local"

        print(message)

    inner()

outer_local()

# Local


# LEGB Example 2 (Without Local Variable)

# If Local is not found,
# Python searches the Enclosing scope.

message = "Global"

def outer_enclosing():

    message = "Enclosing"

    def inner():
        print(message)

    inner()

outer_enclosing()

# Enclosing


# LEGB Example 3 (Without Enclosing Variable)

# If Local and Enclosing are not found,
# Python searches the Global scope.

message = "Global"

def outer_global():

    def inner():
        print(message)

    inner()

outer_global()

# Global

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