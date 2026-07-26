"""
Problem 2: Student Result Management

Create a program to manage a student's academic results.
Use functions to calculate the total marks, average,
percentage, and grade, then display the final result.
"""

def input_marks():
    marks = []

    for subject in range(1, 6):
        mark = float(input(f"Enter marks for Subject {subject}: "))
        marks.append(mark)

    return marks


def calculate_total(marks):
    return sum(marks)


def calculate_average(total, subjects):
    return total / subjects


def calculate_percentage(total, maximum_marks):
    return (total / maximum_marks) * 100


def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def display_result(marks, total, average, percentage, grade):
    print("\n===== Student Result =====")
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


marks = input_marks()

total = calculate_total(marks)

average = calculate_average(total, len(marks))

percentage = calculate_percentage(total, 500)

grade = assign_grade(percentage)

display_result(marks, total, average, percentage, grade)