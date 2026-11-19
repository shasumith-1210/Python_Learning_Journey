"""
# Problem 17 : Student Record

Represent student records using namedtuple and analyze their academic performance.

Requirements : 
1. Create student records.
2. Access fields by name.
3. Calculate average marks.
4. Find the student with the highest marks.
5. Display the records.
"""

from collections import namedtuple

Student = namedtuple("Student", ["name", "roll_no", "marks"])

students = [
    Student("Aman", 101, 85),
    Student("Riya", 102, 92),
    Student("Rahul", 103, 78),
    Student("Sneha", 104, 88)
]

average = sum(student.marks for student in students) / len(students)

topper = max(students, key=lambda student: student.marks)

print("===== STUDENT RECORDS =====")

for student in students:
    print(f"{student.name:<10} | Roll No: {student.roll_no} | Marks: {student.marks}")

print(f"\nClass Average : {average:.2f}")
print(f"Topper        : {topper.name} ({topper.marks})")


# Output:
# ===== STUDENT RECORDS =====
#
# Aman       | Roll No: 101 | Marks: 85
# Riya       | Roll No: 102 | Marks: 92
# Rahul      | Roll No: 103 | Marks: 78
# Sneha      | Roll No: 104 | Marks: 88
#
# Class Average : 85.75
# Topper        : Riya (92)