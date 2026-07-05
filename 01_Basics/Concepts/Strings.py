# Strings

# Creating Strings

name = "Shasumith"
city = 'Mumbai'
message = """Welcome to Python"""

print(name)  
print(city)
print(message)


# Accessing Characters

print(name[0]) # S
print(name[3]) # s
print(name[-1]) # h


# String Concatenation

first_name = "Shasumith"
last_name = "Kotian"

full_name = first_name + " " + last_name

print(full_name) # Shasumith Kotian


# String Repetition

print("Python " * 3) # Python Python Python


# String Length

print(len(full_name))   # 16


# Checking a Substring

print("Python" in message)  # True
print("Java" not in message) # False


# Comparing Strings

print("apple" == "apple")  # True
print("apple" != "Apple")  # True


