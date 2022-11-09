class Employees:
    no_of_leaves = 8

    def __init__(self, _age, _name, _salary):
        self.age = _age
        self.name = _name
        self.salary = _salary

    @classmethod
    def _change__leaves(cls):
        cls.no_of_leaves = 10

    @classmethod
    def alternative_constructor(cls, _input__string):
        return cls(*_input__string.split("-"))

    @staticmethod
    def static_method(string):
        return "Normal string" + string

    def post__details(self):
        return f"Age : {self.age}, Name : {self.name}, Salary : {self.salary}"


anshu = Employees(16, "Anshu", 80000)
ravi = Employees.alternative_constructor("16-ravi-90000")
print(ravi.post__details())
normal_str = anshu.static_method(" normal")
print(normal_str)
print(anshu.post__details())
