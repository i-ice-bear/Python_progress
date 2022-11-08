import pyttsx3

engine_Voice = pyttsx3.init("sapi5")
voices = engine_Voice.getProperty("voices")
voice = engine_Voice.setProperty("voice", voices[0])
engine_Voice.setProperty("rate", 160)


def speak_function(audio):
    engine_Voice.say(audio)
    engine_Voice.runAndWait()


class Employees:
    """
    :return: Methods help to print the statements from the class as
             a template of the class. Can be defined from any name.
    """

    def __init__(self, name, age, role, work_experience, salary):
        """
        :param age: It takes the age which is given as the self
        :param name: It takes the name which is given as the self
        :param role: It takes the role which is given as the self
        :param work_experience: It takes the work_experience which is given as the self
        :param salary: It takes the salary which is given as the self

        :return: A constructor is a function in the class where we add the arguments
                 in the class which takes it as the self. inside the class

        """
        self.name = name
        self.age = age
        self.work_experience = work_experience
        self.salary = salary
        self.role = role

    def post_details(self):
        """
         :return: Methods help to print the statements from the class as
                  a template of the class. Can be defined from any name.
         """
        print(f'{self.name} salary is {self.work_experience} and role is {self.salary}')


anshu = Employees("Anshu", 16, 3, 40000, "Deep learning enthusiast")  # arguments were passed through the class func.
yash = Employees(name="Yash", age=12, work_experience=4, role="UI UX designer", salary=9000)
print(yash.post_details())
print(anshu.post_details())


def private_Variables():
    """
    :return: this are the private variables.
    """

    # anshu.role = "Deep learning enthusiast"
    # anshu.workExperience = "7 Years"
    # anshu.salary = 300000
    #
    # yash.role = "UI UX designer"
    # yash.workExperience = "4 Years"
    # yash.salary = 300000
