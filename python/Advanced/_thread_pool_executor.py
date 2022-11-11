from concurrent.futures import ThreadPoolExecutor
from time import sleep

cubic_numerics = [2, 4, 6, 8]
_cube_numerics = list(map(lambda x: x * x * x, cubic_numerics))
print(_cube_numerics)


def cube(x):
    return x * x * x


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as exe:
        exe.submit(_cube_numerics, 2)
        result = exe.map(cube, cubic_numerics)

    for i in result:
        print(i)

