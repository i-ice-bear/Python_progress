get_args = float(input("Get your args : "))


def args(*args):
    print(type(args))
    if get_args > 3:
        print(["Arg-1", "Arg-2", "Arg-3", "Arg-4", "Arg-", args])
        print("Args is greater than 3")
    elif get_args < 3:
        print(["Arg-1", "Arg-2", "Arg-3"])
        print("Args is smaller than 3 ")
    else:
        print("Args is equally working")


def kwargs(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
    if get_args == 4:
        print("Args", "Arg-1", "Arg", "Arg-2")


kwargs()
