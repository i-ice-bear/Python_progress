import pyttsx3
import time

current_time = time.asctime(time.localtime(time.time()))

voice_engine = pyttsx3.init("sapi5")
voice_engine_get_property = voice_engine.getProperty("voices")
voice_engine_set_property = voice_engine.setProperty("voice", voice_engine_get_property[1])
voice_engine.setProperty("rate", 180)


def speak_Func__audio(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()


class Employees:
    """
       :return: There we create the class variable where we access these variables
                In any variable globally, not locally.
       :parameter: Example : role : { anything you want }

    """
    no_of_leaves = 8

    def __init__(self, _name, _age, _work_role, _salary, _experience):
        """
           :return: There we create the instance variable where we assign the variables,
           into the constructor as the __init__ function.
           :parameter: Example : role : { anything you want }
           :except: It also can be accessible globally, Not locally. for a variable
        """
        self.name = _name
        self.age = _age
        self.work_role = _work_role
        self.salary = _salary
        self.experience = _experience

    @classmethod
    def change_leave(cls, __new_leaves):
        """
        :param __new_leaves: Change the leaves index from the previous class variable.
        :return: Class method works to change the class variable from any instance variable from
                 constructor and any other function from class.
        :parameter: It can be accessible for both class variable and instance variable, also
                    the constructor variable. without any problem.
        :ivar: Important: The cls variable should have to same as per the class variable assigned
                          In class method, to change it.
        """
        cls.no_of_leaves = __new_leaves

    def returns_statement(self):
        """
        :return: This is the instance method where, we pass the instance variable
                 in Any way and convert it as a template for re-usability.
        :parameter: it can contain logics and any other statements like, generating
                    cache log, api fetch requests, with class etc.
        """
        return f"Name : {self.name} Age : {self.age} Work Role : {self.work_role} Salary : {self.salary} " \
               f"Experience : {self.experience} Leaves : {self.no_of_leaves} Days"


harry = Employees(_name="Harry", _age=16, _work_role="Deep learning enthusiast", _salary=90000, _experience=3)
Anshu = Employees(_name="Anshu", _age=16, _work_role="Machine learner", _salary=90000, _experience=3)

harry.change_leave(10)
print(harry.no_of_leaves)

# returns the statement
speak_Func__audio(harry.returns_statement())
time.sleep(10)
speak_Func__audio(Anshu.returns_statement())

if __name__ == "__main__":
    print(__name__)
