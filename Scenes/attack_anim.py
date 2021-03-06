from time import sleep
coor = [0, 0]
angle = 90
clock = pygame.time.Clock()

a_player = utilities.r_text("You've caused {:.2f} damage".format(damages[0]), (218, 165, 32),
                            "./Assets/Fonts/bitwise.ttf", 30)
a_monster = utilities.r_text("-{:.2f} health".format(damages[1]), (220, 20, 60),
                             "./Assets/Fonts/bitwise.ttf", 30)

if damages[2] == "player":
    # Player attack

    coor = [220, 360]
    while coor[0] < 350 or coor[1] > 250:
        clock.tick(45)
        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(enemy_, (280, 130))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        weapon = pygame.transform.rotate(weapon, angle)

        screen.blit(weapon, (int(coor[0]), int(coor[1])))
        coor[0], coor[1] = coor[0] + 7, coor[1] - 7

    # Monster Hitted
    coor[0], coor[1] = 280, 130

    while coor[0] < 340:
        clock.tick(45)

        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(enemy_, (coor[0], coor[1]))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        coor[0] += 8
    while coor[0] >= 240:
        clock.tick(45)

        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(enemy_, (coor[0], coor[1]))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        coor[0] -= 8

    coor = [280, 130]

    # Message dmg Player

    while coor[1] > 100:
        clock.tick(45)
        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(enemy_, (280, 130))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        screen.blit(a_player, (coor[0], coor[1]))

        coor[1] -= 1

    if monster.health <= 0:
            monster_die = True

    if not monster_die:
        # Monster attack

        coor[0], coor[1] = 280, 130

        while coor[1] < 230:
            clock.tick(45)

            for event in pygame.event.get():
                pass

            pygame.display.update()
            pygame.display.flip()

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))


            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            screen.blit(enemy_, (coor[0], coor[1]))

            coor[1] += 8   

        # Message dmg Monster

        coor[0], coor[1] = 280, 420
        while coor[1] < 440:
            clock.tick(45)
            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))

            screen.blit(enemy_, (280, 130))

            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            if monster.health > 0:
                screen.blit(a_monster, (coor[0], coor[1]))

            coor[1] += 1

        #  Life Left

        if damages[0] > 0:
            damaged = round(life - damages[1], 2)
        else:
            damaged = (life - damages[1])

        if damaged <= 0:
            damaged = 0.00

        while life >= damaged:
            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))

            screen.blit(enemy_, (280, 130))

            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            if life > 0:
                life = life - 0.05
            else:
                life = 0
                break

            player_health = utilities.r_text("{:.2f}".format(life), (220, 20, 60),
                                            "./Assets/Fonts/bitwise.ttf", 30)

        # END FIGHT

        if life <= 0:
            life = 0
            player_health = utilities.r_text("{:.2f}".format(0), (220, 20, 60),
                                "./Assets/Fonts/bitwise.ttf", 30)
            player_die = True

        player_health = utilities.r_text("{:.2f}".format(life), (225, 225, 225),
                                        "./Assets/Fonts/bitwise.ttf", 30)

else:
    # Monster attack

    coor[0], coor[1] = 280, 130

    while coor[1] < 230:
        clock.tick(45)

        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        screen.blit(enemy_, (coor[0], coor[1]))

        coor[1] += 8

    # Monster dmg

    coor[0], coor[1] = 280, 420

    while coor[1] < 440:
        clock.tick(45)
        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(enemy_, (280, 130))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        screen.blit(a_monster, (coor[0], coor[1]))

        coor[1] += 1

    #  Life Left

    if damages[0] > 0:
        damaged = round(life - damages[1], 2)
    else:
        damaged = (life - damages[1])

    if damaged <= 0:
        damaged = 0.00

    while life >= damaged:
        pygame.display.update()
        pygame.display.flip()

        for event in pygame.event.get():
            pass

        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        screen.blit(enemy_, (280, 130))

        screen.blit(attack, (150, 430))
        screen.blit(phy, (200, 455))

        screen.blit(magic, (150, 500))
        screen.blit(chol, (200, 528))

        screen.blit(surrender, (500, 460))
        screen.blit(stats, (500, 490))

        pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

        if life > 0:
            life = life - 0.05
        else:
            life = 0
            break


        player_health = utilities.r_text("{:.2f}".format(life), (220, 20, 60),
                                        "./Assets/Fonts/bitwise.ttf", 30)

    # END FIGHT

    if life <= 0:
        life = 0
        player_health = utilities.r_text("{:.2f}".format(0), (220, 20, 60),
                                "./Assets/Fonts/bitwise.ttf", 30)
        player_die = True

    player_health = utilities.r_text("{:.2f}".format(life), (225, 255, 255),
                                "./Assets/Fonts/bitwise.ttf", 30)
        

    # Player attack
    if not player_die:
        coor = [220, 360]
        while coor[0] < 350 or coor[1] > 250:
            clock.tick(45)
            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))

            screen.blit(enemy_, (280, 130))

            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            weapon = pygame.transform.rotate(weapon, angle)

            screen.blit(weapon, (int(coor[0]), int(coor[1])))
            coor[0], coor[1] = coor[0] + 7, coor[1] - 7

        # Monster Hitted
        coor[0], coor[1] = 280, 130

        while coor[0] < 340:
            clock.tick(45)

            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))

            screen.blit(enemy_, (coor[0], coor[1]))

            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            coor[0] += 8
        while coor[0] >= 240:
            clock.tick(45)

            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))

            screen.blit(enemy_, (coor[0], coor[1]))

            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            coor[0] -= 8

        # Player dmg

        coor = [280, 130]

        while coor[1] > 100:
            clock.tick(45)
            pygame.display.update()
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            screen.blit(back, (0, 0))
            screen.blit(bat_bg, (0, 400))
            screen.blit(avatar, (5, 420))
            screen.blit(player_health, (7, 530))

            screen.blit(enemy_, (280, 130))

            screen.blit(attack, (150, 430))
            screen.blit(phy, (200, 455))

            screen.blit(magic, (150, 500))
            screen.blit(chol, (200, 528))

            screen.blit(surrender, (500, 460))
            screen.blit(stats, (500, 490))

            pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

            if player.health > 0:
                screen.blit(a_player, (coor[0], coor[1]))

            coor[1] -= 1

        if monster.health <= 0:
            monster_die = True


is_anim = False