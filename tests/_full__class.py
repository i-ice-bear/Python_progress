from abc import ABCMeta, ABC, abstractmethod
import pyttsx3

voice_engine__init = pyttsx3.init("sapi5")
_voice_engine__voices = voice_engine__init.getProperty("voices")
_voice_engine_set__voice = voice_engine__init.setProperty("voice", _voice_engine__voices[1])
voice_engine__init.setProperty("rate", 150)


def __speak__func_audio(audio):
    voice_engine__init.say(audio)
    voice_engine__init.runAndWait()
    voice_engine__init.stop()


class Employees:
    _no_of__employees_required__ = 100
    _no_of_staff_managers__required__ = 10
    _default_salary_of_employee = 30000

    def __init__(self, _employee_name__, _employee_skills__, _employee_expertise__):
        self.employee__name_ = _employee_name__
        self.employee_skills__ = _employee_skills__
        self.employee_expertise__ = _employee_expertise__

    def returns_output_string__(self):
        return f'Employee Name : {self.employee__name_} \n' \
               f'Employee Skills : {self.employee_skills__} \n' \
               f'Employee Expertise : {self.employee_expertise__}'

    def __repr__(self):
        return self.returns_output_string__()

    def __add__(self, other):
        return self.employee__name_ + other.employee__name_


anshu = Employees("anshu", "UI", 3)



