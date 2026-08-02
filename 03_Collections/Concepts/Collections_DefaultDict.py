""" ================ defaultdict ===================="""

"""
# defaultdict

defaultdict is a dictionary subclass that automatically
creates a default value for a missing key instead of
raising a KeyError.

It requires a default factory function that specifies
the default value for new keys.

Syntax:
defaultdict(default_factory)

Applications
- Counting Frequencies
- Grouping Data
- Building Dictionaries of Lists
- Graph Representations
- Adjacency Lists
"""

from collections import defaultdict


"""
# defaultdict(int)

int() returns 0 as the default value.
"""

marks = defaultdict(int)

marks["Maths"] += 10
marks["Physics"] += 15

print(marks)

# Output:
# defaultdict(<class 'int'>,
# {'Maths': 10, 'Physics': 15})

# Accessing a Missing Key

marks = defaultdict(int)

print(marks["Chemistry"])

# Output:
# 0

"""
Unlike a normal dictionary, defaultdict does not raise a KeyError for missing keys.
"""



# defaultdict(list) : list() creates an empty list for every new key.

students = defaultdict(list)

students["Rahul"].append("Maths")
students["Rahul"].append("Physics")

students["Aman"].append("Chemistry")

print(students)

# Output:
# defaultdict(<class 'list'>,
# {'Rahul': ['Maths', 'Physics'],
#  'Aman': ['Chemistry']})

# Grouping Data Using defaultdict(list)

employees = [
    ("IT", "Rahul"),
    ("HR", "Aman"),
    ("IT", "Priya"),
    ("Sales", "Rohan")
]

departments = defaultdict(list)

for department, employee in employees:
    departments[department].append(employee)

print(departments)

# Output:
# defaultdict(<class 'list'>,
# {'IT': ['Rahul', 'Priya'],
#  'HR': ['Aman'],
#  'Sales': ['Rohan']})


# defaultdict(set) : set() creates an empty set for every new key.

subjects = defaultdict(set)

subjects["Rahul"].add("Maths")
subjects["Rahul"].add("Physics")
subjects["Rahul"].add("Maths")

print(subjects)

# Output:
# defaultdict(<class 'set'>,
# {'Rahul': {'Maths', 'Physics'}})

"""
Duplicate values are automatically removed.
"""

# defaultdict(str) : str() creates an empty string as the default value.

details = defaultdict(str)

print(details["City"])

# Output:
# ''

# defaultdict(float) : float() creates 0.0 as the default value.

accounts = defaultdict(float)

accounts["Rahul"] += 1500.50

print(accounts)

# Output:
# defaultdict(<class 'float'>,
# {'Rahul': 1500.5})


# Using lambda as the Default Factory

students = defaultdict(lambda: "Not Available")

print(students["Rahul"])

# Output:
# Not Available

# Counting Characters

text = "programming"

frequency = defaultdict(int)

for character in text:
    frequency[character] += 1

print(frequency)

# Output:
# defaultdict(<class 'int'>,
# {'p':1,'r':2,'o':1,'g':2,
#  'a':1,'m':2,'i':1,'n':1})

# Counting Words

sentence = "Python is easy and Python is powerful"

frequency = defaultdict(int)

for word in sentence.lower().split():
    frequency[word] += 1

print(frequency)

# Output:
# defaultdict(<class 'int'>,
# {'python':2,
#  'is':2,
#  'easy':1,
#  'and':1,
#  'powerful':1})


# Practical Example - Student Marks

records = [("Rahul", 90),("Rahul", 85),("Aman", 78),("Priya", 95),("Aman", 82)]

marks = defaultdict(list)

for name, mark in records:
    marks[name].append(mark)

print(marks)

# Output:
# defaultdict(<class 'list'>,
# {'Rahul':[90,85],
#  'Aman':[78,82],
#  'Priya':[95]})


# Practical Example - Graph Representation

edges = [("A", "B"),("A", "C"),("B", "D"),("C", "D")]

graph = defaultdict(list)

for source, destination in edges:
    graph[source].append(destination)

print(graph)

# Output:
# defaultdict(<class 'list'>,
# {'A':['B','C'],
#  'B':['D'],
#  'C':['D']})

"""
This representation is called an Adjacency List and is widely used in Graph algorithms.
"""

# ===============================x=================================