#Dictionaries in Python


y = {'key': 4}
print(y['key'])


'''
WHAT IS A DICTIONARY?

- WELL HERE IS THE BASIC DEFINITION:
    
-Dictionaries are used to store data values in key:value pairs. 
A dictionary is a collection which is ordered*, changeable and 
do not allow duplicates.

'''

#EXAMPLES of what one can do

# x = {'key': 4}
# x['key2'] = 5
# x[2] = [1,2,3,4,5]
# print(x)

#How to check if something is in the dictionary
x = {'key': 4}
print('key' in x)

#How to get all the values from the dictionary
x = {'key': 4}
print(list(x.values()))

#How to get all the keys from the dictionary
x = {'key': 4}
print(list(x.keys()))

#How to DELETE from the dictionary
x = {'key': 4}
del x['key']
print(x)


#How to loop the dictionary
x = {'key': 4}

for key,value in x.items():
    print(key,value)

