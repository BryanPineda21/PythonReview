#ARGS & **KWARGS in python

def func(x):
    def func2():
        print(x)

    return func2

func(3)()


#ARGS & **KWARGS

'''
WHAT DOES THE EXAMPLE BELOW DO?
    - Essentially it unpacks whatever is in the list
'''
x = [1,23,10,5]
print(*x)


#EXAMPLE
def func(x,y):
    print(x,y)

pairs = [(1,2),(3,4)]

for pair in pairs:
    func(*pair) #Note, * is for list and ** is for sets

'''
    NOW THAT YOU KIND OF GET THE IDEA!
    
    LETS SEE HOW ARGS & **KWARGS COME INTO PLAY
'''


def func(*args, **kwargs):
    print(args, kwargs)

func(1,2,3,4, one = 3, three= 2)
