# Method 1 : Import the complete module
import calculator.addition
print(calculator.addition.add(10,5))

# Method 2 : Import a module using from 
from calculator import subtraction
print(subtraction.subtract(10,5))

# Method 3 : Import a specific function

from calculator.multiplication import multiply
print(multiply(10,5))

# Importing Multiple Modules from a package 

from calculator import addition, subtraction, multiplication, division
print(addition.add(20,10))
print(subtraction.subtract(20,10))
print(multiplication.multiply(20,10))
print(division.divide(20,10))


