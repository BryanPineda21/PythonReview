#Collections in python

#what is a collection?
# a collection is an unordered or ordered group of elements

#LIST AND TUPLES IN PYTHON


#List in python,

x = [4, True, "hi"]
print(len(x))
# prints the length of x


x = [4, True, "hi"]
x.append("John") # Appending an element to the list
print(x)

x = [4, True, "hi"]
x.extend([1,2,3,4,5]) # Extending the list by another list
print(x)


#How to remove an element from the list
x = [4, True, "hi"]
print(x.pop()) # .pop() removes an element from the end of list
               # returns the removed element

print(x)

#NOTE: LISTS are known as mutable



#MOVING ON FROM LISTS, THERE ARE TUPLES AS WELL

#TUPLES ARE THE OPPOSITE OF LISTS, TUPLES ARE IMMUTABLE
#THIS MEANS THAT WE CANNOT APPEND OR REMOVE AN ELEMENT

#USES ROUND BRACKETS INSTEAD OF SQUARE BRACKETS

x = (0,0,1,3,5)
print(x[2])




