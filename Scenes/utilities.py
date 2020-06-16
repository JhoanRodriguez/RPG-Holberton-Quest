import pygame
import random


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

    # f = pygame.font.SysFont(font, size)

    t_surface = f.render(text, False, color)

    return t_surface


def EndBattle(player, monster):
    stats = player.load_save_json_file(player.name)
    for key, value in stats.items():
        if key == "health":
            player.health = value
    print("You have being healed")
    player.xp += monster.xp
    print("{} just earned {} exp and now have {}.".format(
        player.name, monster.xp, player.xp))


def fight(player, monster, damagetype):
    if player.speed > monster.speed:
        # player attacks first
        if damagetype == "atkdamage":
            damage = (player.atkdamage + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with physical  damage and deals {:.2f} to the {}, now he have {:.2f} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                print("{} died".format(monster.name))
                EndBattle(player, monster)
                return
        elif damagetype == "magic":
            damage = (player.magic + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with magic and deals {:.2f} to the {}, now he have {:.2f} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                print("{} died".format(monster.name))
                stats = player.load_save_json_file(player.name)
                for key, value in stats.items():
                    if key == "health":
                        player.health = value
                return
        damage = (monster.atkdamage + monster.weapon.damage *
                  (random.randrange(1, 100)/100)) - (player.defense + (player.armor * random.randrange(1, 100)/100))
        if damage < 0:
            damage = 0
        live = player.health - damage
        player.health = live
        print(
            "{} atk with physical  damage and deals {:.2f} to the {}, now he have {:.2f} of HP left".format(monster.name, damage, player.name, player.health))
        if player.health <= 0:
            print("{} died".format(player.name))
            return
    else:
        # Enemy attacks first
        damage = (monster.atkdamage + monster.weapon.damage *
                  (random.randrange(1, 100)/100)) - (player.defense + (player.armor * random.randrange(1, 100)/100))
        if damage < 0:
            damage = 0
        live = player.health - damage
        player.health = live
        print(
            "{} atk with physical  damage and deals {:.2f} to the {}, now he have {:.2f} of HP left".format(monster.name, damage, player.name, player.health))
        if player.health <= 0:
            print("{} died".format(player.name))
            return
        if damagetype == "atkdamage":
            damage = (player.atkdamage + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with physical  damage and deals {:.2f} to the {}, now he have {:.2f} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                print("{} died".format(monster.name))
                stats = player.load_save_json_file(player.name)
                for key, value in stats.items():
                    if key == "health":
                        player.health = value
                return
        elif damagetype == "magic":
            damage = (player.magic + player.weapon.damage *
                      (random.randrange(1, 100)/100)) - (monster.defense + (monster.armor * random.randrange(1, 100)/100))
            if damage < 0:
                damage = 0
            live = monster.health - damage
            monster.health = live
            print(
                "{} atk with magic and deals {:.2f} to the {}, now he have {:.2f} of HP left".format(player.name, damage, monster.name, monster.health))
            if monster.health <= 0:
                print("{} died".format(monster.name))
                stats = player.load_save_json_file(player.name)
                for key, value in stats.items():
                    if key == "health":
                        player.health = value
                return
