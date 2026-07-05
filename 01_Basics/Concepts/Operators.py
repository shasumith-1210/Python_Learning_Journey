# Operators

# Arithmetic Operators

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# Comparison Operators

x = 15
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# Assignment Operators

num = 10

num += 5
print(num)

num -= 3
print(num)

num *= 2
print(num)

num /= 4
print(num)


# Logical Operators

p = True
q = False

print(p and q)
print(p or q)
print(not p)


# Membership Operators

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)
print("Orange" not in fruits)


# Identity Operators

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)

# Bitwise Operators

a = 10
b = 4

# Bitwise AND (&)
print("a & b =", a & b)

# Bitwise OR (|)
print("a | b =", a | b)

# Bitwise XOR (^)
print("a ^ b =", a ^ b)

# Bitwise NOT (~)
print("~a =", ~a)

# Left Shift (<<)
print("a << 2 =", a << 2)

# Right Shift (>>)
print("a >> 2 =", a >> 2)