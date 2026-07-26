"""
Problem 5: ATM Simulation

Design a simple ATM system using functions.
Allow users to check their balance, deposit money,
withdraw money, and exit the application through
a menu-driven interface.
"""

balance = 10000


def check_balance():
    print(f"\nCurrent Balance: ₹{balance:.2f}")


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
    else:
        print("Invalid amount.")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")


while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")