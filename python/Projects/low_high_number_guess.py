"""
    It's a normal number guessing game which work on the principal
    of random module and stored guessing number
"""


import random
import time

random_module_number = 50
random_mods_number = random.randint(1, 20)
print("Welcome to the number guessing game, ")
difficulty_level = str(input("Enter your difficulty level \nEasy, medium, hard, nightmare : ", ))


def number_guess_function():
    """
        Here is the function which execute the whole code
        It's having 4 levels according to the difficulties.

        1. Easy = 20 chances
        2. Medium = 10 chances
        3. Hard = 5 chances
        4. Nightmare = 2 chances

        According to levels the logic was written down below
        with the usage of while loop and provided clean input
        at all logics to reset the number from its past value
        to continue the game

    """

    if difficulty_level == "easy":
        chances_to_play = 20
        print("You have : ", chances_to_play, "chances 1 chance in free")
        user_number_input = int(input("Enter your number : "))

        while True:
            if user_number_input == random_module_number:
                print("You won")
                break
            else:
                if user_number_input < random_module_number:
                    chances_to_play -= 1
                    print("Your guess is too low try another time")
                    user_number_input = int(input("Enter your number again : "))

                else:
                    chances_to_play -= 1
                    print("Your guess is too high")
                    user_number_input = int(input("Enter your number again : "))
                if chances_to_play == 0:
                    print("You have : ", chances_to_play, "chances")
                    break
                else:
                    continue

    if difficulty_level == "medium":
        chances_to_play = 10
        print("You have : ", chances_to_play, "chances 1 chance in free")
        user_number_input = int(input("Enter your number : "))

        while True:
            if user_number_input == random_module_number:
                print("You won")
                break
            else:
                if user_number_input < random_module_number:
                    chances_to_play -= 1
                    print("Your guess is too low try another time")
                    user_number_input = int(input("Enter your number again : "))

                else:
                    chances_to_play -= 1
                    print("Your guess is too high")
                    user_number_input = int(input("Enter your number again : "))
                if chances_to_play == 0:
                    print("You have : ", chances_to_play, "chances")
                    break
                else:
                    continue

    if difficulty_level == "hard":
        chances_to_play = 5
        print("You have : ", chances_to_play, "chances 1 chance in free")
        user_number_input = int(input("Enter your number : "))

        while True:
            if user_number_input == random_module_number:
                print("You won")
                break
            else:
                if user_number_input < random_module_number:
                    chances_to_play -= 1
                    print("Your guess is too low try another time")
                    user_number_input = int(input("Enter your number again : "))

                else:
                    chances_to_play -= 1
                    print("Your guess is too high")
                    user_number_input = int(input("Enter your number again : "))
                if chances_to_play == 0:
                    print("You have : ", chances_to_play, "chances")
                    break
                else:
                    continue

    if difficulty_level == "nightmare":
        chances_to_play = 2
        print("You have : ", chances_to_play, "chances 1 chance in free")
        user_number_input = int(input("Enter your number : "))

        while True:
            if user_number_input == random_module_number:
                print("You won")
                break
            else:
                if user_number_input < random_module_number:
                    chances_to_play -= 1
                    print("Your guess is too low try another time")
                    user_number_input = int(input("Enter your number again : "))

                else:
                    chances_to_play -= 1
                    print("Your guess is too high")
                    user_number_input = int(input("Enter your number again : "))
                if chances_to_play == 0:
                    print("You have : ", chances_to_play, "chances")
                    break
                else:
                    continue


def play_again():
    """
        It's a play again function where if user wants to play again
        then he can play it again as a new game

    """
    time.sleep(2)
    play_again_input = str(input("Do you want to play again ? : "))
    if play_again_input == "yes":
        number_guess_function()
    else:
        print("Never see you again")


number_guess_function()
play_again()
