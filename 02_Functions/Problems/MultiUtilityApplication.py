"""
Problem 15: Multi-Utility Application

Develop a menu-driven utility program that combines
multiple mathematical operations into a single application.
Implement each operation using a separate function.
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


def factorial(number):
    if number == 0 or number == 1:
        return 1

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def fibonacci(terms):
    first = 0
    second = 1

    for _ in range(terms):
        print(first, end=" ")

        first, second = second, first + second

    print()


while True:
    print("\n===== Multi-Utility Application =====")
    print("1. Prime Number Check")
    print("2. Palindrome Check")
    print("3. Armstrong Number Check")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a number: "))

        if is_prime(number):
            print(f"{number} is a Prime Number.")
        else:
            print(f"{number} is not a Prime Number.")

    elif choice == "2":
        number = int(input("Enter a number: "))

        if is_palindrome(number):
            print(f"{number} is a Palindrome.")
        else:
            print(f"{number} is not a Palindrome.")

    elif choice == "3":
        number = int(input("Enter a number: "))

        if is_armstrong(number):
            print(f"{number} is an Armstrong Number.")
        else:
            print(f"{number} is not an Armstrong Number.")

    elif choice == "4":
        number = int(input("Enter a number: "))
        print("Factorial =", factorial(number))

    elif choice == "5":
        terms = int(input("Enter the number of terms: "))
        fibonacci(terms)

    elif choice == "6":
        print("Thank you for using the application!")
        break

    else:
        print("Invalid choice. Please try again.")