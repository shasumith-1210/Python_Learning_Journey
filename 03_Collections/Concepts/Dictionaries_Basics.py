"""
DICTIONARIES IN PYTHON

Definition:

A dictionary is a mutable collection that stores data as
key-value pairs.

Each key is unique and is used to access its corresponding value.

Unlike lists and tuples, dictionaries store data using keys
instead of indexes.

Why Learn Dictionaries?
1. Store related information together.
2. Fast lookup using keys.
3. Represent real-world objects easily.
4. Widely used in APIs, JSON, databases, and applications.

Characteristics
1. Mutable
2. Ordered (Python 3.7+)
3. Stores data as key-value pairs
4. Keys must be unique
5. Keys must be immutable
6. Values can be of any data type

Advantages
1. Fast searching using keys.
2. Easy to update values.
3. Flexible data storage.
4. Efficient for mapping relationships.

Disadvantages
1. Cannot have duplicate keys.
2. Mutable keys (like lists) are not allowed.
3. Uses more memory than lists.

Syntax
dictionary = {
    key1: value1,
    key2: value2
}
"""

# Creating a Dictionary

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

print(student)

# Output: {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


# Empty Dictionary

student = {}

print(student)

# Output: {}


# Creating Dictionary Using dict()

student = dict( name="Rahul", age=20, city="Mumbai" )

print(student)

# Output: {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


# Dictionary with Mixed Data Types

employee = {"id": 101,"name": "Aman","salary": 45000,"is_active": True}

print(employee)

# Output: {'id': 101, 'name': 'Aman', 'salary': 45000, 'is_active': True}


# Duplicate Keys
# The last value replaces the previous one.

student = {"name": "Rahul","name": "Aman","age": 20 }

print(student)

# Output:
# {'name': 'Aman', 'age': 20}


# Valid Dictionary Keys

data = { 1: "Integer", 3.14: "Float", True: "Boolean", (1, 2): "Tuple" }

print(data)

# Output: Order may vary

"""
# Invalid Dictionary Key
Lists cannot be dictionary keys.

Example:
data = { [1, 2]: "List" }

Raises: TypeError
"""


# Accessing Values Using Keys

student = {"name": "Rahul", "age": 20, "city": "Mumbai"}

print(student["name"])
print(student["age"])

# Output:
# Rahul
# 20


# Accessing a Missing Key

student = {"name": "Rahul"}

# print(student["city"])

# Output: KeyError


"""
# get()

Returns the value of the specified key.

If the key is not found, returns None by default.

Syntax: dictionary.get(key)
"""

student = {"name": "Rahul","age": 20}

print(student.get("name"))

# Output: Rahul

print(student.get("city"))

# Output: None


# get() with Default Value

student = {"name": "Rahul"}

print(student.get("city", "Not Available"))

# Output: Not Available


# Adding New Key-Value Pair

student = {"name": "Rahul", "age": 20}

student["city"] = "Mumbai"

print(student)

# Output: {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


# Updating Existing Value

student = {"name": "Rahul","age": 20 }

student["age"] = 21

print(student)

# Output: {'name': 'Rahul', 'age': 21}


# Dictionary Length

student = {"name": "Rahul", "age": 20, "city": "Mumbai"}

print(len(student))

# Output: 3


# Traversing a Dictionary (Keys)

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

for key in student:
    print(key)

# Output:
# name
# age
# city


# Traversing Keys and Values

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

for key in student:
    print(key, ":", student[key])

# Output:
# name : Rahul
# age : 20
# city : Mumbai


"""
# keys()

Returns a view object containing all keys.

Syntax: dictionary.keys()
"""

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

print(student.keys())

# Output: dict_keys(['name', 'age', 'city'])


"""
# values()

Returns a view object containing all values.

Syntax: dictionary.values()
"""

print(student.values())

# Output: dict_values(['Rahul', 20, 'Mumbai'])


"""
# items()

Returns key-value pairs as tuples.

Syntax: dictionary.items()
"""

print(student.items())

# Output: dict_items([('name', 'Rahul'), ('age', 20), ('city', 'Mumbai')])


# Traversing Using items()

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Rahul
# age : 20
# city : Mumbai


# Membership Operator (in)

student = {"name": "Rahul","age": 20}

print("name" in student)

# Output: True


# Membership Operator (not in)

print("city" not in student)

# Output: True


"""
# pop()

Removes the specified key and returns its value.

Syntax: dictionary.pop(key)
"""

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

removed = student.pop("city")

print(removed)
print(student)

# Output:
# Mumbai
# {'name': 'Rahul', 'age': 20}


# pop() with Default Value

student = {"name": "Rahul"}

print(student.pop("city", "Key Not Found"))

# Output: Key Not Found


"""
# popitem()

Removes and returns the last inserted key-value pair.

Syntax: dictionary.popitem()
"""

student = {"name": "Rahul","age": 20,"city": "Mumbai"}

print(student.popitem())

# Output: ('city', 'Mumbai')

print(student)

# Output: {'name': 'Rahul', 'age': 20}


"""
# clear()

Removes all key-value pairs.

Syntax: dictionary.clear()
"""

student = { "name": "Rahul", "age": 20 }

student.clear()

print(student)

# Output: {}


"""
# copy()

Creates a shallow copy of the dictionary.

Syntax: dictionary.copy()
"""

student = {"name": "Rahul","age": 20}

student_copy = student.copy()

print(student_copy)

# Output: {'name': 'Rahul', 'age': 20}


# Copy Independence

student = {"name": "Rahul","age": 20}

student_copy = student.copy()

student_copy["city"] = "Mumbai"

print(student)
print(student_copy)

# Output:
# {'name': 'Rahul', 'age': 20}
# {'name': 'Rahul', 'age': 20, 'city': 'Mumbai'}


"""
# fromkeys()

Creates a new dictionary with specified keys and a common default value.

Syntax: dict.fromkeys(keys, value)
"""

subjects = ["Maths", "Physics", "Chemistry"]

marks = dict.fromkeys(subjects, 0)

print(marks)

# Output:
# {'Maths': 0, 'Physics': 0, 'Chemistry': 0}


"""
# setdefault()

Returns the value of the specified key.

If the key does not exist, it inserts the key with
the given default value.

Syntax: dictionary.setdefault(key, default_value)
"""

student = {"name": "Rahul", "age": 20}

print(student.setdefault("age", 18))

# Output: 20

print(student)

# Output: {'name': 'Rahul', 'age': 20}


# setdefault() - New Key

student = {"name": "Rahul"}

print(student.setdefault("city", "Mumbai"))

# Output: Mumbai

print(student)

# Output: {'name': 'Rahul', 'city': 'Mumbai'}


# max()
# max() works on dictionary keys.

marks = {"Maths": 95,"Physics": 88,"Chemistry": 92}

print(max(marks))

# Output:
# Physics

"""

"""


# ---------------------------------------------------------
# min()

print(min(marks))

# Output: Chemistry


# sorted()

print(sorted(marks))

# Output: ['Chemistry', 'Maths', 'Physics']


# any()

data = {"a": 1, "b": 2}

print(any(data))

# Output: True


# all()

print(all(data))

# Output: True

data = {"": 10,"b": 20}

print(all(data))

# Output:
# False


# Nested Dictionary

students = {
    101: {"name": "Rahul","age": 20},
    102: { "name": "Aman", "age": 21}
}

print(students)

# Output:
# {101: {'name': 'Rahul', 'age': 20}, 102: {'name': 'Aman', 'age': 21}}


# Accessing Nested Dictionary

print(students[101]["name"])

# Output: Rahul

print(students[102]["age"])

# Output: 21


# Practical Example - Student Marks

marks = {"Maths": 95,"Physics": 88,"Chemistry": 91}

for subject, mark in marks.items():
    print(subject, ":", mark)

# Output:
# Maths : 95
# Physics : 88
# Chemistry : 91


# Practical Example - Word Frequency

sentence = "python is easy and python is powerful"

frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Output: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}


"""
# Time Complexity

+--------------------------+---------------+
| Operation                | Complexity    |
+--------------------------+---------------+
| Access by Key            | O(1) Average  |
| Insert                   | O(1) Average  |
| Update                   | O(1) Average  |
| Delete                   | O(1) Average  |
| Search by Key            | O(1) Average  |
| keys()                   | O(1)          |
| values()                 | O(1)          |
| items()                  | O(1)          |
| Traversal                | O(n)          |
| Copy                     | O(n)          |
+--------------------------+---------------+
"""


"""
# Common Mistakes

1. Accessing a missing key.

student["city"]

Raises: KeyError

Use get() if the key may not exist.


2. Using mutable objects as keys.

data = {[1, 2]: "List"}

Raises: TypeError


3. Assuming duplicate keys are stored.

Only the last value is kept.


4. Forgetting that dictionaries use keys,
not indexes.

student[0]

Raises: KeyError
"""

"""
# Quick Revision

1. Use meaningful key names.
2. Use get() when the key may not exist.
3. Use items() when both keys and values are needed.
4. Use copy() before modifying a dictionary copy.
5. Keep keys immutable.
6. Use nested dictionaries for structured data.
7. Avoid duplicate keys.
"""



"""
# Quick Revision :
1. Dictionaries store data as key-value pairs.
2. Dictionaries are mutable.
3. Keys must be unique.
4. Values can be duplicated.

# Main Methods :
get()
keys()
values()
items()
pop()
popitem()
clear()
copy()
fromkeys()
setdefault()

# Built-in Functions :
len()
max()
min()
sorted()
any()
all()

# Dictionaries are best suited for:
1. Fast lookup
2. Mapping data
3. Configuration settings
4. JSON-like data
5. Student records
6. Employee records
"""