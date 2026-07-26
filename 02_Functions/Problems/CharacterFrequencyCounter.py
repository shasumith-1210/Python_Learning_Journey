"""
Problem 13: Character Frequency Counter

Write a program that counts the frequency of every
character in a string without using collections.Counter
or any external libraries.
"""

def character_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


def display_frequency(frequency):
    print("\n===== Character Frequency =====")

    for character, count in frequency.items():
        if character == " ":
            print(f"'Space' : {count}")
        else:
            print(f"'{character}' : {count}")


text = input("Enter a string: ")

frequency = character_frequency(text)

display_frequency(frequency)