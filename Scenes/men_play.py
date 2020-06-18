from time import sleep
import json

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

confirm = True

# SOUNDTRACK
pygame.mixer.init()


# PLAYER STATS

icon = utilities.n_render(player.avatar, (110, 100))

p_name = utilities.r_text("Name: " + player.name, (128, 0, 0),
                          "./Assets/Fonts/bitwise.ttf", 35)

p_level = utilities.r_text("Level: {}".format(player.lvl), (128, 0, 0),
                           "./Assets/Fonts/bitwise.ttf", 35)

pygame.mouse.set_cursor(*pygame.cursors.arrow)

run = True

skilling = False

attribs = {}

filename = "./Database/Saves/" + player.name + ".json"
try:
    with open(filename, "r") as Myfile:
        attribs = json.load(Myfile)
except Exception:
    raise FileExistsError("{} was not found".format(filename))

for a, b in attribs.items():
    if a == "health":
        total_life = b


for a, b in attribs.items():
    if a == "health":
        if player.health > b:
            skilled = True
            break
    elif a == "defense":
        if player.defense > b:
            skilled = True
            break
    elif a == "atkdamage":
        if player.atkdamage > b:
            skilled = True
            break
    elif a == "magic":
        if player.magic > b:
            skilled = True
            break
    elif a == "speed":
        if player.speed > b:
            skilled = True
            break
else:
    skilled = False

while run:
    mouse = pygame.mouse.get_pos()

    # Hover
    if not skilling:
        if utilities.p_mouse(mouse, (550, 672), (156, 200)):
            fight = utilities.r_text("Fight", (255, 255, 255),
                                     "./Assets/Fonts/bitwise.ttf", 60)
            screen.blit(pointer, (510, 160))
            pygame.display.flip()
        else:
            fight = utilities.r_text("Fight", (25, 25, 112),
                                     "./Assets/Fonts/bitwise.ttf", 60)

        if utilities.p_mouse(mouse, (550, 690), (223, 263)):
            _stats_ = utilities.r_text("Stats", (255, 255, 255),
                                       "./Assets/Fonts/bitwise.ttf", 60)
            screen.blit(pointer, (510, 230))
            pygame.display.flip()
        else:
            _stats_ = utilities.r_text("Stats", (25, 25, 112),
                                       "./Assets/Fonts/bitwise.ttf", 60)

        if utilities.p_mouse(mouse, (550, 680), (290, 327)):
            save = utilities.r_text("Save", (255, 255, 255),
                                    "./Assets/Fonts/bitwise.ttf", 60)
            screen.blit(pointer, (510, 290))
            pygame.display.flip()
        else:
            save = utilities.r_text("Save", (25, 25, 112),
                                    "./Assets/Fonts/bitwise.ttf", 60)

        if utilities.p_mouse(mouse, (567, 660), (345, 380)):
            exit = utilities.r_text("Exit", (255, 255, 255),
                                    "./Assets/Fonts/bitwise.ttf", 60)
            screen.blit(pointer, (530, 350))
            pygame.display.flip()
        else:
            exit = utilities.r_text("Exit", (25, 25, 112),
                                    "./Assets/Fonts/bitwise.ttf", 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import sys
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if utilities.p_mouse(mouse, (550, 672), (156, 200)):
                    exec(open("Scenes/scene_fight.py").read())
                elif utilities.p_mouse(mouse, (550, 690), (223, 263)):
                    sleep(0.2)
                    exec(open("Scenes/skills.py").read())
                elif utilities.p_mouse(mouse, (550, 680), (290, 327)):
                    player.serialize()
                elif utilities.p_mouse(mouse, (567, 660), (345, 380)):
                    exec(open("main.py").read())
                    run = False

    if run and not skilling:
        screen.blit(back_play, (0, 0))
        screen.blit(icon, (10, 5))
        screen.blit(p_name, (140, 30))
        screen.blit(p_level, (140, 65))

        screen.blit(fight, (550, 150))  # FIGHT

        screen.blit(_stats_, (550, 220))  # STATS

        screen.blit(save, (550, 280))  # SAVE

        screen.blit(exit, (565, 340))  # EXIT

        pygame.display.update()
