import time
import requests

fetch_url = "https://newsapi.org/v2/top-headlines?country=kr&apiKey=391b845c95b64b0ea4a5c67fe7d31a41"

numbers = ["5", "15", "25"]
numbers = list(map(int, numbers))
fixed_tick = time.time()

# random For loop
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])


def square_function(a):
    return a * a


def fetch_to_append_in_generated():
    result_get = requests.get(fetch_url)
    with open("../../generated/results.json", "a", encoding="utf-8") as result_file:
        result_file.write(result_get)


fetch_to_append_in_generated()


current_function_tick_time = time.time() - fixed_tick
print(current_function_tick_time)

list_num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = list(map(square_function, list_num))
print(square_list, type(square_list))
