# # sort of ascending and descending order in the form of sort function
#
# list_set = eval(input("Enter a list : "))
# list_set.sort()
# print("Sorted in ascending order : ", list_set)
# list_set.sort(reverse=True)
# print("Sorted in descending order : ", list_set)
#
# # program to calculate of the mean of it.

mean_num = eval(input("Enter your mean list : "))
length = len(mean_num)
mean = sum = 0
for meanList in range(0, length):
    sum += mean_num[meanList]
    print(sum)
mean = sum / length
print("Given list is : ", mean_num)
print("The mean of given list is ", mean)
