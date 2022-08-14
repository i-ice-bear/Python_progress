marks = int(input("Enter Your marks : "));

print(marks)

if(marks>90 and marks<100):
    print("A grade")
elif(marks>50 and marks<60):
    print("B Grade")
else:
    print("Don't know what to do { Fail }");
print("The grade is", marks);