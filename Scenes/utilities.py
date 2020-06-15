import pygame
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

    #f = pygame.font.SysFont(font, size)

    t_surface = f.render(text, False, color)

    return t_surface


def fight(player, monster, damagetype):
    if player.speed > monster.speed:
        # player attacks first
        if damagetype == "atkdamage":
            damage = player.atkdamage - monster.defence
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with physicall damage and deals {} to the {}, now he have {} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                return
        elif damagetype == "magic":
            damage = player.magic - monster.defence
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with magic and deals {} to the {}, now he have {} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                return
        damage = monster.atkdamage - player.defence
        live = player.health - damage
        player.health = live
        print(
            "{} atk with physicall damage and deals {} to the {}, now he have {} of HP left".format(monster.name, damage, player.name, player.health))
        if player.health <= 0:
            return
    else:
        # player attacks first
        damage = monster.atkdamage - player.defence
        live = player.health - damage
        player.health = live
        print(
            "{} atk with physicall damage and deals {} to the {}, now he have {} of HP left".format(monster.name, damage, player.name, player.health))
        if player.health <= 0:
            return
        if damagetype == "atkdamage":
            damage = player.atkdamage - monster.defence
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with physicall damage and deals {} to the {}, now he have {} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                return
        elif damagetype == "magic":
            damage = player.magic - monster.defence
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with magic and deals {} to the {}, now he have {} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                return
