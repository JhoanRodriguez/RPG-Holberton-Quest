import pygame

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
run = True
wait = [True, True, True]
pygame.display.set_caption("RPG Holberton Quest")
icon = pygame.image.load("../Images/Holberton.png")
pygame.display.set_icon(icon)
pygame.mouse.set_pos([400, 300])
data = {}

# Position
gender1x = 150
gender1y = 150
gender2x = 450
gender2y = 150

# Images loads
gender1 = pygame.image.load("../Images/Male.png")
gender1 = pygame.transform.scale(gender1, (150, 300))
gender2 = pygame.image.load("../Images/Female.png")
gender2 = pygame.transform.scale(gender2, (180, 280))


def fgender():
    screen.blit(gender1, (gender1x, gender1y))
    screen.blit(gender2, (gender2x, gender2y))


def frace():
    screen.blit(gender1, (gender1x, gender1y))
    screen.blit(gender2, (gender2x, gender2y))


# Game loop
while run:
    pygame.display.update()
    screen.fill((50, 50, 50))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and wait[0]:
            if (150 < mouse[0] < 300) and (150 < mouse[1] < 450):
                data.update({"gender": "Male"})
                print(data)
                wait[0] = False
            elif (450 < mouse[0] < 630) and (150 < mouse[1] < 430):
                gender = "Female"
                data.update({"gender": "Female"})
                wait[0] = False
                print(data)
    if wait[0]:
        fgender()
    if wait[0] is False and wait[1]:
        frace()

pygame.quit()
