import pygame
import os
from Models.Champion import Champion
from Models.Enemy import Enemy
from Scenes import utilities
from Models.Equipment import Equipment

os.environ['SDL_VIDEO_WINDOW_POS'] = "250, 50"

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Holberton Quest")
icon = pygame.image.load("./Assets/Images/Holberton.png")
pygame.display.set_icon(icon)

# Load Banners
b_play = utilities.n_render("./Assets/Images/banner.png", (250, 100))
t_play = utilities.n_render("./Assets/Images/play.png", (150, 50))

e_play = utilities.n_render("./Assets/Images/banner.png", (250, 100))
t_exit = utilities.n_render("./Assets/Images/exit.png", (150, 50))

l_play = utilities.n_render("./Assets/Images/banner.png", (250, 100))
t_load = utilities.n_render("./Assets/Images/load.png", (150, 50))

# Load PostGame
hippo = utilities.n_render("./Assets/Images/Holberton.png", (80, 130))
holb = utilities.n_render("./Assets/Images/holbie.png", (300, 100))
qust = utilities.n_render("./Assets/Images/quest.png", (200, 100))

run = True
loading = False

while run:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if utilities.p_mouse(mouse, (307, 502), (245, 300)) and not loading:  # play btn
                exec(open("./Scenes/selec.py").read())
                run = False
            elif utilities.p_mouse(mouse, (307, 502), (343, 400)) and not loading:  # load char
                loading = True
                exec(open("./Scenes/LoadPlayer.py").read())
            elif utilities.p_mouse(mouse, (307, 502), (445, 500)) and not loading:  # exit btn
                run = False

    if run and not loading:
        screen.fill((50, 50, 50))

        screen.blit(hippo, (200, 30))
        screen.blit(holb, (290, 10))
        screen.blit(qust, (330, 100))

        screen.blit(b_play, (280, 200))  # render play button
        screen.blit(t_play, (330, 245))  # text play

        screen.blit(e_play, (280, 300))  # render load button
        screen.blit(t_load, (330, 345))  # text load

        screen.blit(l_play, (280, 400))  # render exit button
        screen.blit(t_exit, (330, 445))  # text exit

        pygame.display.update()


pygame.quit()
