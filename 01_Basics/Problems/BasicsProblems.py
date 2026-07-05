# Basic Problems

# 1. Print your name.

print("Shasumith")


# 2. Print your name, age and city.

print("Name: Shasumith")
print("Age: 19")
print("City: Navi Mumbai")


# 3. Add two numbers.

num1 = 20
num2 = 30

print("Sum:", num1 + num2)            # Sum: 50


# 4. Swap two variables.

a = 10
b = 20

a, b = b, a

print("a =", a)                       # a = 20
print("b =", b)                       # b = 10


# 5. Find the area of a rectangle.

length = 10
breadth = 5

area = length * breadth

print("Area:", area)                  # Area: 50


# 6. Find the area of a circle.

radius = 7

area = 3.14 * radius ** 2

print("Area:", area)                  # Area: 153.86


# 7. Convert Celsius to Fahrenheit.

celsius = 30

fahrenheit = (celsius * 9 / 5) + 32

print(fahrenheit)                     # 86.0


# 8. Convert Fahrenheit to Celsius.

fahrenheit = 86

celsius = (fahrenheit - 32) * 5 / 9

print(celsius)                        # 30.0


# 9. Calculate Simple Interest.

principal = 5000
rate = 10
time = 2

si = (principal * rate * time) / 100

print(si)                             # 1000.0


# 10. Calculate Compound Interest.

principal = 5000
rate = 10
time = 2

amount = principal * (1 + rate / 100) ** time

ci = amount - principal

print(round(ci, 2))                   # 1050.0


# 11. Find the square of a number.

number = 8

print(number ** 2)                    # 64


# 12. Find the cube of a number.

number = 5

print(number ** 3)                    # 125


# 13. Calculate the average of three numbers.

a = 20
b = 30
c = 40

average = (a + b + c) / 3

print(average)                        # 30.0


# 14. Convert kilometers to meters.

kilometers = 5

meters = kilometers * 1000

print(meters)                         # 5000


# 15. Convert meters to centimeters.

meters = 8

centimeters = meters * 100

print(centimeters)                    # 800


# 16. Find the remainder of two numbers.

print(17 % 5)                         # 2


# 17. Find quotient and remainder.

a = 17
b = 5

print(a // b)                         # 3
print(a % b)                          # 2


# 18. Find the ASCII value of a character.

print(ord("A"))                       # 65


# 19. Check the data type of a variable.

value = 25.5

print(type(value))                    # <class 'float'>


# 20. Perform all arithmetic operations.

a = 20
b = 6

print(a + b)                          # 26
print(a - b)                          # 14
print(a * b)                          # 120
print(a / b)                          # 3.3333333333333335
print(a // b)                         # 3
print(a % b)                          # 2
print(a ** b)                         # 64000000