#Handling Exceptions

# HANDLING EXCEPTIONS IN PYTHON

# Basic Exception Handling
try:
    x = 7/0                # This will raise a ZeroDivisionError
except Exception as e:
    print(e)              # Output: division by zero
finally:
    print("finally")      # This always executes

# More Specific Exception Handling
try:
    x = 7/0
except ZeroDivisionError as e:    # Catch specific exception first
    print(f"Can't divide by zero: {e}")
except ValueError as e:           # Handle different types of errors
    print(f"Invalid value: {e}")
except Exception as e:            # Catch any other exceptions
    print(f"Other error: {e}")
finally:
    print("Cleanup code here")    # Always runs, even if exception occurs

# Real-World Example
def divide_numbers(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Please provide numbers"
    else:
        return f"Result: {result}"    # Only runs if no exception occurs
    finally:
        print("Calculation attempt completed")

# Testing the function
print(divide_numbers(10, 2))    # Result: 5.0
print(divide_numbers(10, 0))    # Error: Division by zero
print(divide_numbers(10, "2"))  # Error: Please provide numbers

# Multiple Exceptions in One Line
try:
    x = int("abc")
except (ValueError, TypeError) as e:    # Handle multiple exceptions the same way
    print(f"Conversion error: {e}")



