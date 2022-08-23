# Header args

def args_function(*args):
    print(type(args))
    if len(args) == 3:
        print("The name is", args[0], "and the state is", args[1], "And the value is", args[2])
    else:
        print("The name is", args[0], "and the state is", args[1])


# Header kwargs;

def kwargs_function(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(kwargs.items())
        print(key, value)


# Header master function :

def master_args_kwargs(normal, *args, **kwargs):
    print(normal)
    print(type(args))
    print(type(kwargs))

    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(key, value)


master_list = [233, 100]
master_Kwarg_up = {"Min": "Object", "Tuple": "Variables"}
master_args_kwargs("Random arg", *master_list)
