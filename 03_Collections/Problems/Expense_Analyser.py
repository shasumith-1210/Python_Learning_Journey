"""
# Problem 02 : Expense Analyzer

Analyze personal expenses by category and generate a spending summary.

Requirements
------------
1. Calculate total expenses.
2. Calculate average expense.
3. Find the highest expense.
4. Calculate total spending by category.
5. Find the highest-spending category.
6. Find expenses above ₹500.
7. Sort categories by total spending.
"""

expenses = [
    ("Food", 250),
    ("Travel", 120),
    ("Food", 180),
    ("Shopping", 1500),
    ("Travel", 80),
    ("Food", 300),
    ("Entertainment", 600),
    ("Shopping", 750)
]

total = sum(amount for category, amount in expenses)
average = total / len(expenses)

highest_expense = max(expenses, key=lambda expense: expense[1])

category_totals = {}

for category, amount in expenses:
    category_totals[category] = category_totals.get(category, 0) + amount

highest_category = max(category_totals, key=category_totals.get)

large_expenses = [(category, amount) for category, amount in expenses if amount > 500]

sorted_categories = sorted(category_totals.items(), key=lambda item: item[1], reverse=True)


print("===== EXPENSE REPORT =====")

print(f"Total Expenses   : ₹{total}")
print(f"Average Expense  : ₹{average:.2f}")

print(f"\nHighest Expense  : {highest_expense[0]} (₹{highest_expense[1]})")

print("\nCategory Spending:")
for category, amount in category_totals.items():
    print(f"{category:<15}: ₹{amount}")

print(f"\nHighest Category : {highest_category} (₹{category_totals[highest_category]})")

print("\nExpenses Above ₹500:")
for category, amount in large_expenses:
    print(f"{category:<15}: ₹{amount}")

print("\nCategories by Spending:")
for category, amount in sorted_categories:
    print(f"{category:<15}: ₹{amount}")


# Output:
# ===== EXPENSE REPORT =====
# Total Expenses   : ₹3780
# Average Expense  : ₹472.50
#
# Highest Expense  : Shopping (₹1500)
#
# Category Spending:
# Food           : ₹730
# Travel         : ₹200
# Shopping       : ₹2250
# Entertainment  : ₹600
#
# Highest Category : Shopping (₹2250)
#
# Expenses Above ₹500:
# Shopping       : ₹1500
# Entertainment  : ₹600
# Shopping       : ₹750
#
# Categories by Spending:
# Shopping       : ₹2250
# Food           : ₹730
# Entertainment  : ₹600
# Travel         : ₹200