from functools import lru_cache
import pyttsx3 as voice__engine
from abc import ABC, ABCMeta, abstractmethod

__Voice__engine_init = voice__engine.init()
voice_engine_get_prop = __Voice__engine_init.getProperty("voices")
_voice_engine_set_Prop = __Voice__engine_init.setProperty("voice", voice_engine_get_prop[0])


@lru_cache(maxsize=60)
def __Speak__func__audio(audio):
    if not __Voice__engine_init.inLoop:
        __Voice__engine_init.say(audio)
        __Voice__engine_init.runAndWait()

    elif __Voice__engine_init.inLoop:
        __Voice__engine_init.endLoop()
        __Voice__engine_init.stop()


class _Required__method(metaclass=ABCMeta):
    @abstractmethod
    def _returns__statement(self):
        return 0


class Main(ABC, _Required__method):
    __no__of_students = 1000
    _no__of__teachers = 100
    _no__of_staff = 200

    def __init__(self, _teacher__name, _subject_expertise, _teach_to_subject):
        self.teacher__name = _teacher__name
        self.subject__expertise = _subject_expertise
        self.teach_to_subject = _teach_to_subject

    def _returns__statement(self):
        print("\n")
        with open(f"./data/{self.teacher__name}.txt", 'a') as append_file_mod:
            pass

        with open(f"./data/{self.teacher__name}.txt", "r+") as read_write_file_mod:
            read_write_file_mod.write(f"Teacher name : {self.teacher__name}. \n"
                                      f"Subject expertise : {self.subject__expertise}. \n"
                                      f"Subject to teach : {self.teach_to_subject}.")

            return read_write_file_mod.read()

        # return f"Teacher name : {self.teacher__name}. \n" \
        #        f"Subject expertise : {self.subject__expertise}. \n" \
        #        f"Subject to teach : {self.teach_to_subject}."

    def __str__(self):
        return self._returns__statement()


if __name__ == '__main__':
    @lru_cache(maxsize=40)
    def __fetch_get_data():
        _get__teacher__name = input("Enter your name : ")
        _get__teacher_expertise = input("Enter your expertise : ")
        _get_teacher_subject = input("Enter your subject : ")

        added__data = Main(_get__teacher__name, _get__teacher_expertise, _get_teacher_subject)
        __Speak__func__audio("Your data is added successfully")
        print(added__data)


    __fetch_get_data()
