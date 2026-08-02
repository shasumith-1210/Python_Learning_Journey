"""
TUPLES IN PYTHON

Definition:
A tuple is an ordered, immutable collection of elements.
Unlike lists, tuples cannot be modified after they are created.

Tuples can store multiple values of different data types in a
single variable.

Why Learn Tuples?
- Protect data from accidental modification.
- Faster than lists for read-only operations.
- Can be used as dictionary keys (if immutable).
- Consume less memory than lists.

Characteristics
1. Ordered
2. Immutable
3. Allows duplicate values
4. Supports multiple data types
5. Supports indexing and slicing

Advantages
- Faster than lists.
- Memory efficient.
- Safe for fixed data.
- Hashable (when elements are immutable).

Disadvantages
- Cannot add, remove or update elements.
- Fewer built-in methods compared to lists.

Syntax:
tuple_name = (element1, element2, element3)
"""

# Creating Tuples

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)


# Tuple Without Parentheses

numbers = 10, 20, 30

print(numbers)

# Output:
# (10, 20, 30)


# Empty Tuple

empty_tuple = ()

print(empty_tuple)

# Output:
# ()


# Single Element Tuple

number = (10,)

print(number)

# Output:
# (10,)


# Common Mistake

number = (10)

print(type(number))

# Output:
# <class 'int'>

"""
Without a comma, Python treats it as an integer, not a tuple.
"""


# Tuple with Different Data Types

mixed = (10, 3.14, "Python", True)

print(mixed)

# Output:
# (10, 3.14, 'Python', True)


# Nested Tuple

student = (
    ("Rahul", 20),
    ("Aman", 21),
    ("Priya", 19)
)

print(student)

# Output:
# (('Rahul', 20), ('Aman', 21), ('Priya', 19))


# Creating Tuples Using tuple()

letters = tuple("Python")

print(letters)

# Output:
# ('P', 'y', 't', 'h', 'o', 'n')


# Accessing Elements

fruits = ("Apple", "Banana", "Mango", "Orange")

print(fruits[0])
print(fruits[2])

# Output:
# Apple
# Mango


# Negative Indexing

print(fruits[-1])
print(fruits[-2])

# Output:
# Orange
# Mango


# Tuple Slicing

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])

# Output:
# (20, 30, 40)

print(numbers[:3])

# Output:
# (10, 20, 30)

print(numbers[3:])

# Output:
# (40, 50, 60)

print(numbers[::-1])

# Output:
# (60, 50, 40, 30, 20, 10)

# Traversing a Tuple Using a for Loop

colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)

# Output:
# Red
# Green
# Blue


# Traversing a Tuple Using a while Loop

colors = ("Red", "Green", "Blue")

index = 0

while index < len(colors):
    print(colors[index])
    index += 1

# Output:
# Red
# Green
# Blue


# Traversing Using enumerate()

students = ("Rahul", "Aman", "Priya")

for index, student in enumerate(students):
    print(index, student)

# Output:
# 0 Rahul
# 1 Aman
# 2 Priya


# Tuple Concatenation

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

# Output:
# (1, 2, 3, 4, 5, 6)


# Tuple Repetition

numbers = (1, 2, 3)

print(numbers * 3)

# Output:
# (1, 2, 3, 1, 2, 3, 1, 2, 3)


# Membership Operator (in)

numbers = (10, 20, 30, 40)

print(20 in numbers)

# Output:
# True


# Membership Operator (not in)

print(100 not in numbers)

# Output:
# True


# Built-in Function: len()

numbers = (10, 20, 30, 40, 50)

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


# Built-in Function: sorted()

numbers = (50, 10, 40, 20, 30)

print(sorted(numbers))

# Output:
# [10, 20, 30, 40, 50]

"""
sorted() always returns a list.
"""


# Built-in Function: reversed()

numbers = (10, 20, 30, 40)

print(tuple(reversed(numbers)))

# Output:
# (40, 30, 20, 10)


# Built-in Function: any()

values = (0, False, "", 5)

print(any(values))

# Output:
# True


# Built-in Function: all()

values = (10, 20, 30)

print(all(values))

# Output:
# True

values = (10, 0, 30)

print(all(values))

# Output:
# False


# Tuple Packing

student = "Rahul", 20, "Mumbai"

print(student)

# Output:
# ('Rahul', 20, 'Mumbai')


# Tuple Unpacking

student = ("Rahul", 20, "Mumbai")

name, age, city = student

print(name)
print(age)
print(city)

# Output:
# Rahul
# 20
# Mumbai


# Extended Unpacking

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50


"""
# Tuple Immutability
Tuples are immutable, which means their elements cannot
be changed after creation.
"""

numbers = (10, 20, 30)

# numbers[0] = 100

# Output:
# TypeError:
# 'tuple' object does not support item assignment


# Modifying a Tuple (Workaround)

numbers = (10, 20, 30)

temp = list(numbers)

temp[0] = 100

numbers = tuple(temp)

print(numbers)

# Output:
# (100, 20, 30)



"""
# count()
Returns the number of occurrences of a specified element.

Syntax:
tuple.count(element)
"""

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

# Output:
# 3


"""
# index()
Returns the index of the first occurrence of an element.

Syntax:
tuple.index(element)
"""

numbers = (10, 20, 30, 40)

print(numbers.index(30))

# Output:
# 2


# index() - Common Mistake

numbers = (10, 20, 30)

# print(numbers.index(100))

# Output:
# ValueError:
# tuple.index(x): x not in tuple


# Comparing Tuples

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

print(tuple1 == tuple2)
print(tuple1 < tuple2)
print(tuple1 > tuple2)

# Output:
# False
# True
# False


# Nested Tuple

students = (
    ("Rahul", 85),
    ("Aman", 90),
    ("Priya", 95)
)

print(students[1])

# Output:
# ('Aman', 90)

print(students[2][1])

# Output:
# 95


"""
# Time Complexity

+--------------------------+---------------+
| Operation                | Complexity    |
+--------------------------+---------------+
| Indexing                 | O(1)          |
| Traversing               | O(n)          |
| Search (in)              | O(n)          |
| count()                  | O(n)          |
| index()                  | O(n)          |
| Concatenation (+)        | O(n)          |
| Repetition (*)           | O(n)          |
| Slicing                  | O(k)          |
+--------------------------+---------------+
"""


"""
# Common Mistakes

1. Forgetting the comma in a single-element tuple.

number = (10)

Correct:

number = (10,)


2. Trying to modify a tuple.

numbers[0] = 100

Raises:
TypeError


3. Assuming sorted() returns a tuple.

sorted(tuple)

Returns a LIST.


4. Accessing an invalid index.

Raises:
IndexError
"""


"""
# Best Practices
1. Use tuples when data should not change.
2. Use tuples for fixed records.
3. Prefer tuples over lists for better memory efficiency.
4. Use packing and unpacking to write cleaner code.
5. Use meaningful variable names.
6. Use tuples as dictionary keys only when all elements inside the tuple are immutable.
"""


"""
# Quick Revision
1. Tuples are ordered.
2. Tuples are immutable.
3. Tuples allow duplicate values.
4. Tuples support indexing and slicing.
5. A single-element tuple must contain a comma.
6. Tuple methods:
   count()
   index()
7. Tuples support:
   +
   *
   in
   not in
8. Built-in Functions:
   len()
   max()
   min()
   sum()
   sorted()
   reversed()
   any()
   all()
9. Packing combines values into a tuple.
10. Unpacking extracts values from a tuple.
11. Tuples are generally faster and more memory-efficient than lists.
"""