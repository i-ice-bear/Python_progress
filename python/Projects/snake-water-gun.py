"""

   Snake water gun
   play for 10 times

"""

import random

print("Welcome to snake water and gun game \nYou will play against computer")

attributes = ["snake", "water", "gun"]
print(f"Choose from : {attributes}")
random_attribute = random.choice(attributes)
print(random_attribute)


def play_game():
    while True:
        chances_to_play = 2
        player_win_stat = 0
        computer_win_stat = 0
        player_turn = input("Enter your attribute : ")


play_game()
