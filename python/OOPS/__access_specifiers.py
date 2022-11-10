"""
:return: Python having 3 AccessSpecifiers,
         Public | Private | Protected

         Public: Can be accessible anywhere
         Private: Cannot be accessible anywhere via name mangling
         Protected: Protected variables are protected with the help
                    of _variable like this, Can't be able to access
                    at other environment
"""


class AccessSpecifiers:
    public_class_variable = "I'm public"
    _protected_class__Variable = "I'm protected class variable "
    __private_Class_variable = "I'm private class variable"

    def print__statement(self):
        return f"{self.public_class_variable} : {self._protected_class__Variable}"

    @property
    def protected_class__Variable(self):
        return self._protected_class__Variable


instance = AccessSpecifiers()
public_Access_specifier = AccessSpecifiers.public_class_variable
protected_Access_specifier = AccessSpecifiers.protected_class__Variable

print(public_Access_specifier, protected_Access_specifier)


class Student:
    """
    :return: Name mangling example
    """
    def __init__(self, name):
        self.__name = name

    def displayName(self):
        print(self.__name)


s1 = Student("Santhosh")
s1.displayName()

