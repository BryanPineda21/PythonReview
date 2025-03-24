#EXEPTIONS IN PYTHON

raise Exception('BAD')

# EXCEPTIONS IN PYTHON

# Basic Exception Raising
raise Exception('Something went wrong!')  # Generic exception
raise ValueError('Invalid input!')        # Specific built-in exception

# Try-Except Basic Structure
try:
    number = int("not a number")
except ValueError as e:
    print(f"Conversion error: {e}")

# Multiple Exception Handling
try:
    file = open("nonexistent.txt")
    number = int(file.readline())
except FileNotFoundError:
    print("File doesn't exist!")
except ValueError:
    print("Couldn't convert to number!")
except Exception as e:
    print(f"Something else went wrong: {e}")

# Using Else and Finally
try:
    number = int("42")
except ValueError:
    print("Not a valid number")
else:
    print("Conversion succeeded!")  # Runs if no exception occurs
finally:
    print("This always runs")      # Cleanup code goes here

# Custom Exceptions
class CustomError(Exception):
    def __init__(self, message="My custom error"):
        self.message = message
        super().__init__(self.message)

# Raising Custom Exception
try:
    raise CustomError("Something specific went wrong!")
except CustomError as e:
    print(f"Caught custom error: {e}")

# Context Managers (with statement)
with open("file.txt", "w") as file:  # File automatically closes after block
    file.write("Hello")