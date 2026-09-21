"""
# Problem 07 : Contact Book

Build a contact book that stores and manages people's contact
information using a dictionary.

Requirements : 
1. Display all contacts.
2. Add a new contact.
3. Update an existing contact.
4. Search for a contact.
5. Find contacts from a specific city.
6. Remove a contact.
"""

contacts = {
    "Aman": {"phone": "9876543210", "city": "Mumbai"},
    "Riya": {"phone": "9123456780", "city": "Pune"},
    "Rahul": {"phone": "9988776655", "city": "Mumbai"},
    "Sneha": {"phone": "9090909090", "city": "Nashik"}
}

contacts["Karan"] = {"phone": "9345678901", "city": "Pune"}

contacts["Aman"]["phone"] = "9000011111"

search_name = "Rahul"

mumbai_contacts = {
    name: details
    for name, details in contacts.items()
    if details["city"] == "Mumbai"
}

removed_contact = contacts.pop("Sneha")

print("===== CONTACT BOOK =====")

print("\nAll Contacts:")
for name, details in contacts.items():
    print(f"{name:<10}: {details['phone']} | {details['city']}")

print(f"\nSearch Result:")
if search_name in contacts:
    print(f"{search_name}: {contacts[search_name]}")
else:
    print("Contact not found.")

print("\nMumbai Contacts:")
for name in mumbai_contacts:
    print(name)

print(f"\nRemoved Contact: Sneha")


# Output:
# ===== CONTACT BOOK =====
#
# All Contacts:
# Aman      : 9000011111 | Mumbai
# Riya      : 9123456780 | Pune
# Rahul     : 9988776655 | Mumbai
# Karan     : 9345678901 | Pune
#
# Search Result:
# Rahul: {'phone': '9988776655', 'city': 'Mumbai'}
#
# Mumbai Contacts:
# Aman
# Rahul
#
# Removed Contact: Sneha