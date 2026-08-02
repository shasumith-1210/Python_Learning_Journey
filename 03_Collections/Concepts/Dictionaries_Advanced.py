"""
ADVANCED DICTIONARIES IN PYTHON

Definition
----------
This module covers advanced dictionary features that are widely
used in real-world Python applications.

Topics Covered
--------------
- update()
- del
- Dictionary Merge
- Dictionary Comprehension
- Sorting Dictionaries
- Shallow Copy
- Deep Copy
- collections.defaultdict
- collections.OrderedDict
- collections.ChainMap
- collections.Counter

These concepts make dictionary programming cleaner,
shorter and more efficient.
"""


"""
# update()

Adds new key-value pairs or updates existing ones.

Syntax:
dictionary.update(other_dictionary)
"""

student = {"name": "Rahul","age": 20}

student.update({"city": "Mumbai","age": 21})

print(student)

# Output:
# {'name': 'Rahul', 'age': 21, 'city': 'Mumbai'}


# update() Using Keyword Arguments

student = {
    "name": "Rahul"
}

student.update(age=20, city="Mumbai")

print(student)

# Output: {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


"""
# del Statement

Deletes a specific key-value pair.

Syntax:
del dictionary[key]
"""

student = {"name": "Rahul", "age": 20, "city": "Mumbai"}

del student["city"]

print(student)

# Output:
# {'name': 'Rahul', 'age': 20}


# del - Common Mistake

student = { "name": "Rahul" }

# del student["city"]

# Output:
# KeyError


"""
# Dictionary Merge (Python 3.9+)

The | operator creates a new merged dictionary.
"""

student = {"name": "Rahul"}

details = {"age": 20, "city": "Mumbai"}

merged = student | details

print(merged)

# Output: {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


# Dictionary Merge Assignment (|=)

student = {"name": "Rahul"}

student |= {"age": 20,"city": "Mumbai"}

print(student)

# Output: {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


"""
# Dictionary Comprehension

Creates dictionaries using a concise syntax.

Syntax:

{
    key_expression: value_expression
    for item in iterable
}
"""

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Dictionary Comprehension with Condition

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)

# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# Creating Dictionary from Two Lists

subjects = [ "Maths", "Physics", "Chemistry"]

marks = [95,88,91]

student_marks = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}

print(student_marks)

# Output: {'Maths': 95, 'Physics': 88, 'Chemistry': 91}


# Inverting Keys and Values

student = { "Maths": 95, "Physics": 88, "Chemistry": 91}

reversed_dictionary = {
    value: key
    for key, value in student.items()
}

print(reversed_dictionary)

# Output: {95: 'Maths', 88: 'Physics', 91: 'Chemistry'}


"""
# Sorting Dictionary by Keys

sorted() returns a list of sorted keys.

Syntax:
sorted(dictionary)
"""

student = {"Physics": 88,"Maths": 95,"Chemistry": 91}

print(sorted(student))

# Output:
# ['Chemistry', 'Maths', 'Physics']


# Sorting Dictionary by Keys (Ascending)

student = {"Physics": 88,"Maths": 95,"Chemistry": 91}

sorted_student = dict(sorted(student.items()))

print(sorted_student)

# Output:
# {'Chemistry': 91, 'Maths': 95, 'Physics': 88}


# Sorting Dictionary by Keys (Descending)

sorted_student = dict( sorted(student.items(), reverse=True) )

print(sorted_student)

# Output:
# {'Physics': 88, 'Maths': 95, 'Chemistry': 91}


"""
# Sorting Dictionary by Values

Sort using the value of each key-value pair.

key=lambda item: item[1]
"""

student = { "Maths": 95, "Physics": 88, "Chemistry": 91 }

sorted_by_marks = dict(sorted( student.items(), key=lambda item: item[1]))

print(sorted_by_marks)

# Output:
# {'Physics': 88, 'Chemistry': 91, 'Maths': 95}


# Sorting Dictionary by Values (Descending)

sorted_by_marks = dict(
    sorted(
        student.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

print(sorted_by_marks)

# Output:
# {'Maths': 95, 'Chemistry': 91, 'Physics': 88}



"""
# copy() (Shallow Copy)

Creates a shallow copy.

Nested mutable objects are still shared.
"""

student = {
    "name": "Rahul",
    "marks": [90, 95, 88]
}

student_copy = student.copy()

student_copy["marks"][0] = 100

print(student)
print(student_copy)

# Output:
# {'name': 'Rahul', 'marks': [100, 95, 88]}
# {'name': 'Rahul', 'marks': [100, 95, 88]}



"""
# Deep Copy

deepcopy() creates a completely independent copy.

Syntax:
copy.deepcopy(object)
"""

import copy

student = {
    "name": "Rahul",
    "marks": [90, 95, 88]
}

student_copy = copy.deepcopy(student)

student_copy["marks"][0] = 100

print(student)
print(student_copy)

# Output:
# {'name': 'Rahul', 'marks': [90, 95, 88]}
# {'name': 'Rahul', 'marks': [100, 95, 88]}


# Shallow Copy vs Deep Copy

data = {
    "numbers": [1, 2, 3]
}

shallow = data.copy()
deep = copy.deepcopy(data)

shallow["numbers"][0] = 99

print("Original :", data)
print("Shallow :", shallow)
print("Deep :", deep)

# Output:
# Original : {'numbers': [99, 2, 3]}
# Shallow : {'numbers': [99, 2, 3]}
# Deep : {'numbers': [1, 2, 3]}



"""
# defaultdict

defaultdict automatically creates a default value
for missing keys.

Syntax:
defaultdict(default_factory)
"""

from collections import defaultdict

student = defaultdict(int)

student["Maths"] += 10
student["Physics"] += 5

print(student)

# Output:
# defaultdict(<class 'int'>, # {'Maths': 10, 'Physics': 5})

# defaultdict(list)

subjects = defaultdict(list)

subjects["Rahul"].append("Maths")
subjects["Rahul"].append("Physics")
subjects["Aman"].append("Chemistry")

print(subjects)

# Output:
# defaultdict(<class 'list'>, {'Rahul': ['Maths', 'Physics'], 'Aman': ['Chemistry']})


# defaultdict(str)

details = defaultdict(str)

print(details["city"])

# Output: ''

# Practical Example - Counting Characters

from collections import defaultdict

text = "programming"

frequency = defaultdict(int)

for character in text:
    frequency[character] += 1

print(dict(frequency))

# Output:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2,
#  'a': 1, 'm': 2, 'i': 1, 'n': 1}


"""
# OrderedDict

OrderedDict is a dictionary subclass that remembers the
insertion order of keys.

From Python 3.7 onwards, the built-in dictionary also
preserves insertion order, but OrderedDict still provides
additional methods.

Syntax:
from collections import OrderedDict
"""

from collections import OrderedDict

student = OrderedDict()

student["name"] = "Rahul"
student["age"] = 20
student["city"] = "Mumbai"

print(student)

# Output:
# OrderedDict([
# ('name', 'Rahul'),
# ('age', 20),
# ('city', 'Mumbai')
# ])



"""
# move_to_end()

Moves an existing key to either the end or beginning.

Syntax:
move_to_end(key, last=True)
"""

student = OrderedDict({"A": 1,"B": 2,"C": 3
})

student.move_to_end("A")

print(student)

# Output:
# OrderedDict([ ('B', 2), ('C', 3), ('A', 1) ])


# move_to_end(last=False)

student = OrderedDict({"A": 1,"B": 2,"C": 3})

student.move_to_end("C", last=False)

print(student)

# Output:
# OrderedDict([ ('C', 3), ('A', 1), ('B', 2) ])



"""
# popitem()

OrderedDict allows removing from either end.

Syntax:
popitem(last=True)
"""

student = OrderedDict({"A": 1, "B": 2, "C": 3 })

print(student.popitem())

# Output:
# ('C', 3)

print(student)

# Output:
# OrderedDict([('A', 1), ('B', 2)])


# popitem(last=False)

student = OrderedDict({"A": 1,"B": 2,"C": 3
})

print(student.popitem(last=False))

# Output:
# ('A', 1)



"""
# ChainMap

ChainMap groups multiple dictionaries into a single view.

Syntax:
from collections import ChainMap
"""

from collections import ChainMap

student = {"name": "Rahul"}

details = {"age": 20,"city": "Mumbai"}

combined = ChainMap(student, details)

print(combined["name"])
print(combined["city"])

# Output:
# Rahul
# Mumbai


# ChainMap Example

defaults = {"theme": "Light","language": "English"}

user = {"theme": "Dark"}

settings = ChainMap(user, defaults)

print(settings["theme"])
print(settings["language"])

# Output:
# Dark
# English


"""
# Counter
Counter counts the frequency of elements.

Syntax:
from collections import Counter
"""

from collections import Counter

numbers = [1, 2, 1, 3, 2, 1]

counter = Counter(numbers)

print(counter)

# Output:
# Counter({1: 3, 2: 2, 3: 1})


# Counter with String

text = "banana"

counter = Counter(text)

print(counter)

# Output:
# Counter({'a': 3, 'n': 2, 'b': 1})


# most_common()

marks = ["Maths", "Physics", "Maths", "English", "Maths", "Physics"]

counter = Counter(marks)

print(counter.most_common(2))

# Output:
# [('Maths', 3), ('Physics', 2)]


# elements()

counter = Counter({
    "A": 2,
    "B": 3
})

print(list(counter.elements()))

# Output:
# ['A', 'A', 'B', 'B', 'B']


# Practical Example - Word Frequency

sentence = """
Python is easy.
Python is powerful.
Python is popular.
"""

words = sentence.lower().split()

counter = Counter(words)

print(counter)

# Output:
# Frequency of each word



"""
# Time Complexity


+--------------------------------------+---------------+
| Operation                            | Complexity    |
+--------------------------------------+---------------+
| Access by Key                        | O(1) Average  |
| Insert                               | O(1) Average  |
| Delete                               | O(1) Average  |
| Search                               | O(1) Average  |
| Traversal                            | O(n)          |
| Sorting                              | O(n log n)    |
| Dictionary Comprehension             | O(n)          |
| Shallow Copy                         | O(n)          |
| Deep Copy                            | O(n)          |
| Counter Creation                     | O(n)          |
| defaultdict Access                   | O(1)          |
+--------------------------------------+---------------+
"""


"""
# Common Mistakes

1. Assuming copy() copies nested objects.

Use deepcopy() for nested dictionaries.


2. Using defaultdict without understanding
its default value.

defaultdict(int)

Returns 0 for missing keys.


3. Forgetting that Counter is a dictionary.

Counter supports most dictionary operations.


4. Using OrderedDict when a normal dictionary
is sufficient.

Python 3.7+ dictionaries already preserve
insertion order.


5. Assuming dictionary sorting modifies
the original dictionary.

sorted() returns a new object.
"""

"""
# Best Practices

1. Use dictionary comprehensions for concise code.
2. Use defaultdict when handling missing keys.
3. Use Counter for frequency counting.
4. Use ChainMap when working with multiple configuration dictionaries.
5. Use deepcopy() for nested mutable objects.
6. Prefer normal dictionaries unless OrderedDict features are specifically required.
7. Keep dictionary keys immutable.
"""


"""
# Quick Revision

✓ Advanced Dictionary Features
------------------------------

update()
del
Dictionary Merge (|)
Merge Assignment (|=)

✓ Dictionary Comprehension

✓ Sorting
----------
By Keys
By Values

✓ Copying
----------
copy()
deepcopy()

✓ collections Module
--------------------
defaultdict
OrderedDict
ChainMap
Counter

✓ Best Uses
-----------
Configuration Management

Frequency Counting

Nested Data

JSON Processing

Caching

Grouping Data
"""

