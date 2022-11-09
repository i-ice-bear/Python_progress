"""
:return: Demonstration from the science example,
:parameter : Transfer of the genetic data from parent to child
             of the parent default function and features to child
             functions and features. ( From Reproduction ).
"""


class Employees:  # Parent Class
    no_of__employees = 8

    def __init__(self, _name, _age, _salary):
        self.name = _name
        self.age = _age
        self.salary = _salary

    @classmethod
    def change__class_variables(cls, __new_leave_index):
        cls.no_of__employees = __new_leave_index
        return cls.no_of__employees

    @classmethod
    def _alternative_class__method(cls, _input__string_meth):
        return cls(*_input__string_meth.split("-"))

    def string_return__statement(self):
        return f"Name : {self.name}\n" \
               f"Age : {self.age} \n" \
               f"Salary : {self.salary}"


anshu = Employees(_name="Anshu", _age=16, _salary=80000)
yash = Employees(_name="Yash", _age=16, _salary=80000)

print(anshu.string_return__statement(), "\n")
print(yash.string_return__statement(), "\n")


class Programmer(Employees):  # inherited from the parent class.
    """
    :return: Prevents the over-writing of the class statement variables form other
             classes. Which also follows the rule of code re-usability. Without
             any code malfunctions
    """
    def __init__(self, _name, _age, _salary, _programming_language):
        super().__init__(_name, _age, _salary)
        self.programming_language = _programming_language

    def print__statement(self):
        return f"Name : {self.name} \n" \
               f"Age : {self.age} \n" \
               f"Salary : {self.salary} \n" \
               f"Language : {self.programming_language}"
    pass


mayank = Programmer("Mayank", 16, 40000, "Go")

print(mayank.print__statement(), "\n")


if __name__ == "__main__":
    print(__name__)
