# noinspection PyUnusedLocal

"""
:return: Setters and property Decorators, functionality in python.
:return: Setters, getters and property decorators are the functionality
         in class functionality in python which helps to change the content
         of the class variables, with the help of @property, @deleters,
         @setters with the function decorators,
"""


class Emails:
    def __init__(self, _first_name, _country__name):
        self.first__name = _first_name
        self.country__name_ = _country__name

    def pass_statement_str__(self):
        return f'{self.first__name}.{self.country__name_}@codewithharry.com'

    @property
    def return_emails(self):
        """
        :return: Initialized a property decorator for this function, to use
                 Setters, getters and deleters for it.
                 Without the property decorator, it is not possible to change
                 the class variables inside the class-program
        """
        if self.first__name is None and self.country__name_ is None:
            print("Email is not set! Set it not you sussy baka")
        else:
            return f'{self.first__name}.{self.country__name_}@codewithharry.com'

    @return_emails.setter
    def return_emails(self, string):
        """
        :param string:
        :return: Defined a setter for the program, where this function sets the data
                 Along the splitting of the string from the attributes passed in the
                 split function,
        """
        print("setting the variables...")
        names = string.split("@")
        print(names)
        self.first__name = string.split(".")[0]
        self.country__name_ = string.split(".")[1]

    @return_emails.deleter
    def return_emails(self):
        """
        :return: Deletes the variable from the class variable, Generally in class
                 we didn't delete any kind of variables, we simply set it as None
                 boolean, for the constructor
        """
        self.first__name = None
        self.country__name_ = None

    def __str__(self):
        return self.pass_statement_str__()


anshu = Emails("anshu", "u.s.a")
anshu.country__name_ = "India"  # getters called where it takes the variable for changes
del anshu.return_emails
print(anshu.return_emails)
