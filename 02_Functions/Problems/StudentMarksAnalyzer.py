"""
Problem 14: Student Marks Analyzer

Create a program that accepts any number of student
marks using *args. Calculate and display useful
statistics such as the total, average, highest,
lowest, and grade of the entered marks.
"""

def analyze_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def display_result(total, average, highest, lowest, grade):
    print("\n===== Student Marks Report =====")
    print("Total Marks :", total)
    print("Average Marks :", round(average, 2))
    print("Highest Marks :", highest)
    print("Lowest Marks :", lowest)
    print("Grade :", grade)


number_of_subjects = int(input("Enter the number of subjects: "))

marks = []

for subject in range(number_of_subjects):
    mark = float(input(f"Enter marks for Subject {subject + 1}: "))
    marks.append(mark)

total, average, highest, lowest = analyze_marks(*marks)

grade = assign_grade(average)

display_result(total, average, highest, lowest, grade)