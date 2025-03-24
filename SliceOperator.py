#SLICING IN PYTHON



y = ["hi", "hello", "goodbye", "cya", "lol"]
s = "hello"


'''

    sliced = [start:stop:step]
    
    WHAT DOES THIS REMIND YOU OF? REMEMBER FOR LOOPS?
    
    - Its pretty much the same with
      START, STOP, STEP
'''

#HERE IS AN EXAMPLE IN ACTION

x = [0,1,2,3,4,5,6,7,8]

sliced = x[0:4:2]

print(sliced)


#How else can this be used, well lets reverse a list

x = [0,1,2,3,4,5,6,7,8]

sliced = x[::-1]

print(sliced)