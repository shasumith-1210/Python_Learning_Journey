"""
COMPREHENSIONS IN PYTHON

Definition
Comprehensions provide a concise and readable way to create
new collections from existing iterables.

Instead of writing multiple lines using loops, comprehensions
allow you to create lists, sets, and dictionaries in a
single expression.

Types of Comprehensions
1. List Comprehension
2. Set Comprehension
3. Dictionary Comprehension

Advantages
- Shorter code
- Better readability
- Faster than traditional loops
- Cleaner syntax

General Syntax

List: [expression for item in iterable]
Set:  {expression for item in iterable}
Dictionary: {key: value for item in iterable}
"""


# Traditional Loop vs List Comprehension

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# Output:
# [1, 4, 9, 16, 25]


squares = [number ** 2 for number in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# Creating a List

numbers = [number for number in range(1, 6)]

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# Squares of Numbers

squares = [number ** 2 for number in range(1, 6)]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# Cubes of Numbers

cubes = [number ** 3 for number in range(1, 6)]

print(cubes)

# Output:
# [1, 8, 27, 64, 125]


# Using Strings

word = "Python"

letters = [character for character in word]

print(letters)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']


# Converting Strings to Uppercase

names = ["rahul","aman","priya"]

upper_names = [
    name.upper()
    for name in names
]

print(upper_names)

# Output:
# ['RAHUL', 'AMAN', 'PRIYA']


# Conditional List Comprehension

even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]


# Odd Numbers

odd_numbers = [
    number
    for number in range(1, 11)
    if number % 2 != 0
]

print(odd_numbers)

# Output:
# [1, 3, 5, 7, 9]


# Filtering Strings

names = ["Rahul","Aman","Priya","Rohit"]

filtered = [
    name
    for name in names
    if name.startswith("R")
]

print(filtered)

# Output:
# ['Rahul', 'Rohit']


"""
# if-else in List Comprehension

if-else can be used to choose between two values.

Syntax:
[true_value if condition else false_value for item in iterable]
"""

numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# Replacing Negative Numbers

numbers = [-10, 20, -30, 40, -50]

positive_numbers = [
    number if number >= 0 else 0
    for number in numbers
]

print(positive_numbers)

# Output:
# [0, 20, 0, 40, 0]


# Nested List Comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print(flattened)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Creating a Matrix

matrix = [
    [0 for column in range(3)]
    for row in range(3)
]

print(matrix)

# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]


# Multiplication Table

table = [
    [number * value for value in range(1, 6)]
    for number in range(1, 6)
]

print(table)

# Output:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]


# Set Comprehension

squares = {
    number ** 2
    for number in range(1, 6)
}

print(squares)

# Output:
# {1, 4, 9, 16, 25}


# Set Comprehension with Condition

even_numbers = {
    number
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_numbers)

# Output:
# {2, 4, 6, 8, 10}


# Dictionary Comprehension

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Dictionary Comprehension with Condition

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)

# Output:
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# Creating a Dictionary from Two Lists

subjects = ["Maths","Physics","Chemistry"]

marks = [95,88,91]

student_marks = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}

print(student_marks)

# Output:
# {'Maths': 95,
#  'Physics': 88,
#  'Chemistry': 91}

# Nested Dictionary Comprehension

students = {
    student: {
        subject: 0
        for subject in ["Maths", "Physics", "Chemistry"]
    }
    for student in ["Rahul", "Aman", "Priya"]
}

print(students)

# Output:
# {
# 'Rahul': {'Maths': 0, 'Physics': 0, 'Chemistry': 0},
# 'Aman': {'Maths': 0, 'Physics': 0, 'Chemistry': 0},
# 'Priya': {'Maths': 0, 'Physics': 0, 'Chemistry': 0}
# }


# Swapping Dictionary Keys and Values

student = {"Maths": 95,"Physics": 88,"Chemistry": 91}

reversed_dictionary = {
    value: key
    for key, value in student.items()
}

print(reversed_dictionary)

# Output:
# {95: 'Maths', 88: 'Physics', 91: 'Chemistry'}


# Removing Duplicate Values

numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = [
    number
    for number in set(numbers)
]

print(unique_numbers)

# Output:
# [10, 20, 30, 40, 50]


# Filtering Long Words

sentence = ["Python","Java","Artificial","Data","Machine","AI"]

long_words = [
    word
    for word in sentence
    if len(word) > 5
]

print(long_words)

# Output:
# ['Python', 'Artificial', 'Machine']


# Extracting File Extensions

files = ["notes.pdf","photo.png","program.py","report.docx"]

extensions = [
    file.split(".")[-1]
    for file in files
]

print(extensions)

# Output:
# ['pdf', 'png', 'py', 'docx']


# Creating a Dictionary from a Sentence

sentence = "python is easy"

length = {
    word: len(word)
    for word in sentence.split()
}

print(length)

# Output:
# {'python': 6, 'is': 2, 'easy': 4}


# Traditional Loop vs Comprehension

numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number ** 2)

print(result)

# Output:
# [1, 4, 9, 16, 25]


result = [
    number ** 2
    for number in numbers
]

print(result)

# Output:
# [1, 4, 9, 16, 25]

"""
List comprehensions are generally faster and more concise than equivalent for loops.
"""


"""
# Time Complexity
+--------------------------------+---------------+
| Operation                      | Complexity    |
+--------------------------------+---------------+
| List Comprehension             | O(n)          |
| Set Comprehension              | O(n)          |
| Dictionary Comprehension       | O(n)          |
| Nested Comprehension           | O(n × m)      |
| Filtering                      | O(n)          |
| Mapping                        | O(n)          |
+--------------------------------+---------------+
"""


"""
# Common Mistakes

1. Writing overly complex comprehensions.
Prefer readability over writing everything in a single line.

2. Forgetting the order of nested loops.

Correct:

[number
 for row in matrix
 for number in row]


3. Confusing filter conditions with if-else.

Filter:

[number
 for number in numbers
 if number % 2 == 0]

if-else:

["Even" if number % 2 == 0 else "Odd"
 for number in numbers]

------------------------------------
4. Using comprehensions when a normal loop
is easier to understand.
"""


"""
# Best Practices
1. Keep comprehensions short and readable.
2. Use descriptive variable names.
3. Avoid deeply nested comprehensions.
4. Use comprehensions for creating new collections.
5. Prefer normal loops for complex business logic.
6. Use dictionary comprehensions for mappings.
7. Use set comprehensions for unique values.
"""



"""
# Quick Revision:

1. Types of Comprehensions
- List Comprehension
- Set Comprehension
- Dictionary Comprehension

2. Features
- Filtering
- Mapping
- Nested Comprehensions
- Conditional Expressions

3. Benefits
- Shorter Code
- Better Readability
- Improved Performance
- Cleaner Syntax

4. Common Use Cases
- Creating Lists
- Filtering Data
- Transforming Data
- Removing Duplicates
- Creating Dictionaries
- Generating Matrices
"""

