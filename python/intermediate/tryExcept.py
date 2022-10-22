try:
    first_input = int(input("Enter the number first : "))
    second_input = int(input("Enter the number second : "))
    print("Sum of these number is ",
          first_input + second_input)
except ValueError as e:
    print(e)


def asset_function():
    assets_amount = int(input("Enter your assets amount : "))
    liabilities_amount = int(input("Enter your liabilities amount : "))
    capital_amount = int(input("Enter your capital amount : "))

    try:
        if assets_amount == capital_amount + liabilities_amount:
            print("Your accounting equation is matched")
        else:
            print("You have a flaw in your accounting equation recheck it")
    except Exception as x:
        print(x)


asset_function()
