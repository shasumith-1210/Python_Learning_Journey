# Loop Problems

# 1. Print numbers from 1 to 10.

for i in range(1, 11):
    print(i)


# 2. Print numbers from 10 to 1.

for i in range(10, 0, -1):
    print(i)


# 3. Print even numbers from 1 to 100.

for i in range(2, 101, 2):
    print(i)


# 4. Print odd numbers from 1 to 100.

for i in range(1, 101, 2):
    print(i)


# 5. Find the sum of first n natural numbers.

n = int(input("\nEnter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# 6. Find the factorial of a number.

number = int(input("\nEnter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)


# 7. Generate the multiplication table of a number.

number = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# 8. Count the number of digits in a number.

number = int(input("\nEnter a number: "))

count = 0

while number != 0:
    count += 1
    number //= 10

print("Digits:", count)


# 9. Reverse a number.

number = int(input("\nEnter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse:", reverse)


# 10. Check whether a number is a palindrome.

number = int(input("\nEnter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 11. Check whether a number is an Armstrong number.

number = int(input("\nEnter a number: "))

original = number
digits = len(str(number))
total = 0

while number > 0:
    digit = number % 10
    total += digit ** digits
    number //= 10

if original == total:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 12. Check whether a number is a Strong number.

number = int(input("\nEnter a number: "))

original = number
total = 0

while number > 0:
    digit = number % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    total += factorial
    number //= 10

if original == total:
    print("Strong Number")
else:
    print("Not a Strong Number")


# 13. Check whether a number is a Perfect number.

number = int(input("\nEnter a number: "))

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i

if total == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# 14. Print the Fibonacci series.

terms = int(input("\nEnter number of terms: "))

first = 0
second = 1

for i in range(terms):
    print(first, end=" ")
    first, second = second, first + second


# 15. Check whether a number is prime.

number = int(input("\nEnter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")


# 16. Print all prime numbers in a given range.

start = int(input("\nEnter start: "))
end = int(input("Enter end: "))

for number in range(start, end + 1):

    if number <= 1:
        continue

    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)


# 17. Find the GCD of two numbers.

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD:", a)


# 18. Find the LCM of two numbers.

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

greater = max(a, b)

while True:
    if greater % a == 0 and greater % b == 0:
        print("LCM:", greater)
        break
    greater += 1


# 19. Print all factors of a number.

number = int(input("\nEnter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)


# 20. Count vowels and consonants in a string.

text = input("\nEnter a string: ")

vowels = 0
consonants = 0

for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)