import pygame

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
run = True
wait = [True, True, True]
pygame.display.set_caption("RPG Holberton Quest")
icon = pygame.image.load("./Images/Holberton.png")
pygame.display.set_icon(icon)
pygame.mouse.set_pos([400, 300])
data = {}

# Images loads
gender1 = pygame.image.load("./Images/Male.png")
gender1 = pygame.transform.scale(gender1, (150, 300))
gender2 = pygame.image.load("./Images/Female.png")
gender2 = pygame.transform.scale(gender2, (150, 300))
race1 = pygame.image.load("./Images/Human.png")
race1 = pygame.transform.scale(race1, (150, 250))
race2 = pygame.image.load("./Images/Dwarf.png")
race2 = pygame.transform.scale(race2, (150, 250))
race3 = pygame.image.load("./Images/Elf.png")
race3 = pygame.transform.scale(race3, (150, 250))
race4 = pygame.image.load("./Images/Orc.png")
race4 = pygame.transform.scale(race4, (150, 250))


# Position
gender1p = [150, 150]
gender2p = [450, 150]
race1p = [75, 30]
race2p = [600, 30]
race3p = [75, 320]
race4p = [600, 320]


def fgender():
    screen.blit(gender1, (gender1p[0], gender1p[1]))
    screen.blit(gender2, (gender2p[0], gender2p[1]))


def frace():
    screen.blit(race1, (race1p[0], race1p[1]))
    screen.blit(race2, (race2p[0], race2p[1]))
    screen.blit(race3, (race3p[0], race3p[1]))
    screen.blit(race4, (race4p[0], race4p[1]))


# Game loop
while run:
    pygame.display.update()
    screen.fill((50, 50, 50))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and wait[0]:
            if (75 < mouse[0] < 300) and (150 < mouse[1] < 450):
                data.update({"gender": "Male"})
                print(data)
                wait[0] = False
            elif (450 < mouse[0] < 630) and (150 < mouse[1] < 450):
                gender = "Female"
                data.update({"gender": "Female"})
                wait[0] = False
                print(data)
        elif event.type == pygame.MOUSEBUTTONDOWN and wait[1]:
            if (150 < mouse[0] < 225) and (30 < mouse[1] < 280):
                data.update({"race": "Human"})
                wait[1] = False
                print(data)
            elif (600 < mouse[0] < 750) and (30 < mouse[1] < 280):
                data.update({"race": "Dwarf"})
                wait[1] = False
                print(data)
            elif (150 < mouse[0] < 225) and (320 < mouse[1] < 570):
                data.update({"race": "Elf"})
                wait[1] = False
                print(data)
            elif (600 < mouse[0] < 750) and (320 < mouse[1] < 570):
                data.update({"race": "Orc"})
                wait[1] = False
                print(data)

    if wait[0]:
        fgender()
    if wait[0] is False and wait[1]:
        frace()

pygame.quit()
