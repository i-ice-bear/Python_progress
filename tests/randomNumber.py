import random

try:
    difficulty_level = str(input("Enter your difficulty level : ")).lower()
except Exception as e:
    print(e)
else:
    print("Game is now started")


def random_number_game():
    random_number = random.randint(1, 10)
    if difficulty_level == "easy":
        chances_to_play = 20
        print("You have", chances_to_play, "Chances")
        while True:
            player_input = int(input("Enter the number : "))
            if player_input != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost, you can't play anymore")
                    break
                else:
                    print("Try again")
            else:
                print("You won")
                break

    if difficulty_level == "medium":
        chances_to_play = 10
        print("You have", chances_to_play, "Chances")
        while True:
            player_input = int(input("Enter the number : "))
            if player_input != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost, you can't play anymore")
                    break
                else:
                    print("Try again")
            else:
                print("You won")
                break

    if difficulty_level == "hard":
        chances_to_play = 5
        print("You have", chances_to_play, "Chances")
        while True:
            player_input = int(input("Enter the number : "))
            if player_input != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost, you can't play anymore")
                    break
                else:
                    print("Try again")
            else:
                print("You won")
                break

    if difficulty_level == "nightmare":
        chances_to_play = 2
        print("You have", chances_to_play, "Chances")
        while True:
            player_input = int(input("Enter the number : "))
            if player_input != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost, you can't play anymore")
                    break
                else:
                    print("Try again")
            else:
                print("You won")
                break


random_number_game()
