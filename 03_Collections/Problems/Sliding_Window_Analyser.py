"""
# Problem 15 : Sliding Window Analyzer

Find the maximum sum of a fixed-size sliding window in a
sequence of values.

Requirements :
1. Create a window of size 3.
2. Calculate the sum of each window.
3. Find the maximum window sum.
4. Display the window producing the maximum sum.
"""

from collections import deque

numbers = [4, 2, 7, 1, 8, 3, 6, 5]
window_size = 3

window = deque()
window_sums = []

for number in numbers:
    window.append(number)

    if len(window) == window_size:
        window_sums.append((list(window), sum(window)))
        window.popleft()

maximum_window = max(window_sums, key=lambda item: item[1])

print("===== SLIDING WINDOW ANALYZER =====")

print("\nWindow Sums:")
for values, total in window_sums:
    print(f"{values} -> {total}")

print(f"\nMaximum Window : {maximum_window[0]}")
print(f"Maximum Sum    : {maximum_window[1]}")


# Output:
# ===== SLIDING WINDOW ANALYZER =====
#
# Window Sums:
# [4, 2, 7] -> 13
# [2, 7, 1] -> 10
# [7, 1, 8] -> 16
# [1, 8, 3] -> 12
# [8, 3, 6] -> 17
# [3, 6, 5] -> 14
#
# Maximum Window : [8, 3, 6]
# Maximum Sum    : 17