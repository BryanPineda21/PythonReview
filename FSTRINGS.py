# FSTRINGS IN PYTHON

# Basic f-string with variables
apple = 100
x = f'HELLO {6+8} {apple}'
print(x)  # Output: HELLO 14 100

# Different Ways to Use f-strings
name = "Alice"
age = 25
price = 49.99

# Simple variable insertion
print(f"My name is {name}")  # Output: My name is Alice

# Expressions inside f-strings
print(f"In 5 years, I'll be {age + 5}")  # Output: In 5 years, I'll be 30

# Formatting numbers
print(f"Price: ${price:.2f}")  # Output: Price: $49.99

# Using dictionaries
person = {"name": "Bob", "age": 30}
print(f"Name: {person['name']}")  # Output: Name: Bob

# Multiple lines
message = f"""
Name: {name}
Age: {age}
Price: ${price:.2f}
"""

# Advanced Formatting
number = 42

# Width and alignment
print(f"|{name:>10}|")  # Right align, width 10
print(f"|{name:<10}|")  # Left align, width 10
print(f"|{name:^10}|")  # Center align, width 10

# Number formatting
print(f"Binary: {number:b}")    # Binary format
print(f"Hex: {number:x}")       # Hexadecimal format
print(f"Scientific: {number:e}") # Scientific notation

# Datetime formatting
from datetime import datetime
now = datetime.now()
print(f"Date: {now:%Y-%m-%d}")  # Custom date format

# Using quotes inside f-strings
print(f'He said "Hello"')       # Use different quotes
print(f"It's a nice day")       # Mix quotes as needed