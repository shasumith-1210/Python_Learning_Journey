"""
# Problem 04 : Inventory Manager

Build a simple inventory system to manage products and their stock.

Requirements : 
1. Display all products and their stock.
2. Add a new product.
3. Update existing stock.
4. Find products with low stock.
5. Calculate the total number of items.
6. Find the product with the highest stock.
7. Remove an out-of-stock product.
"""

inventory = {"Laptop": 12, "Keyboard": 25, "Mouse": 40, "Monitor": 8, "Headphones": 15}

# Add a new product
inventory["Webcam"] = 10

# Update stock
inventory["Mouse"] += 10

# Find low-stock products
low_stock = {product: stock for product, stock in inventory.items() if stock < 10}

# Calculate total items
total_items = sum(inventory.values())

# Find product with highest stock
highest_stock_product = max(inventory, key=inventory.get)

# Remove out-of-stock products
inventory = {product: stock for product, stock in inventory.items() if stock > 0}


print("===== INVENTORY REPORT =====")

print("\nProducts:")
for product, stock in inventory.items():
    print(f"{product:<15}: {stock}")

print(f"\nTotal Items     : {total_items}")
print(f"Highest Stock   : {highest_stock_product} ({inventory[highest_stock_product]})")

print("\nLow Stock:")
for product, stock in low_stock.items():
    print(f"{product:<15}: {stock}")


# Output:
# ===== INVENTORY REPORT =====
#
# Products:
# Laptop         : 12
# Keyboard       : 25
# Mouse          : 50
# Monitor        : 8
# Headphones     : 15
# Webcam         : 10
#
# Total Items     : 110
# Highest Stock   : Mouse (50)
#
# Low Stock:
# Monitor        : 8