i = 0

while True:
    if i < 5:
        i = i + 1
        continue
    print(i + 1, end="")
    if i == 44:
        break
    i = i + 1
