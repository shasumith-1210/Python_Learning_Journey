"""
# Problem 12 : Transaction Analyzer

Analyze banking transactions and generate an account summary.

Requirements : 
1. Calculate total deposits.
2. Calculate total withdrawals.
3. Calculate the final balance.
4. Group transactions by type.
5. Find the largest transaction.
6. Find accounts with total withdrawals above ₹5000.
"""

transactions = [
    ("Aman", "Deposit", 5000),
    ("Riya", "Deposit", 8000),
    ("Aman", "Withdrawal", 1500),
    ("Rahul", "Deposit", 10000),
    ("Riya", "Withdrawal", 3000),
    ("Aman", "Deposit", 2500),
    ("Rahul", "Withdrawal", 6000),
    ("Riya", "Deposit", 4000)
]

from collections import defaultdict

deposits = defaultdict(float)
withdrawals = defaultdict(float)

for name, transaction_type, amount in transactions:
    if transaction_type == "Deposit":
        deposits[name] += amount
    else:
        withdrawals[name] += amount

balances = {
    name: deposits[name] - withdrawals[name]
    for name in set(deposits) | set(withdrawals)
}

largest_transaction = max(transactions, key=lambda transaction: transaction[2])

high_withdrawals = {
    name: amount
    for name, amount in withdrawals.items()
    if amount > 5000
}

print("===== TRANSACTION ANALYZER =====")

print("\nDeposits:")
for name, amount in deposits.items():
    print(f"{name:<10}: ₹{amount:.2f}")

print("\nWithdrawals:")
for name, amount in withdrawals.items():
    print(f"{name:<10}: ₹{amount:.2f}")

print("\nBalances:")
for name, balance in balances.items():
    print(f"{name:<10}: ₹{balance:.2f}")

print(f"\nLargest Transaction: {largest_transaction}")

print("\nHigh Withdrawal Accounts:")
for name, amount in high_withdrawals.items():
    print(f"{name}: ₹{amount:.2f}")


# Output:
# ===== TRANSACTION ANALYZER =====
#
# Deposits:
# Aman      : ₹7500.00
# Riya      : ₹12000.00
# Rahul     : ₹10000.00
#
# Withdrawals:
# Aman      : ₹1500.00
# Riya      : ₹3000.00
# Rahul     : ₹6000.00
#
# Balances:
# Aman      : ₹6000.00
# Riya      : ₹9000.00
# Rahul     : ₹4000.00
#
# Largest Transaction: ('Rahul', 'Deposit', 10000)
#
# High Withdrawal Accounts:
# Rahul: ₹6000.00