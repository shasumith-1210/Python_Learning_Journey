""" ====================== deque =========================="""

"""
# deque

deque (Double Ended Queue) is a specialized container that
supports fast insertion and deletion from both ends.

Unlike lists, deque provides O(1) time complexity for
adding and removing elements from both the front and rear.

Syntax:
deque(iterable)

Applications
- Queue
- Stack
- Browser History
- Undo / Redo
- BFS (Breadth First Search)
- Sliding Window Problems
"""

from collections import deque


# Creating a deque

numbers = deque([10, 20, 30, 40])

print(numbers)

# Output:
# deque([10, 20, 30, 40])


# Empty deque

numbers = deque()

print(numbers)

# Output:
# deque([])


# Creating a deque from a String

letters = deque("Python")

print(letters)

# Output:
# deque(['P', 'y', 't', 'h', 'o', 'n'])


# append() : Adds an element to the right end.

numbers = deque([10, 20, 30])

numbers.append(40)

print(numbers)

# Output:
# deque([10, 20, 30, 40])


# appendleft() : Adds an element to the left end.

numbers = deque([20, 30, 40])

numbers.appendleft(10)

print(numbers)

# Output:
# deque([10, 20, 30, 40])


# pop() : Removes and returns the last element.

numbers = deque([10, 20, 30, 40])

removed = numbers.pop()

print(removed)
print(numbers)

# Output:
# 40
# deque([10, 20, 30])


# popleft() : Removes and returns the first element.

numbers = deque([10, 20, 30, 40])

removed = numbers.popleft()

print(removed)
print(numbers)

# Output:
# 10
# deque([20, 30, 40])


# append() vs appendleft()

numbers = deque([20, 30])

numbers.append(40)
numbers.appendleft(10)

print(numbers)

# Output:
# deque([10, 20, 30, 40])


# pop() vs popleft()

numbers = deque([10, 20, 30, 40])

print(numbers.pop())

# Output:
# 40

print(numbers.popleft())

# Output:
# 10

print(numbers)

# Output:
# deque([20, 30])


# Traversing a deque

numbers = deque([10, 20, 30, 40])

for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30
# 40


# Membership Operators

numbers = deque([10, 20, 30])

print(20 in numbers)

# Output:
# True

print(50 not in numbers)

# Output:
# True

# extend() : Adds multiple elements to the right end.

numbers = deque([10, 20])

numbers.extend([30, 40, 50])

print(numbers)

# Output:
# deque([10, 20, 30, 40, 50])


# extendleft() : Adds multiple elements to the left end.

numbers = deque([30, 40])

numbers.extendleft([20, 10])

print(numbers)

# Output:
# deque([10, 20, 30, 40])

"""
extendleft() inserts elements from left to right,
so the iterable appears reversed in the deque.
"""


# rotate() : Rotates the deque to the right.

numbers = deque([1, 2, 3, 4, 5])

numbers.rotate(2)

print(numbers)

# Output:
# deque([4, 5, 1, 2, 3])


# rotate() with Negative Value : Rotates the deque to the left.

numbers = deque([1, 2, 3, 4, 5])

numbers.rotate(-2)

print(numbers)

# Output:
# deque([3, 4, 5, 1, 2])


# reverse() : Reverses the deque in place.

numbers = deque([10, 20, 30, 40])

numbers.reverse()

print(numbers)

# Output:
# deque([40, 30, 20, 10])


# clear() : Removes all elements from the deque.

numbers = deque([10, 20, 30])

numbers.clear()

print(numbers)

# Output:
# deque([])


# copy() : Creates a shallow copy of the deque.

numbers = deque([10, 20, 30])

copy_numbers = numbers.copy()

print(copy_numbers)

# Output:
# deque([10, 20, 30])


# count() : Returns the number of occurrences of an element.

numbers = deque([10, 20, 10, 30, 10])

print(numbers.count(10))

# Output:
# 3


# index() : Returns the index of the first occurrence.

numbers = deque([10, 20, 30, 40])

print(numbers.index(30))

# Output:
# 2


# insert() : Inserts an element at a specified position.

numbers = deque([10, 20, 40])

numbers.insert(2, 30)

print(numbers)

# Output:
# deque([10, 20, 30, 40])


# remove() : Removes the first occurrence of an element.

numbers = deque([10, 20, 30, 20])

numbers.remove(20)

print(numbers)

# Output:
# deque([10, 30, 20])


# maxlen : Limits the maximum size of a deque.

numbers = deque(maxlen=5)

for number in range(1, 8):
    numbers.append(number)

print(numbers)

# Output:
# deque([3, 4, 5, 6, 7], maxlen=5)

"""
When a deque reaches its maximum length,
adding a new element automatically removes
an element from the opposite end.
"""

# Queue Implementation using deque

"""
Queue follows FIFO (First In, First Out).

The first element inserted is the first one removed.
"""

queue = deque()

queue.append("Rahul")
queue.append("Aman")
queue.append("Priya")

print(queue)

# Output:
# deque(['Rahul', 'Aman', 'Priya'])

print(queue.popleft())

# Output:
# Rahul

print(queue)

# Output:
# deque(['Aman', 'Priya'])

# Stack Implementation using deque

"""
Stack follows LIFO (Last In, First Out).

The last element inserted is the first one removed.
"""

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Output:
# deque([10, 20, 30])

print(stack.pop())

# Output:
# 30

print(stack)

# Output:
# deque([10, 20])

# Browser History

"""
The most recently visited page is removed first
when going back.
"""

history = deque()

history.append("google.com")
history.append("github.com")
history.append("youtube.com")

print(history)

# Output:
# deque(['google.com', 'github.com', 'youtube.com'])

print("Back:", history.pop())

# Output:
# Back: youtube.com

print(history)

# Output:
# deque(['google.com', 'github.com'])


# Recent Messages

"""
A deque with maxlen automatically keeps only
the latest messages.
"""

messages = deque(maxlen=4)

for i in range(1, 7):
    messages.append(f"Message {i}")

print(messages)

# Output:
# deque(['Message 3',
#        'Message 4',
#        'Message 5',
#        'Message 6'],
#       maxlen=4)


# Undo Operation

"""
Undo removes the most recent action.
"""


undo_stack = deque()

undo_stack.append("Typed Hello")
undo_stack.append("Typed World")
undo_stack.append("Deleted Line")

print(undo_stack)

# Output:
# deque(['Typed Hello', 'Typed World', 'Deleted Line'])

print("Undo:", undo_stack.pop())

# Output:
# Undo: Deleted Line

print(undo_stack)

# Output:
# deque(['Typed Hello', 'Typed World'])

# Sliding Window

"""
rotate() is useful for circular movement.
"""

window = deque([1, 2, 3, 4, 5])

window.rotate(1)

print(window)

# Output:
# deque([5, 1, 2, 3, 4])

window.rotate(-2)

print(window)

# Output:
# deque([2, 3, 4, 5, 1])

# Round Robin Scheduling

players = deque([
    "Player 1",
    "Player 2",
    "Player 3",
    "Player 4"
])

for _ in range(4):
    current = players[0]

    print(current)

    players.rotate(-1)

# Output:
# Player 1
# Player 2
# Player 3
# Player 4


"""
Applications of deque
- Queue Implementation
- Stack Implementation
- Browser History
- Undo / Redo Systems
- Sliding Window Problems
- Round Robin Scheduling
- Breadth First Search (BFS)
- Task Scheduling
- Caching
- Message Buffers
"""

# ===============================x=================================