#Loops in python

#EXAMPLES

for i in range (10):
    print(i, end="|")

#Input to range, range(start,stop,step)

print(end="\n")

#range(stop)
for i in range (10):
    print(i, end="|")
# this stops at 10 but does not print 10 since n-1

print(end="\n")

#range(start,stop)
for i in range (1,10):
    print(i, end="|")
# this starts at 1 and stops at 10 but does not print 10 since n-1

print(end="\n")
#range(start,stop,step)
for i in range (10,-1,-1):
    print(i, end="|")
# this starts at 10 and stops at -1 and we step by -1
# what does step do? well step is really just incrementing or decrementing

print(end="\n")

'''
NOW THAT YOU KNOW THIS, WELL WHAT ELSE CAN WE DO?

- WE CAN ALSO LOOP THROUGH LISTS
'''
#HERE IS AN EXAMPLE


for i in [1,2,3,5,10]:
    print(i,end="|")

#This just prints 1 2 3 5 10

''''
    WHAT IF WE WANTED TO DO IT A DIFFERENT WAY?
    
    WELL THIS IS HOW WE CAN DO IT :) 
'''
#EXAMPLE
print(end="\n")

x = [1,2,3,5,10]

for i in range (len(x)):
    print(x[i], end="|")

print(end="\n")


#ANOTHER FANCY VERSION OF THIS IS


x = [1,2,3,5,10]

for i, element in enumerate(x):
    print(i, element)

print(end="\n")

'''
    WHAT DOES ENUMERATE DO?
    
    GOOD QUESTION :)
    
    WELL ENUMERATE JUST PROVIDES US WITH BOTH THE
    INDEXES AND ELEMENT DURING ITERATION
    
    THINK OF THIS LIKE PAIRS
    
    HERE IS WHAT I MEAN BY PAIRS:
    0 1 - Index 0 for element 1 
    1 2 - Index 1 for element 2 
    2 3 - Index 2 for element 3 
    3 5 - Index 3 for element 5 
    4 10 - Index 4 for element 10 
    
'''

print(end="\n")

'''
NOW THAT YOU GET THE HANG OF FOR LOOPS

LETS MOVE ONTO WHILE LOOPS

NOTE: A WHILE LOOP ALLOWS US TO EXECUTE A SET OF 
STATEMENTS AS LONG AS A CONDITION IS TRUE

IMPORTANT: REMEMBER TO INCREMENT I OR ELSE THE LOOP 
WILL CONTINUE FOREVER. 

WHAT DO YOU CALL A LOOP THAT CONTINUES FOREVER?

IF YOU THOUGHT OF A INFINITE LOOP, YOU ARE CORRECT :) 

'''

x = [1,2,3,5,10]

#HERE IS AN EXAMPLE OF A WHILE LOOP

i = 0
while i < 10:
    print("run")
    i += 1






