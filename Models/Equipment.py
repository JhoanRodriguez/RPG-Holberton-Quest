class Equipment:

    def __init__(self, name="Weapon/Armor"):
        self.name = name
        self.damage = 0
        self.defense = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        self.__defense = value
