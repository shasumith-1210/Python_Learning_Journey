# Type Casting

# Implicit Type Casting : Also known as type coercion or automatic conversion, this happens without the programmer's intervention. 
# Compilers do this safely by automatically promoting "smaller" data types to "larger" ones to avoid data loss.

num = 10
decimal = 5.5

result = num + decimal

print(result)
print(type(result))


# Explicit Type Casting : Also known as type conversion, this requires manual instructions. The programmer explicitly specifies the target type in parentheses before the value. This is typically done when converting a larger data type to a smaller one (known as narrowing), which can lead to data loss or truncation.

age = "19"

print(type(age))

age = int(age)

print(age)
print(type(age))


price = 99

price = float(price)

print(price)
print(type(price))


marks = 95.8

marks = int(marks)

print(marks)
print(type(marks))


number = 100

number = str(number)

print(number)
print(type(number))


value = 1

value = bool(value)

print(value)
print(type(value))