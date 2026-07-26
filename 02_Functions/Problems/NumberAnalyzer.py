"""
Problem 11: Number Analyzer

Create a program that analyzes a given number using
separate functions. Determine whether the number is
Prime, Palindrome, and Armstrong, then display all
the results together.
"""

def is_prime(number):
    if number <= 1:
        return False

    for value in range(2, int(number ** 0.5) + 1):
        if number % value == 0:
            return False

    return True


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def is_armstrong(number):
    digits = str(number)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number


def display_result(number):
    print("\n===== Number Analysis =====")
    print("Number :", number)
    print("Prime :", is_prime(number))
    print("Palindrome :", is_palindrome(number))
    print("Armstrong :", is_armstrong(number))


number = int(input("Enter a number: "))

display_result(number)