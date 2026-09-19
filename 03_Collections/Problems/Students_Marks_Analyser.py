"""
# Problem 01 : Student Marks Analyzer

Analyze a student's marks and generate a performance summary
using Python dictionaries and data structure utilities.

Requirements
------------
1. Calculate total and average marks.
2. Find highest and lowest scoring subjects.
3. Sort subjects by marks.
4. Find subjects above average.
5. Check whether the student passed every subject.
6. Assign grades to each subject.
"""

marks = {"Python": 85, "DBMS": 78, "DSA": 92, "Mathematics": 88, "Digital Logic": 74}

total = sum(marks.values())
average = total / len(marks)

highest_subject = max(marks, key=marks.get)
lowest_subject = min(marks, key=marks.get)

sorted_marks = sorted(marks.items(), key=lambda item: item[1], reverse=True)

above_average = {subject: mark for subject, mark in marks.items() if mark > average}

passed = all(mark >= 40 for mark in marks.values())


def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


grades = {subject: get_grade(mark) for subject, mark in marks.items()}


print("===== STUDENT PERFORMANCE REPORT =====")

for subject, mark in marks.items():
    print(f"{subject:<15}: {mark}")

print(f"\nTotal Marks     : {total}")
print(f"Average Marks   : {average:.2f}")

print(f"\nHighest Subject : {highest_subject} ({marks[highest_subject]})")
print(f"Lowest Subject  : {lowest_subject} ({marks[lowest_subject]})")

print("\nSorted Marks:")
for subject, mark in sorted_marks:
    print(f"{subject:<15}: {mark}")

print("\nAbove Average:")
for subject in above_average:
    print(subject)

print(f"\nResult          : {'PASS' if passed else 'FAIL'}")

print("\nGrades:")
for subject, grade in grades.items():
    print(f"{subject:<15}: {grade}")


# Output:
# ===== STUDENT PERFORMANCE REPORT =====
#
# Python         : 85
# DBMS           : 78
# DSA            : 92
# Mathematics    : 88
# Digital Logic  : 74
#
# Total Marks     : 417
# Average Marks   : 83.40
#
# Highest Subject : DSA (92)
# Lowest Subject  : Digital Logic (74)
#
# Sorted Marks:
# DSA             : 92
# Mathematics     : 88
# Python          : 85
# DBMS            : 78
# Digital Logic   : 74
#
# Above Average:
# Python
# DSA
# Mathematics
#
# Result          : PASS
#
# Grades:
# Python          : A
# DBMS            : B
# DSA             : A+
# Mathematics     : A
# Digital Logic   : B