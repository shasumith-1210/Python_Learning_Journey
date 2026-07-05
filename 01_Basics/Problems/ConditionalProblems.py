# Conditional Problems

# 1. Check whether a number is positive, negative or zero.

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd.

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Find the largest of two numbers.

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)


# 4. Find the largest of three numbers.

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 5. Check whether a year is a leap year.

year = int(input("\nEnter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 6. Check voting eligibility.

age = int(input("\nEnter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# 7. Assign grades based on marks.

marks = int(input("\nEnter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")


# 8. Check whether a character is a vowel or consonant.

ch = input("\nEnter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# 9. Check whether a character is uppercase or lowercase.

ch = input("\nEnter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an Alphabet")


# 10. Check whether a number is divisible by 5 and 11.

number = int(input("\nEnter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")


# 11. Find the smallest of three numbers.

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest:", a)
elif b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)


# 12. Check whether a number is a multiple of both 3 and 7.

number = int(input("\nEnter a number: "))

if number % 3 == 0 and number % 7 == 0:
    print("Yes")
else:
    print("No")


# 13. Check whether a person can donate blood.

age = int(input("\nEnter age: "))
weight = int(input("Enter weight: "))

if age >= 18 and weight >= 50:
    print("Eligible")
else:
    print("Not Eligible")


# 14. Find profit or loss.

cost_price = float(input("\nEnter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    print("Profit")
elif selling_price < cost_price:
    print("Loss")
else:
    print("No Profit No Loss")


# 15. Check whether a triangle is valid.

a = int(input("\nEnter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# 16. Check whether a character is an alphabet.

ch = input("\nEnter a character: ")

if ch.isalpha():
    print("Alphabet")
else:
    print("Not an Alphabet")


# 17. Check whether a character is a digit.

ch = input("\nEnter a character: ")

if ch.isdigit():
    print("Digit")
else:
    print("Not a Digit")


# 18. Check whether a number is a three-digit number.

number = int(input("\nEnter a number: "))

if 100 <= abs(number) <= 999:
    print("Three-Digit Number")
else:
    print("Not a Three-Digit Number")


# 19. Check whether a number is divisible by both 2 and 3.

number = int(input("\nEnter a number: "))

if number % 2 == 0 and number % 3 == 0:
    print("Yes")
else:
    print("No")


# 20. Simple Calculator using match-case.

num1 = float(input("\nEnter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Division by zero is not allowed.")
    case _:
        print("Invalid Operator")