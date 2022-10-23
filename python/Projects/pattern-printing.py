print("how many rows do you want")
one = int(input())
print("Type 1 or 0")
two = int(input())
new = bool(two)

if new:
    for i in range(1, one + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
elif not new:
    for i in range(one, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()
