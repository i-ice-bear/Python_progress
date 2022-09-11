import numpy as np

array_state = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array_state)


def argsFunction(*args):
    print(type(args))
    if len(args) == 3:
        return "args len is : 3"
    else:
        print("args is initially working")


def kwargsFunction(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items:
        print(key, value)
    if len(kwargs == 3):
        print("args length is", len(kwargs))
    else:
        print("args is initially working")


