"""
Problem 7: Fibonacci Generator

Generate the Fibonacci sequence using a recursive function.
Allow the user to specify the number of terms and display
the generated sequence.
"""

def fibonacci(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


def generate_fibonacci(terms):
    sequence = []

    for index in range(terms):
        sequence.append(fibonacci(index))

    return sequence


terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    fibonacci_sequence = generate_fibonacci(terms)

    print("\n===== Fibonacci Sequence =====")
    print(fibonacci_sequence)