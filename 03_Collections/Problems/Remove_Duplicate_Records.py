"""
# Problem 03 : Remove Duplicate Records

Clean a list of student records by removing duplicate entries
while keeping the original order.

Requirements : 
1. Identify duplicate student records.
2. Remove duplicates.
3. Preserve the original order.
4. Display the number of duplicate records removed.
5. Display the cleaned records.
"""

students = [
    ("Aman", 20, "CSE"),
    ("Riya", 19, "IT"),
    ("Rahul", 21, "CSE"),
    ("Aman", 20, "CSE"),
    ("Sneha", 20, "AIML"),
    ("Riya", 19, "IT"),
    ("Karan", 21, "CSE")
]

unique_students = []
seen = set()

for student in students:
    if student not in seen:
        seen.add(student)
        unique_students.append(student)

duplicates_removed = len(students) - len(unique_students)

print("===== STUDENT RECORD CLEANER =====")

print("\nOriginal Records:")
for student in students:
    print(student)

print("\nCleaned Records:")
for student in unique_students:
    print(student)

print(f"\nOriginal Count    : {len(students)}")
print(f"Unique Count      : {len(unique_students)}")
print(f"Duplicates Removed: {duplicates_removed}")


# Output:
# ===== STUDENT RECORD CLEANER =====
#
# Original Records:
# ('Aman', 20, 'CSE')
# ('Riya', 19, 'IT')
# ('Rahul', 21, 'CSE')
# ('Aman', 20, 'CSE')
# ('Sneha', 20, 'AIML')
# ('Riya', 19, 'IT')
# ('Karan', 21, 'CSE')
#
# Cleaned Records:
# ('Aman', 20, 'CSE')
# ('Riya', 19, 'IT')
# ('Rahul', 21, 'CSE')
# ('Sneha', 20, 'AIML')
# ('Karan', 21, 'CSE')
#
# Original Count    : 7
# Unique Count      : 5
# Duplicates Removed: 2