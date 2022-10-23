import random

try:
    difficulty_level = str(input("Enter the difficulty level easy or medium or hard: ")).lower()
except Exception as e:
    print(e)
else:
    print("Game is now started")


def guessNumber():
    random_number = random.randint(1, 10)
    if difficulty_level == "easy":
        print("You have 10 chances")
        chances_to_play = 20
        while True:
            number_to_choose = int(input("Enter your number : "))
            if number_to_choose != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost")
                    break
                else:
                    print("You are wrong")
            else:
                print("You won")
                break
    elif difficulty_level == "medium":
        print("You have 10 chances")
        chances_to_play = 10
        while True:
            number_to_choose = int(input("Enter your number : "))
            if number_to_choose != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost")
                    break
                else:
                    print("You are wrong")
            else:
                print("You won")
                break
    elif difficulty_level == "hard":
        print("You have 5 chances")
        chances_to_play = 10
        while True:
            number_to_choose = int(input("Enter your number : "))
            if number_to_choose != random_number:
                chances_to_play -= 1
                if chances_to_play == 0:
                    print("You lost")
                    break
                else:
                    print("You are wrong")
            else:
                print("You won")
                break


guessNumber()
