"""
# Problem 18 : Product Frequency Counter

Analyze product purchases using Counter and generate a purchase-frequency report.

Requirements : 
1. Count product purchases.
2. Find the top 3 products.
3. Find products purchased only once.
4. Compare two days of purchases.
5. Find products purchased on both days.
"""

from collections import Counter

day_1 = ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Monitor"]
day_2 = ["Mouse", "Laptop", "Headphones", "Mouse", "Keyboard", "Laptop"]

count_1 = Counter(day_1)
count_2 = Counter(day_2)

combined = count_1 + count_2

top_products = combined.most_common(3)

single_products = {
    product
    for product, count in combined.items()
    if count == 1
}

common_products = set(count_1) & set(count_2)

print("===== PRODUCT FREQUENCY REPORT =====")

print("\nCombined Frequency:")
for product, count in combined.most_common():
    print(f"{product:<15}: {count}")

print("\nTop 3 Products:")
for product, count in top_products:
    print(f"{product:<15}: {count}")

print("\nPurchased Once:")
for product in single_products:
    print(product)

print("\nPurchased On Both Days:")
for product in common_products:
    print(product)


# Output:
# ===== PRODUCT FREQUENCY REPORT =====
#
# Combined Frequency:
# Laptop         : 4
# Mouse          : 4
# Keyboard       : 2
# Monitor        : 1
# Headphones     : 1
#
# Top 3 Products:
# Laptop         : 4
# Mouse          : 4
# Keyboard       : 2
#
# Purchased Once:
# Monitor
# Headphones
#
# Purchased On Both Days:
# Laptop
# Mouse
# Keyboard