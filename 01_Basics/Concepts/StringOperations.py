# String Operations

text = "Hello, Python!"

# Length
print(len(text))                      # 14

# Indexing

print(text[0])                        # H
print(text[7])                        # P
print(text[-1])                       # !

# Slicing

print(text[0:5])                      # Hello
print(text[7:])                       # Python!
print(text[:5])                       # Hello
print(text[::2])                      # Hlo yhn
print(text[::-1])                     # !nohtyP ,olleH

# Case Conversion

print(text.upper())                   # HELLO, PYTHON!
print(text.lower())                   # hello, python!
print(text.title())                   # Hello, Python!
print(text.capitalize())              # Hello, python!
print(text.swapcase())                # hELLO, pYTHON!

# Whitespace Removal

message = "   Python Programming   "

print(message.strip())                # Python Programming
print(message.lstrip())               # Python Programming
print(message.rstrip())               #    Python Programming

# Searching

print(text.find("Python"))            # 7
print(text.find("Java"))              # -1

print(text.rfind("o"))                # 10

print(text.index("Python"))           # 7

print(text.count("o"))                # 2

# Replacing

print(text.replace("Python", "Java")) # Hello, Java!

# Startswith & Endswith

print(text.startswith("Hello"))       # True
print(text.endswith("!"))             # True

# Splitting

sentence = "Python Java C++ JavaScript"

print(sentence.split())               # ['Python', 'Java', 'C++', 'JavaScript']
print(sentence.split("a"))            # ['Python J', 'v', ' C++ J', 'v', 'Script']

# Joining

languages = ["Python", "Java", "C++"]

print(", ".join(languages))           # Python, Java, C++


# Checking Methods

sample = "Python123"

print(sample.isalpha())               # False
print(sample.isdigit())               # False
print(sample.isalnum())               # True
print(sample.islower())               # False
print(sample.isupper())               # False
print(sample.istitle())               # True
print(sample.isascii())               # True
print(sample.isidentifier())          # True

print("123".isdigit())                # True
print("python".islower())             # True
print("PYTHON".isupper())             # True
print("Python".istitle())             # True
print("   ".isspace())                # True

# Alignment

word = "Python"

print(word.center(20))
print(word.ljust(20))
print(word.rjust(20))
print(word.zfill(10))                 # 0000Python

# Partition

email = "user@gmail.com"

print(email.partition("@"))           # ('user', '@', 'gmail.com')
print(email.rpartition("@"))          # ('user', '@', 'gmail.com')

# Formatting

name = "Shasumith"
age = 19

print("Name: {}, Age: {}".format(name, age))  # Name: Shasumith, Age: 19

print(f"Name: {name}, Age: {age}")  # Name: Shasumith, Age: 19

# Prefix & Suffix

filename = "program.py"

print(filename.removesuffix(".py"))   # program

url = "https://github.com"

print(url.removeprefix("https://"))   # github.com

# Expand Tabs

text = "Python\tJava\tC++"

print(text.expandtabs(10))


# Encoding

print("Python".encode())              # b'Python'


# Translation

table = str.maketrans("aeiou", "12345")

print("education".translate(table))   # 2d5c1t34n


# String Comparison

print("apple" == "apple")             # True
print("apple" != "Apple")             # True
print("apple" < "banana")             # True

# Membership

print("Python" in text)               # True
print("Java" in text)                 # True
print("C" not in text)                # True