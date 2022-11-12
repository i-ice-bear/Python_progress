class Employee:
    no_of_employees = 10

    def __init__(self, _programming_language, _frame_works):
        self.programming_language = _programming_language
        self.frame_works = _frame_works

    @classmethod
    def change__no_of_employees_(cls, _no__of_employees):
        cls.no_of_employees = _no__of_employees

    def __returns_Statement(self):
        return f"Programming Language : {self.programming_language} \n" \
               f"Frameworks : {self.frame_works}"


anshu = Employee(_programming_language="GOlang", _frame_works="Rust")
print(Employee.no_of_employees)
anshu.change__no_of_employees_(200)
print(Employee.no_of_employees)
