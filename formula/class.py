class applicationView:
    def __init__(self, _letter, _application):
        self.letter = _letter
        self.application = _application

    def letterExecution(self):
        print("I will ready your letter with the topic of " + self.letter + "and application like" + self.application)


letter = applicationView("Holiday enjoyment letter", "Sick leave")
letter.letterExecution()


class settings:
    def __init__(self, _settings, _datatypes, _mainFunction):
        self.settings = _settings
        self.datatypes = _datatypes
        self.mainFunction = _mainFunction
        if __name__ == "__main__":
            print("Calls from" + __name__)

    def exec(self):
        settingInput = str(input("Enter your settings : "))
        print(settingInput + " " + self.settings)


execution = settings("Something", "Something", 'Something')
execution.exec()
