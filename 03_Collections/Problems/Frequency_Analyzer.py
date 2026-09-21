"""
# Problem 05 : Frequency Analyzer

Analyze a collection of products and find how frequently
each product appears.

Requirements : 
1. Count the frequency of each product.
2. Find the most frequently purchased product.
3. Find products purchased only once.
4. Sort products by frequency.
5. Display the total number of purchases.
"""

purchases = [
    "Laptop", "Mouse", "Keyboard", "Laptop",
    "Mouse", "Laptop", "Headphones", "Keyboard",
    "Mouse", "Monitor", "Laptop", "Headphones"
]

frequency = {}

for product in purchases:
    frequency[product] = frequency.get(product, 0) + 1

most_frequent = max(frequency, key=frequency.get)

single_purchases = {product for product, count in frequency.items() if count == 1}

sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)


print("===== PRODUCT FREQUENCY ANALYZER =====")

print("\nProduct Frequency:")
for product, count in sorted_frequency:
    print(f"{product:<15}: {count}")

print(f"\nMost Purchased  : {most_frequent} ({frequency[most_frequent]})")

print("\nPurchased Once:")
for product in single_purchases:
    print(product)

print(f"\nTotal Purchases : {len(purchases)}")


# Output:
# ===== PRODUCT FREQUENCY ANALYZER =====
#
# Product Frequency:
# Laptop         : 4
# Mouse          : 3
# Keyboard       : 2
# Headphones     : 2
# Monitor        : 1
#
# Most Purchased  : Laptop (4)
#
# Purchased Once:
# Monitor
#
# Total Purchases : 12