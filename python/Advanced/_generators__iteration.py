"""

:return: Iteration, Iterable, Iterator.
:return: Iterable defines as __iter__() and __getitem__()
:return: Iteration defines __next__() object

"""


def generator__function(n):
    for i in range(n):
        yield i


generator_variable__ = generator__function(9000)

while True:
    try:
        print(generator_variable__.__next__())

    except StopIteration as Iteration__stopped:
        print("Iteration stopped ! ", Iteration__stopped)
        break
    else:
        print("Iterator didn't defined properly")
        break

