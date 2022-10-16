import os


class Main:
    def __init__(self, __date, __state, __package):
        self.date = __date
        self.state = __state
        self.package = __package

    def outro(self):
        print("Date is : " + self.date + " State library is : " + self.state + " Package name is : " + self.package)

open = Main("40", "redux", "tensorflow")
open.outro()