import numpy as np
from functools import lru_cache


def __Random_numpy__array():
    """
    :return: Generates an array, with the given attribute,
    """
    numpy_array = np.array([1, 2, 3, 4], dtype=np.int32)
    arrange_numpy_numbers = np.arange(9)
    print(arrange_numpy_numbers)
    print(numpy_array.itemsize)
    print(numpy_array)


def __dimensional__arrays():
    __2d_dimension = np.array([[1, 2, 3], [3, 2, 1]])
    print(__2d_dimension)


__dimensional__arrays()


if __name__ == '__main__':
    @lru_cache(maxsize=40)
    def __math_random_numpy(x_co_ordinate_1, x_co_ordinate_2, y_co_ordinate_1, y_co_ordinate_2):
        import math
        try:
            distance_formula_logarithm = \
                math.sqrt((int(x_co_ordinate_2) - int(x_co_ordinate_1)) ^ 2
                          + (int(y_co_ordinate_2) - int(y_co_ordinate_1)) ^ 2)
            print("The distance of the co-ordinates is : ", distance_formula_logarithm)
            print("Distances are : ", x_co_ordinate_2, x_co_ordinate_1, y_co_ordinate_2, y_co_ordinate_1)
        except TypeError as Typo_integration_error:
            print("Value not provided", Typo_integration_error[10])
        else:
            exit()


    print(__math_random_numpy(2, 6, 2, 6))
