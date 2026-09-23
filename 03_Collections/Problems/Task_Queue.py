"""
# Problem 14 : Task Queue

Build a task processing system using a deque.

Requirements : 
1. Add tasks to the queue.
2. Process tasks in FIFO order.
3. Add an urgent task to the front.
4. Display completed tasks.
5. Display remaining tasks.
"""

from collections import deque

tasks = deque(["Compile Code", "Run Tests", "Generate Report", "Push to GitHub"])

completed = []

tasks.append("Deploy Application")
tasks.appendleft("Fix Critical Bug")

while tasks:
    task = tasks.popleft()
    completed.append(task)

print("===== TASK PROCESSOR =====")

print("\nCompleted Tasks:")
for task in completed:
    print(f"✓ {task}")

print("\nRemaining Tasks:")
for task in tasks:
    print(task)

print(f"\nTotal Completed: {len(completed)}")


# Output:
# ===== TASK PROCESSOR =====
#
# Completed Tasks:
# ✓ Fix Critical Bug
# ✓ Compile Code
# ✓ Run Tests
# ✓ Generate Report
# ✓ Push to GitHub
# ✓ Deploy Application
#
# Remaining Tasks:
#
# Total Completed: 6