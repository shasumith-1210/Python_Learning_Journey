"""
# Data Structure Utilities

Python provides several built-in functions that make it easier
to work with lists, tuples, dictionaries, sets, and other
iterable data structures.

These utilities help with:
- Traversing data
- Combining data
- Transforming data
- Filtering data
- Sorting data
- Checking conditions
- Working with object types
- Hashing and slicing

Main Utilities
--------------
1. enumerate()
2. zip()
3. map()
4. filter()
5. reduce()
6. sorted()
7. reversed()
8. any()
9. all()
10. slice()
11. hash()
12. isinstance()
13. type()

Applications
------------
- Data processing
- Searching and filtering
- Sorting
- DSA
- Competitive Programming
- Data Analysis
- Automation
"""

from functools import reduce


# enumerate() : Adds a counter to an iterable.

students = ["Aman", "Riya", "Rahul", "Sneha"]

for index, student in enumerate(students):
    print(index, student)

# Output:
# 0 Aman
# 1 Riya
# 2 Rahul
# 3 Sneha


# enumerate() with start : Starts counting from the given number.

for number, student in enumerate(students, start=1):
    print(number, student)

# Output:
# 1 Aman
# 2 Riya
# 3 Rahul
# 4 Sneha


# zip() : Combines elements from two or more iterables.

names = ["Aman", "Riya", "Rahul"]
marks = [85, 92, 78]

result = zip(names, marks)

print(list(result))

# Output:
# [('Aman', 85), ('Riya', 92), ('Rahul', 78)]


# zip() with multiple iterables : Combines multiple collections together.

names = ["Aman", "Riya", "Rahul"]
marks = [85, 92, 78]
subjects = ["Python", "Java", "DBMS"]

result = zip(names, marks, subjects)

print(list(result))

# Output:
# [('Aman', 85, 'Python'), ('Riya', 92, 'Java'), ('Rahul', 78, 'DBMS')]


# zip() stops at the shortest iterable.

numbers = [1, 2, 3, 4]
letters = ["A", "B"]

print(list(zip(numbers, letters)))

# Output:
# [(1, 'A'), (2, 'B')]


# map() : Applies a function to every element of an iterable.

numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)

print(list(squares))

# Output:
# [1, 4, 9, 16, 25]


# map() with built-in functions : Applies an existing function.

numbers = ["10", "20", "30", "40"]

numbers = map(int, numbers)

print(list(numbers))

# Output:
# [10, 20, 30, 40]


# map() with multiple iterables : Passes corresponding elements to the function.

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = map((lambda x, y: x + y), numbers1, numbers2)

print(list(result))

# Output:
# [11, 22, 33]


# filter() : Selects elements that satisfy a condition.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))

# Output:
# [2, 4, 6]


# filter() with strings : Filters elements based on a condition.

names = ["Aman", "Riya", "Rahul", "Sneha"]

long_names = filter(lambda name: len(name) > 4, names)

print(list(long_names))

# Output:
# ['Rahul', 'Sneha']


# filter() with None : Removes falsy values.

values = [0, 1, False, True, "", "Python", None, 10]

result = filter(None, values)

print(list(result))

# Output:
# [1, True, 'Python', 10]


# reduce() : Reduces an iterable to a single value.

numbers = [1, 2, 3, 4, 5]

total = reduce((lambda x, y: x + y), numbers)

print(total)

# Output:
# 15


# reduce() for multiplication : Combines all values using multiplication.

numbers = [1, 2, 3, 4, 5]

product = reduce((lambda x, y: x * y), numbers)

print(product)

# Output:
# 120


# reduce() with initial value : Starts the reduction from a given value.

numbers = [1, 2, 3]

total = reduce((lambda x, y: x + y), numbers, 10)

print(total)

# Output:
# 16


# sorted() : Returns a new sorted list without changing the original iterable.

numbers = [5, 2, 8, 1, 3]

result = sorted(numbers)

print(result)
print(numbers)

# Output:
# [1, 2, 3, 5, 8]
# [5, 2, 8, 1, 3]


# sorted() reverse : Sorts elements in descending order.

numbers = [5, 2, 8, 1, 3]

print(sorted(numbers, reverse=True))

# Output:
# [8, 5, 3, 2, 1]


# sorted() with key : Sorts according to a custom rule.

names = ["Rahul", "Aman", "Christopher", "Riya"]

result = sorted(names, key=len)

print(result)

# Output:
# ['Aman', 'Riya', 'Rahul', 'Christopher']


# sorted() with lambda : Sorts complex data using a specific value.

students = [("Aman", 85), ("Riya", 92), ("Rahul", 78)]

result = sorted(students, key=lambda student: student[1])

print(result)

# Output:
# [('Rahul', 78), ('Aman', 85), ('Riya', 92)]


# reversed() : Returns an iterator that traverses an iterable in reverse order.

numbers = [1, 2, 3, 4, 5]

result = reversed(numbers)

print(list(result))

# Output:
# [5, 4, 3, 2, 1]


# reversed() with string : Reverses the characters of a string.

word = "Python"

print("".join(reversed(word)))

# Output:
# nohtyP


# any() : Returns True if at least one element is truthy.

numbers = [0, 0, 5, 0]

print(any(numbers))

# Output:
# True


# any() practical example : Checks whether any student passed.

marks = [35, 28, 42, 19]

print(any(mark >= 40 for mark in marks))

# Output:
# True


# all() : Returns True if every element is truthy.

numbers = [1, 2, 3, 4]

print(all(numbers))

# Output:
# True


# all() practical example : Checks whether all students passed.

marks = [65, 72, 81, 55]

print(all(mark >= 40 for mark in marks))

# Output:
# True


# slice() : Creates a reusable slicing object.

numbers = [10, 20, 30, 40, 50, 60]

s = slice(1, 5)

print(numbers[s])

# Output:
# [20, 30, 40, 50]


# slice() with step : Supports start, stop, and step.

numbers = [10, 20, 30, 40, 50, 60]

s = slice(0, 6, 2)

print(numbers[s])

# Output:
# [10, 30, 50]


# hash() : Returns the hash value of a hashable object.

value = "Python"

print(hash(value))

# Output:
# Hash value varies between Python runs.


"""
hash() is mainly used internally by hash-based data structures
such as dictionaries and sets.

Only hashable objects can be passed to hash().

Examples of hashable objects:
- int
- float
- str
- tuple containing hashable values

Lists, sets, and dictionaries are not hashable.
"""


# isinstance() : Checks whether an object belongs to a particular type.

value = 100

print(isinstance(value, int))

# Output:
# True


# isinstance() with multiple types : Checks against multiple types.

value = 10.5

print(isinstance(value, (int, float)))

# Output:
# True


# isinstance() practical example : Validates data type before processing.

marks = [85, 90, "75", 92]

for mark in marks:
    if isinstance(mark, int):
        print(mark)

# Output:
# 85
# 90
# 92


# type() : Returns the exact type of an object.

value = 100

print(type(value))

# Output:
# <class 'int'>


# type() with different data structures : Identifies the object's type.

data = [1, 2, 3]

print(type(data))

# Output:
# <class 'list'>


# Practical Example 1 : Create a student marks dictionary using zip().

names = ["Aman", "Riya", "Rahul"]
marks = [85, 92, 78]

student_marks = dict(zip(names, marks))

print(student_marks)

# Output:
# {'Aman': 85, 'Riya': 92, 'Rahul': 78}


# Practical Example 2 : Find even numbers using filter().

numbers = range(1, 11)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]


# Practical Example 3 : Convert marks to percentages using map().

marks = [75, 80, 90, 85]

percentages = list(map(lambda x: x / 100 * 100, marks))

print(percentages)

# Output:
# [75.0, 80.0, 90.0, 85.0]


# Practical Example 4 : Calculate total marks using reduce().

marks = [75, 80, 90, 85]

total = reduce(lambda x, y: x + y, marks)

print(total)

# Output:
# 330


# Practical Example 5 : Find the highest mark using max().

marks = [75, 80, 90, 85]

print(max(marks))

# Output:
# 90


# Practical Example 6 : Sort students by marks.

students = {"Aman": 85, "Riya": 92, "Rahul": 78, "Sneha": 88}

result = sorted(students.items(), key=lambda item: item[1], reverse=True)

print(result)

# Output:
# [('Riya', 92), ('Sneha', 88), ('Aman', 85), ('Rahul', 78)]


# Practical Example 7 : Check whether all numbers are positive.

numbers = [10, 20, 30, 40]

print(all(number > 0 for number in numbers))

# Output:
# True


# Practical Example 8 : Check whether any number is negative.

numbers = [10, 20, -5, 40]

print(any(number < 0 for number in numbers))

# Output:
# True


# Practical Example 9 : Combine names and marks using enumerate().

names = ["Aman", "Riya", "Rahul"]
marks = [85, 92, 78]

for index, (name, mark) in enumerate(zip(names, marks), start=1):
    print(index, name, mark)

# Output:
# 1 Aman 85
# 2 Riya 92
# 3 Rahul 78


# Practical Example 10 : Pipeline using map() and filter().

numbers = range(1, 11)

result = map(lambda x: x ** 2,
             filter(lambda x: x % 2 == 0, numbers))

print(list(result))

# Output:
# [4, 16, 36, 64, 100]


"""
# Iterator vs List

Many utilities such as map(), filter(), zip(), reversed()
and enumerate() return iterators instead of creating a complete
list immediately.

This makes them memory-efficient because values are generated
when needed.

Example:

numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(result)

To see all values:

print(list(result))
"""


"""
# Time Complexity

enumerate()      : O(n) for complete traversal
zip()            : O(n)
map()            : O(n)
filter()         : O(n)
reduce()         : O(n)
sorted()         : O(n log n)
reversed()       : O(1) to create iterator
any()            : O(n) worst case
all()            : O(n) worst case
hash()           : O(1) average for common hashable types
isinstance()     : O(1)
type()           : O(1)

Note: 
any() and all() can stop early.
any() stops when it finds a truthy value.
all() stops when it finds a falsy value.
"""


"""
# Common Mistakes

1. Forgetting that map(), filter(), and zip() return iterators.
2. Calling list() on very large or infinite iterators unnecessarily.
3. Forgetting that zip() stops at the shortest iterable.
4. Using sorted() when the original list must be modified.
5. Confusing any() with all().
6. Using hash() with mutable objects such as lists.
7. Using reduce() when a simple sum() or built-in function is clearer.
8. Forgetting that reversed() returns an iterator.
"""


"""
# Best Practices

- Prefer built-in functions when they make the code clearer.
- Use enumerate() instead of manually maintaining a counter.
- Use zip() when processing corresponding elements together.
- Use map() for simple transformations.
- Use filter() for simple filtering operations.
- Use comprehensions when they are more readable than map/filter.
- Use sorted() when the original data should remain unchanged.
- Use any() and all() for clean condition checking.
- Avoid unnecessary conversion of iterators into lists.
- Use reduce() only when it makes the operation clearer.
"""


"""
# Quick Revision

enumerate() -> Adds index/counter
zip()       -> Combines iterables
map()       -> Transforms elements
filter()    -> Selects elements
reduce()    -> Reduces to one value
sorted()    -> Returns sorted data
reversed()  -> Reverse iterator
any()       -> At least one is True
all()       -> Every value is True
slice()     -> Creates slicing object
hash()      -> Returns hash value
isinstance()-> Checks object type
type()      -> Returns exact type

These utilities are frequently used with Python's
lists, tuples, sets, dictionaries, and iterators.
"""