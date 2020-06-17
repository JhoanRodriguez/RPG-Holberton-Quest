back_fight = "Assets/BFights/bb{}.png".format(random.randint(0, 6))

back = utilities.n_render(back_fight, (800, 600))
bat_bg = utilities.n_render("Assets/BFights/bgmenu.jpg", (800, 200))
avatar = utilities.n_render(player.avatar, (110, 100))

enemy_bg = utilities.n_render("Assets/BFights/bgmenu.jpg", (800, 60))

monster_name = ('Aries', 'Anaconda', 'Mosquito',
                'MetalKnight', 'DwarfDrill', 'SpiderWoman')

if not player_die or not monster_die:
    lvl_enemy = random.randint(0, 2) if player.lvl < 3 else random.randint(0, 5)
    monster = Enemy("{}".format(monster_name[lvl_enemy]),
                    "Assets/Enemies/{}.png".format(monster_name[lvl_enemy]))
    enemy_ = utilities.n_render(monster.avatar, (300, 250))

Enemies = ('Aries',
            'Conda',
            'Mosquito',
            'Metal Knight',
            'Dwarf Drill',
            'Spider Woman')

mon_heal = monster.health

show_name = utilities.r_text(Enemies[lvl_enemy], (240,230,140),
                        "./Assets/Fonts/bitwise.ttf", 52)
show_health_en = utilities.r_text("{:.2f}/{:.2f}".format(monster.health, mon_heal), (240,230,140),
                        "./Assets/Fonts/bitwise.ttf", 52)

weapon = utilities.n_render("Assets/Weapons/knife.png", (100, 100))


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

life = player.health

player_health = utilities.r_text("{:.2f}".format(life), (225, 225, 225),
                                 "./Assets/Fonts/bitwise.ttf", 30)
run = True
s_stat = False
is_anim = False

exp_updated = False

while run:

    mouse = pygame.mouse.get_pos()

    if not s_stat and not is_anim and not (player_die or monster_die):
        screen.blit(back, (0, 0))
        screen.blit(bat_bg, (0, 400))
        screen.blit(avatar, (5, 420))
        screen.blit(player_health, (7, 530))

        show_health_en = utilities.r_text("{:.2f}/{:.2f}".format(monster.health, mon_heal), (240,230,140),
                            "./Assets/Fonts/bitwise.ttf", 52)

        screen.blit(enemy_bg, (0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 55), (800, 55), 8)
        screen.blit(show_name, (20, 5))
        screen.blit(show_health_en, (300, 5))
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
            phy = utilities.r_text(
                "Physical", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            phy = utilities.r_text(
                "Physical", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

        if utilities.p_mouse(mouse, (200, 300), (532, 550)):
            chol = utilities.r_text(
                "Cholera", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            chol = utilities.r_text(
                "Cholera", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

        if utilities.p_mouse(mouse, (500, 637), (468, 482)):
            surrender = utilities.r_text(
                "Surrender", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            surrender = utilities.r_text(
                "Surrender", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

        if utilities.p_mouse(mouse, (500, 570), (493, 511)):
            stats = utilities.r_text(
                "Stats", (220, 20, 60), "./Assets/Fonts/bitwise.ttf", 30)
        else:
            stats = utilities.r_text(
                "Stats", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)

    else:
        if s_stat:
            stats = utilities.r_text(
                "Stats", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)
            screen.blit(stats, (500, 490))
            exec(open("Scenes/stats.py").read())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if not s_stat and not is_anim and not (player_die or monster_die):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if utilities.p_mouse(mouse, (200, 307), (461, 480)):
                    is_anim = True
                    damages = utilities.fight(player, monster, "atkdamage")
                    phy = utilities.r_text(
                            "Physical", (255, 255, 255), "./Assets/Fonts/bitwise.ttf", 30)
                    exec(open("Scenes/attack_anim.py").read())
                if utilities.p_mouse(mouse, (200, 300), (532, 550)):
                    utilities.fight(player, monster, "magic")
                if utilities.p_mouse(mouse, (500, 637), (468, 482)):
                    exec(open("Scenes/men_play.py").read())
                if utilities.p_mouse(mouse, (500, 570), (493, 511)):
                    s_stat = True
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s_stat:
                    if utilities.p_mouse(mouse, (532, 638), (462, 490)):
                        s_stat = False
                if monster_die or player_die:
                    if utilities.p_mouse(mouse, c_x, c_y):
                        player_die = False
                        monster_die = False
                        exec(open("Scenes/men_play.py").read())
                    if monster_die:
                        if utilities.p_mouse(mouse, (183, 544), (291, 342)):
                            player_die = False
                            monster_die = False
                            exec(open("Scenes/scene_fight.py").read())

    pygame.display.update()
    pygame.display.flip()

    if monster_die or player_die:
        exec(open("Scenes/prompts.py").read())

    if not s_stat:
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
