import time

initial_time = time.time()  # initial current time
print(initial_time)

for i in range(5):
    print("I will print 5 times")
initial_for_loop_time = time.time() - initial_time
print(initial_for_loop_time)

i = 0
while i < 5:
    print("I wil print for 45 times")
    i += 1
initial_while_loop_time = time.time() - initial_time
print(initial_while_loop_time)

current_local_Time = time.asctime(time.localtime(time.time()))
print(current_local_Time, type(current_local_Time))

