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