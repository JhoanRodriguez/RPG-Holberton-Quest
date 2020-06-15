monster = Enemy("Enemy")

while(player.health > 0 and monster.health > 0):
    utilities.fight(player, monster, "atkdamage")
