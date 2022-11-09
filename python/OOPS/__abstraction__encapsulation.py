"""

:return: Data abstraction and encapsulation are synonymous as data abstraction
         is achieved through encapsulation. Abstraction is used to hide internal
         details and show only functionalities. Abstracting something means
         to give names to things, so that the name captures the basic idea of
         what a function or a whole program does.

:param: Abstraction - The main output of class. ( execution )
:parameter: Encapsulation - the functionality of class ( process )
"""


class FriendList:
    __annotations__ = True
    no__of_friends = 6

    def __init__(self, _name, _friendship_level, _time__of_friendship, _loving__rate):
        self.name = _name
        self.friendship_level = _friendship_level
        self.time_of__friendship = _time__of_friendship
        self.loving__rate = _loving__rate

    def return_statement(self):
        return f"Oh, {self.name} our friendship level is {self.friendship_level} and we know each " \
               f"other from {self.time_of__friendship} years and we like {self.loving__rate} each " \
               f"other"

    @classmethod
    def class_method(cls):
        """
        :return: These changes the main friendList class variable
        """
        cls.no__of_friends = 8
        return cls.no__of_friends

    @staticmethod
    def static__method(string):
        return "Norms string " + string

    @classmethod
    def alternative__class_method(cls, _data__string):
        return cls(*_data__string.split("-"))


contents = FriendList.alternative__class_method("anshika-cool-1-so,much")
print(FriendList.class_method())
print(contents.class_method())
print(contents.return_statement())


if __name__ == "__main__":
    print(__name__)
