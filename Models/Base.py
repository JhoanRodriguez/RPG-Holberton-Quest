import json


class Base:

    def __init__(self, name="name"):
        self.name = name
        self.health = 10
        self.atkdamage = 10
        self.defense = 10
        self.magic = 10
        self.speed = 10
        self.exp = 0
        self.lvl = 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 11:
            self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 101:
            self.__health = value

    @property
    def atkdamage(self):
        return self.__atkdamage

    @atkdamage.setter
    def atkdamage(self, value):
        if value < 101:
            self.__atkdamage = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if value < 101:
            self.__defense = value

    @property
    def magic(self):
        return self.__magic

    @magic.setter
    def magic(self, value):
        if value < 101:
            self.__magic = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 101:
            self.__speed = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This functions returns the json string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes the json
        string representation of list_objs
        to a file
        """

        print(cls.__dict__)
        # filename = cls.__getattribute__('name') + '.json'
        newlist = []
        if list_objs is None:
            cls.to_json_string(list_objs)
        else:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))
        with open(filename, "w") as Myfile:
            Myfile.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list
        of the json string represenation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def load_json_file(self, json_file):
        newlist = {}
        if json_file is not None:
            filename = "./Database/" + json_file + ".json"
        try:
            with open(filename, "r") as Myfile:
                newlist = json.load(Myfile)
        except Exception:
            pass
        return newlist

    def load_save_json_file(self, json_file):
        newlist = {}
        if json_file is not None:
            filename = "./Database/Saves/" + json_file + ".json"
        try:
            with open(filename, "r") as Myfile:
                newlist = json.load(Myfile)
        except Exception:
            pass
        return newlist

    def load_character(self, stats=[]):
        stats = stats[0]

        for key, value in stats.items():
            if key == "health":
                self.health = value
            elif key == "atkdamage":
                self.atkdamage = value
            elif key == "defense":
                self.defense = value
            elif key == "magic":
                self.magic = value
            elif key == "speed":
                self.speed = value
            elif key == "weapon":
                for index, val in value.items():
                    if index == "name":
                        self.weapon.name = val
                    elif index == "damage":
                        self.weapon.damage = val
                    elif index == "defense":
                        self.weapon.defense = val
            elif key == "armor":
                for index, val in value.items():
                    if index == "Helmet":
                        for idx, value in val.items():
                            if idx == "name":
                                self.Helmet.name = value
                            elif idx == "damage":
                                self.Helmet.damage = value
                            elif idx == "defense":
                                self.Helmet.defense = value
                    elif index == "Gauntlets":
                        for idx, value in val.items():
                            if idx == "name":
                                self.Gauntlets.name = value
                            elif idx == "damage":
                                self.Gauntlets.damage = value
                            elif idx == "defense":
                                self.Gauntlets.defense = value
                    elif index == "Chest":
                        for idx, value in val.items():
                            if idx == "name":
                                self.Chest.name = value
                            elif idx == "damage":
                                self.Chest.damage = value
                            elif idx == "defense":
                                self.Chest.defense = value
                    elif index == "Leg":
                        for idx, value in val.items():
                            if idx == "name":
                                self.Leg.name = value
                            elif idx == "damage":
                                self.Leg.damage = value
                            elif idx == "defense":
                                self.Leg.defense = value
            elif key == "lvl":
                self.lvl = value
            elif key == "exp":
                self.exp = value
