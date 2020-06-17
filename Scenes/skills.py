import json

skilling = True

tablesxp = {}
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


st_exp = utilities.r_text("EXP: {}/{}".format(player.xp, max_exp), ((128, 0, 0)),
                          "./Assets/Fonts/bitwise.ttf", 35)

st_skillp = utilities.r_text("Push Points", ((128, 0, 0)),
                             "./Assets/Fonts/bitwise.ttf", 35)

st_pnts = utilities.r_text("{}".format(player.p_skills), ((128, 0, 0)),
                           None, 50)

st_health = utilities.r_text("Health -> {}".format(0), ((128, 0, 0)),
                             "./Assets/Fonts/bitwise.ttf", 45)
st_defense = utilities.r_text("Defense -> {}".format(0), ((128, 0, 0)),
                              "./Assets/Fonts/bitwise.ttf", 45)
st_damage = utilities.r_text("Damage -> {}".format(0), ((128, 0, 0)),
                             "./Assets/Fonts/bitwise.ttf", 45)
st_magic = utilities.r_text("Magic -> {}".format(0), ((128, 0, 0)),
                            "./Assets/Fonts/bitwise.ttf", 45)
st_speed = utilities.r_text("Speed -> {}".format(0), ((128, 0, 0)),
                            "./Assets/Fonts/bitwise.ttf", 45)

# Operations


class Button:
    def __init__(self, text="", pos=(0, 0), color=(255, 255, 255)):
        self.text = utilities.r_text(
            text, (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 45)
        self.color = color
        self.pos = pos
        self.marc = text

    def button_ins(self):
        a = pygame.draw.circle(screen, self.color, self.pos, 30, 0)
        if a.collidepoint(pygame.mouse.get_pos()):
            if self.marc == "+":
                a = pygame.draw.circle(screen, (0, 125, 0), self.pos, 30, 0)
            elif self.marc == "-":
                a = pygame.draw.circle(screen, (125, 0, 0), self.pos, 30, 0)
        screen.blit(
            self.text, (self.pos[0] - (10 if self.marc == '-' else 20), self.pos[1] - 20))


add_health = Button("+", (370, 165))
less_health = Button("-", (440, 165))

add_defense = Button("+", (370, 245))
less_defense = Button("-", (440, 245))

add_damage = Button("+", (370, 325))
less_damage = Button("-", (440, 325))

add_magic = Button("+", (370, 405))
less_magic = Button("-", (440, 405))

add_speed = Button("+", (370, 485))
less_speed = Button("-", (440, 485))

get_back = utilities.r_text("BACK", ((25, 25, 112)),
                            "./Assets/Fonts/bitwise.ttf", 60)

while skilling:
    mouse = pygame.mouse.get_pos()

    screen.blit(back_play, (0, 0))
    screen.blit(icon, (10, 5))
    screen.blit(p_name, (140, 30))
    screen.blit(p_level, (140, 65))

    screen.blit(st_exp, (500, 45))

    screen.blit(st_skillp, (505, 90))
    screen.blit(st_pnts, (595 - (10 * len(str(player.p_skills))), 130))

    screen.blit(st_health, (30, 150))
    add_health.button_ins()
    less_health.button_ins()

    screen.blit(st_defense, (30, 230))
    add_defense.button_ins()
    less_defense.button_ins()

    screen.blit(st_damage, (30, 310))
    add_damage.button_ins()
    less_damage.button_ins()

    screen.blit(st_magic, (30, 390))
    add_magic.button_ins()
    less_magic.button_ins()

    screen.blit(st_speed, (30, 470))
    add_speed.button_ins()
    less_speed.button_ins()

    screen.blit(get_back, (620, 545))

    if utilities.p_mouse(mouse, (622, 783), (550, 588)):
        get_back = utilities.r_text("BACK", ((255, 255, 255)),
                                    "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (580, 550))
    else:
        get_back = utilities.r_text("BACK", ((25, 25, 112)),
                                    "./Assets/Fonts/bitwise.ttf", 60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            skilling = not skilling
            run = not run
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if utilities.p_mouse(mouse, (622, 783), (550, 588)):
                skilling = not skilling

    pygame.display.update()
