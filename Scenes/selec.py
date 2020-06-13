import pygame
import os
import utilities

run = True
sub_scenes = [True, False, False]
data = {}

# Images loads
gender1 = utilities.n_render("../Assets/Images/Male.png", (200, 400))
gender2 = utilities.n_render("../Assets/Images/Female.png", (160, 350))

race1 = utilities.n_render("../Assets/Images/Human.png", (200, 250))
race2 = utilities.n_render("../Assets/Images/Dwarf.png", (150, 250))
race3 = utilities.n_render("../Assets/Images/Elf.png", (200, 250))
race4 = utilities.n_render("../Assets/Images/Orc.png", (150, 250))

frame_s = utilities.n_render("../Assets/Images/frame.png", (200, 395))
frame_r = utilities.n_render("../Assets/Images/frame.png", (150, 200))

# Text
gender = utilities.r_text("GENDER", (220, 20, 60),
                          "../Assets/Fonts/bitwise.ttf", 72)

race = utilities.r_text("RACE", (220, 20, 60),
                          "../Assets/Fonts/bitwise.ttf", 72)

font = pygame.font.Font(None, 32)
input_box = pygame.Rect(320, 550, 160, 32)
color_inactive = (165, 42, 42)
color_active = (220, 20, 60)
color = color_inactive
text = 'Name'
active = False

# Game loop
while run:
    mouse = pygame.mouse.get_pos()

    # Anim Selector
    if sub_scenes[0]:
        if utilities.p_mouse(mouse, (174, 270), (160, 455)):
            screen.blit(frame_s, (125, 102))
        elif utilities.p_mouse(mouse, (525, 611), (180, 450)):
            screen.blit(frame_s, (480, 102))

    if sub_scenes[1]:
        if utilities.p_mouse(mouse, (137, 213), (53, 270)):
            screen.blit(frame_r, (100, 30))
        elif utilities.p_mouse(mouse, (617, 735), (88, 265)):
            screen.blit(frame_r, (600, 30))
        elif utilities.p_mouse(mouse, (126, 217), (345, 563)):
            screen.blit(frame_r, (85, 300))
        elif utilities.p_mouse(mouse, (607, 697), (327, 562)):
            screen.blit(frame_r, (580, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and sub_scenes[0]:
            if active:
                if event.key == pygame.K_RETURN:
                    data.update({"name": text})
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if len(text) < 10:
                        text += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if sub_scenes[0]:
                if (utilities.p_mouse(mouse, (174, 270), (160, 455)) and
                        (text != 'Name')):

                    data.update({"gender": "Male"})
                    data.update({"name": text})
                    sub_scenes[0] = False
                    sub_scenes[1] = True
                elif (utilities.p_mouse(mouse, (525, 611), (180, 450)) and
                      (text != 'Name')):

                    data.update({"gender": "Female"})
                    data.update({"name": text})
                    sub_scenes[0] = False
                    sub_scenes[1] = True
                elif input_box.collidepoint(event.pos):
                    active = not active
                    if text == 'Name':
                        text = ''
                else:
                    active = False
                    if text == '':
                        text = 'Name'
                color = color_active if active else color_inactive
            elif sub_scenes[1]:
                if utilities.p_mouse(mouse, (137, 213), (53, 270)):
                    data.update({"race": "Human"})
                    sub_scenes[1] = False
                elif utilities.p_mouse(mouse, (617, 735), (88, 265)):
                    data.update({"race": "Dwarf"})
                    sub_scenes[1] = False
                elif utilities.p_mouse(mouse, (126, 217), (345, 563)):
                    data.update({"race": "Elf"})
                    sub_scenes[1] = False
                elif utilities.p_mouse(mouse, (607, 697), (327, 562)):
                    data.update({"race": "Orc"})
                    sub_scenes[1] = False
                print(data)

    if sub_scenes[0]:
        txt_surface = font.render(text, True, (color))
        screen.blit(gender1, (125, 100))
        screen.blit(gender2, (500, 125))
        screen.blit(gender, (260, 25))
        screen.blit(txt_surface, (input_box.x + 10, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
    elif sub_scenes[1]:
        screen.blit(race1, (75, 30))
        screen.blit(race2, (600, 30))
        screen.blit(race3, (75, 320))
        screen.blit(race4, (600, 320))
        screen.blit(race, (310, 250))

    pygame.display.update()
    screen.fill((50, 50, 50))

pygame.quit()
