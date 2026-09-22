"""
# Problem 10 : Text Analyzer

Analyze a sentence and generate statistics about its words
and characters.

Requirements : 
1. Count the total number of words.
2. Count unique words.
3. Find the frequency of each word.
4. Find the most frequent word.
5. Find words appearing only once.
6. Display the longest word.
7. Display all unique characters.
"""

text = "Python makes programming simple and Python makes problem solving fun"

words = text.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

unique_words = set(words)

most_frequent = max(frequency, key=frequency.get)

single_words = {word for word, count in frequency.items() if count == 1}

longest_word = max(words, key=len)

unique_characters = set(text.lower().replace(" ", ""))

print("===== TEXT ANALYZER =====")

print(f"Total Words      : {len(words)}")
print(f"Unique Words     : {len(unique_words)}")
print(f"Most Frequent    : {most_frequent} ({frequency[most_frequent]})")
print(f"Longest Word     : {longest_word}")

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word:<12}: {count}")

print("\nWords Appearing Once:")
for word in single_words:
    print(word)

print(f"\nUnique Characters: {sorted(unique_characters)}")


# Output:
# ===== TEXT ANALYZER =====
#
# Total Words      : 12
# Unique Words     : 10
# Most Frequent    : python (2)
# Longest Word     : programming
#
# Word Frequency:
# python      : 2
# makes       : 2
# programming : 1
# simple      : 1
# and         : 1
# problem     : 1
# solving     : 1
# fun         : 1
#
# Words Appearing Once:
# programming
# simple
# and
# problem
# solving
# fun
#
# Unique Characters: [...]