# MAPS & FILTER IN PYTHON

# Example 1: Using map() to add 2 to each element
x = [1,2,3,4,5,5,6,67,7,8,9,10]

# map() applies the lambda function to each element in x
# lambda i: i + 2 means "take input i and return i + 2"
mp = map(lambda i: i + 2, x)
print(list(mp))  # Convert map object to list for display
# Output: [3,4,5,6,7,7,8,69,9,10,11,12]

print(end="\n")

# Example 2: Using filter() to get even numbers
x = [1,2,3,4,5,5,6,67,7,8,9,10]

# filter() keeps elements where lambda function returns True
# lambda i: i % 2 == 0 means "keep i if dividing by 2 gives no remainder"
mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))  # Convert filter object to list for display
# Output: [2,4,6,8,10]


'''
Q: What is map() in Python?
 - map() is a built-in function that applies a given function to each item in an iterable (like list, tuple). It returns a map object that can be converted to a list or other sequence types.

Q: What is filter() in Python?
 - filter() is a built-in function that creates an iterator of elements that return True when passed to the given function. It filters out elements that don't meet the condition.
Q: What's the difference between map() and filter()?
 - map() transforms each element, while filter() selects elements based on a condition. map() keeps the same number of elements (unless None is returned), while filter() can reduce the number of elements.

Q: Why use lambda functions with map() and filter()?
 - Lambda functions provide a concise way to write simple functions without defining them separately. They're especially useful for one-time operations.

Q: Can I use regular functions instead of lambda?
 - Yes! Example:

    def add_two(x):
        return x + 2
        
    numbers = [1, 2, 3]
    result = map(add_two, numbers)
    
    
Q: Why do we need list() around map() and filter()?
 - map() and filter() return iterator objects. Converting to list() allows us to see all elements at once and reuse them (iterators can only be used once).

Q: Can map() and filter() be used with other data types?
 - Yes! They work with any iterable (lists, tuples, sets, etc.):
    # With tuple
    numbers = (1, 2, 3, 4)
    mapped = map(lambda x: x*2, numbers)

# With string
filtered = filter(lambda x: x.isupper(), "Hello World")
'''



