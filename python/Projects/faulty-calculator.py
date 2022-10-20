import numpy as np


def calculation():
    first_number = int(input("Enter the first number : "))
    type_of_calculation = str(input("Enter the operator : "))
    second_number = int(input("Enter the second number : "))

    a = "+"
    b = "-"
    c = "/"
    d = "*"

    if type_of_calculation == a:
        if first_number == 53 and second_number == 5 or first_number == 80 and second_number == 10:
            print(900)
        else:
            print(first_number - second_number + 324)

    if type_of_calculation == b:
        if first_number == 20 and second_number == 10 or first_number == 90 and second_number == 20:
            print(8323)
        else:
            print(first_number + second_number + 12)

    if type_of_calculation == c:
        if first_number == 73 and second_number == 43 or first_number == 234 and second_number == 90:
            print(90032)
        else:
            print(first_number * second_number + 32)

    if type_of_calculation == d:
        if first_number == 23 and second_number == 90 or first_number == 283 and second_number == 123:
            print(234235)
        else:
            print(first_number / second_number + 233)
    againCalculation()


def againCalculation():
    again_calculation = input("Do you want to calculate again : ")
    if again_calculation == "y":
        calculation()
    elif again_calculation == "n":
        print("See you later")
    else:
        againCalculation()


calculation()
