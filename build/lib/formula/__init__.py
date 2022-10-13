import math


def area_of_circle():
    radius = int(input("Enter your radius : "))
    area_formula = math.pi * radius * radius
    print("Your radius is ", area_formula)


class Data:
    def __int__(self):
        print("Constructor ")


area_of_circle()
