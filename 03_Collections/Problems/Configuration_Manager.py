"""
# Problem 16 : Configuration Manager

Build a configuration system using multiple configuration
sources with different priorities.

Requirements : 
1. Store default settings.
2. Store user settings.
3. Store temporary settings.
4. Give higher priority to newer configurations.
5. Access the final configuration.
6. Display all available settings.
"""

from collections import ChainMap

default_config = {
    "theme": "light", "language": "English",
    "font_size": 14, "notifications": True
}

user_config = {"theme": "dark", "font_size": 16}

temporary_config = {"notifications": False}

config = ChainMap(temporary_config, user_config, default_config)

print("===== CONFIGURATION MANAGER =====")

print(f"Theme         : {config['theme']}")
print(f"Language      : {config['language']}")
print(f"Font Size     : {config['font_size']}")
print(f"Notifications : {config['notifications']}")

print("\nAvailable Settings:")
for key in config:
    print(f"{key}: {config[key]}")


# Output:
# ===== CONFIGURATION MANAGER =====
#
# Theme         : dark
# Language      : English
# Font Size     : 16
# Notifications : False
#
# Available Settings:
# theme: dark
# language: English
# font_size: 16
# notifications: False