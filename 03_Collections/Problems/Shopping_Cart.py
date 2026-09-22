"""
# Problem 09 : Shopping Cart

Build a shopping cart that calculates item-wise and total costs
for a customer's purchase.

Requirements :  
1. Store products, prices, and quantities.
2. Calculate the cost of each item.
3. Calculate the subtotal.
4. Apply a discount if the subtotal exceeds ₹2000.
5. Calculate the final bill.
6. Display the most expensive item.
"""

cart = {
    "Laptop": {"price": 55000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1},
    "Headphones": {"price": 2500, "quantity": 1}
}

item_totals = {
    product: details["price"] * details["quantity"]
    for product, details in cart.items()
}

subtotal = sum(item_totals.values())

discount = subtotal * 0.10 if subtotal > 2000 else 0

final_amount = subtotal - discount

most_expensive = max(item_totals, key=item_totals.get)

print("===== SHOPPING CART =====")

print("\nItems:")
for product, total in item_totals.items():
    print(f"{product:<15}: ₹{total}")

print(f"\nSubtotal        : ₹{subtotal}")
print(f"Discount        : ₹{discount:.2f}")
print(f"Final Amount    : ₹{final_amount:.2f}")
print(f"Highest Item    : {most_expensive} (₹{item_totals[most_expensive]})")


# Output:
# ===== SHOPPING CART =====
#
# Items:
# Laptop         : ₹55000
# Mouse          : ₹1600
# Keyboard       : ₹1500
# Headphones     : ₹2500
#
# Subtotal        : ₹60600
# Discount        : ₹6060.00
# Final Amount    : ₹54540.00
# Highest Item    : Laptop (₹55000) 