import statistics

_input_variable = input("Your investment amount : ")
_yearly_income = input("Enter years : ")


print(f"Your, average investment amount is {int(_input_variable) / int(_yearly_income)}")


if int(_yearly_income) == 0:
    raise ZeroDivisionError("You can't divide 0 from any number. FUck you")

if _input_variable.istitle():
    raise Exception("Objects, are not allowed")

