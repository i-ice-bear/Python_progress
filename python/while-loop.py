
number = int(input("Enter your number : "))

while number > 4:
    print("Your current no is : ", number)
    if number > 9:
        break
    if number > 7:
        continue
        print("Continue on the program")
