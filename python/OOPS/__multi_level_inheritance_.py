class Daddy:
    """
    :return: Main parent class, all the genetic data as class variables
    """
    basketball = 4
    pass


class Son(Daddy):
    """
    :return: Son parent inherited class, all the genetic data
             as class variables, has inherited or transferred
             from main class to Son class,
    """
    dancing = 3
    basketball = 6

    def return_statement__(self):
        return f"Dancing : {self.dancing}"


class GrandSon(Son):
    """
    :return: Grandson son parent inherited class, all the genetic
             data from Son and daddy, has transferred init.
    """
    dancing = 4

    def return_statement__(self):
        return f"Oh yeah! Dancing : {self.dancing}"


darry = Daddy()
larry = Son()
harry = GrandSon()
print(harry.basketball)