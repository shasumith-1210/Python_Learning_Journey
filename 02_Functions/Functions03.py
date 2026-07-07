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