import statistics

a = 10
b = 100
c = sum((a, b))
print(c)


# build in function hit ctrl + mouse click to open inbuilt function

# self defined function { doesn't return anything }
def selfFunction():
    print("Self defined function")


def averageFunction(e, d):
    """ this makes the average function of two numbers, and
     it doesn't work for three numbers careful with that """
    # upper line is the docstring
    average_statement = (e + d) / 2
    return average_statement


function_variable = averageFunction(10, 20)
print(function_variable)


print(averageFunction.__doc__)