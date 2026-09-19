# ITERTOOLS PART 1 - WHAT IS ITERTOOLS? AND INFITE ITERATORS

"""
# itertools

itertools is a built-in Python module that provides
fast and memory-efficient iterator building tools.

Instead of creating new collections in memory,
itertools generates values one at a time, making it
ideal for working with large datasets.

Syntax:
import itertools

Main Categories
---------------
1. Infinite Iterators
2. Combinatoric Iterators
3. Terminating Iterators

Applications
------------
- Combinatorics
- Data Processing
- DSA
- Competitive Programming
- Machine Learning
- Automation
"""

import itertools

"""
# count()

Generates consecutive numbers indefinitely.

Syntax:
itertools.count(start=0, step=1)
"""

# Basic count()

counter = itertools.count()

for number in counter:
    print(number)

    if number == 5:
        break

# Output:
# 0
# 1
# 2
# 3
# 4
# 5

# count() with Starting Value

counter = itertools.count(10)

for number in counter:
    print(number)

    if number == 15:
        break

# Output:
# 10
# 11
# 12
# 13
# 14
# 15

# count() with Step

counter = itertools.count(0, 5)

for number in counter:
    print(number)

    if number == 25:
        break

# Output:
# 0
# 5
# 10
# 15
# 20
# 25

# count() with Floating Point Numbers

counter = itertools.count(0.5, 0.5)

for number in counter:
    print(number)

    if number == 3.0:
        break

# Output:
# 0.5
# 1.0
# 1.5
# 2.0
# 2.5
# 3.0

# Practical Example - Auto Increment IDs

student_id = itertools.count(101)

print(next(student_id))

# Output:
# 101

print(next(student_id))

# Output:
# 102

print(next(student_id))

# Output:
# 103

"""
Applications of count()
- Auto Increment IDs
- Infinite Counters
- Index Generation
- Sequence Generation
- Simulation Programs
"""

# cycle() : Repeats the elements of an iterable indefinitely.

colors = itertools.cycle(["Red", "Green", "Blue"])

for _ in range(7):
    print(next(colors))

# Output:
# Red
# Green
# Blue
# Red
# Green
# Blue
# Red


# cycle() with a String

letters = itertools.cycle("ABC")

for _ in range(8):
    print(next(letters))

# Output:
# A
# B
# C
# A
# B
# C
# A
# B


"""
cycle() keeps repeating the iterable forever.

Always use a stopping condition when using cycle()
inside a loop.
"""


# Practical Example - Round Robin

players = itertools.cycle([
    "Player 1",
    "Player 2",
    "Player 3"
])

for _ in range(6):
    print(next(players))

# Output:
# Player 1
# Player 2
# Player 3
# Player 1
# Player 2
# Player 3


# repeat() : Repeats the same value indefinitely.

values = itertools.repeat("Python")

for _ in range(5):
    print(next(values))

# Output:
# Python
# Python
# Python
# Python
# Python


# repeat() with a Number

numbers = itertools.repeat(10)

for _ in range(4):
    print(next(numbers))

# Output:
# 10
# 10
# 10
# 10


# repeat() with a Specific Number of Times

values = itertools.repeat("Hello", 3)

for value in values:
    print(value)

# Output:
# Hello
# Hello
# Hello


# Practical Example - Default Values

default_values = itertools.repeat(0, 5)

print(list(default_values))

# Output:
# [0, 0, 0, 0, 0]


# Practical Example - Initializing Data

scores = list(itertools.repeat(0, 5))

print(scores)

# Output:
# [0, 0, 0, 0, 0]


"""
Applications of cycle()

- Round Robin Scheduling
- Repeating Patterns
- Turn-Based Systems
- Circular Buffers
- Playlist Rotation

Applications of repeat()

- Default Values
- Initialization
- Repeated Function Arguments
- Testing
- Generating Constant Values
"""

"""
# Infinite Iterators - Quick Revision

count() : Generates an infinite sequence.

count(start, step)

Example: 0, 1, 2, 3, 4, ...


cycle() : Repeats an iterable indefinitely.

Example:
A, B, C, A, B, C, ...


repeat() : Repeats the same value.

Example:
10, 10, 10, 10, ...

repeat(value, times) : can be used when a fixed number of repetitions is required.
"""