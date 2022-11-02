import numpy as np

args_list = ["Stored-Directory", "Non-Volatile-Memory", "Volatile-Memory"]
kwargs_list = {"Volatile-Memory": "Random-Access-Memory", "Non-volatile": "Hard Disk (HDD)"}


def args(*args):
    for items in args:
        print(np.array([items]), end=" ")


def kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value, end=" ")


args(*args_list)
kwargs(**kwargs_list)
