"""
LISTS IN PYTHON (PART 2 - LIST METHODS)

Definition

Python provides several built-in methods that allow us to add,
remove, search, sort, copy, and manipulate list elements.

Why Learn List Methods?
1. Simplifies list manipulation.
2. Reduces the amount of code.
3. Makes programs more readable.
4. Improves productivity.

Categories of List Methods
1. Adding Elements
2. Removing Elements
3. Searching Elements
4. Ordering Elements
5. Copying Lists
"""

"""
# append()
Adds a single element at the end of the list.

Syntax: list.append(element)
"""

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# Output:
# [10, 20, 30, 40]


# append() with Different Data Types

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

# Output: ['Apple', 'Banana', 'Mango']


# append() with a List

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)

# Output: [1, 2, 3, [4, 5]]

# Notice that append() inserts the entire list as a single element.


"""
# extend()
Adds all elements from another iterable.

Syntax:list.extend(iterable)
"""

numbers = [10, 20]

numbers.extend([30, 40, 50])

print(numbers)

# Output: [10, 20, 30, 40, 50]


# extend() with a Tuple

numbers = [1, 2]

numbers.extend((3, 4))

print(numbers)

# Output: [1, 2, 3, 4]


# extend() with a String

letters = ["A", "B"]

letters.extend("CD")

print(letters)

# Output: ['A', 'B', 'C', 'D']


# Difference Between append() and extend()

list1 = [1, 2]

list1.append([3, 4])

print(list1)

# Output: [1, 2, [3, 4]]

list2 = [1, 2]

list2.extend([3, 4])

print(list2)

# Output: [1, 2, 3, 4]


"""
# insert()
Inserts an element at a specified position.

Syntax: list.insert(index, element)
"""

numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)

# Output:  [10, 20, 30, 40]


# insert() at the Beginning

numbers = [20, 30]

numbers.insert(0, 10)

print(numbers)

# Output:
# [10, 20, 30]


# insert() Beyond the Last Index

numbers = [10, 20]

numbers.insert(100, 30)

print(numbers)

# Output: [10, 20, 30]


"""
# remove()
Removes the first occurrence of the specified element.

Syntax: list.remove(element)
Raises: ValueError if the element is not found.
"""

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)

# Output: [10, 30, 20, 40]


# remove() with Strings

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

# Output: ['Apple', 'Mango']


# remove() - Common Mistake

numbers = [10, 20, 30]

# numbers.remove(100)

# Output: ValueError: list.remove(x): x not in list


"""
# pop()
Removes and returns an element.

Syntax: list.pop(index)
If no index is provided, the last element is removed.
"""

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print(removed)
print(numbers)

# Output:
# 40
# [10, 20, 30]


# pop() Using an Index

numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print(removed)
print(numbers)

# Output:
# 20
# [10, 30, 40]


# pop() - Common Mistake

numbers = [10, 20]

# numbers.pop(10)

# Output:
# IndexError: pop index out of range



"""
# clear()
Removes all elements from the list.

Syntax: list.clear()
"""

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

# Output: []


"""
# del Statement

The del statement removes elements using an index
or deletes the entire list.
"""

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

# Output: [10, 30, 40]

# Deleting a Slice

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

# Output: [10, 50]


# Deleting an Entire List

numbers = [10, 20, 30]

del numbers

# print(numbers)

# Output:
# NameError:
# name 'numbers' is not defined


"""
# index()
Returns the index of the first occurrence of an element.

Syntax: list.index(element)
"""

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))

# Output: 1


# index() - Common Mistake

numbers = [10, 20, 30]

# print(numbers.index(100))

# Output:
# ValueError:
# 100 is not in list



"""
# count()
Returns the number of times an element appears.

Syntax: list.count(element)
"""

numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))

# Output: 3


# count() with Strings

fruits = ["Apple", "Banana", "Apple", "Orange"]

print(fruits.count("Apple"))

# Output: 2


"""
# sort()
Sorts the list in ascending order by default.

Syntax: list.sort()
Note: The original list is modified.
"""

numbers = [40, 10, 50, 20, 30]

numbers.sort()

print(numbers)

# Output: [10, 20, 30, 40, 50]


# sort() in Descending Order

numbers = [40, 10, 50, 20, 30]

numbers.sort(reverse=True)

print(numbers)

# Output:
# [50, 40, 30, 20, 10]


# sort() with Strings

fruits = ["Mango", "Apple", "Orange", "Banana"]

fruits.sort()

print(fruits)

# Output: ['Apple', 'Banana', 'Mango', 'Orange']


# sort() - Common Mistake

numbers = [3, 2, 1]

result = numbers.sort()

print(result)

# Output: None

# sort() modifies the original list. 
# It does not return a new list.



"""
# reverse()
Reverses the order of elements in the list.

Syntax: list.reverse()
"""

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# Output:  [40, 30, 20, 10]

"""
# copy()
Creates a shallow copy of a list.

Syntax: list.copy()
"""

numbers = [10, 20, 30]

copied = numbers.copy()

print(copied)

# Output: [10, 20, 30]

"""
# List Aliasing :
Aliasing means two variables refer to the same list object.
"""

list1 = [10, 20, 30]

list2 = list1

list2.append(40)

print(list1)
print(list2)

# Output:
# [10, 20, 30, 40]
# [10, 20, 30, 40]

# Changing one variable also changes the other because both point to the same list.


# Shallow Copy

list1 = [10, 20, 30]
list2 = list1.copy()
list2.append(40)

print(list1)
print(list2)

# Output:
# [10, 20, 30]
# [10, 20, 30, 40]

"""
A shallow copy creates a new list object.
Changes made to one list do not affect the other.
"""


# Nested Lists

students = [
    ["Rahul", 85],
    ["Aman", 90],
    ["Priya", 95]
]

print(students)

# Output: [['Rahul', 85], ['Aman', 90], ['Priya', 95]]


# Accessing Nested List Elements

print(students[0][0])
print(students[2][1])

# Output:
# Rahul
# 95


# 2D List (Matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# Output:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Traversing a 2D List

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# 3D List

cube = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print(cube)

# Output: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

"""
# Deep Copy

A deep copy creates a completely independent copy of a list,
including all nested lists.

Syntax:
import copy

copy.deepcopy(list)
"""

import copy

list1 = [
    [10, 20],
    [30, 40]
]

list2 = copy.deepcopy(list1)

list2[0][0] = 100

print(list1)
print(list2)

# Output:
# [[10, 20], [30, 40]]
# [[100, 20], [30, 40]]


# Shallow Copy vs Deep Copy

nested = [
    [1, 2],
    [3, 4]
]

shallow = nested.copy()
deep = copy.deepcopy(nested)

shallow[0][0] = 99

print("Original :", nested)
print("Shallow :", shallow)
print("Deep :", deep)

# Output:
# Original : [[99, 2], [3, 4]]
# Shallow : [[99, 2], [3, 4]]
# Deep : [[1, 2], [3, 4]]

"""
# Time Complexity of Common List Operations

+----------------------+----------------+
| Operation            | Complexity     |
+----------------------+----------------+
| Indexing             | O(1)           |
| Updating             | O(1)           |
| Append               | O(1) Average   |
| Insert               | O(n)           |
| Remove               | O(n)           |
| Pop (Last)           | O(1)           |
| Pop (Middle)         | O(n)           |
| Search (in/index)    | O(n)           |
| Count                | O(n)           |
| Sort                 | O(n log n)     |
| Reverse              | O(n)           |
| Copy                 | O(n)           |
+----------------------+----------------+
"""


"""
# Common Mistakes

1. Confusing append() and extend().

append([4, 5])

Result:
[1, 2, 3, [4, 5]]

extend([4, 5])

Result:
[1, 2, 3, 4, 5]


2. Assuming sort() returns a new list.

numbers.sort()

Correct

sorted_numbers = sorted(numbers)

Also Correct


3. Using remove() for an element that doesn't exist.

Raises:
ValueError


4. Forgetting that aliasing points to the same object.


5. Using shallow copy for nested lists.
"""

"""
# Best Practices

1. Use append() for adding a single element.
2. Use extend() for adding multiple elements.
3. Use remove() only when the element is known to exist.
4. Use pop() when you need the removed value.
5. Prefer sorted() if you need a new sorted list.
6. Use copy() instead of assignment when creating another list.
7. Use deepcopy() for nested lists.
8. Avoid unnecessary nested lists if a simpler structure works.
"""

"""
# Quick Revision

Adding Methods:
append()
extend()
insert()

Removing Methods :
remove()
pop()
clear()
del

Searching Methods : 
index()
count()

Ordering Methods : 
sort()
reverse()

Copying : 
copy()
shallow copy
deep copy

Other Concepts : 
nested lists
2D lists
3D lists
aliasing

Important Difference : 
append() -> Adds one element
extend() -> Adds multiple elements
copy() -> Creates a shallow copy
deepcopy() -> Creates a completely independent copy
"""