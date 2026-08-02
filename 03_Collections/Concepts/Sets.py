"""
SETS IN PYTHON

Definition:
A set is an unordered, mutable collection of unique elements.

Unlike lists and tuples, sets do not store duplicate values and
do not support indexing because they are unordered.

Sets are mainly used for storing unique data and performing
mathematical set operations such as union and intersection.

Why Learn Sets?
1. Remove duplicate values.
2. Perform fast membership testing.
3. Perform mathematical set operations.
4. Store unique collections of data.

Characteristics:
1. Unordered
2. Mutable
3. Does not allow duplicate values
4. Can store different immutable data types
5. Supports set operations

Advantages
1. Very fast searching.
2. Automatically removes duplicates.
3. Efficient mathematical operations.

Disadvantages
1. No indexing or slicing.
2. Cannot store mutable objects like lists.
3. Order is not guaranteed.

Syntax: set_name = {element1, element2, element3}
"""

# Creating Sets

numbers = {10, 20, 30, 40}

print(numbers)

# Output: {10, 20, 30, 40}


# Empty Set

empty_set = set()

print(empty_set)

# Output: set()

# Using {} creates an empty dictionary, not an empty set.


# Duplicate Elements

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)

# Output: {10, 20, 30, 40}

# Duplicate values are automatically removed.


# Mixed Data Types

mixed = {10, 3.14, "Python", True}

print(mixed)

# Output:
# Order may vary


# Creating a Set Using set()

letters = set("Python")

print(letters)

# Output: Order may vary


# Creating a Set from a List

numbers = [10, 20, 30, 20, 40, 10]

unique_numbers = set(numbers)

print(unique_numbers)

# Output: {10, 20, 30, 40}


# Membership Operators

numbers = {10, 20, 30, 40}

print(20 in numbers)

# Output: True

print(100 not in numbers)

# Output: True


# Traversing a Set

fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)

# Output: Order may vary


# Built-in Functions

numbers = {10, 20, 30, 40, 50}

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# Output:
# 5
# 50
# 10
# 150


# sorted()
# sorted() returns a list.
numbers = {50, 10, 30, 20, 40}

print(sorted(numbers))

# Output: [10, 20, 30, 40, 50]


# any()

values = {0, False, "", 5}

print(any(values))

# Output: True


# all()

values = {10, 20, 30}

print(all(values))

# Output:
# True

values = {10, 0, 30}

print(all(values))

# Output:
# False


"""
# add()
Adds a single element to the set.

Syntax: set.add(element)
"""

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Output: {10, 20, 30, 40}


# add() - Duplicate Element
# Duplicate values are ignored.

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)

# Output: {10, 20, 30}


"""
# update()
# Adds multiple elements to a set.

Syntax: set.update(iterable)
"""

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)

# Output: {10, 20, 30, 40, 50}


# update() with Another Set

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)

print(set1)

# Output: {1, 2, 3, 4, 5}


# update() with Tuple

numbers = {10, 20}

numbers.update((30, 40))

print(numbers)

# Output: {10, 20, 30, 40}


"""
# remove()
Removes the specified element.

Raises KeyError if the element does not exist.

Syntax: set.remove(element)
"""

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

# Output: {10, 30}


# remove() - Common Mistake

numbers = {10, 20}

# numbers.remove(100)

# Output:
# KeyError


"""
# discard()

Removes an element if it exists.

Does NOT raise an error if the element is absent.

Syntax: set.discard(element)
"""

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)

# Output: {10, 30}


# discard() - Missing Element

numbers = {10, 20}

numbers.discard(100)

print(numbers)

# Output: {10, 20}


"""
# remove() vs discard()

remove() : Raises KeyError if the element is not found.
discard() : Does nothing if the element is not found.
"""


"""
# pop()
Removes and returns an arbitrary element.
Since sets are unordered, the removed element cannot be predicted.
"""

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print(removed)
print(numbers)

# Output: Output may vary


# pop() on an Empty Set

numbers = set()

# numbers.pop()

# Output:
# KeyError:
# 'pop from an empty set'


"""
# clear()
Removes all elements from the set.
"""

numbers = {10, 20, 30}

numbers.clear()

print(numbers)

# Output:
# set()


"""
# copy()
# Creates a shallow copy of the set.
"""

set1 = {10, 20, 30}
set2 = set1.copy()

print(set1)
print(set2)

# Output:
# {10, 20, 30}
# {10, 20, 30}


# Copy Independence

set1 = {10, 20, 30}
set2 = set1.copy()
set2.add(40)

print(set1)
print(set2)

# Output:
# {10, 20, 30}
# {10, 20, 30, 40}


"""
# union()
Returns a new set containing all unique elements from both sets.
Syntax: set1.union(set2)
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# Output: {1, 2, 3, 4, 5}


# Union Operator (|)

set1 = {10, 20}
set2 = {20, 30}

print(set1 | set2)

# Output: {10, 20, 30}


"""
# intersection()
Returns common elements present in both sets.

Syntax: set1.intersection(set2)
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))

# Output : {3, 4}


# Intersection Operator (&)

print(set1 & set2)

# Output: {3, 4}



"""
# difference()
Returns elements present in the first set but not in the second.

Syntax: set1.difference(set2)
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

print(set1.difference(set2))

# Output: {1, 2}


# Difference Operator (-)

print(set1 - set2)

# Output: {1, 2}

print(set2 - set1)

# Output: {5}


"""
# symmetric_difference()
Returns elements that are present in either set, but not in both.

Syntax: set1.symmetric_difference(set2)
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.symmetric_difference(set2))

# Output: {1, 2, 4, 5}


# Symmetric Difference Operator (^)

print(set1 ^ set2)

# Output: {1, 2, 4, 5}


"""
# issubset()
# Checks whether all elements of one set are present in another set.

Syntax: set1.issubset(set2)
"""

small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))

# Output: True


"""
# issuperset()
Checks whether a set contains all elements of another set.

Syntax: set1.issuperset(set2)
"""

large = {1, 2, 3, 4}
small = {1, 2}

print(large.issuperset(small))

# Output:
# True


"""
# isdisjoint()
Returns True if both sets have no common elements.

Syntax: set1.isdisjoint(set2)
"""

set1 = {1, 2}
set2 = {3, 4}

print(set1.isdisjoint(set2))

# Output:
# True


"""
# intersection_update()
# Keeps only the common elements.

Modifies the original set.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set1.intersection_update(set2)

print(set1)

# Output:
# {3, 4}


"""
# difference_update()
Removes elements that are present
in another set.
"""

set1 = {1, 2, 3, 4}
set2 = {3, 4}

set1.difference_update(set2)

print(set1)

# Output:
# {1, 2}


"""
# symmetric_difference_update()
Updates the set with elements that are
not common in both sets.
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.symmetric_difference_update(set2)

print(set1)

# Output: {1, 2, 4, 5}


"""
# update() as Union
update() performs an in-place union.
"""

set1 = {1, 2}
set2 = {2, 3, 4}

set1.update(set2)

print(set1)

# Output:
# {1, 2, 3, 4}


"""
# frozenset()
A frozenset is an immutable version of a set.

Once created, elements cannot be added or removed.

Syntax: frozenset(iterable)
"""

numbers = frozenset({10, 20, 30})

print(numbers)

# Output:
# frozenset({10, 20, 30})


# frozenset - Immutability

numbers = frozenset({1, 2, 3})

# numbers.add(4)

# Output:
# AttributeError:
# 'frozenset' object has no attribute 'add'


"""
# Set Comprehension
Creates a new set using a concise syntax.

Syntax:
{expression for item in iterable}
"""

squares = {number ** 2 for number in range(1, 6)}

print(squares)

# Output:
# {1, 4, 9, 16, 25}


# Set Comprehension with Condition

even_numbers = {number for number in range(1, 11) if number % 2 == 0}

print(even_numbers)

# Output:
# {2, 4, 6, 8, 10}


# Practical Example - Remove Duplicates

marks = [85, 90, 85, 78, 90, 95, 78]

unique_marks = list(set(marks))

print(unique_marks)

# Output:
# Order may vary


# Practical Example - Common Subjects

student1 = {"Maths", "Physics", "Chemistry"}

student2 = {"Physics", "English", "Maths"}

common_subjects = student1.intersection(student2)

print(common_subjects)

# Output:
# {'Maths', 'Physics'}


# Practical Example - Unique Subjects

student1 = {"Maths", "Physics", "Chemistry"}

student2 = {"Physics", "English", "Maths"}

print(student1.symmetric_difference(student2))

# Output:
# {'Chemistry', 'English'}



"""
# Time Complexity

+-----------------------------------+---------------+
| Operation                         | Complexity    |
+-----------------------------------+---------------+
| Membership (in)                   | O(1) Average  |
| add()                             | O(1) Average  |
| remove()                          | O(1) Average  |
| discard()                         | O(1) Average  |
| pop()                             | O(1) Average  |
| union()                           | O(len(s)+len(t)) |
| intersection()                    | O(min(s,t))   |
| difference()                      | O(len(s))     |
| symmetric_difference()            | O(len(s)+len(t)) |
| copy()                            | O(n)          |
| clear()                           | O(n)          |
+-----------------------------------+---------------+
"""


"""
# Common Mistakes

1. Creating an empty set using {}.

{}

Creates an empty dictionary.

Correct: set()


2. Expecting a set to maintain insertion order.
Sets are unordered.


3. Trying to access elements using indexing.
numbers[0]

Raises: TypeError


4. Trying to store mutable objects.
{[1, 2], [3, 4]}

Raises: TypeError


5. Using remove() without checking if the element exists.
remove()

Raises: KeyError
Use discard() if unsure.
"""


"""
# Best Practices
1. Use sets when duplicate values should be removed.
2. Use sets for fast searching.
3. Prefer discard() over remove() if an element may not exist.
4. Use frozenset for immutable collections.
5. Use set operations instead of loops whenever possible.
6. Store only immutable objects inside sets.
7. Use meaningful variable names.
"""


"""
# Quick Revision
1. Sets are unordered.
2. Sets are mutable.
3. Duplicate values are automatically removed.
4. Sets do not support indexing.

5. Main Methods
add()
update()
remove()
discard()
pop()
clear()
copy()

6. Set Operations
union()
intersection()
difference()
symmetric_difference()

7. Comparison Methods
issubset()
issuperset()
isdisjoint()

8. In-place Update Methods
intersection_update()
difference_update()
symmetric_difference_update()

9. Special Features
frozenset
Set Comprehension

10. Best Use Cases
- Removing duplicates
- Fast membership testing
- Mathematical set operations
"""