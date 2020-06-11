import pygame

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
run = True
pygame.display.set_caption("RPG Holberton Quest")
icon = pygame.image.load("../Images/Holberton.png")
pygame.display.set_icon(icon)

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


def gender():
    screen.blit(gender1, (gender1x, gender1y))
    screen.blit(gender2, (gender2x, gender2y))


# Game loop
while run:
    pygame.display.update()
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    gender()
pygame.quit()
