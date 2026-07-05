# User Input

# The input() by default takes the argument as String data type 

# Taking String Input

name = input("Enter your name: ")

print("Name:", name)


# Taking Integer Input

age = int(input("Enter your age: "))

print("Age:", age)


# Taking Float Input

height = float(input("Enter your height: "))

print("Height:", height)


# Taking Multiple Inputs

city, country = input("Enter your city and country: ").split()

print("City:", city)
print("Country:", country)


# Taking Multiple Integer Inputs

num1, num2 = map(int, input("Enter two numbers: ").split())

print("First Number:", num1)
print("Second Number:", num2)
print("Sum:", num1 + num2)