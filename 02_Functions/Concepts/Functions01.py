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