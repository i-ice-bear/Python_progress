marks = int(input("Enter Your marks : "));

print(marks)

if(marks>90 and marks<100):
    print("A grade")
elif(marks>50 and marks<60):
    print("B Grade")
else:
    print("Don't know what to do { Fail }");
print("The grade is", marks);

# shorthand like agar magar in single nagar
a = int(input("Enter the first number : "));
b = int(input("Enter the second number : "))

if a<b: print("B is greater than a")
else: print("A is smaller than b")