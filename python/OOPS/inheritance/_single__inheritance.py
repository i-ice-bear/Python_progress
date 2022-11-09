"""
:return: Motherfucker it's related from scientific methods of science
"""


class Employees:
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

no__of_employees = Employees.no_of__employees
print("Older employee list : ", no__of_employees)

new_employee_list = Employees.change__class_variables(10)
print("New employee list : ", new_employee_list)

print(anshu.string_return__statement())