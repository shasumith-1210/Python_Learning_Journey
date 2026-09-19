# ITERATORS - PART 2 - COMBINATORIC ITERATORS

import itertools

"""
# Combinatoric Iterators

Combinatoric iterators generate combinations, permutations,
and Cartesian products from one or more iterables.

Main Functions
- product()
- permutations()
- combinations()
- combinations_with_replacement()

These are useful for:
- DSA
- Competitive Programming
- Probability
- Brute Force Problems
- Searching Possible Arrangements
- Generating Test Cases
"""


# product() : Generates the Cartesian product of iterables.

colors = ["Red", "Blue"]
sizes = ["Small", "Large"]

result = itertools.product(colors, sizes)

print(list(result))

# Output:
# [
# ('Red', 'Small'),
# ('Red', 'Large'),
# ('Blue', 'Small'),
# ('Blue', 'Large')
# ]


# product() with repeat

numbers = [1, 2, 3]

result = itertools.product(numbers, repeat=2)

print(list(result))

# Output:
# [
# (1, 1), (1, 2), (1, 3),
# (2, 1), (2, 2), (2, 3),
# (3, 1), (3, 2), (3, 3)
# ]


# Practical Example - Product Configurations

operating_systems = ["Windows", "Linux"]
processors = ["Intel", "AMD"]

configurations = itertools.product(operating_systems, processors)

for configuration in configurations:
    print(configuration)

# Output:
# ('Windows', 'Intel')
# ('Windows', 'AMD')
# ('Linux', 'Intel')
# ('Linux', 'AMD')


# permutations() : Generates all possible arrangements
# of elements.

numbers = [1, 2, 3]

result = itertools.permutations(numbers)

print(list(result))

# Output:
# [
# (1, 2, 3),
# (1, 3, 2),
# (2, 1, 3),
# (2, 3, 1),
# (3, 1, 2),
# (3, 2, 1)
# ]


# permutations() with r

numbers = [1, 2, 3, 4]

result = itertools.permutations(numbers, 2)

print(list(result))

# Output:
# [
# (1, 2),
# (1, 3),
# (1, 4),
# (2, 1),
# (2, 3),
# (2, 4),
# (3, 1),
# (3, 2),
# (3, 4),
# (4, 1),
# (4, 2),
# (4, 3)
# ]


# Practical Example - Arranging Students

students = ["Rahul", "Aman", "Priya"]

arrangements = itertools.permutations(students)

for arrangement in arrangements:
    print(arrangement)

# Output:
# ('Rahul', 'Aman', 'Priya')
# ('Rahul', 'Priya', 'Aman')
# ('Aman', 'Rahul', 'Priya')
# ...


# combinations() : Generates selections where order
# does not matter.

numbers = [1, 2, 3, 4]

result = itertools.combinations(numbers, 2)

print(list(result))

# Output:
# [
# (1, 2),
# (1, 3),
# (1, 4),
# (2, 3),
# (2, 4),
# (3, 4)
# ]


"""
Difference between permutations() and combinations()

permutations()
- Order matters.

(1, 2) and (2, 1)
are different.

combinations()
- Order does not matter.

(1, 2) and (2, 1)
represent the same selection.
"""


# Practical Example - Selecting a Team

students = ["Rahul", "Aman", "Priya", "Rohan"]

teams = itertools.combinations(students, 2)

for team in teams:
    print(team)

# Output:
# ('Rahul', 'Aman')
# ('Rahul', 'Priya')
# ('Rahul', 'Rohan')
# ('Aman', 'Priya')
# ('Aman', 'Rohan')
# ('Priya', 'Rohan')


# combinations_with_replacement()
# Allows the same element to appear more than once.

numbers = [1, 2, 3]

result = itertools.combinations_with_replacement(numbers,2)

print(list(result))

# Output:
# [
# (1, 1),
# (1, 2),
# (1, 3),
# (2, 2),
# (2, 3),
# (3, 3)
# ]


# Practical Example - Selecting Flavors

flavors = ["Vanilla", "Chocolate", "Strawberry"]

selections = itertools.combinations_with_replacement(flavors,2)

for selection in selections:
    print(selection)

# Output:
# ('Vanilla', 'Vanilla')
# ('Vanilla', 'Chocolate')
# ('Vanilla', 'Strawberry')
# ('Chocolate', 'Chocolate')
# ('Chocolate', 'Strawberry')
# ('Strawberry', 'Strawberry')


"""
Combinatoric Functions - Quick Revision

product() : Generates Cartesian products.

Order of positions matters.

Example:
A x B


permutations() : Generates arrangements.

Order matters.

Example:
(1, 2) != (2, 1)


combinations() : Generates selections.

Order does not matter.

Example:
(1, 2) == (2, 1)


combinations_with_replacement() : Generates selections where elements can repeat.
"""