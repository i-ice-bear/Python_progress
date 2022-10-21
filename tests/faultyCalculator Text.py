def faulty_calculator():
    print("Welcome to the calculator, integrate with inputs and calculate")
    get_user_input = int(input("Enter the first number : "))
    get_second_input = int(input("Enter the second number : "))
    get_operator = str(input("Select your operator : "))

    a = "+"
    b = "/"
    c = "-"
    d = "*"

    if get_operator == a:
        if get_user_input == 10 and get_second_input == 20 or get_user_input == 30 and get_second_input == 40:
            print(432)
        else:
            print(get_user_input + get_second_input)

    if get_operator == b:
        if get_user_input == 50 and get_second_input == 60 or get_user_input == 70 and get_second_input == 80:
            print(232)
        else:
            print(get_user_input + get_second_input)

    if get_operator == c:
        if get_user_input == 90 and get_second_input == 100 or get_user_input == 110 and get_second_input == 120:
            print(632)
        else:
            print(get_user_input + get_second_input)

    if get_operator == d:
        if get_user_input == 130 and get_second_input == 140 or get_user_input == 150 and get_second_input == 160:
            print(902)
        else:
            print(get_user_input + get_second_input)

    calculate_again()


def calculate_again():
    again_calculation = str(input("Do you want to calculate again y / n : "))
    if again_calculation == "y":
        faulty_calculator()
    else:
        print("See you never again")


faulty_calculator()
