#SETS IN PYTHON


x = set()

''''

WHAT ARE SETS?
- SETS ARE ESSENTIALLY AN UNORDERED UNIQUE COLLECTION OF ELEMENTS

WHAT DOES THIS REALLY MEAN?

    - What this really means is that there is:
        - No duplicate elements
        - We dont care about order or frequency of elements
    
    - What do really care about?
        - We just care if the element is there or not

'''''

#EXAMPLES

s = {4,32,5,6,5}
print(s)


#Adding an element to the set
s = {4,32,5,6,5}
s.add(3)
print(s)

#Removing an element to the set
s = {4,32,5,6,5}
s.remove(6)
print(s)

#Checking for an element in the set
s = {4,32,5,6,5}
print(6 in s)



