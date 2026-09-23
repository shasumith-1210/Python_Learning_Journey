"""
# Problem 13 : Browser History

Simulate browser history using a double-ended queue.

Requirements : 
1. Store visited pages.
2. Visit a new page.
3. Move backward in history.
4. Move forward in history.
5. Display the current page.
6. Limit history to the latest 5 pages.
"""

from collections import deque

history = deque(maxlen=5)

pages = [
    "google.com",
    "github.com",
    "youtube.com",
    "leetcode.com",
    "python.org"
]

for page in pages:
    history.append(page)

print("===== BROWSER HISTORY =====")

print("\nHistory:")
for page in history:
    print(page)

print(f"\nCurrent Page: {history[-1]}")

history.pop()

print("\nAfter Going Back:")
print(f"Current Page: {history[-1]}")

history.append("stackoverflow.com")

print("\nAfter Visiting New Page:")
print(f"Current Page: {history[-1]}")


# Output:
# ===== BROWSER HISTORY =====
#
# History:
# google.com
# github.com
# youtube.com
# leetcode.com
# python.org
#
# Current Page: python.org
#
# After Going Back:
# Current Page: leetcode.com
#
# After Visiting New Page:
# Current Page: stackoverflow.com