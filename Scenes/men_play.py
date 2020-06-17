back_play = utilities.n_render("./Assets/Images/back_play.jpg", (800, 600))

pointer = utilities.n_render("./Assets/Images/pointer.png", (30, 30))

fight = utilities.r_text("Fight", (25, 25, 112),
                         "./Assets/Fonts/bitwise.ttf", 60)
_stats_ = utilities.r_text("Stats", (25, 25, 112),
                        "./Assets/Fonts/bitwise.ttf", 60)
save = utilities.r_text("Save", (25, 25, 112),
                        "./Assets/Fonts/bitwise.ttf", 60)
exit = utilities.r_text("Exit", (25, 25, 112),
                        "./Assets/Fonts/bitwise.ttf", 60)

# PLAYER STATS

life_t = {'Human': 10,
          'Orc': 9,
          'Dwarf': 9,
          'Elf': 9}

icon = utilities.n_render(player.avatar, (110, 100))

p_name = utilities.r_text("Name: " + player.name, (128, 0, 0),
                          "./Assets/Fonts/bitwise.ttf", 35)

p_level = utilities.r_text("Level: {}".format(player.lvl), (128, 0, 0),
                            "./Assets/Fonts/bitwise.ttf", 35)

#p_health = utilities.r_text("Health: " +
#                            str((round(player.health * 100
#                                       / life_t[player.race]))) + "%",
#                            (205, 92, 92),
#                            "./Assets/Fonts/bitwise.ttf", 35)

#p_race = utilities.r_text("Race: " + player.race, (205, 92, 92),
#                          "./Assets/Fonts/bitwise.ttf", 35)

pygame.mouse.set_cursor(*pygame.cursors.arrow)

run = True

player_die = False
monster_die = False

while run:
    mouse = pygame.mouse.get_pos()

    # Hover
    if utilities.p_mouse(mouse, (550, 672), (156, 200)):
        fight = utilities.r_text("Fight", (255, 255, 255),
                         "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (510, 160))
        pygame.display.update()
        pygame.display.flip()
    else:
            fight = utilities.r_text("Fight", (25, 25, 112),
                         "./Assets/Fonts/bitwise.ttf", 60)

    if utilities.p_mouse(mouse, (550, 690), (223, 263)):
        _stats_ = utilities.r_text("Stats", (255, 255, 255),
                        "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (510, 230))
        pygame.display.update()
        pygame.display.flip()
    else:
        _stats_ = utilities.r_text("Stats", (25, 25, 112),
                        "./Assets/Fonts/bitwise.ttf", 60)

    if utilities.p_mouse(mouse, (550, 680), (290, 327)):
        save = utilities.r_text("Save", (255, 255, 255),
                        "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (510, 290))
        pygame.display.update()
        pygame.display.flip()
    else:
        save = utilities.r_text("Save", (25, 25, 112),
                        "./Assets/Fonts/bitwise.ttf", 60)
    
    if utilities.p_mouse(mouse, (567, 660), (345, 380)):
        exit = utilities.r_text("Exit", (255, 255, 255),
                      "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (530, 350))
        pygame.display.update()
        pygame.display.flip()
    else:
        exit = utilities.r_text("Exit", (25, 25, 112),
                      "./Assets/Fonts/bitwise.ttf", 60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if utilities.p_mouse(mouse, (550, 672), (156, 200)):
                exec(open("Scenes/scene_fight.py").read())
            elif utilities.p_mouse(mouse, (550, 690), (223, 263)):
                print("stats")
            elif utilities.p_mouse(mouse, (550, 680), (290, 327)):
                player.serialize()
            elif utilities.p_mouse(mouse, (567, 660), (345, 380)):
                exec(open("main.py").read())
                run = False

    if run:
        screen.blit(back_play, (0, 0))
        screen.blit(icon, (10, 5))
        screen.blit(p_name, (140, 30))
        screen.blit(p_level, (140, 65))

        screen.blit(fight, (550, 150))  # FIGHT

        screen.blit(_stats_, (550, 220))  # STATS        

        screen.blit(save, (550, 280))  # SAVE

        screen.blit(exit, (565, 340))  # EXIT

        pygame.display.update()
