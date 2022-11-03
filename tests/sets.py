import math
import statistics

# # sort of ascending and descending order in the form of sort function
#
# list_set = eval(input("Enter a list : "))
# list_set.sort()
# print("Sorted in ascending order : ", list_set)
# list_set.sort(reverse=True)
# print("Sorted in descending order : ", list_set)
#
# # program to calculate of the mean of it.

# mean_num = eval(input("Enter your mean list : "))
# length = len(mean_num)
# mean = sum = 0
# for meanList in range(0, length):
#     sum += mean_num[meanList]
#     print(sum)
# mean = sum / length
# print("Given list is : ", mean_num)
# print("The mean of given list is ", mean)


# mean_given_data = eval(input("Enter list for confirmation : "))
# mean_output = statistics.mean(mean_given_data)
# print(mean_output)

mean_number = eval(input("Enter your data : "))  # takes data from the input
mean_length = len(mean_number)  # get the length of the input
mean = sum_data = 0  # setting index to 0

for mean_data in range(0, mean_length):  # for Loop for iterating the length with 1
    """
       Addition of all of the elements in the mean_number data 
       from the above of the input, in the form of numerical array
    """
    sum_data += mean_number[mean_data]  # extract the position of mean_number from mean_data length
    print(sum_data)  # prints the sum_data value

# extract the mean from overall sum_data above from loop and divide it from the length
# of the array.
mean_calculation = sum_data / mean_length

print(mean_calculation)# overall output
