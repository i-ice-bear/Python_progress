assets = eval(input("Enter list of assets : "))
liabilities = eval(input("Enter list of liabilities : "))
capital = eval(input("Enter the capital list : "))

if sum(assets) == sum(liabilities) + sum(capital):
    print("Accounting equation is matched")
else:
    print("Accounting equation is didn't match")