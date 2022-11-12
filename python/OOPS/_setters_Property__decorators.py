class Support__email:
    def __init__(self, _name__, _country__):
        self.name = _name__
        self.country = _country__
        self.email = f"{self.name}.{self.country}@codewithharry.com"

    @property
    def returns_email(self):
        return f"Support email : {self.name}.{self.country}@codewithharry.com"

    @returns_email.setter
    def returns_email(self, _string_input):
        attributes = _string_input.split("@")[0]
        name = _string_input.split('.')[0]
        country = _string_input.split(".")[1]


andy = Support__email("andy", "romania")
print(andy.returns_email)

ishan = Support__email("ishan", "india")
ishan.returns_email = "ishan.romania@gmail.com"
print(ishan.returns_email)
