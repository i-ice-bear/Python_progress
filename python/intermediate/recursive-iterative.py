"""
   Factorial :
   n! = n * n-1 * n-2 * n-3.....1
   n! = n * (n-1)

"""


# Iterative method
def factorialFunction_iterative(n):
    factorialNum = 1
    for i in range(n):
        factorialNum = factorialNum * (i + 1)  # it returns only 1
    return factorialNum


userInput = int(input("Enter your number : "))
# print(factorialFunction_iterative(userInput))


# Recursive method
def factorial_recursive(numberRecursive):
    """
       :return: IT works like this
        numberRecursive * factorial_recursive(numberRecursive - 1)
        if value provided as 5 :
        then it gonna to be executed like this
        5 * factorial_recursive(4)
        5 * 4 factorial_recursive(3)
        5 * 4 * 3 factorial_recursive(2)
        5 * 4 * 3 * 2 factorial_recursive(1)
        = 120

        { Like a binary search }

    """
    if numberRecursive == 1:
        return 1
    else:
        return numberRecursive * factorial_recursive(numberRecursive - 1)


# print(factorial_recursive(userInput))


def fibonacci(n):
    """
    :return [0, 1, 1, 2, 3, 5, 8, 12, 20, 32, 52, 84...]:
    """

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(userInput))


# use recursion for normal programs and easy programs
# use iterative for complex and big programs