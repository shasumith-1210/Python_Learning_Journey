# Match Case

# Basic Match

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")            # Wednesday
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")


# Match Multiple Values

letter = "a"

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")                # Vowel
    case _:
        print("Consonant")


# Match with Numbers

number = 20

match number:
    case 10:
        print("Ten")
    case 20:
        print("Twenty")               # Twenty
    case 30:
        print("Thirty")
    case _:
        print("Unknown Number")


# Match with Guard

age = 19

match age:
    case age if age >= 18:
        print("Adult")                # Adult
    case _:
        print("Minor")


# Match with Strings

fruit = "Apple"

match fruit:
    case "Apple":
        print("Red Fruit")            # Red Fruit
    case "Banana":
        print("Yellow Fruit")
    case "Mango":
        print("King of Fruits")
    case _:
        print("Fruit Not Found")


# Match with Boolean

is_logged_in = True

match is_logged_in:
    case True:
        print("Welcome!")             # Welcome!
    case False:
        print("Please Login")


# Simple Calculator

operator = "+"

a = 20
b = 10

match operator:
    case "+":
        print(a + b)                  # 30
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid Operator")