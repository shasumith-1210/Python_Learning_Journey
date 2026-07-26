"""
Problem 3: Password Validator

Create a password validation system using functions.
Verify whether a password satisfies basic security rules
and display whether it is valid or invalid.
"""

def has_uppercase(password):
    return any(character.isupper() for character in password)


def has_lowercase(password):
    return any(character.islower() for character in password)


def has_digit(password):
    return any(character.isdigit() for character in password)


def has_special_character(password):
    special_characters = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

    return any(character in special_characters for character in password)


def is_valid_password(password):
    if len(password) < 8:
        return False

    if not has_uppercase(password):
        return False

    if not has_lowercase(password):
        return False

    if not has_digit(password):
        return False

    if not has_special_character(password):
        return False

    return True


password = input("Enter Password: ")

if is_valid_password(password):
    print("Password is Valid.")
else:
    print("Password is Invalid.")