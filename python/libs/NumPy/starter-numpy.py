import numpy as np
from functools import lru_cache
import speech_recognition as speechRecognition
import time
import pyttsx3 as voice_api_engine

voice_engine = voice_api_engine.init()
voice_engine_get = voice_engine.getProperty("voices")
voice_engine_set = voice_engine.setProperty("voice", voice_engine_get[1])
voice_engine.setProperty("rate", 150)

__speak__func__audio("I'm working now")

_speech__recognition_recognizer = speechRecognition.Recognizer()
_speech__recognition_recognizer_microphone = speechRecognition.Microphone()

with _speech__recognition_recognizer_microphone as source:
    string_voice_meta_data = str(source)
    _speech__recognition_recognizer.adjust_for_ambient_noise(source)
    audio_listen = _speech__recognition_recognizer.listen(source)


def __Random_numpy__array():
    """
    :return: Generates an array, with the given attribute,
def __speak__func__audio(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()

    """
    numpy_array = np.array([1, 2, 3, 4], dtype=np.int32)
    arrange_numpy_numbers = np.arange(9)
    print(arrange_numpy_numbers)
    print(numpy_array.itemsize)
    print(numpy_array)


def __dimensional__arrays():
    __2d_dimension = np.array([[1, 2, 3], [3, 2, 1]])
    print(__2d_dimension)


__dimensional__arrays()

if __name__ == '__main__':
    @lru_cache(maxsize=40)
    def __math_random_numpy(x_co_ordinate_1, x_co_ordinate_2, y_co_ordinate_1, y_co_ordinate_2):
        import math
        try:
            distance_formula_logarithm = \
                math.sqrt((int(x_co_ordinate_2) - int(x_co_ordinate_1)) ^ 2
                          + (int(y_co_ordinate_2) - int(y_co_ordinate_1)) ^ 2)
            print("The distance of the co-ordinates is : ", distance_formula_logarithm)
            print("Distances are : ", x_co_ordinate_2, x_co_ordinate_1, y_co_ordinate_2, y_co_ordinate_1)
        except TypeError as Typo_integration_error:
            print("Value not provided", Typo_integration_error[10])
        else:
            exit()


    print(__math_random_numpy(2, 6, 2, 6))
