"""
Problem 6: Factorial Comparison

Calculate the factorial of a number using both
iterative and recursive approaches. Display the
result from each method and compare the two
implementations.
"""

def iterative_factorial(number):
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    return factorial


def recursive_factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * recursive_factorial(number - 1)


number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    iterative_result = iterative_factorial(number)
    recursive_result = recursive_factorial(number)

    print("\n===== Factorial Comparison =====")
    print("Iterative Factorial :", iterative_result)
    print("Recursive Factorial :", recursive_result)

    if iterative_result == recursive_result:
        print("Both methods produced the same result.")
    else:
        print("The results are different.")