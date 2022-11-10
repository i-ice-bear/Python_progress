class Employee:
    no_of__leaves = 10
    time_of__work = 7
    required__employees = 20
    no_of_test__required = 23

    def __init__(self, _programming_language, _experience, _projects, _github_link):
        self.programming_language = _programming_language
        self.experience = _experience
        self.projects = _projects
        self.github_link = _github_link

    def print_statement__str(self):
        return f"Programming language : {self.programming_language} \n" \
               f"Approx Experience : {self.experience} Years \n" \
               f"Projects : {self.projects} \n" \
               f"Github Profile Link : {self.github_link}"

    @classmethod
    def employees__need_(cls, _custom_leave_arg):
        cls.required__employees = _custom_leave_arg

    @classmethod
    def alternative_cls_method__(cls, __input__strings_statement):
        return cls(*__input__strings_statement.split("-"))


class Skills:
    _required__skills = "Better scripting"
    _gui_programming = "UI UX"
    no_of_test__required = 23

    def __init__(self, _name, __additional__skills):
        self.name = _name
        self.additional_skill = __additional__skills

    def print_statement__(self):
        return f"Name : {self.name} \n" \
               f"Additional Skill : {self.additional_skill}"


class Tests_cleared(Employee, Skills):
    no_of_test__required = 1

    def __init__(self, _programming_language, _experience, _projects, _github_link, __migrant_Type):
        super().__init__(_programming_language, _experience, _projects, _github_link)
        self.migrant_type = __migrant_Type


anshu = Tests_cleared(_programming_language="GO", _experience=8,
                      _projects="VoiceAPI", _github_link="i-ice-bear", __migrant_Type="canada")

print(anshu.no_of_test__required)
