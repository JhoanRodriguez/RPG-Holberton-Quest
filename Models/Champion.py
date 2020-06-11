from Base import Base


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
        for item in stats:
            if item == "health":
                self.health(item)
            elif item == "atkdamage":
                self.atkdamage(item)
            elif item == "defence":
                self.defence(item)
            elif item == "magic":
                self.magic(item)
            elif item == "speed":
                self.speed(item)

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        self.__race = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value
