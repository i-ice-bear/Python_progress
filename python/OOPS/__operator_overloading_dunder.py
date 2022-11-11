"""
:return: The __function__() are the, dunder method function class,
         Which starts from __ and end at __ these, are the special
         methods, which provides, special functionality,
"""


class Employees:
    _no_of__employees = 10

    def __init__(self, _no_of__employees, _config__employees):
        self.no_of__employees = _no_of__employees
        self.config_employees = _config__employees

    def returns_statement(self):
        return f"No of Employees : {self.no_of__employees} \n" \
               f"Config Employees : {self.config_employees} \n"

    @classmethod
    def _change__no_of_require_employees__(cls, _new__no_required_employees):
        cls._no_of__employees = _new__no_required_employees

    def __add__(self, other):
        """
        :param other: Employees attributes
        :return: Adds, the element of the class between each other
                 And returns the final statement at the end of the
                 program after the execution of it.
        """
        return self.no_of__employees + other.no_of__employees

    def __truediv__(self, other):
        """
            :param other: Employees attributes
            :return: Divides, the element of the class between each other
                     And returns the final statement at the end of the
                     program after the execution of it.
        """
        return self.no_of__employees / other.no_of__employees

    def __repr__(self):
        """
        :return: Returns the class variable in the form of the string, normal language
                 instead of any machine language, with the help of the function which
                 returns all the element of the, class.
        """
        return self.returns_statement()

    def __str__(self):
        """
        :return: Returns the class variable in the form of the string, normal language
                 instead of any machine language, with the help of the function which
                 returns all the element of the, class.

        :parameter: Python first prefers to run __str__ dunder method,
        """
        return self.returns_statement()


print("\n")
Proprietor = Employees(10, "Expert")
Manager = Employees(10, "Minimal")
print(Proprietor.returns_statement())
print(Proprietor / Manager) # overloading of the operator

if __name__ == __name__:
    print(__name__)
