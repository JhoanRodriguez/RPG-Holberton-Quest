from Models.Base import Base
from Models.Equipment import Equipment


class Enemy(Base):

    def __init__(self, name="Enemy"):
        super().__init__(name)

        """ self.level = 1
        self.xpnextlvl = 0
        self.xpcurrent = 0
        self.xptotal = 0 """

        self.weapon = Equipment("Knife")
        self.Helmet = Equipment("Helmet")
        self.Gauntlets = Equipment("Gauntlets")
        self.Chest = Equipment("Chest")
        self.Leg = Equipment("Leg")
        self.armor = self.weapon.defense + self.Helmet.defense + \
            self.Gauntlets.defense + self.Chest.defense + self.Leg.defense

        stats = super().load_json_file("Enemy")
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

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value
