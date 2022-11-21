from functools import lru_cache
from abc import ABCMeta, ABC, abstractmethod
from time import time
import datetime
import os
import pyttsx3 as voice__engine

voice_engine__init = voice__engine.init()
voice_engine__get_Prop = voice_engine__init.getProperty("voices")
voice_engine_set_Prop = voice_engine__init.setProperty("voice", voice_engine__get_Prop[2])
voice_engine__init.setProperty("rate", 150)


@lru_cache(maxsize=15)
def _speak__audio_func(audio):
    if not voice_engine__init.inLoop:
        voice_engine__init.say(audio)
        voice_engine__init.runAndWait()
    elif voice_engine__init.inLoop():
        voice_engine__init.stop()
        voice_engine__init.endLoop()


class Header(metaclass=ABCMeta):
    @abstractmethod
    def _returns__statement(self):
        return 0


class Main(Header, ABC):
    __no_of_employees = 10
    __job_requirement_rate = 20
    __ungraduated_employees = 20
    _graduated__employees = 2

    def __init__(self, __name__var, __cgp__test_grade, _graduation_val, __employee_work_role):
        self.name = __name__var
        self.__cgp__test_grade = __cgp__test_grade
        self.graduation_val = _graduation_val
        self.__employee_role = __employee_work_role

    @lru_cache(maxsize=10)
    def _returns__statement(self):
        with open(f"./data/{self.name}_info.txt", "r+") as save__information:
            print(save__information.read())
            print(save__information.write(f"Name : {self.name} "
                                          f"Speciality rate : {self.__cgp__test_grade}. "
                                          f"Graduation Level : {self.graduation_val}. "
                                          f"Employee role : {self.__employee_role}. "))
            print("Information, saved")

        return f"Name : {self.name} " \
               f"Speciality rate : {self.__cgp__test_grade}. " \
               f"Graduation Level : {self.graduation_val}. " \
               f"Employee role : {self.__employee_role}. "

    @classmethod
    def _change_class_var(cls, __updated_ungraduated__employee):
        cls.__ungraduated_employees = __updated_ungraduated__employee

    def __repr__(self):
        return self._returns__statement()

    def __str__(self):
        return self._returns__statement()


class Employee_Classification(Main, ABC):
    __minimum_certification = "OSCP"

    def __init__(self, __name, __mastered_programming_language, __name__var, __cgp__test_grade, _graduation_val,
                 __employee_work_role):
        super().__init__(__name__var, __cgp__test_grade, _graduation_val, __employee_work_role, )

    @lru_cache(maxsize=10)
    def _returns__statement(self):
        return 0


if __name__ == '__main__':
    @lru_cache(maxsize=30)
    def __gather__information():
        _speak__audio_func("Welcome to Infosys registration panel. Good luck")
        __name__input = str(input("Enter your name : "))
        __cgp_test_grade = input("Enter your cgp test Grade : ")
        __graduation_level = str(input("Enter your graduation : "))
        _job__role = str(input("Enter your job role which you want to apply for it"))
        anshu = Main(__name__input, __cgp_test_grade, __graduation_level, _job__role)
        _speak__audio_func(anshu)

    __gather__information()
