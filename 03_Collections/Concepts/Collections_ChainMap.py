"""" ================= ChainMap ============"""

"""
# ChainMap

ChainMap groups multiple dictionaries into a single
logical view without merging them.

It searches dictionaries from left to right until
the key is found.

Syntax:
ChainMap(dict1, dict2, ...)

Applications
- Configuration Management
- Multiple Scope Lookup
- Combining Dictionaries
- Layered Settings
"""

from collections import ChainMap


# Creating a ChainMap

student = {
    "name": "Rahul"
}

details = {
    "age": 20,
    "city": "Mumbai"
}

combined = ChainMap(student, details)

print(combined)

# Output:
# ChainMap({'name': 'Rahul'}, {'age': 20, 'city': 'Mumbai'})


# Accessing Values

print(combined["name"])

# Output:
# Rahul

print(combined["city"])

# Output:
# Mumbai


# Searching Order

dict1 = {
    "A": 1,
    "B": 2
}

dict2 = {
    "B": 20,
    "C": 30
}

chain = ChainMap(dict1, dict2)

print(chain["B"])

# Output:
# 2

"""
The first occurrence of the key is returned.
"""


# Updating Values

chain["A"] = 100

print(dict1)

# Output:
# {'A': 100, 'B': 2}

"""
Updates always affect the first dictionary.
"""


# maps : Returns the list of underlying dictionaries.

print(chain.maps)

# Output:
# [{'A': 100, 'B': 2},
#  {'B': 20, 'C': 30}]


# new_child()

"""
Creates a new ChainMap with an empty dictionary
added to the front.
"""

chain = ChainMap(dict1, dict2)

new_chain = chain.new_child()

print(new_chain)

# Output:
# ChainMap({}, {'A':100,'B':2}, {'B':20,'C':30})


# parents

"""
Returns a ChainMap excluding the first dictionary.
"""

print(new_chain.parents)

# Output:
# ChainMap({'A':100,'B':2}, {'B':20,'C':30})


# Iterating Through a ChainMap

for key, value in combined.items():
    print(key, ":", value)

# Output:
# name : Rahul
# age : 20
# city : Mumbai


# Practical Example - Configuration Settings

default_settings = {
    "theme": "Light",
    "language": "English",
    "font_size": 12
}

user_settings = {
    "theme": "Dark"
}

settings = ChainMap(user_settings, default_settings)

print(settings["theme"])

# Output:
# Dark

print(settings["language"])

# Output:
# English


# Practical Example - Environment Variables

system = {
    "PATH": "/usr/bin",
    "HOME": "/home/user"
}

application = {
    "HOME": "/app/home"
}

environment = ChainMap(application, system)

print(environment["HOME"])

# Output:
# /app/home

print(environment["PATH"])

# Output:
# /usr/bin


# Practical Example - Student Records

personal = {
    "name": "Rahul"
}

academic = {
    "CGPA": 9.1
}

placement = {
    "Company": "Google"
}

student = ChainMap(
    personal,
    academic,
    placement
)

print(student["Company"])

# Output:
# Google


"""
Applications of ChainMap

- Configuration Management

- Command Line Arguments

- Environment Variables

- Multiple Scope Lookup

- Layered Settings

- Template Rendering
"""

# ===============================x=================================