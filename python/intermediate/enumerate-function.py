custom_list = [1, 2, 3, 4]


# printing the odd functions
l = 1
for item in custom_list:
    if l % 2 != 0:
        print(item)
    l += 1

for index, item in enumerate(custom_list):
    if index%2 == 0:
        print([item])
        print([index])
