from Models.Base import Base


class Enemy(Base):

    def __init__(self, name="Enemy"):
        super().__init__(name)

        """ self.level = 1
        self.xpnextlvl = 0
        self.xpcurrent = 0
        self.xptotal = 0 """

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
