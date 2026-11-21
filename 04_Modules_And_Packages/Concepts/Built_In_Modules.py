# Topic - 3

"""
PYTHON BUILT-IN MODULES

Python provides a collection of ready-to-use modules
through its standard library.

These modules help us perform common tasks without
writing everything from scratch.

Some commonly used modules are:
1. math
2. random
3. datetime
4. os
5. sys
6. statistics
7. time
8. calendar
9. json
10. pathlib
"""

# 1. MATH MODULE

import math

# Mathematical calculations

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("GCD:", math.gcd(12, 18))

# Mathematical constants

print("PI:", math.pi)
print("Euler's Number:", math.e)


# 2. RANDOM MODULE

import random

# Generate a random integer

print("Random Number:", random.randint(1, 100))

# Generate a random floating-point number

print("Random Float:", random.random())

# Select a random element

subjects = ["Python", "Java", "DBMS", "DSA"]
print("Random Subject:", random.choice(subjects))

# Shuffle a list

numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print("Shuffled List:", numbers)

# Select multiple random elements

print("Random Samples:", random.sample(subjects, 2))


# 3. DATETIME MODULE

import datetime

# Get the current date and time

current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Get the current date

current_date = datetime.date.today()
print("Current Date:", current_date)

# Create a specific date

birth_date = datetime.date(2005, 8, 15)
print("Birth Date:", birth_date)

# Extract date components

print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)

# Calculate the difference between dates

future_date = datetime.date(2027, 1, 1)
difference = future_date - current_date

print("Days Until 2027:", difference.days)


# 4. OS MODULE

import os

# Get the current working directory

print("Current Directory:", os.getcwd())

# Get the operating system name

print("Operating System:", os.name)

# List files and folders in the current directory

print("Directory Contents:", os.listdir())

# Check whether a path exists

print("File Exists:", os.path.exists("sample.txt"))

# Get the file extension

print("File Extension:", os.path.splitext("notes.txt")[1])

# Create a directory

# os.mkdir("NewFolder")

# Rename a file

# os.rename("old.txt", "new.txt")

# Delete a file

# os.remove("sample.txt")

# Note: The above modification statements are commented
# to prevent accidental changes to your files.


# 5. SYS MODULE

import sys

# Get the Python version

print("Python Version:", sys.version)

# Get the Python executable location

print("Python Executable:", sys.executable)

# Get the platform information

print("Platform:", sys.platform)

# Get the maximum size of an integer

print("Maximum Integer Size:", sys.maxsize)

# Get command-line arguments

print("Command Line Arguments:", sys.argv)

# Get the module search path

print("Module Search Path:", sys.path)


# 6. STATISTICS MODULE

import statistics

marks = [85, 90, 78, 92, 85, 88, 95]

# Calculate statistical values

print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))
print("Mode:", statistics.mode(marks))
print("Standard Deviation:", statistics.stdev(marks))
print("Variance:", statistics.variance(marks))


# 7. TIME MODULE

import time

# Get the current timestamp

print("Current Timestamp:", time.time())

# Display the current local time

print("Local Time:", time.ctime())

# Pause program execution

print("Starting...")
time.sleep(2)
print("Finished after 2 seconds.")

# Measure execution time

start_time = time.perf_counter()

total = sum(range(1, 1000001))

end_time = time.perf_counter()

print("Total:", total)
print("Execution Time:", end_time - start_time)


# 8. CALENDAR MODULE

import calendar

# Display a calendar for a particular month

print(calendar.month(2026, 11))

# Check whether a year is a leap year

print("Is Leap Year:", calendar.isleap(2028))

# Get the number of days in a month

print("Days in November 2026:", calendar.monthrange(2026, 11)[1])


# 9. JSON MODULE

import json

# Python dictionary

student = {"name": "Aman", "age": 20, "branch": "AIML"}

# Convert Python object into JSON string

json_data = json.dumps(student)
print("JSON String:", json_data)

# Convert JSON string back into Python object

python_data = json.loads(json_data)
print("Python Dictionary:", python_data)

# Access values

print("Student Name:", python_data["name"])


# 10. PATHLIB MODULE

from pathlib import Path

# Get the current working directory

current_path = Path.cwd()
print("Current Path:", current_path)

# Create a path object

file_path = Path("notes.txt")

# Check whether the path exists

print("Path Exists:", file_path.exists())

# Get file information

print("File Name:", file_path.name)
print("File Extension:", file_path.suffix)
print("File Stem:", file_path.stem)

# Create a directory

# Path("NewFolder").mkdir(exist_ok=True)

# Pathlib provides an object-oriented way
# to work with file and directory paths.


# IMPORTANT NOTES

"""
1. Standard library modules are provided with Python.
2. They do not usually require separate installation.
3. We must import a module before using its contents.
4. Different modules serve different purposes.
5. We can explore module documentation to understand
   additional functions and features.
"""
