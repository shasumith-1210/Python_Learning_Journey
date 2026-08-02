""" ================== OrderedDict ====================="""

"""
# OrderedDict

OrderedDict is a dictionary subclass that remembers
the insertion order of keys.

Although normal dictionaries (Python 3.7+) also preserve
insertion order, OrderedDict provides additional methods
that are useful in certain situations.

Syntax:
OrderedDict()

Applications
- LRU Cache
- Task Scheduling
- Configuration Files
- Ordered Data Processing
"""

from collections import OrderedDict


# Creating an OrderedDict

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


# Creating an OrderedDict from a Dictionary

student = OrderedDict({"name": "Rahul","age": 20,"city": "Mumbai"})

print(student)

# Output:
# OrderedDict([
# ('name', 'Rahul'),
# ('age', 20),
# ('city', 'Mumbai')
# ])


# move_to_end() : Moves a key to the end.

student = OrderedDict({"A": 1,"B": 2,"C": 3})

student.move_to_end("A")

print(student)

# Output:
# OrderedDict([
# ('B', 2),
# ('C', 3),
# ('A', 1)
# ])


# move_to_end(last=False) : Moves a key to the beginning.

student = OrderedDict({"A": 1,"B": 2,"C": 3})

student.move_to_end("C", last=False)

print(student)

# Output:
# OrderedDict([
# ('C', 3),
# ('A', 1),
# ('B', 2)
# ])


# popitem() : Removes the last inserted key-value pair.

student = OrderedDict({"A": 1,"B": 2,"C": 3})

print(student.popitem())

# Output:
# ('C', 3)

print(student)

# Output:
# OrderedDict([
# ('A', 1),
# ('B', 2)
# ])


# popitem(last=False) : Removes the first key-value pair.

student = OrderedDict({"A": 1,"B": 2,"C": 3})

print(student.popitem(last=False))

# Output:
# ('A', 1)

print(student)

# Output:
# OrderedDict([
# ('B', 2),
# ('C', 3)
# ])


# Equality Comparison

dictionary = {"A": 1,"B": 2}

ordered = OrderedDict({"A": 1,"B": 2})

print(dictionary == ordered)

# Output:
# True


# OrderedDict Equality

ordered1 = OrderedDict({"A": 1,"B": 2})

ordered2 = OrderedDict({"B": 2,"A": 1})

print(ordered1 == ordered2)

# Output:
# False

"""
For OrderedDict, the insertion order also matters
during comparison.
"""


# Practical Example - Recently Used Files

recent_files = OrderedDict()

recent_files["notes.pdf"] = "Opened"
recent_files["python.py"] = "Opened"
recent_files["resume.docx"] = "Opened"

recent_files.move_to_end("notes.pdf")

print(recent_files)

# Output:
# OrderedDict([
# ('python.py', 'Opened'),
# ('resume.docx', 'Opened'),
# ('notes.pdf', 'Opened')
# ])


# Practical Example - Task Queue

tasks = OrderedDict()

tasks["Task 1"] = "Pending"
tasks["Task 2"] = "Pending"
tasks["Task 3"] = "Pending"

print(tasks)

# Output:
# OrderedDict([
# ('Task 1', 'Pending'),
# ('Task 2', 'Pending'),
# ('Task 3', 'Pending')
# ])


"""
Applications of OrderedDict

- LRU Cache
- Recently Opened Files
- Ordered Configuration
- Task Scheduling
- Data Processing Pipelines
"""

# ===============================x=================================