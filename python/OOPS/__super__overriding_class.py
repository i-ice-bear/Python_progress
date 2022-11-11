"""
:return: The super() function in class helps to access the class methods, and
         variables from the inherited class in the other class, by the synonym
         of over-riding

:param: Over-riding in class is the theory where the class method, variables get
        over-ride between classes, to pass the variables between class, if
        classes are inherited. After over-riding methods-and variables are not
        printable.

:rtype: To prevent this we use super() function between classes,

"""

import pyttsx3
import numpy as np

voice_engine = pyttsx3.init("sapi5")
voice_engine_Voice = voice_engine.getProperty("voices")
engine_Voice_set = voice_engine.setProperty("voice", voice_engine_Voice[1])
voice_engine.setProperty("rate", 150)


def __speakFunc_audio_engine(audio):
    """
    :param audio: takes the audio as an argument
    :return: A simple audio say function for speak audio,
    """
    if not voice_engine.inLoop:
        voice_engine.say(audio)
        voice_engine.runAndWait()
        voice_engine.stop()

    elif voice_engine.inLoop:
        voice_engine.say(audio)
        voice_engine.runAndWait()
        voice_engine.stop()
    else:
        print("Your Custom error")


class A:
    # noinspection SpellCheckingInspection
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
