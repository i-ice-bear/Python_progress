import random

print("Welcome to number guessing game")
user_Difficulty = str(input("Choose your difficulty [easy/hard] : "))


def generate_random():
    random_number = random.randint(1, 10)
    print(random_number)
    chances_to_play = 20

    if user_Difficulty == "easy":
        while True:
            print("you have : ", chances_to_play)
            user_number_input = int(input("Enter random number : "))
            if user_number_input != random_number:
                print("You guess a wrong number")
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost the game")
                    break
            else:
                print("You won")
                break

    elif user_Difficulty == "hard":
        chances_to_play = 10
        while True:
            user_number_input = int(input("Enter random number : "))
            if user_number_input != random_number:
                print("You guess a wrong number")
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost the game")
                    break
            else:
                print("You won")
                break


def play_again():
    play_again_input = str(input("Do you want to play again ? : "))
    if play_again_input == "yes":
        generate_random()
    else:
        print("Never gonna see you soon ")


generate_random()
play_again()