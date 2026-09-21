"""
# Problem 06 : Employee Department Grouper

Group employees according to their departments and generate
a department-wise employee report.

Requirements : 
1. Group employees by department.
2. Display all employees in each department.
3. Count employees in each department.
4. Find the department with the most employees.
5. Find departments having more than 2 employees.
"""

employees = [
    ("Aman", "CSE"),
    ("Riya", "IT"),
    ("Rahul", "CSE"),
    ("Sneha", "AIML"),
    ("Karan", "CSE"),
    ("Priya", "IT"),
    ("Arjun", "AIML"),
    ("Neha", "CSE"),
    ("Rohan", "IT")
]

from collections import defaultdict

departments = defaultdict(list)

for employee, department in employees:
    departments[department].append(employee)

department_counts = {department: len(names) for department, names in departments.items()}

largest_department = max(department_counts, key=department_counts.get)

large_departments = {
    department: count
    for department, count in department_counts.items()
    if count > 2
}

print("===== DEPARTMENT REPORT =====")

for department, names in departments.items():
    print(f"\n{department}:")
    for name in names:
        print(f"- {name}")

print("\nEmployee Count:")
for department, count in department_counts.items():
    print(f"{department:<10}: {count}")

print(f"\nLargest Department: {largest_department}")

print("\nDepartments With More Than 2 Employees:")
for department in large_departments:
    print(department)


# Output:
# ===== DEPARTMENT REPORT =====
#
# CSE:
# - Aman
# - Rahul
# - Karan
# - Neha
#
# IT:
# - Riya
# - Priya
# - Rohan
#
# AIML:
# - Sneha
# - Arjun
#
# Employee Count:
# CSE       : 4
# IT        : 3
# AIML      : 2
#
# Largest Department: CSE
#
# Departments With More Than 2 Employees:
# CSE
# IT