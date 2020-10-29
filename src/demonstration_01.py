"""
Challenge #1:

Create a function that takes two numbers as arguments and return their sum.

Examples:
- addition(3, 2) ➞ 5
- addition(-3, -6) ➞ -9
- addition(7, 3) ➞ 10
"""

'''
def addition(a, b):
    # Your code here
    # set a sum to the value of the express a plus b
    
    # return our sum to the caller

    pass #pass is added here so the linter doesn't get mad
'''

def anotherAddition(a, b):
    # Your code here
    # set a sum to the value of the express a plus b
    sum = a + b
    return sum

print(anotherAddition(3,2))
print(anotherAddition(-3,-2))
print(anotherAddition(298,2))

# another way to do above 
def andAnotherAddition(a, b):
    # Your code here
    # RETURN the sum to the value of the express a plus b
    return a + b

print(andAnotherAddition(3,2))
print(andAnotherAddition(-3,-2))
print(andAnotherAddition(298,2))





''' intro notes
typing python3 will access repl
where you can print directly in the terminal
"hello" will return 'hello'
23 will return 23
and print('bye') will return 'bye'
to exit repl, type quit()
to start a function or define a function, use the def keyword
'''

'''
storing a variable in python
label <assignment operator> value
a = 1
^ example of assignments
b = 2
^ example of assignments
2 + b
^ example of expressions

you assign labels to expressions, e.g.
thisIsMath = 2 + b
or even better c = 2 + b, just make sure the name of the label makes sense

c = a + b -> 1 + 2 -> 3 
c = 3

we can use the return keyword e.g. return c

'''

