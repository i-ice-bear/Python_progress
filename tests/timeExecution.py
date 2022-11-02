import time as time

current_time = time.time()


def first_iteration(n):
    """
    :raises: Iteration recursion
    :return: Iterative recursion along with fibonacci mathematical
             algorithm.
    :except: [n = n * n - 1 * n - 2......;
    """
    factorial_starter_index = 1
    for i in range(n):
        factorial_starter_index = factorial_starter_index * (i + 1)
    return factorial_starter_index


fibonacci_input = int(input("Enter the number : "))
print(first_iteration(fibonacci_input))
first_iteration_time = current_time - time.time()
print(first_iteration_time)


def second_iteration(number_recursion):
    if number_recursion == 1:
        return 1
    else:
        fibonacci_number = number_recursion * second_iteration(number_recursion - 1)
        return fibonacci_number


print(second_iteration(fibonacci_input))
first_iteration_time = current_time - time.time()
print(first_iteration_time)
