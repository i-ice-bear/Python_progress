"""
    There are two types of scope variables in python :
        1. Global scope variable : defines in the global state
        2. local scope variable : defines in a function

"""

l = 100  # global scope variable


def function1(n):
    print(n, "I added something")
    l = 50  # local scope variable
    print(l)


function1("I was me")
print(l)
