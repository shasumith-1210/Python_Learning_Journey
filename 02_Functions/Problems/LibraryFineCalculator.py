"""
Problem 8: Library Fine Calculator

Develop a program to calculate the library fine
based on the number of overdue days. Use functions
to determine the fine amount and display the final
amount to the user.
"""

def calculate_fine(days_late):
    if days_late <= 0:
        return 0
    elif days_late <= 5:
        return days_late * 2
    elif days_late <= 10:
        return days_late * 5
    else:
        return days_late * 10


def display_bill(days_late, fine):
    print("\n===== Library Fine Receipt =====")
    print("Days Late :", days_late)
    print(f"Fine Amount : ₹{fine}")


days_late = int(input("Enter the number of overdue days: "))

fine = calculate_fine(days_late)

display_bill(days_late, fine)