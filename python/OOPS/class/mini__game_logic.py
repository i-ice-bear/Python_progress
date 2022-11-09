class Player:

    name__of__player = "liuX"
    no__of_guns__limit = 2
    no_of__life_limit = 3
    minimum__sprint_speed = 20
    shooting_accuracy = 3

    def __init__(self, _name, _guns_limit, _life__limit, _sprint__speed, _shooting__accuracy):
        self.player_name = _name
        self.guns__limit = _guns_limit
        self.no__life_limit = _life__limit
        self.sprint_speed = _sprint__speed
        self.shooting_accuracy_ = _shooting__accuracy

    def __return__statement(self):
        return f"Player name : {self.player_name} \n" \
               f"Guns limit : {self.guns__limit} \n" \
               f"Life limit : {self.no__life_limit} \n" \
               f"Spring speed : {self.sprint_speed} \n" \
               f"Shooting Accuracy : {self.shooting_accuracy_}"

    @classmethod
    def _change_default__variables(cls, _player_config_name, _player_config_guns, _player_config_life_limit,
                                   _player_config__sprint_speed, _player__config_shooting_accuracy):
        cls.name__of__player = _player_config_name
        cls.no__of_guns__limit = _player_config_guns
        cls.no_of__life_limit = _player_config_life_limit
        cls.minimum__sprint_speed = _player_config__sprint_speed
        cls.shooting_accuracy = _player__config_shooting_accuracy

    @classmethod
    def _config_file_configuration(cls, _configuration__file):
        return cls(*_configuration__file.split("-"))

    @staticmethod
    def __static_method(string):
        return f"All settings updated {string}"

