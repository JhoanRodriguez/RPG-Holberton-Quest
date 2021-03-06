from Models.Base import Base
from Models.Equipment import Equipment


class Enemy(Base):

    def __init__(self, name="Enemy", avatar=""):
        super().__init__(name)

        self.avatar = avatar
        self.weapon = Equipment("Knife")
        self.Helmet = Equipment("Helmet")
        self.Gauntlets = Equipment("Gauntlets")
        self.Chest = Equipment("Chest")
        self.Leg = Equipment("Leg")
        self.armor = self.weapon.defense + self.Helmet.defense + \
            self.Gauntlets.defense + self.Chest.defense + self.Leg.defense

        stats = super().load_json_file(self.name)
        super().load_character(stats)

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value
