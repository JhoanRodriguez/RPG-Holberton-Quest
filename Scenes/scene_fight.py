back_fight = "Assets/BFights/bb{}.png".format(random.randint(0, 6))

back = utilities.n_render(back_fight, (800, 600))
bat_bg = utilities.n_render("Assets/BFights/bgmenu.jpg", (800, 200))
avatar = utilities.n_render(player.avatar, (110, 100))

lvl_enemy = random.randint(0, 2) if player.lvl < 3 else random.randint(0, 5)
new_enemy = Enemy("Enemy{}".format(lvl_enemy), "Assets/Enemies/Enemy{}.png".format(lvl_enemy))
enemy_ = utilities.n_render(new_enemy.avatar, (300, 250))


attack = utilities.r_text("Attack:", (0, 0, 0),
                          "./Assets/Fonts/bitwise.ttf", 30)
phy = utilities.r_text("Physical", (255, 255, 255),
                       "./Assets/Fonts/bitwise.ttf", 30)
magic = utilities.r_text("Magic:", (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 30)
chol = utilities.r_text("Cholera", (255, 255, 255),
                        "./Assets/Fonts/bitwise.ttf", 30)

surrender = utilities.r_text(
    "Surrender", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

stats = utilities.r_text("Stats", (255, 255, 255),
                         "./Assets/Fonts/bitwise.ttf", 30)

run = True
s_stat = False

while run:

    mouse = pygame.mouse.get_pos()

    if not s_stat:
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


        #  Hover
        if utilities.p_mouse(mouse, (200, 307), (461, 480)):
            phy = utilities.r_text("Physical", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            phy = utilities.r_text("Physical", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

        if utilities.p_mouse(mouse, (200, 300), (532, 550)):
            chol = utilities.r_text("Cholera", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            chol = utilities.r_text("Cholera", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

        if utilities.p_mouse(mouse, (500, 637), (468, 482)):
            surrender = utilities.r_text("Surrender", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            surrender = utilities.r_text("Surrender", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

        if utilities.p_mouse(mouse, (500, 570), (493, 511)):
            stats = utilities.r_text("Stats", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            stats = utilities.r_text("Stats", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

    else:
        stats = utilities.r_text("Stats", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)
        screen.blit(stats, (500, 490))
        exec(open("Scenes/stats.py").read())
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not s_stat:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if utilities.p_mouse(mouse, (200, 307), (461, 480)):
                    utilities.fight(player, new_enemy, "atkdamage")
                if utilities.p_mouse(mouse, (200, 300), (532, 550)):
                    utilities.fight(player, new_enemy, "magic")
                if utilities.p_mouse(mouse, (500, 637), (468, 482)):
                    exec(open("Scenes/men_play.py").read())
                if utilities.p_mouse(mouse, (500, 570), (493, 511)): 
                    s_stat = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if utilities.p_mouse(mouse, (532, 638), (462, 490)):
                    s_stat = False

    pygame.display.update()
    pygame.display.flip()

    if not s_stat:
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
