"""
# Problem 11 : Student Record Manager

Manage student records and generate class performance statistics.

Requirements : 
1. Calculate each student's average marks.
2. Find the class topper.
3. Find students who passed all subjects.
4. Find students with an average above 80.
5. Calculate subject-wise averages.
6. Display students in descending order of average.
"""

students = {
    "Aman": {"Python": 85, "DBMS": 78, "DSA": 92},
    "Riya": {"Python": 91, "DBMS": 88, "DSA": 95},
    "Rahul": {"Python": 72, "DBMS": 68, "DSA": 75},
    "Sneha": {"Python": 88, "DBMS": 84, "DSA": 90},
    "Karan": {"Python": 65, "DBMS": 72, "DSA": 70}
}

averages = {
    student: sum(marks.values()) / len(marks)
    for student, marks in students.items()
}

topper = max(averages, key=averages.get)

passed_students = {
    student
    for student, marks in students.items()
    if all(mark >= 40 for mark in marks.values())
}

high_performers = {
    student: average
    for student, average in averages.items()
    if average > 80
}

subjects = students["Aman"].keys()

subject_averages = {
    subject: sum(students[student][subject] for student in students) / len(students)
    for subject in subjects
}

sorted_students = sorted(averages.items(), key=lambda item: item[1], reverse=True)

print("===== STUDENT RECORD MANAGER =====")

print("\nStudent Averages:")
for student, average in sorted_students:
    print(f"{student:<10}: {average:.2f}")

print(f"\nClass Topper : {topper} ({averages[topper]:.2f})")

print("\nStudents Who Passed:")
for student in passed_students:
    print(student)

print("\nStudents Above 80:")
for student, average in high_performers.items():
    print(f"{student}: {average:.2f}")

print("\nSubject Averages:")
for subject, average in subject_averages.items():
    print(f"{subject:<10}: {average:.2f}")


# Output:
# ===== STUDENT RECORD MANAGER =====
#
# Student Averages:
# Riya      : 91.33
# Sneha     : 87.33
# Aman      : 85.00
# Rahul     : 71.67
# Karan     : 69.00
#
# Class Topper : Riya (91.33)
#
# Students Who Passed:
# Aman
# Riya
# Rahul
# Sneha
# Karan
#
# Students Above 80:
# Aman: 85.00
# Riya: 91.33
# Sneha: 87.33
#
# Subject Averages:
# Python    : 80.20
# DBMS      : 78.00
# DSA       : 84.40