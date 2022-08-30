# iterators in generator runs only one time

def generator(n):
    for int in range(n):
        print(int)
        yield int


print(generator(1000))

# iterators in next loop which runs on next looping base

fruits = ["Apple", "Banana", "Guava", "Grapes", "Anything-else"];

fruits_iterator = iter(fruits);
print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
