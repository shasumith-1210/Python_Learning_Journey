# ITERTOOLS - PART 4: Practical Examples


import itertools

# Practical Example - Running Total

numbers = [10, 20, 30, 40, 50]

running_total = itertools.accumulate(numbers)

print(list(running_total))

# Output:
# [10, 30, 60, 100, 150]


# Practical Example - Running Maximum

numbers = [10, 5, 25, 15, 30]

running_maximum = itertools.accumulate(numbers, max)    

print(list(running_maximum))

# Output:
# [10, 10, 25, 25, 30]


# Practical Example - Combining Multiple Data Sources

students_a = ["Rahul", "Aman"]
students_b = ["Priya", "Rohan"]
students_c = ["Karan", "Neha"]

all_students = itertools.chain(students_a, students_b, students_c)

print(list(all_students))

# Output:
# [
# 'Rahul',
# 'Aman',
# 'Priya',
# 'Rohan',
# 'Karan',
# 'Neha'
# ]


# Practical Example - Selecting Active Users

users = [ "Rahul", "Aman", "Priya", "Rohan" ]

active = [1, 0, 1, 0]

active_users = itertools.compress(users, active)

print(list(active_users))

# Output:
# ['Rahul', 'Priya']


# Practical Example - Processing Until a Limit

numbers = [10, 20, 30, 40, 60, 70]

values = itertools.takewhile(
    lambda number: number <= 40,
    numbers
)

print(list(values))

# Output:
# [10, 20, 30, 40]


# Practical Example - Skip Values Below a Limit

numbers = [10, 20, 30, 50, 60, 70]

values = itertools.dropwhile(
    lambda number: number < 50,
    numbers
)

print(list(values))

# Output:
# [50, 60, 70]


# Practical Example - Processing Part of a Large Dataset

data = range(1, 1000000)

first_values = itertools.islice(data,10)

print(list(first_values))

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Practical Example - Pairwise Temperature Changes

temperatures = [30, 32, 31, 35, 37]

changes = [
    current - previous
    for previous, current in itertools.pairwise(temperatures)
]

print(changes)

# Output:
# [2, -1, 4, 2]


# Practical Example - Group Students by Department

students = [("IT", "Rahul"), ("IT", "Aman"), ("HR", "Priya"), ("HR", "Rohan"), ("Sales", "Karan")]

for department, group in itertools.groupby(
    students,
    key=lambda student: student[0]
):
    print(department, list(group))

# Output:
# IT [('IT', 'Rahul'), ('IT', 'Aman')]
# HR [('HR', 'Priya'), ('HR', 'Rohan')]
# Sales [('Sales', 'Karan')]


# Practical Example - zip_longest() for Student Data

names = ["Rahul", "Aman", "Priya"]
marks = [90, 85]

records = itertools.zip_longest(names, marks, fillvalue="N/A")

print(list(records))

# Output:
# [
# ('Rahul', 90),
# ('Aman', 85),
# ('Priya', 'N/A')
# ]

# Iterator vs List

numbers = range(1, 6)

iterator = itertools.islice(numbers, 3)

print(iterator)

# Output:
# <itertools.islice object ...>

print(list(iterator))

# Output:
# [1, 2, 3]

"""
itertools functions generally return iterators instead of
immediately creating complete lists.

This allows values to be processed lazily.
"""

# Memory Efficiency Example

numbers = range(1, 1000000)

result = itertools.islice(numbers, 5)

for number in result:
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5

"""
The complete range does not need to be converted into
a list before processing the first five values.
"""

# Combining itertools Functions

numbers = itertools.count(1)

result = itertools.islice(itertools.filterfalse(lambda number: number % 2 == 0, numbers),5)

print(list(result))

# Output:
# [1, 3, 5, 7, 9]

"""
Here:

count() : generates numbers indefinitely.

filterfalse() : keeps odd numbers.

islice() : takes only the first five results.
"""

# Using product() for a Small Brute Force Search

digits = "012"

passwords = itertools.product(digits, repeat=2)

for password in passwords:
    print("".join(password))

# Output:
# 00
# 01
# 02
# 10
# 11
# 12
# 20
# 21
# 22

"""
This approach can be useful for small combinatorial
search problems.

The number of possibilities grows rapidly as the
input size increases.
"""

# permutations() for Arrangement Problems

items = ["A", "B", "C"]

arrangements = itertools.permutations(items)

print(list(arrangements))

# Output:
# [
# ('A', 'B', 'C'),
# ('A', 'C', 'B'),
# ('B', 'A', 'C'),
# ('B', 'C', 'A'),
# ('C', 'A', 'B'),
# ('C', 'B', 'A')
# ]

# combinations() for Selection Problems

students = ["Rahul", "Aman", "Priya", "Rohan"]

teams = itertools.combinations(students, 2) 

print(list(teams))

# Output:
# [
# ('Rahul', 'Aman'),
# ('Rahul', 'Priya'),
# ('Rahul', 'Rohan'),
# ('Aman', 'Priya'),
# ('Aman', 'Rohan'),
# ('Priya', 'Rohan')
# ]

"""
Time Complexity

The exact complexity depends on the input size and
the specific operation.

count() : Generating each value: O(1)

cycle() : Each generated value: O(1) amortized

repeat() : Each generated value: O(1)

chain() : Processing n total elements: O(n)

accumulate() : Processing n elements: O(n)

compress() : Processing n elements: O(n)

filterfalse() : Processing n elements: O(n)

takewhile() : Processing n elements: O(n) (worst case)

dropwhile() : Processing n elements: O(n) (worst case)

islice() : O(k) for k consumed elements

zip_longest() : O(n) for n total processed elements

pairwise() : O(n) for n total processed elements

starmap() : O(n), excluding the cost of the function itself

groupby() : O(n) for processing n elements

tee() : 
Depends on how far the returned iterators
move apart; buffering may require O(n) memory.

product() : O(number of generated products)

permutations() : O(P(n, r)) generated results

combinations() : O(C(n, r)) generated results

combinations_with_replacement() : O(C(n+r-1, r)) generated results
"""

"""
Common Mistakes

1. Forgetting that infinite iterators never end.

count()
cycle()
repeat()

Use a stopping condition or islice().


2. Converting a huge or infinite iterator into a list.

list(itertools.count())

This never finishes.


3. Assuming itertools returns lists.

Most itertools functions return iterators.

Use list() only when you actually need the
complete result in memory.


4. Misunderstanding groupby().

groupby() groups consecutive elements.

Sort the data by the grouping key first when
all matching items need to be grouped together.


5. Confusing permutations() and combinations().

permutations()
Order matters.

combinations()
Order does not matter.


6. Generating enormous Cartesian products.

product(), permutations(), and combinations()
can produce extremely large numbers of results.

Use them carefully.
"""

"""
Best Practices
- Prefer itertools when processing iterators lazily.
- Use islice() when only part of an iterator is required.
- Use chain() instead of repeatedly creating large
combined lists.
- Use product(), permutations(), and combinations()
for systematic combinatorial generation.
- Be careful with infinite iterators.
- Avoid converting large iterators to lists unnecessarily.
- Remember that iterators are consumed as they are used.
- Sort data before groupby() when grouping all equal
keys together is required.
- Use itertools to make iterator-based code concise
and memory efficient.
"""

"""
Quick Revision

$ Infinite Iterators
count()
cycle()
repeat()

$ Combinatoric Iterators
product()
permutations()
combinations()
combinations_with_replacement()

$ Terminating Iterators
accumulate()
chain()
compress()
filterfalse()
takewhile()
dropwhile()
islice()
zip_longest()
pairwise()
starmap()
groupby()
tee()

# Important Concepts
Lazy Evaluation
Iterators
Memory Efficiency
Combinatorics
Iterator Composition

# Key Differences::

permutations() : Order matters.
combinations() : Order does not matter.
product() : Generates Cartesian products.
cycle() : Repeats an iterable indefinitely.
repeat() : Repeats one value.
takewhile() : Takes while condition is True.
dropwhile() : Skips while condition is True.
filterfalse() : Keeps elements where condition is False.
groupby() : Groups consecutive elements.
islice() : Slices an iterator.
"""

