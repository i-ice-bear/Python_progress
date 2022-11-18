import json


def __normal_json__data():
    """
    :return: Json module helps to change the data into the form of json(), like json() function
             in Javascript, This json module have multiple inbuilt functions to process the data
             in the form of json, for various ways of integration.
    :param: This function converts normal object to json data.
    """
    _json__data = {
        "name": "Anshu",
        "Class": "11th A",
        "Stream": "Intermediary commerce",
        "Future Role": "Computer scientist"
    }

    print("\n")
    _json_conversion = json.dumps(_json__data)
    print(_json_conversion)


def _specified__json__data():
    """
    :return: This function converts a valid json data, into the json.
    """
    x_data_json_module = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    def __specified_data_conversion_formation():
        """
        :return: Prints the json data in a valid form, including indentations
                 spacings, separators, and sort_keys.

        :param: indent variable : indent the json data. ### takes only number input
        :param: Separator variable : Separate data from various keys,
                ex = separators=(" : ", " = ") # takes these arguments
        :param : sort_keys variable : sort the json data along the letter
                 wise, ### Takes only boolean values, True or False
        """
        print("\n")
        print(json.dumps(x_data_json_module, indent=4, separators=(". ", " : ")))

    __specified_data_conversion_formation()


_specified__json__data()
