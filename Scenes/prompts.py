import json

if monster_die == True:
    experience = ["{}".format(player.lvl), "{}".format(player.xp)]
    message = "You win!"
    wh = (255, 350)
    c_x = (258, 423)
    c_y = (357, 403)

elif player_die == True:
    message = "You've died"
    wh = (255, 250)
    c_x = (258, 423)
    c_y = (255, 307)

# Hover
if utilities.p_mouse(mouse, c_x, c_y):
    # MENU
    m_menu = utilities.r_text("Menu", (72, 61, 139),
                              "./Assets/Fonts/bitwise.ttf", 72)
else:
    m_menu = utilities.r_text("Menu", (255, 255, 255),
                              "./Assets/Fonts/bitwise.ttf", 72)

if utilities.p_mouse(mouse, (183, 544), (291, 342)):
    m_fight = utilities.r_text("Go to fight!", (72, 61, 139),
                               "./Assets/Fonts/bitwise.ttf", 72)
else:
    m_fight = utilities.r_text("Go to fight!", (255, 255, 255),
                               "./Assets/Fonts/bitwise.ttf", 72)

m_prompt = utilities.r_text(message, (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 72)

# Experience

tablexp = {}
filename = "./Database/Experience.json"
try:
    with open(filename, "r") as Myfile:
        tablexp = json.load(Myfile)
except Exception:
    raise FileExistsError("{} was not found".format(filename))
tablexp = tablexp[0]
for key, value in tablexp.items():
    if key == str(player.lvl):
        max_exp = value
        #if value <= player.xp:
        #    player.lvl += 1
        #    player.xp -= value

is_up = False

if monster_die:
    while player.xp <= monster.xp:

        if player.xp == max_exp:
            player.lvl += 1
            monster.xp = 0
            is_up = True
            break

        m_lvl = utilities.r_text("Exp: {}/{} (LvL. {})".format(player.xp, max_exp, player.lvl), (255, 255, 255),
                                   "./Assets/Fonts/bitwise.ttf", 40)

        pygame.draw.rect(screen, (255, 165, 0), (100, 50, 500, 400), 0)

        screen.blit(m_prompt, (160, 50) if message == "You've died" else (210, 50))
        screen.blit(m_menu, (wh))
        screen.blit(m_fight, (180, 280))

        screen.blit(m_lvl, (120, 130))

        pygame.display.update()
        pygame.display.flip()

        player.xp += 1


pygame.draw.rect(screen, (255, 165, 0), (100, 50, 500, 400), 0)

screen.blit(m_prompt, (160, 50) if message == "You've died" else (210, 50))
screen.blit(m_menu, (wh))
screen.blit(m_fight, (180, 280))

screen.blit(m_lvl, (115, 130))

# Hover
if utilities.p_mouse(mouse, c_x, c_y):
    # MENU
    m_menu = utilities.r_text("Menu", (72, 61, 139),
                              "./Assets/Fonts/bitwise.ttf", 72)
else:
    m_menu = utilities.r_text("Menu", (255, 255, 255),
                              "./Assets/Fonts/bitwise.ttf", 72)

if utilities.p_mouse(mouse, (183, 544), (291, 342)):
    m_fight = utilities.r_text("Go to fight!", (72, 61, 139),
                               "./Assets/Fonts/bitwise.ttf", 72)
else:
    m_fight = utilities.r_text("Go to fight!", (255, 255, 255),
                               "./Assets/Fonts/bitwise.ttf", 72)


if is_up:
    player.xp = 0