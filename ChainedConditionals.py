# Chained Conditionals

x = 7
y = 3
z = 5
result1 = x == y
result2 = y > x
result3 =  z < x + 2

# How to make a condition that uses the results

# You can use the following separate keywords

# and, or , not


#Here is an example

result4 = result1 or not result2 or result3

print(result4)

#IMPORTANT NOTE
    # not comes first
    # and comes second
    # or comes last
# This is important because these
# are the precedence for these key words
