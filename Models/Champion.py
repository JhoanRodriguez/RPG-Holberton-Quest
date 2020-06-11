
class Champion:

    def __init__(self, name="Anonymous", race="Human", gender="Male"):
        self.name = name
        self.race = race
        self.gender = gender
        self.health = 10
        self.atkdamage = 10
        self.defence = 10
        self.magic = 10
        self.speed = 10

        """ self.level = 1
        self.xpnextlvl = 0
        self.xpcurrent = 0
        self.xptotal = 0 """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 11:
            self.__name = value

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
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        if value < 101:
            self.__defence = value

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
