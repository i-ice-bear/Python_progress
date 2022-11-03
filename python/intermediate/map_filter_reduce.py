"""
    Map function map() : the map function is the most powerful function
    which runs very effectively in programs. In a single line.

    :Important: list() function is compulsory for returning the list using with
                the map function like array-string{boolean} conversion. anything
                else etc.

    :return: Anatomy of map({inbuilt-parameters}, {for_which_should_logic_applied} )

"""

number_list = ["2", "4", "6", "8", "10"]  # assigned a number array in the form of integer
function_map_list = list(map(int, number_list))  # converted number array into integer via map.
print(function_map_list)

square_array = [2, 4, 6, 8, 10]


def num_to_square(element):
    """
    :param: multiplication of number from the number for getting the square element:
    :return: element * element ( 2 * 2 )
    """
    return element * element
    pass


square_loops = list(map(num_to_square, square_array))
print(square_loops)

"""
    Iteration from for-loop works like map function 
"""


# def for_loop_looping():
#     for i in range(len(number_list)):
#         number_list[i] = int(number_list[i])
#     number_list[4] = number_list[4]
#     print(number_list)


def square_func(square_element):
    return square_element * square_element
    pass


def cube_func(cube_element):
    return cube_element * cube_element * cube_element
    pass


function_array = [square_func, cube_func]

for i in range(3):
    val_exec = list(map(lambda x: x(i), function_array))
    print(val_exec)


