# Loops

# For Loop

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4


# range(start, stop)

for i in range(1, 6):
    print(i)
# 1
# 2
# 3
# 4
# 5


# range(start, stop, step)

for i in range(2, 11, 2):
    print(i)
# 2
# 4
# 6
# 8
# 10


# Reverse Loop

for i in range(5, 0, -1):
    print(i)
# 5
# 4
# 3
# 2
# 1


# Loop Through a String

text = "Python"

for ch in text:
    print(ch)
# P
# y
# t
# h
# o
# n


# Loop Through a List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
# Apple
# Banana
# Mango


# While Loop

count = 1

while count <= 5:
    print(count)
    count += 1
# 1
# 2
# 3
# 4
# 5


# Break

for i in range(1, 11):
    if i == 6:
        break
    print(i)
# 1
# 2
# 3
# 4
# 5


# Continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# 1
# 2
# 4
# 5


# Pass

for i in range(3):
    pass

print("Loop Completed")
# Loop Completed


# Nested Loops

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


# else with for

for i in range(3):
    print(i)
else:
    print("Loop Finished")
# 0
# 1
# 2
# Loop Finished


# else with while

num = 1

while num <= 3:
    print(num)
    num += 1
else:
    print("While Loop Finished")
# 1
# 2
# 3
# While Loop Finished