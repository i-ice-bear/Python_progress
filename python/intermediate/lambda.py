"""
   lambda function is a one line function which is used
   to create the one line function. Which is also known
   as Anonymous function its use for convenience not for
   big production usage.
"""

decrease_lambda = lambda x, y: x - y
print(decrease_lambda(3, 4))


# sort function with lambda and normal function

# def sortIteration(a):
#     return a[1]

sortIteration = lambda a: a[1]

"""
   Here the nth number of list in list prints in the 
   ascending order. [0, 1] list works like this
"""
list_list = [[2, 5], [5, 3], [3, 1]]
list_list.sort(key=sortIteration)
# or list_list.sort(key=lambda a:a[1])
print(list_list)
