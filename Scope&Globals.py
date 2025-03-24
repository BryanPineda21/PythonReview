#SCOPE IN PYTHON

# HOW DOES SCOPING WORK IN PYTHON? OR IN GENERAL?

# Scope refers to where variables can be accessed in your code. Python follows the LEGB rule:
# Local → Enclosed → Global → Built-in

# -------- Global Scope Example --------
message = "I'm a global variable"  # Global scope


def print_message():
    print(message)  # Can access global variable


print_message()  # Output: I'm a global variable


# -------- Local Scope Example --------
def calculate_sum():
    x = 10  # Local variable
    y = 20  # Local variable
    return x + y


print(calculate_sum())  # Output: 30
# print(x)  # This would raise an error - x is not accessible here

# -------- Modifying Global Variables --------
counter = 0


def increment_counter():
    global counter  # Must declare global to modify
    counter += 1


increment_counter()
print(counter)  # Output: 1


# -------- Best Practices --------
# Good Practice: Pass as parameters
def good_function(data):
    return data * 2


# Bad Practice: Relying on global
global_data = 10


def bad_function():
    return global_data * 2


# -------- Nested Functions Example --------
def outer_function():
    message = "Hello"  # Enclosed scope

    def inner_function():
        print(message)  # Can access parent's scope

    inner_function()