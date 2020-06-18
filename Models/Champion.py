from Models.Base import Base
from Models.Equipment import Equipment
import json


class Champion(Base):

    def __init__(self, name="Anonymous", race="Human", gender="Male", Avatar=""):
        super().__init__(name)
        self.race = race
        self.gender = gender
        self.avatar = Avatar

        self.p_skills = 0

        self.weapon = Equipment("Knife")
        self.Helmet = Equipment("Helmet")
        self.Gauntlets = Equipment("Gauntlets")
        self.Chest = Equipment("Chest")
        self.Leg = Equipment("Leg")
        self.armor = (self.weapon.defense + self.Helmet.defense +
                      self.Gauntlets.defense + self.Chest.defense + self.Leg.defense)

        stats = super().load_json_file(race)
        super().load_character(stats)

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

    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value

    def serialize(self):
        '''
        Serializes the player to JSON.
        '''

        dic = {"name": self.name,
               "health": self.health,
               "p_skills": self.p_skills,
               "atkdamage": self.atkdamage,
               "defense": self.defense,
               "magic": self.magic,
               "speed": self.speed,
               "race": self.race,
               "gender": self.gender,
               "avatar": self.avatar,
               "lvl": self.lvl,
               "xp": self.xp,
               "weapon": {"name": self.weapon.name,
                          "damage": self.weapon.damage,
                          "defense": self.weapon.defense},
               "armor": {"Helmet": {"name": self.Helmet.name,
                                    "damage": self.Helmet.damage,
                                    "defense": self.Helmet.defense},
                         "Gauntlets": {"name": self.Gauntlets.name,
                                       "damage": self.Gauntlets.damage,
                                       "defense": self.Gauntlets.defense},
                         "Chest": {"name": self.Chest.name,
                                   "damage": self.Chest.damage,
                                   "defense": self.Chest.defense},
                         "Leg": {"name": self.Leg.name,
                                 "damage": self.Leg.damage,
                                 "defense": self.Leg.defense}
                         }
               }
        filename = self.name + ".json"

        with open("Database/Saves/" + filename, "w") as player:
            player.write(json.dumps(dic))
