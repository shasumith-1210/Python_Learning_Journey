"""
Problem 10: Recreate Built-in Functions

Implement your own versions of common Python
built-in functions such as max(), min(), sum(),
and len() without using their built-in implementations.
"""

def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def find_min(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


def find_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def find_length(items):
    count = 0

    for _ in items:
        count += 1

    return count


numbers = []

size = int(input("How many numbers do you want to enter? "))

for index in range(size):
    number = int(input(f"Enter number {index + 1}: "))
    numbers.append(number)

print("\n===== Results =====")
print("Maximum Value :", find_max(numbers))
print("Minimum Value :", find_min(numbers))
print("Sum :", find_sum(numbers))
print("Length :", find_length(numbers))