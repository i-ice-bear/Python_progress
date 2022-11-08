class Employees:
    no_of_leaves = 8

    def __init__(self, _age, _name, _leave, _salary, _work_experience):
        self.name = _name
        self.age = _age
        self.leave = _leave
        self.salary = _salary
        self.work_experience = _work_experience

    @classmethod
    def change_leave_class_method(cls, _new__leave):
        cls.no_of_leaves = _new__leave

    @classmethod
    def alternative__constructor_class(cls, _input_string):
        """
        :param _input_string: Takes the input from the function from the class,
        :return: The alternative__constructor works to add data only one string and then,
                 return it into the object.
        :parameter: Class methods as the alternative constructor.

        """

        # params_split = _input_string.split("-")
        # print(params_split)
        # return cls(params_split[0], params_split[1], params_split[2], params_split[3], params_split[4])
        # Multi liner functions
        return cls(*_input_string.split("-"))

    def return__employee_statement(self):
        return f"Name : {self.name} Age : {self.age} leave : {self.leave} salary : {self.salary}" \
               f"Work Experience : {self.work_experience}"


anshu = Employees(_name="Anshu", _salary=70000, _leave=8, _work_experience=6, _age=16)
shivam = Employees.alternative__constructor_class("shivam-16-7000-4-2")
print(shivam.return__employee_statement())

anshu.change_leave_class_method(30)
print(Employees.no_of_leaves)
