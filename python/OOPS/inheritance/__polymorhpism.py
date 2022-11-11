"""
:return: What is Polymorphism: The word polymorphism means having many forms.
         In programming, polymorphism means the same function name (but different signatures)
         being used for different types. The key difference is the data types and number of arguments used in function.
"""


import pyttsx3
import numpy as np

voice_engine = pyttsx3.init("sapi5")
voice_engine_Voice = voice_engine.getProperty("voices")
engine_Voice_set = voice_engine.setProperty("voice", voice_engine_Voice[1])
voice_engine.setProperty("rate", 150)


def __speakFunc_audio_engine(audio):
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


class Employees:
    required_employees = 10
    required_programming_language = 'Golang'
    required_skills = "Data research"
    fresher_salary = 30000

    def __init__(self, _required_employees, _required_programming_language,
                 _required_skills, _fresher_salary):
        self.required_employees = _required_employees
        self.required_programming_language = _required_programming_language
        self.required_skills = _required_skills
        self.fresher_salary = _fresher_salary

    def employee_forum(self):
        return f"Our, Requirements \n" \
               f"Required No. of employees : {self._required_employees} \n" \
               f"Required Programming language : {self.required_programming_language} \n" \
               f"Required skills : {self.required_skills} \n" \
               f"Fresher salary : {self.fresher_salary} \n"

    @classmethod
    def change_required___employees(cls, _required_employees):
        cls._required_employees = _required_employees
        print(cls._required_employees)

    @classmethod
    def _bunch_data_feeding_alternative_constructor(cls, _input__data):
        return cls(*_input__data.split("-"))

    @property
    def require_employee(self):
        return self._required_employees


class Projects(Employees):
    _required_project = "AI BOT"


class Certifications(Projects):
    _minimum_certification = "OSCP Qualified"
    _minimum_experience_in_years = 2


anshu = Employees(_required_employees=10, _required_programming_language="Java", _required_skills="Data analytics",
                  _fresher_salary=302322)

# __speakFunc_audio_engine(anshu.employee_forum())
print(anshu.employee_forum())
anshu.change_required___employees(32)
print(anshu.require_employee)
