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


def fight(player, monster, damagetype):
    attributes = [0.00, 0.00, "player", 0.00]
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
                return attributes

    return (attributes)
