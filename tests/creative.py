rows = eval(input("Enter how many ladders you want to print out : "))

for i in range(0, rows):
    for n in range(0, i + 1):
        print('*', end="")
        print()

