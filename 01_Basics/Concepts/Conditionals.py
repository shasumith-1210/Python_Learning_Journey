# Conditional Statements

# if Statement

age = 18

if age >= 18:
    print("You are eligible to vote.")      # You are eligible to vote.


# if-else Statement

number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")                            # Odd


# if-elif-else Statement

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")                        # Grade B
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# Nested if

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")             # You can drive.
    else:
        print("License required.")
else:
    print("You are underage.")


# Short Hand if

x = 10

if x > 5:
    print("x is greater than 5")            # x is greater than 5


# Short Hand if-else (Ternary Operator)

a = 20
b = 15

print("a is greater") if a > b else print("b is greater")
# a is greater


# Multiple Conditions

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")               # Login Successful
else:
    print("Invalid Credentials")


# Using 'or'

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")                        # Weekend
else:
    print("Weekday")


# Using 'not'

is_logged_in = False

if not is_logged_in:
    print("Please login.")                  # Please login.

# Pass Statement

age = 18

if age >= 18:
    pass