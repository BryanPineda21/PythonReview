#String Methods in python

hello = "hello"
print(type(hello))


#How do we use a method on a string

#What is a method?

 # A method is something with a dot operator


 # For example:

hello = "hello"
print(hello.upper()) # can be called like this

#or

hello = "hello".upper() # Like this
print(hello)

#returns HELLO

# More Examples

hello = "heLLo"
print(hello.lower())

#Returns hello


#----------------
hello = "Hello World"
print(hello.capitalize())

#returns Hello world

#-------------------
hello = "Hello World"
print(hello.count("ll"))

#returns 1 since there is 1 pair of "ll"

#----------------------

x = "Hello"
y = 3
print(x * y)

#returns HelloHelloHello

#-------------------
x = "Hello"
y = "Apple"
print(x + y) # Concatenation

#returns HelloApple

#returns Hello world