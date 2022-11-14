import inspect


class Emails:
    def __init__(self, _first__name, _country__name):
        self.first__name_ = _first__name
        self.country__name = _country__name

    @property
    def return_email(self):
        if self.first__name_ is None and self.country__name is None:
            print("Set, Email properly 암캐!!")
        else:
            return f"{self.first__name_}.{self.country__name}@codewithharry.com"

    @return_email.setter
    def return_email(self, _string):
        name = _string.split("@")[0]
        print(name)
        self.first__name_ = string.split(".")[0]
        self.country__name = string.split(".")[1]

    @return_email.deleter
    def return_email(self):
        self.first__name_ = None
        self.country__name = None

    def __str__(self):
        return self.return_email


anshu = Emails("Anshu", "india")
anshu.country__name = "usa"
print(f"\nSupporter email : {anshu}")


def object__introspection():
    """
    :return: Object introspection is a method in python where, we check the type of object
             in class, along it's members
    """
    print(type(anshu))
    print(dir(anshu))
    print(id(anshu))
    print(inspect.getmembers(anshu))
