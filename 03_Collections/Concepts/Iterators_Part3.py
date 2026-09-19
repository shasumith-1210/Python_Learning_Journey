# ITERATORS - PART 3 - TERMINATING ITERATORS

import itertools

"""
# Terminating Iterators

Terminating iterators process one or more iterables and
produce a finite sequence of results.

Unlike infinite iterators such as count(), cycle(), and
repeat(), these iterators eventually stop.

Important Functions
- accumulate()
- chain()
- compress()
- filterfalse()
- dropwhile()
- takewhile()
- islice()
- zip_longest()
- pairwise()
- starmap()
- groupby()
- tee()
"""


# accumulate() : Produces accumulated results.

numbers = [1, 2, 3, 4, 5]

result = itertools.accumulate(numbers)

print(list(result))

# Output:
# [1, 3, 6, 10, 15]


# accumulate() with multiplication

numbers = [1, 2, 3, 4]

result = itertools.accumulate(numbers, (lambda x, y: x * y))

print(list(result))

# Output:
# [1, 2, 6, 24]


"""
accumulate() can be used for:

- Running Sum
- Running Product
- Prefix Calculations
- Cumulative Statistics
"""


# chain() : Combines multiple iterables into one iterator.

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = itertools.chain(numbers1, numbers2)    

print(list(result))

# Output:
# [1, 2, 3, 4, 5, 6]


# chain() with different iterable types

numbers = [1, 2]
letters = ("A", "B")
word = "CD"

result = itertools.chain(numbers, letters, word)

print(list(result))

# Output:
# [1, 2, 'A', 'B', 'C', 'D']


"""
chain() is useful when multiple iterables need to be
processed as one continuous sequence.
"""

# compress() : Selects elements based on selectors.

data = ["Python", "Java", "C", "JavaScript"]    

selectors = [1, 0, 1, 0]

result = itertools.compress(data, selectors)    

print(list(result))

# Output:
# ['Python', 'C']


"""
A truthy selector keeps the corresponding data element.

1 -> Keep
0 -> Ignore
"""

# filterfalse() : Keeps elements for which the condition is False.

numbers = [1, 2, 3, 4, 5, 6]

result = itertools.filterfalse((lambda number: number % 2 == 0), numbers)

print(list(result))

# Output:
# [1, 3, 5]

# filterfalse() without a function

values = [0, 1, False, True, "", "Python"]

result = itertools.filterfalse(None, values)    

print(list(result))

# Output:
# [0, False, '']


# takewhile() : Takes elements while the condition is True.

numbers = [2, 4, 6, 8, 9, 10, 12]

result = itertools.takewhile( (lambda number: number % 2 == 0), numbers)

print(list(result))

# Output:
# [2, 4, 6, 8]


"""
takewhile() stops at the first element
that fails the condition.

It does not continue searching after that point.
"""

# dropwhile() : Skips elements while the condition is True.

numbers = [2, 4, 6, 8, 9, 10, 12]

result = itertools.dropwhile( (lambda number: number % 2 == 0), numbers )

print(list(result))

# Output:
# [9, 10, 12]


"""
dropwhile() skips elements until the first element
that fails the condition.

After that, all remaining elements are returned.
"""

# islice() : Performs slicing on an iterator.

numbers = itertools.count(1)

result = itertools.islice( numbers, 5 )

print(list(result))

# Output:
# [1, 2, 3, 4, 5]


# islice() with start and stop

numbers = itertools.count(1)

result = itertools.islice( numbers, 2, 7 )

print(list(result))

# Output:
# [3, 4, 5, 6, 7]


# islice() with step

numbers = itertools.count(1)

result = itertools.islice( numbers, 1, 10, 2 )

print(list(result))

# Output:
# [2, 4, 6, 8, 10]


# islice() : Performs slicing on an iterator.

numbers = itertools.count(1)

result = itertools.islice( numbers, 5 )

print(list(result))

# Output:
# [1, 2, 3, 4, 5]


# islice() with start and stop

numbers = itertools.count(1)

result = itertools.islice( numbers,2,7 )

print(list(result))

# Output:
# [3, 4, 5, 6, 7]


# islice() with step

numbers = itertools.count(1)

result = itertools.islice( numbers,1,10,2 )

print(list(result))

# Output:
# [2, 4, 6, 8, 10]


# zip_longest() : Combines iterables of different lengths.

numbers = [1, 2, 3]
letters = ["A", "B"]

result = itertools.zip_longest( numbers, letters )

print(list(result))

# Output:
# [
# (1, 'A'),
# (2, 'B'),
# (3, None)
# ]


# zip_longest() with fillvalue

numbers = [1, 2, 3]
letters = ["A", "B"]

result = itertools.zip_longest( numbers, letters, fillvalue="N/A"
)

print(list(result))

# Output:
# [
# (1, 'A'),
# (2, 'B'),
# (3, 'N/A')
# ]

# pairwise() : Produces consecutive overlapping pairs.

# Available in Python 3.10+


numbers = [10, 20, 30, 40]

result = itertools.pairwise(numbers)

print(list(result))

# Output:
# [
# (10, 20),
# (20, 30),
# (30, 40)
# ]


# Practical Example - Differences Between Consecutive Values

prices = [100, 120, 115, 130]

differences = [
    current - previous
    for previous, current in itertools.pairwise(prices)
]

print(differences)

# Output:
# [20, -5, 15]

# starmap() : Applies a function to arguments
# unpacked from each iterable element.

data = [ (2, 3), (4, 5), (6, 7) ]

result = itertools.starmap( (lambda x, y: x + y), data )

print(list(result))

# Output:
# [5, 9, 13]


# Practical Example - Multiplication

numbers = [ (2, 5), (3, 4), (6, 7) ]

result = itertools.starmap( (lambda x, y: x * y), numbers )

print(list(result))

# Output:
# [10, 12, 42]

# groupby() : Groups consecutive elements
# based on a key function.

"""
Important:
groupby() groups consecutive elements with the same key.

The data should usually be sorted by the same key
before using groupby() when you want all matching
items in the same group.
"""

numbers = [
    1, 1, 2, 2, 2, 3, 3
]

for key, group in itertools.groupby(numbers):
    print(key, list(group))

# Output:
# 1 [1, 1]
# 2 [2, 2, 2]
# 3 [3, 3]


# groupby() with a key function

words = [
    "apple",
    "ant",
    "banana",
    "ball",
    "cat"
]

for key, group in itertools.groupby(
    words,
    key=lambda word: word[0]
):
    print(key, list(group))

# Output:
# a ['apple', 'ant']
# b ['banana', 'ball']
# c ['cat']

# tee() : Creates multiple independent iterators
# from a single iterator.

numbers = iter([10, 20, 30, 40])

iterator1, iterator2 = itertools.tee(numbers, 2)

print(list(iterator1))

# Output:
# [10, 20, 30, 40]

print(list(iterator2))

# Output:
# [10, 20, 30, 40]


"""
tee() is useful when the same iterator needs to be
consumed independently in multiple places.

The returned iterators should generally be consumed
independently rather than advancing them unpredictably
at the same time.
"""

"""
Terminating Iterators - Quick Revision

accumulate() : Generates cumulative results.
chain() : Combines multiple iterables.
compress() : Selects elements using selectors.
filterfalse() : Keeps elements that fail a condition.
takewhile() : Takes elements while condition is True.
dropwhile() : Skips elements while condition is True.
islice() : Performs slicing on an iterator.
zip_longest() : Combines iterables of unequal lengths.
pairwise() : Creates consecutive overlapping pairs.
starmap() : Calls a function using unpacked arguments.
groupby() : Groups consecutive elements.
tee() : Creates multiple independent iterators.
"""