import pygame
import random
import json


def p_mouse(mouse_obj, pos_x=(0, 0), pos_y=(0, 0)):
    '''
    Get the position of the mouse.
    '''
    return ((pos_x[0] < mouse_obj[0] < pos_x[1]) and
            (pos_y[0] < mouse_obj[1] < pos_y[1]))


def n_render(path="", size=(0, 0)):
    '''
    Creates a new render.
    '''
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, size)

    return img


def r_text(text="", color=(0, 0, 0), font="", size=0):
    '''
    Renders a text.
    '''

    f = pygame.font.Font(font, size)
    t_surface = f.render(text, False, color)

    return t_surface


def drop(player):
    if random.randrange(1, 100) < 10:
        Randomitem = random.randrange(0, 5)
        tabledrop = {}
        filename = "./Database/Drops.json"
        try:
            with open(filename, "r") as Myfile:
                tabledrop = json.load(Myfile)
        except Exception:
            raise FileExistsError("{} was not found".format(filename))
        tabledrop = tabledrop[Randomitem]
        for key, value in tabledrop.items():
            if key == "name":
                namedrop = value
            elif key == "damage":
                damagedrop = value
            elif key == "defense":
                defensedrop = value

        if namedrop == player.Helmet.name:
            player.Helmet.defense += defensedrop
            return (
                "You've dropped a {} with {} of defense!".format(namedrop, defensedrop))
        elif namedrop == player.Gauntlets.name:
            player.Gauntlets.defense += defensedrop
            return (
                "You've dropped a {} with {} of defense!".format(namedrop, defensedrop))
        elif namedrop == player.Chest.name:
            player.Chest.defense += defensedrop
            return (
                "You've dropped a {} with {} of defense!".format(namedrop, defensedrop))
        elif namedrop == player.Leg.name:
            player.Leg.defense += defensedrop
            return (
                "You've dropped a {} with {} of defense!".format(namedrop, defensedrop))
        else:
            player.weapon.name = namedrop
            player.weapon.damage += damagedrop
            return (
                "You've dropped a {} with {} of damage\n\t\tIt is equipped now!.".format(namedrop, damagedrop))

    return ("")

def fight(player, monster, damagetype):
    attributes = [0.00, 0.00, "player", 0.00, "drop"]
    life = player.health
    if player.speed > monster.speed:
        # player attacks first

        if damagetype == "atkdamage":
            damage = (player.atkdamage + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            attributes[0] = damage
            live = monster.health - damage
            monster.health = live
            if monster.health <= 0:
                player.health = life
                attributes[3] = player.health
                attributes[4] = drop(player)
                return attributes
        elif damagetype == "magic":
            damage = (player.magic + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            attributes[0] = damage
            live = monster.health - damage
            monster.health = live
            if monster.health <= 0:
                player.health = life
                attributes[3] = player.health
                attributes[4] = drop(player)
                return attributes
        damage = (monster.atkdamage + monster.weapon.damage *
                  (random.randrange(1, 100)/100)) - (player.defense + (player.armor * random.randrange(1, 100)/100))
        if damage < 0:
            damage = 0
        attributes[1] = damage
        live = player.health - damage
        player.health = live
        if player.health <= 0:
            player.health = life
            attributes[3] = player.health
            return attributes
    else:
        # Enemy attacks first

        damage = (monster.atkdamage + monster.weapon.damage *
                  (random.randrange(1, 100)/100)) - (player.defense + (player.armor * random.randrange(1, 100)/100))
        attributes[2] = "monster"
        if damage < 0:
            damage = 0
        damage[1] = damage
        live = player.health - damage
        player.health = live
        if player.health <= 0:
            player.health = life
            attributes[3] = player.health
            return attributes
        if damagetype == "atkdamage":
            damage = (player.atkdamage + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            attributes[0] = damage
            live = monster.health - damage
            monster.health = live
            if monster.health <= 0:
                player.health = life
                attributes[3] = player.health
                attributes[4] = drop(player)
                return attributes
        elif damagetype == "magic":
            damage = (player.magic + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            attributes[0] = damage
            live = monster.health - damage
            monster.health = live
            if monster.health <= 0:
                player.health = life
                attributes[3] = player.health
                attributes[4] = drop(player)
                return attributes

    return (attributes)
