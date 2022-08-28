file1 = open("../../generated/Jimmy.txt", "wb")


print(file1.mode)
print(file1.name)
file1.write(bytes("Jimmy carson blah blah", "UTF-8"))
file1.close()
