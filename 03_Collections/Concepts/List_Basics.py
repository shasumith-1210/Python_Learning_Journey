"""
LISTS IN PYTHON (PART 1 - BASICS)

Definition : 
A list is an ordered, mutable (changeable) collection of elements.
Lists can store multiple values of different data types in a single
variable.

Why Learn Lists?
1. Store multiple values in one variable.
2. Modify data after creation.
3. Access elements using indexes.
4. Traverse collections efficiently.
5. One of the most widely used data structures in Python.

Characteristics :
1. Ordered
2. Mutable
3. Allows duplicate values
4. Can store different data types
5. Dynamic in size

Advantages : 
1. Easy to create and use.
2. Supports indexing and slicing.
3. Can grow or shrink dynamically.
4. Rich collection of built-in methods.

Disadvantages :
1. Searching is slower than dictionaries.
2. Inserting or deleting elements in the middle takes more time.

Syntax : list_name = [element1, element2, element3]
"""

# Creating Lists

numbers = [10, 20, 30, 40, 50]
print(numbers)

# Output:
# [10, 20, 30, 40, 50]


# Empty List

empty_list = []
print(empty_list)

# Output:
# []


# List of Strings

fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']


# List of Floating Point Numbers

prices = [99.99, 150.50, 245.75]
print(prices)

# Output:
# [99.99, 150.5, 245.75]


# List of Boolean Values

status = [True, False, True]
print(status)

# Output:
# [True, False, True]


# Mixed Data Type List

mixed = [10, 3.14, "Python", True]
print(mixed)

# Output:
# [10, 3.14, 'Python', True]


# Nested List

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix)

# Output:
# [[1, 2, 3], [4, 5, 6]]


# Creating a List Using list()

letters = list("Python")
print(letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# Accessing Elements Using Positive Indexing

languages = ["Python", "Java", "C", "JavaScript"]

print(languages[0])
print(languages[1])
print(languages[3])

# Output:
# Python
# Java
# JavaScript


# Accessing Elements Using Negative Indexing

print(languages[-1])
print(languages[-2])

# Output:
# JavaScript
# C


# List Slicing

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])

# Output:
# [20, 30, 40]

print(numbers[:3])

# Output:
# [10, 20, 30]

print(numbers[3:])

# Output:
# [40, 50, 60]

print(numbers[:])

# Output:
# [10, 20, 30, 40, 50, 60]


# Slicing with Step

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::2])

# Output:
# [10, 30, 50, 70]

print(numbers[1::2])

# Output:
# [20, 40, 60, 80]


# Reverse a List Using Slicing

print(numbers[::-1])

# Output:
# [80, 70, 60, 50, 40, 30, 20, 10]


# Copying a List Using Slicing

copied_numbers = numbers[:]

print(copied_numbers)

# Output:
# [10, 20, 30, 40, 50, 60, 70, 80]


# Updating List Elements

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

# Output:
# ['Apple', 'Orange', 'Mango']


# Updating Multiple Elements Using Slice Assignment

numbers = [10, 20, 30, 40, 50]

numbers[1:4] = [200, 300, 400]

print(numbers)

# Output:
# [10, 200, 300, 400, 50]


# Traversing a List Using a for Loop

colors = ["Red", "Green", "Blue"]

for color in colors:
    print(color)

# Output:
# Red
# Green
# Blue


# Traversing a List Using a while Loop

colors = ["Red", "Green", "Blue"]

index = 0

while index < len(colors):
    print(colors[index])
    index += 1

# Output:
# Red
# Green
# Blue


# Traversing Using enumerate()

students = ["Rahul", "Aman", "Priya"]

for index, student in enumerate(students):
    print(index, student)

# Output:
# 0 Rahul
# 1 Aman
# 2 Priya


# List Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)

# Output:
# [1, 2, 3, 4, 5, 6]


# List Repetition

numbers = [1, 2, 3]

print(numbers * 3)

# Output:
# [1, 2, 3, 1, 2, 3, 1, 2, 3]


# Membership Operator (in)

numbers = [10, 20, 30, 40]

print(20 in numbers)

# Output:
# True


# Membership Operator (not in)

print(100 not in numbers)

# Output:
# True


# Built-in Function: len()

numbers = [10, 20, 30, 40, 50]

print(len(numbers))

# Output:
# 5


# Built-in Function: max()

print(max(numbers))

# Output:
# 50


# Built-in Function: min()

print(min(numbers))

# Output:
# 10


# Built-in Function: sum()

print(sum(numbers))

# Output:
# 150


# Calculating Average

average = sum(numbers) / len(numbers)

print(average)

# Output:
# 30.0


# Built-in Function: sorted()

numbers = [50, 20, 40, 10, 30]

print(sorted(numbers))

# Output:
# [10, 20, 30, 40, 50]

print(sorted(numbers, reverse=True))

# Output:
# [50, 40, 30, 20, 10]


# Built-in Function: reversed()

numbers = [10, 20, 30, 40, 50]

print(list(reversed(numbers)))

# Output:
# [50, 40, 30, 20, 10]


# Built-in Function: any()

values = [0, False, "", 5]

print(any(values))

# Output:
# True


# Built-in Function: all()

values = [10, 20, 30]

print(all(values))

# Output:
# True

values = [10, 0, 30]

print(all(values))

# Output:
# False


# Packing a List

numbers = [10, 20, 30, 40]

print(numbers)

# Output:
# [10, 20, 30, 40]


# Unpacking a List

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# Output:
# 10
# 20
# 30


# Extended Unpacking

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50


# Common Mistake: Index Out of Range

numbers = [10, 20, 30]

# print(numbers[5])

# Output:
# IndexError: list index out of range


# Common Mistake: Modifying an Immutable Object

text = "Python"

# text[0] = "J"

# Output:
# TypeError: 'str' object does not support item assignment



"""
# Best Practices

1. Use meaningful variable names.
2. Avoid storing unrelated data in the same list.
3. Use loops instead of accessing each element manually.
4. Use built-in functions whenever possible.
5. Prefer slicing over manual copying when appropriate.
6. Keep lists organized and readable.
"""



"""
# Quick Revision
1. Lists are ordered collections.
2. Lists are mutable.
3. Lists allow duplicate elements.
4. Lists can store different data types.
5. Positive indexing starts from 0.
6. Negative indexing starts from -1.
7. Slicing extracts a portion of a list.
8. Lists can be updated after creation.
9. Lists support concatenation and repetition.
10. Membership operators:
    in
    not in
11. Useful built-in functions:
    len()
    max()
    min()
    sum()
    sorted()
    reversed()
    any()
    all()
12. Lists support packing and unpacking.
13. IndexError occurs when an invalid index is accessed.
"""