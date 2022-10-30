import numpy as np


def args_function(normal, *args, **kwargs):
    print(args)
    print(type(args))
    print(normal)
    for items in args:
        name_array = items
        print(name_array)
    for key, value in kwargs.items():
        print(f"the key", key, value)  # prints in single string
    print(kwargs)  # prints in type of dictionary


args_list = ["Harry", "Rohan"]
kwargs_list = {"Harry": 32, "Bois": 23, "Community": 36}
normal_argument = "it's normal babes"
args_function(normal_argument, *args_list, **kwargs_list)
