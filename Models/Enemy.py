from Models.Base import Base


class Enemy(Base):

    def __init__(self, name="Enemy"):
        super().__init__(name)

        """ self.level = 1
        self.xpnextlvl = 0
        self.xpcurrent = 0
        self.xptotal = 0 """

        stats = super().load_json_file(name)
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
