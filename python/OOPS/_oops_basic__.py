"""
   :OOPS : Object oriented programming

   :return: Class is an object-oriented programming concept where we create templates
            of program to unfollow the DRY Concept. Where we build a program easily
            and quickly with the help of class oops concept.

   :param: DRY : Do not repeat yourself | concept.

   :arg: A class is a blueprint or a template for creating objects
         while an object is an instance or a copy of the class with
         actual values.

"""


class __do__not_repeat:
    """
        Header class, This is an empty class where we create the
        templates inside the class.  ` templates `
        like def __init__():
                 like class keywords.
    """
    pass


def __instances_class():
    """
    :return: These keywords are the instances and objects of the class,
             which is defined on the uppers-ide of the program.

    :exception: Where a variable is equal to the defined values from
                other side, They have only private variables, They're
                not sharing any variables between each other.
    """
    variable_1 = __do__not_repeat()  # these instances are not using anywhere
    _variable__2 = __do__not_repeat()


def __argument_Class_append():
    """
    :return: These are the arguments of the variable which is defined and
             equalised to the __instances_objects ( private variables ) , and we're adding the
             value inside the derived class variables.

    :parameter: We used the objects from the upside function to prevent the errors.
                In the program for the compatibility purposes.
    """
    variable_1 = __do__not_repeat()
    _variable__2 = __do__not_repeat()

    variable_1.name = "Current-name"
    variable_1.standard = "memory-locator"
    variable_1.date_formation = "032"
    print(variable_1.name)


__argument_Class_append()

if __name__ == "__main__":
    print(__name__)
