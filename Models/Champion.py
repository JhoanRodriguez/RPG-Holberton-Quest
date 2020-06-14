from Models.Base import Base


class Champion(Base):

    def __init__(self, name="Anonymous", race="Human", gender="Male"):
        super().__init__(name)
        self.race = race
        self.gender = gender

        """ self.level = 1
        self.xpnextlvl = 0
        self.xpcurrent = 0
        self.xptotal = 0 """

        stats = super().load_json_file(race)
        stats = stats[0]

        for key, value in stats.items():
            if key == "health":
                self.health = value
            elif key == "atkdamage":
                self.atkdamage = value
            elif key == "defence":
                self.defence = value
            elif key == "magic":
                self.magic = value
            elif key == "speed":
                self.speed = value

    @ property
    def race(self):
        return self.__race

    @ race.setter
    def race(self, value):
        self.__race = value

    @ property
    def gender(self):
        return self.__gender

    @ gender.setter
    def gender(self, value):
        self.__gender = value
