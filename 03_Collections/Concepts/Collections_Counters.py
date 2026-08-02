"""
COLLECTIONS MODULE IN PYTHON

Definition: 
The collections module is a built-in Python module that provides
specialized container data types as alternatives to Python's
general-purpose built-in containers.

These data structures are optimized for specific use cases and
often provide better readability, convenience, and performance.

Main Data Structures
1. Counter
2. defaultdict
3. deque
4. OrderedDict
5. ChainMap
6. namedtuple

Why Learn collections?
- Simplifies common programming tasks.
- Provides optimized data structures.
- Reduces the amount of code.
- Improves readability and maintainability.

Import Statement
from collections import Counter
from collections import defaultdict
from collections import deque
from collections import OrderedDict
from collections import ChainMap
from collections import namedtuple
"""

""" ===================== COUNTERS ========================="""

"""
# Counter

Counter is a dictionary subclass that counts the frequency
of hashable objects.

Each unique element becomes a key, and its number of
occurrences becomes the corresponding value.

Syntax:
Counter(iterable)
Counter(dictionary)

Applications
- Word Frequency Analysis
- Character Counting
- Vote Counting
- Inventory Management
- Data Analysis
"""

from collections import Counter

# Creating a Counter from a List

numbers = [1, 2, 1, 3, 2, 1, 4]

counter = Counter(numbers)

print(counter)

# Output:
# Counter({1: 3, 2: 2, 3: 1, 4: 1})

# Creating a Counter from a String

text = "programming"

counter = Counter(text)

print(counter)

# Output:
# Counter({
# 'g':2,
# 'r':2,
# 'm':2,
# 'p':1,
# ...
# })

# Creating a Counter from a Tuple

numbers = (10, 20, 10, 30, 20, 10)

counter = Counter(numbers)

print(counter)

# Output:
# Counter({10: 3, 20: 2, 30: 1})

# Creating a Counter from a Dictionary

inventory = { "Apple": 15, "Banana": 10, "Orange": 5}

counter = Counter(inventory)

print(counter)

# Output:
# Counter({ 'Apple':15, 'Banana':10, 'Orange':5 })

# Accessing Frequencies

text = "banana"

counter = Counter(text)

print(counter["a"])
print(counter["n"])
print(counter["b"])

# Output:
# 3
# 2
# 1

# Accessing a Missing Key

text = "python"

counter = Counter(text)

print(counter["z"])

# Output:
# 0

"""
Unlike dictionaries, Counter returns 0 for
missing keys instead of raising KeyError.
"""

# Iterating Through a Counter

text = "apple"

counter = Counter(text)

for character, frequency in counter.items():
    print(character, ":", frequency)

# Output:
# a : 1
# p : 2
# l : 1
# e : 1



"""
# elements()
Returns an iterator containing each element repeated according to its frequency.

Syntax:
counter.elements()
"""

from collections import Counter

letters = Counter({"A": 2,"B": 3,"C": 1})

print(list(letters.elements()))

# Output:
# ['A', 'A', 'B', 'B', 'B', 'C']



"""
# most_common()
Returns the most frequently occurring elements.

Syntax:
counter.most_common()
counter.most_common(n)
"""

text = "banana"

counter = Counter(text)

print(counter.most_common())

# Output:
# [('a', 3), ('n', 2), ('b', 1)]


# most_common(n)

numbers = [1, 2, 1, 3, 2, 1, 4, 5, 2]

counter = Counter(numbers)

print(counter.most_common(2))

# Output:
# [(1, 3), (2, 3)]



"""
# update()
Adds counts from another iterable or Counter.

Syntax: counter.update(iterable)
"""

counter = Counter("apple")

counter.update("banana")

print(counter)

# Output:
# Counter({
# 'a':4,
# 'p':2,
# 'n':2,
# ...
# })

# update() with Another Counter

counter1 = Counter({"Apple": 5,"Banana": 2})

counter2 = Counter({"Apple": 3,"Orange": 4})

counter1.update(counter2)

print(counter1)

# Output:
# Counter({
# 'Apple':8,
# 'Orange':4,
# 'Banana':2
# })



"""
# subtract()
Subtracts counts instead of adding them.

Syntax: counter.subtract(iterable)
"""

counter = Counter("banana")

counter.subtract("ana")

print(counter)

# Output:
# Counter({
# 'a':1,
# 'n':1,
# 'b':1
# })


"""
# total()
Returns the total of all counts.

Available in Python 3.10+

Syntax: counter.total()
"""

counter = Counter({"Apple": 5,"Banana": 4,"Orange": 3})

print(counter.total())

# Output:
# 12


# Counter Addition (+)

counter1 = Counter({"A": 3,"B": 2})

counter2 = Counter({
    "A": 1,
    "B": 4,
    "C": 2
})

print(counter1 + counter2)

# Output:
# Counter({
# 'B':6,
# 'A':4,
# 'C':2
# })


# Counter Subtraction (-)

counter1 = Counter({"A": 5,"B": 4})

counter2 = Counter({"A": 2,"B": 5})

print(counter1 - counter2)

# Output:
# Counter({
# 'A':3
# })

"""
Negative and zero counts are discarded.
"""

# Counter Intersection (&) : Keeps the minimum count for each element.

counter1 = Counter({"A": 4,"B": 2})

counter2 = Counter({"A": 2,"B": 5})

print(counter1 & counter2)

# Output:
# Counter({
# 'A':2,
# 'B':2
# })

# Counter Union (|) : Keeps the maximum count for each element.

counter1 = Counter({"A": 4,"B": 2})

counter2 = Counter({"A": 2,"B": 5,"C": 3})

print(counter1 | counter2)

# Output:
# Counter({
# 'B':5,
# 'A':4,
# 'C':3
# })

# Practical Example - Word Frequency

sentence = "Python is easy and Python is powerful."

words = sentence.lower().split()

counter = Counter(words)

print(counter)

# Output:
# Counter({
# 'python':2,
# 'is':2,
# 'easy':1,
# 'and':1,
# 'powerful.':1
# })

# Practical Example - Vote Counting

votes = ["Alice","Bob","Alice","Charlie","Bob","Alice"]

counter = Counter(votes)

print(counter)

print(counter.most_common(1))

# Output:
# Counter({
# 'Alice':3,
# 'Bob':2,
# 'Charlie':1
# })
#
# [('Alice', 3)]


# Practical Example - Inventory Management

inventory = Counter({"Laptop": 10,"Mouse": 25,"Keyboard": 15})

sales = Counter({"Laptop": 2,"Mouse": 5})

inventory.subtract(sales)

print(inventory)

# Output:
# Counter({
# 'Keyboard':15,
# 'Mouse':20,
# 'Laptop':8
# })

#===================================================================