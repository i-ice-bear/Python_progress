def _copy_function():
    """
        :return: Created the copy of the function into a new variable
        :param : If a function get deleted then it creates a copy into
                 a new variable
    """
    return print("Random-string")


a = _copy_function
del _copy_function
print(a)


def return_func(num):
    """
    :param num: Conditional function return
    :return: if num == 0 then it prints the print
             function. Passed in the argument
    """
    if num == 0:
        return print
    elif num == 1:
        return sum


a = return_func(1)
print(a)


def __function__executor__(function):
    """
        :return: Creates a skeleton then it run a python inbuilt function
        :rtype: Passed in argument
    """
    function("Run by a skeleton")


__function__executor__(print)


def __decorators(__function_1):
    def __inner_dec():
        print("Executing now")
        __function_1()
        print("Executed")
    return __inner_dec()


@__decorators
def __decorators__2():
    print("decorators")