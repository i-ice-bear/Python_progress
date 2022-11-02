import random
from pyfiglet import figlet_format

random_number = random.randint(1, 10)
print(random_number)

print(figlet_format("Dungeon!", font="starwars"))


def game_func():
    chances_to_play = 10
    while True:
        player_input = int(input("Enter your number : "))
        if player_input < random_number:
            print("Your guess is too low! Try again.")
            chances_to_play -= 1
            print(f"You have only {chances_to_play} chances")
        elif chances_to_play == 0:
            print("You out of chances")
            break
        elif chances_to_play == 3:
            print("You have only 3 chances to play! Choose wisely")
        elif player_input > random_number:
            print("Your guess is too high! Try again.")
            chances_to_play -= 1
        else:
            print('Congratulations! Man you won the game.')
            break


game_func()
