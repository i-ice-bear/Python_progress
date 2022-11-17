from functools import lru_cache
from abc import ABC, ABCMeta, abstractmethod
import numpy as np
import os as os_module
import pyttsx3 as voiceEngine

voice_engine = voiceEngine.init("sapi5")
voice_engine_getProperty = voice_engine.getProperty("voices")
voice_engine_set_prop = voice_engine.setProperty("voice", voice_engine_getProperty[0])
voice_engine_set_rate = voice_engine.setProperty("rate", 150)


def __speak_func__audio_return(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()
    print(audio)


def _os_function_fun():
    ip__configuration_sys = os_module.system("ipconfig")
    __speak_func__audio_return("Os, configuration output")
    return str(ip__configuration_sys)


def _sql__config__stats():
    sql_configuration__sys = os_module.system("mysql -u root -p")
    return str(sql_configuration__sys)


class Parent(metaclass=ABCMeta):
    @abstractmethod
    def _returns_statement(self):
        return 0


class Sysinfo_statements(ABC, Parent):
    _no__of_employees = 100

    @lru_cache(maxsize=20)
    def __init__(self, __session_cookies, _tokens):
        self.session_cookies = __session_cookies
        self.token__sessions__ = _tokens
        self.ip__configuration_sys_os__ = _os_function_fun()
        self.sql__confing_stats = _sql__config__stats()

    def _returns_statement(self):
        return f"Session cookies = {self.session_cookies} " \
               f"Token sessions = {self.token__sessions__} " \
               f"Ip configuration = {self.ip__configuration_sys_os__} " \
               f"Sql configuration ; {self.sql__confing_stats}"

    def __str__(self):
        return self._returns_statement()


anshu = Sysinfo_statements(100, 300)
print(anshu)

if __name__ == '__main__':
    print(__name__)
