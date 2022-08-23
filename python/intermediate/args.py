def singleArg(*args):
    for a in args:
        print(a)
    if a < 3:
        print("Less than three values")
    elif a > 3:
        print("More than three values")
    else:
        print("Value provided")


singleArg(1, 2, 3)
