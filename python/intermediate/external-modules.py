import random

random_number = random.randint(0, 10)
print('Current random number :', random_number)

random_func = random.uniform(3, 4)
print(random_func)

choice_list = ["Serum", "Tal filter X", "Tal filter pro", "RefX Nexus"]
random_choice = random.choice(choice_list)
print(random_choice)