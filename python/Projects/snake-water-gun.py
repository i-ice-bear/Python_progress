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
    chances_to_play = 2
    while True:
        player_win_stat = 0
        computer_win_stat = 0
        player_turn = input("Enter your attribute : ")

        if random_attribute != player_turn:
            chances_to_play -= 1
            computer_win_stat += 1
            print("You, are wrong")
            print(f"Computer got {computer_win_stat} point")
        elif random_attribute == player_turn:
            chances_to_play -= 1
            print(chances_to_play)
            player_win_stat += 1
            print(f"Aya men, You got {player_win_stat} point")
        elif random_attribute == "snake" and random_attribute == "water":
            chances_to_play -= 1
            print("Continue")
        elif random_attribute == "gun":
            chances_to_play -= 1
            print(f"Another misconception")
        else:
            print("Something misconception")
        if chances_to_play == 0:
            time.sleep(3)
            print("Chances UP!")
            if player_win_stat > computer_win_stat:
                print(f"Computer wins with {computer_win_stat} points")
            else:
                print(f"\nPlayer wins")
            break
        else:
            continue


play_game()
