""" from Base import Base
from Champion import Champion
from Enemy import Enemy """


"""  Recive the objetc player and monster,
    damagetype is the selection of the player ( magic or atkdamage)
 """


def fight(player, monster, damagetype):
    if player.speed > monster.speed:
        # player attacks first
        if damagetype == "atkdamage":
            damage = player.atkdamage - monster.defence
            damage = monster.health - damage
            monster.health(damage)
            if monster.health <= 0:
                return
        elif damagetype == "magic":
            damage = player.magic - monster.defence
            damage = monster.health - damage
            monster.health(damage)
            if monster.health <= 0:
                return
        damage = monster.atkdamage - player.defence
        damage = player.health - damage
        player.health(damage)
        if player.health <= 0:
            return
    else:
        damage = monster.atkdamage - player.defence
        damage = player.health - damage
        player.health(damage)
        if player.health <= 0:
            return
        if damagetype == "atkdamage":
            damage = player.atkdamage - monster.defence
            damage = monster.health - damage
            monster.health(damage)
            if monster.health <= 0:
                return
        elif damagetype == "magic":
            damage = player.magic - monster.defence
            damage = monster.health - damage
            monster.health(damage)
            if monster.health <= 0:
                return
