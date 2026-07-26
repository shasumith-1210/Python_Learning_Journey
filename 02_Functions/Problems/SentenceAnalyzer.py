"""
Problem 4: Sentence Analyzer

Write a program that analyzes a given sentence.
Using functions, determine statistics such as the number
of words, vowels, consonants, digits, spaces,
and special characters.
"""

def count_words(sentence):
    return len(sentence.split())


def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for character in sentence:
        if character in vowels:
            count += 1

    return count


def count_consonants(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for character in sentence:
        if character.isalpha() and character not in vowels:
            count += 1

    return count


def count_digits(sentence):
    count = 0

    for character in sentence:
        if character.isdigit():
            count += 1

    return count


def count_spaces(sentence):
    count = 0

    for character in sentence:
        if character == " ":
            count += 1

    return count


def count_special_characters(sentence):
    count = 0

    for character in sentence:
        if not character.isalnum() and character != " ":
            count += 1

    return count


def display_analysis(sentence):
    print("\n===== Sentence Analysis =====")
    print("Sentence :", sentence)
    print("Words :", count_words(sentence))
    print("Vowels :", count_vowels(sentence))
    print("Consonants :", count_consonants(sentence))
    print("Digits :", count_digits(sentence))
    print("Spaces :", count_spaces(sentence))
    print("Special Characters :", count_special_characters(sentence))


sentence = input("Enter a sentence: ")

display_analysis(sentence)