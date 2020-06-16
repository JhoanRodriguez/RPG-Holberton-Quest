from time import sleep
coor = [220, 360]


while coor[0] < 350 or coor[1] > 250:
    pygame.display.update()
    pygame.display.flip()
    
    screen.blit(back, (0, 0))
    screen.blit(bat_bg, (0, 400))
    screen.blit(avatar, (5, 420))

    screen.blit(enemy_, (280, 130))

    screen.blit(attack, (150, 430))
    screen.blit(phy, (200, 455))

    screen.blit(magic, (150, 500))
    screen.blit(chol, (200, 528))

    screen.blit(surrender, (500, 460))
    screen.blit(stats, (500, 490))

    pygame.draw.line(screen, (255, 255, 255), (0, 400), (800, 400), 8)

    screen.blit(weapon, (int(coor[0]), int(coor[1])))
    coor[0], coor[1] = coor[0] + 5.5, coor[1] - 5.5

a_player = utilities.r_text("You've caused {:.2f} damage".format(damages[0]), (218, 165, 32),
                          "./Assets/Fonts/bitwise.ttf", 30)
a_monster = utilities.r_text("-{:.2f} health".format(damages[1]), (220, 20, 60),
                          "./Assets/Fonts/bitwise.ttf", 30)

if damages[2] == "player":
    coor = [280, 130]

    while coor[1] > 100:
        pygame.display.update()
        pygame.display.flip()
        
        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))

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

    coor[0], coor[1] = 280, 420
    while coor[1] < 440:
        pygame.display.update()
        pygame.display.flip()
        
        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))

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
else:
    coor[0], coor[1] = 280, 420
    
    while coor[1] < 440:
        pygame.display.update()
        pygame.display.flip()
        
        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))

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

    coor = [280, 130]

    while coor[1] > 100:
        pygame.display.update()
        pygame.display.flip()
        
        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))

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

sleep(0.5)
is_anim = False