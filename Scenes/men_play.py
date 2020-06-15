b_fight = utilities.n_render("./Assets/Images/banner.png", (250, 100))
fight = utilities.r_text("Fight", (00, 32, 64),
                         "./Assets/Fonts/bitwise.ttf", 60)

b_save = utilities.n_render("./Assets/Images/banner.png", (250, 100))
save = utilities.r_text("Save", (00, 32, 64),
                        "./Assets/Fonts/bitwise.ttf", 60)

b_exit = utilities.n_render("./Assets/Images/banner.png", (250, 100))
exit = utilities.r_text("Exit", (00, 32, 64),
                        "./Assets/Fonts/bitwise.ttf", 60)

# PLAYER STATS

life_t = {'Human': 10,
          'Orc': 9,
          'Dwarf': 9,
          'Elf': 9}

if player.gender == 'Male':
    icon = utilities.n_render("./Assets/Images/man_avatar.png", (110, 100))
else:
    icon = utilities.n_render("./Assets/Images/woman_avatar.png", (110, 100))

p_name = utilities.r_text("Name: " + player.name, (205, 92, 92),
                          "./Assets/Fonts/bitwise.ttf", 35)

p_health = utilities.r_text("Health: " +
                            str((round(player.health * 100
                                       / life_t[player.race]))) + "%",
                            (205, 92, 92),
                            "./Assets/Fonts/bitwise.ttf", 35)

p_race = utilities.r_text("Race: " + player.race, (205, 92, 92),
                          "./Assets/Fonts/bitwise.ttf", 35)

p_damage = utilities.r_text("Damage: " + str(player.atkdamage), (205, 92, 92),
                            "./Assets/Fonts/bitwise.ttf", 35)

run = True

while run:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if utilities.p_mouse(mouse, (309, 502), (195, 250)):
                print("Fight!")
            elif utilities.p_mouse(mouse, (309, 502), (293, 348)):
                print("Save")
            elif utilities.p_mouse(mouse, (309, 502), (395, 448)):
                print("Exit")

    screen.blit(icon, (10, 5))
    screen.blit(p_name, (130, 30))
    screen.blit(p_race, (500, 30))
    screen.blit(p_health, (130, 65))
    screen.blit(p_damage, (500, 65))

    screen.blit(b_fight, (280, 150))
    screen.blit(fight, (335, 195))  # FIGHT

    screen.blit(b_fight, (280, 250))
    screen.blit(save, (335, 295))  # SAVE

    screen.blit(b_fight, (280, 350))
    screen.blit(exit, (350, 400))  # EXIT

    pygame.display.update()
    screen.fill((50, 50, 50))
