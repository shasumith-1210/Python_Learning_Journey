"""
Problem 12: Banking System

Build a simple banking application using functions.
Provide features such as account creation, deposits,
withdrawals, money transfers, and balance inquiry
through a menu-driven interface.
"""

accounts = {}


def create_account():
    account_number = input("Enter Account Number: ")

    if account_number in accounts:
        print("Account already exists.")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: ₹"))

    accounts[account_number] = {
        "name": name,
        "balance": balance
    }

    print("Account created successfully.")


def deposit():
    account_number = input("Enter Account Number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter Amount to Deposit: ₹"))
    accounts[account_number]["balance"] += amount

    print("Amount deposited successfully.")


def withdraw():
    account_number = input("Enter Account Number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    amount = float(input("Enter Amount to Withdraw: ₹"))

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount
        print("Amount withdrawn successfully.")


def transfer():
    sender = input("Enter Sender Account Number: ")
    receiver = input("Enter Receiver Account Number: ")

    if sender not in accounts or receiver not in accounts:
        print("Invalid account number.")
        return

    amount = float(input("Enter Amount to Transfer: ₹"))

    if amount > accounts[sender]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[sender]["balance"] -= amount
        accounts[receiver]["balance"] += amount
        print("Transfer completed successfully.")


def check_balance():
    account_number = input("Enter Account Number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    print(f"Current Balance: ₹{accounts[account_number]['balance']:.2f}")


while True:
    print("\n===== Banking System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        transfer()
    elif choice == "5":
        check_balance()
    elif choice == "6":
        print("Thank you for using the Banking System.")
        break
    else:
        print("Invalid choice. Please try again.")