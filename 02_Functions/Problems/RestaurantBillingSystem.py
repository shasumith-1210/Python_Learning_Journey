"""
Problem 9: Restaurant Billing System

Build a restaurant billing application using functions.
Allow users to order multiple food items, calculate the
subtotal, apply GST, and display the final bill.
"""

GST_RATE = 0.05


def add_items():
    menu = {
        "Burger": 120,
        "Pizza": 250,
        "Pasta": 180,
        "Sandwich": 100,
        "Coffee": 80
    }

    subtotal = 0

    while True:
        print("\n===== Menu =====")

        for item, price in menu.items():
            print(f"{item:<10} ₹{price}")

        item = input("\nEnter item name (or 'done' to finish): ").title()

        if item == "Done":
            break

        if item in menu:
            quantity = int(input("Enter quantity: "))
            subtotal += menu[item] * quantity
        else:
            print("Item not available.")

    return subtotal


def calculate_gst(amount):
    return amount * GST_RATE


def generate_bill(subtotal, gst):
    total = subtotal + gst

    print("\n===== Restaurant Bill =====")
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"GST (5%) : ₹{gst:.2f}")
    print("--------------------------")
    print(f"Total     : ₹{total:.2f}")


subtotal = add_items()

gst = calculate_gst(subtotal)

generate_bill(subtotal, gst)