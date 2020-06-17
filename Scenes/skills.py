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

max_points = player.p_skills

# Operations


class Button:
    def __init__(self, name="", text="", pos=(0, 0), button_pair=None, color=(255, 255, 255)):
        self.text = utilities.r_text(
            text, (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 45)
        self.color = color
        self.pos = pos
        self.marc = text
        self.total_skills = player.p_skills

        self.name = name

        if self.name == "health":
            self.pointed = h_pointed
        elif self.name == "defense":
            self.pointed = d_pointed
        elif self.name == "damage":
            self.pointed = da_pointed
        elif self.name == "magic":
            self.pointed = ma_pointed
        elif self.name == "speed":
            self.pointed = sp_pointed

        self.pair = button_pair

    def button_ins(self):
        self.btn = pygame.draw.circle(screen, self.color, self.pos, 30, 0)
        # Hover
        if self.btn.collidepoint(pygame.mouse.get_pos()):
            if self.marc == "+":
                self.btn = pygame.draw.circle(
                    screen, (0, 125, 0), self.pos, 30, 0)
            elif self.marc == "-":
                self.btn = pygame.draw.circle(
                    screen, (125, 0, 0), self.pos, 30, 0)
        screen.blit(
            self.text, (self.pos[0] - (10 if self.marc == '-' else 20), self.pos[1] - 20))

    def button_action(self):
        if self.btn.collidepoint(pygame.mouse.get_pos()):
            if self.marc == "+":
                if player.p_skills > 0:
                    player.p_skills -= 1
                    self.pointed += 1
            else:
                if self.pair.pointed > 0:
                    player.p_skills += 1
                    self.pair.pointed -= 1


add_health = Button("health", "+", (370, 165))
#less_health = Button("health", "-", (440, 165), add_health)

add_defense = Button("defense", "+", (370, 245))
#less_defense = Button("defense", "-", (440, 245), add_defense)

add_damage = Button("damage", "+", (370, 325))
#less_damage = Button("damage", "-", (440, 325), add_damage)

add_magic = Button("magic", "+", (370, 405))
#less_magic = Button("magic", "-", (440, 405), add_magic)

add_speed = Button("speed", "+", (370, 485))
#less_speed = Button("speed", "-", (440, 485), add_speed)

get_back = utilities.r_text("BACK", ((25, 25, 112)),
                            "./Assets/Fonts/bitwise.ttf", 60)

confirm_b = utilities.r_text("CONFIRM", ((25, 25, 112)),
                             "./Assets/Fonts/bitwise.ttf", 60)

while skilling:
    mouse = pygame.mouse.get_pos()

    st_pnts = utilities.r_text("{}".format(player.p_skills), ((128, 0, 0)),
                               None, 50)

    st_health = utilities.r_text("Health -> {}".format(add_health.pointed), ((128, 0, 0)),
                                 "./Assets/Fonts/bitwise.ttf", 45)
    st_defense = utilities.r_text("Defense -> {}".format(add_defense.pointed), ((128, 0, 0)),
                                  "./Assets/Fonts/bitwise.ttf", 45)
    st_damage = utilities.r_text("Damage -> {}".format(add_damage.pointed), ((128, 0, 0)),
                                 "./Assets/Fonts/bitwise.ttf", 45)
    st_magic = utilities.r_text("Magic -> {}".format(add_magic.pointed), ((128, 0, 0)),
                                "./Assets/Fonts/bitwise.ttf", 45)
    st_speed = utilities.r_text("Speed -> {}".format(add_speed.pointed), ((128, 0, 0)),
                                "./Assets/Fonts/bitwise.ttf", 45)

    screen.blit(back_play, (0, 0))
    screen.blit(icon, (10, 5))
    screen.blit(p_name, (140, 30))
    screen.blit(p_level, (140, 65))

    screen.blit(st_exp, (500, 45))

    screen.blit(st_skillp, (505, 90))
    screen.blit(st_pnts, (595 - (10 * len(str(player.p_skills))), 130))

    screen.blit(st_health, (30, 150))
    add_health.button_ins()
    #less_health.button_ins()

    screen.blit(st_defense, (30, 230))
    add_defense.button_ins()
    #less_defense.button_ins()

    screen.blit(st_damage, (30, 310))
    add_damage.button_ins()
    #less_damage.button_ins()

    screen.blit(st_magic, (30, 390))
    add_magic.button_ins()
    #less_magic.button_ins()

    screen.blit(st_speed, (30, 470))
    add_speed.button_ins()
    #less_speed.button_ins()

    screen.blit(get_back, (620, 545))

    screen.blit(confirm_b, (120, 545))

    if utilities.p_mouse(mouse, (622, 783), (550, 588)):
        get_back = utilities.r_text("BACK", ((255, 255, 255)),
                                    "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (580, 550))
    else:
        get_back = utilities.r_text("BACK", ((25, 25, 112)),
                                    "./Assets/Fonts/bitwise.ttf", 60)

    if utilities.p_mouse(mouse, (122, 376), (550, 588)):
        confirm_b = utilities.r_text("CONFIRM", ((255, 255, 255)),
                                     "./Assets/Fonts/bitwise.ttf", 60)
        screen.blit(pointer, (85, 550))
    else:
        confirm_b = utilities.r_text("CONFIRM", ((10, 100, 10)),
                                     "./Assets/Fonts/bitwise.ttf", 60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            skilling = not skilling
            run = not run
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if utilities.p_mouse(mouse, (122, 376), (550, 588)) and not skilled and confirm:
                if h_pointed != add_health.pointed:
                    h_pointed += add_health.pointed
                    skilled = True
                    confirm = False
                elif d_pointed != add_defense.pointed:
                    d_pointed += add_defense.pointed
                    skilled = True
                    confirm = False
                elif da_pointed != add_damage.pointed:
                    da_pointed += add_damage.pointed
                    skilled = True
                    confirm = False
                elif ma_pointed != add_magic.pointed:
                    ma_pointed += add_magic.pointed
                    skilled = True
                    confirm = False
                elif sp_pointed != add_speed.pointed:
                    sp_pointed += add_speed.pointed
                    skilled = True
                    confirm = False

                player.health += h_pointed
                player.defense += d_pointed
                player.atkdamage += da_pointed
                player.magic += ma_pointed
                player.speed += sp_pointed

                player.serialize()
            elif utilities.p_mouse(mouse, (622, 783), (550, 588)):
                if not skilled and confirm:
                    player.p_skills = max_points
                skilling = not skilling

            # Buttons Actions
            add_health.button_action()
            #if confirm:
            #    less_health.button_action()

            add_defense.button_action()
            #if confirm:
            #    less_defense.button_action()

            add_damage.button_action()
            #if confirm:
            #    less_damage.button_action()

            add_magic.button_action()
            #if confirm:
            #    less_magic.button_action()

            add_speed.button_action()
            #if confirm:
            #    less_speed.button_action()

    pygame.display.update()
