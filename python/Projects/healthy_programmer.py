"""
    Healthy Programmer exercise No. 7
    Programmer = 9a.m = 5p.m
    Water alert = water.mp3 (3.5 liters) === Drank ---- Generate a Log
    Eyes alert = Eyes.mp3  === Every 30 Minute alert ---- Generate Log
    Physical Activity = activity.mp3 === Every 45 minutes alert ----- generate a log

"""

import pyttsx3
import time
import datetime

voice_engine = pyttsx3.init()
voices = voice_engine.getProperty("voices")
voice = voice_engine.setProperty("voice", voices[1])
voice_engine.setProperty("rate", 150)
current_time = time.asctime(time.localtime(time.time()))
print(current_time)
print(datetime.time(hour=1))


def _speak_func(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()


def _drink_water():
    while True:
        time.sleep(20)
        _speak_func("It's time to drink water. Drink it now")
        input_confirmation = str(input("Have you drink water > ")).lower()
        if "drank" in input_confirmation:
            _speak_func("That's good, Continue")
            try:
                with open(f"./utilities/healthy_programmer_cache_log/water-log.txt", "x") as water_log_cache:
                    print("Water cache stored")
                    water_log_cache.write(f"[ {current_time} ] : Drink water\n")
            except FileExistsError as file_already_Existed:
                with open(f"./utilities/healthy_programmer_cache_log/water-log.txt", "a") as read_log:
                    read_log.write(f"[ {current_time} ] : Drink water\n")
                print(file_already_Existed)
            except FileNotFoundError as file_not_found:
                print(file_not_found)
            else:
                print("Not worked!")
            time.monotonic()


def _eyes_rest():
    while True:
        time.sleep(35)
        _speak_func("Time! Give some rest to your eyes.")
        input_confirmation = str(input("Have you give rest to your eyes : ")).lower()
        if "yes" in input_confirmation:
            _speak_func("That's good, You're going good")
            try:
                with open(f"./utilities/healthy_programmer_cache_log/eye-Rest_cache-log.txt", "x") as eyes_rest_log:
                    print("Eye rest cache stored")
                    eyes_rest_log.write(f'[ {current_time} ] : Eye rest\n')
            except FileExistsError as file_already_incurred:
                with open(f"./utilities/healthy_programmer_cache_log/eye-Rest_cache-log.txt", "a") as read_eye_log:
                    read_eye_log.write(f'[ {current_time} ] : Eye rest\n')
                    print(file_already_incurred)
            else:
                print("Not worked")
                exit()


def _physical_exercise():
    while True:
        time.sleep(45)
        _speak_func("Aya men! It's time to move your body. Do some exercise")
        input_confirmation = str(input("Have you done exercise : ")).lower()
        if "yes" in input_confirmation:
            _speak_func("That's good, you're becoming a healthy person")
            try:
                with open(f"./utilities/healthy_programmer_cache_log/exercise_cache-log.txt", "x") as eyes_rest_log:
                    print("Eye rest cache stored")
                    eyes_rest_log.write(f'[ {current_time} ] : Exercise done\n')
            except FileExistsError as file_already_incurred:
                with open(f"./utilities/healthy_programmer_cache_log/exercise_cache-log.txt", "a") as read_eye_log:
                    read_eye_log.write(f'[ {current_time} ] : Exercise done\n')
                    print(file_already_incurred)
            else:
                print("Not worked")


def _function_execution():
    _drink_water()
    _eyes_rest()
    _physical_exercise()


_function_execution()

if __name__ == "__main__":
    print(__name__)
