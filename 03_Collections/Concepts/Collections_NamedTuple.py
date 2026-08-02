""" ================ namedtuple =============="""

"""
# namedtuple

namedtuple is a factory function that creates tuple
subclasses with named fields.

Unlike normal tuples, elements can be accessed using
meaningful attribute names instead of indexes.

Syntax:
namedtuple("ClassName", ["field1", "field2"])

Applications
- Student Records
- Employee Records
- Database Rows
- Coordinates
- Configuration Objects
"""

from collections import namedtuple

# Creating a namedtuple

Student = namedtuple(
    "Student",
    ["name", "age", "city"]
)

student = Student(
    "Rahul",
    20,
    "Mumbai"
)

print(student)

# Output:
# Student(name='Rahul',
#         age=20,
#         city='Mumbai')

# Accessing Fields

print(student.name)

# Output:
# Rahul

print(student.age)

# Output:
# 20

print(student.city)

# Output:
# Mumbai

# Accessing Using Index

print(student[0])

# Output:
# Rahul

print(student[1])

# Output:
# 20

# _fields : Returns all field names.

print(Student._fields)

# Output:
# ('name', 'age', 'city')

# _make() : Creates an object from an iterable.

data = [
    "Aman",
    21,
    "Delhi"
]

student = Student._make(data)

print(student)

# Output:
# Student(name='Aman',
#         age=21,
#         city='Delhi')

# _replace() : Returns a new object with updated fields.

student = Student(
    "Rahul",
    20,
    "Mumbai"
)

updated_student = student._replace(age=21)

print(updated_student)

# Output:
# Student(name='Rahul',
#         age=21,
#         city='Mumbai')

# _asdict() : Converts a namedtuple into a dictionary.

student = Student(
    "Rahul",
    20,
    "Mumbai"
)

print(student._asdict())

# Output:
# {
# 'name':'Rahul',
# 'age':20,
# 'city':'Mumbai'
# }

# Default Values

Employee = namedtuple(
    "Employee",
    ["name", "salary", "department"],
    defaults=[
        30000,
        "IT"
    ]
)

employee = Employee("Rahul")

print(employee)

# Output:
# Employee(name='Rahul',
#          salary=30000,
#          department='IT')

# Practical Example - Student Record

Student = namedtuple(
    "Student",
    ["roll_no", "name", "cgpa"]
)

student = Student(
    101,
    "Rahul",
    9.2
)

print(student.name)

# Output:
# Rahul

# Practical Example - Employee Record

Employee = namedtuple(
    "Employee",
    ["id", "name", "salary"]
)

employee = Employee(
    1,
    "Aman",
    50000
)

print(employee.salary)

# Output:
# 50000

# Practical Example - Coordinates

Point = namedtuple(
    "Point",
    ["x", "y"]
)

point = Point(
    10,
    20
)

print(point.x)

# Output:
# 10

print(point.y)

# Output:
# 20

# Practical Example - Books

Book = namedtuple(
    "Book",
    ["title", "author", "price"]
)

book = Book(
    "Python",
    "Guido",
    599
)

print(book)

# Output:
# Book(title='Python',
#      author='Guido',
#      price=599)

"""
Applications of namedtuple:
- Student Records
- Employee Records
- Database Records
- Coordinates
- Inventory Items
- Configuration Objects
- API Responses
- Immutable Data Storage
"""

"""
Time Complexity:
Access by Field      : O(1)
Access by Index      : O(1)
Creation             : O(n)
_replace()           : O(n)
_asdict()            : O(n)
_make()              : O(n)
"""

"""
Common Mistakes :

1. Trying to modify a field.

student.name = "Aman"

Raises: AttributeError


2. Forgetting that _replace() returns a NEW object.


3. Confusing namedtuple with dataclass.

namedtuple is immutable.

dataclass is mutable by default.
"""

"""
Common Mistakes

1. Trying to modify a field.

student.name = "Aman"

Raises:
AttributeError


2. Forgetting that _replace()
returns a NEW object.


3. Confusing namedtuple with dataclass.

namedtuple is immutable.

dataclass is mutable by default.
"""

"""
Best Practices :
1. Use namedtuple for immutable records.
2. Use descriptive field names.
3. Use _replace() instead of modifying fields.
4. Use _asdict() when dictionary conversion is required.
5. Prefer namedtuple over normal tuples when readability is important.
"""
