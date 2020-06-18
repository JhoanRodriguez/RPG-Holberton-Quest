active = False

p_name = "NAME"

while loading:
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

    pygame.draw.rect(screen, (255, 255, 255), (230, 200, 370, 250), 0)

    load_p = utilities.r_text("LOAD PLAYER", (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 45)
    
    # HOVER
    if utilities.p_mouse(pygame.mouse.get_pos(), (250, 368), (402, 433)):
        b_load_p = utilities.r_text("LOAD", (0, 0, 255), "./Assets/Fonts/bitwise.ttf", 45)
    else:
        b_load_p = utilities.r_text("LOAD", (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 45)
    if utilities.p_mouse(pygame.mouse.get_pos(), (418, 585), (400, 430)):
        b_cancel = utilities.r_text("CANCEL", (255, 0, 0), "./Assets/Fonts/bitwise.ttf", 45)
    else:
        b_cancel = utilities.r_text("CANCEL", (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 45)
    if not active:
        pygame.draw.rect(screen, (220, 20, 60), (280, 280, 250, 45), 0)
        input_box = pygame.draw.rect(screen, (125, 0, 0), (280, 280, 250, 45), 2)
    else:
        pygame.draw.rect(screen, (220, 20, 60), (280, 280, 250, 45), 0)
        input_box = pygame.draw.rect(screen, (155, 155, 155), (280, 280, 250, 45), 2)    

    player_name = utilities.r_text(p_name, (0, 0, 0), "./Assets/Fonts/bitwise.ttf", 32)

    screen.blit(load_p, (255, 210))
    screen.blit(player_name, (input_box.x + 7, input_box.y + 7))
    screen.blit(b_load_p, (250, 400))
    screen.blit(b_cancel, (415, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading = False
            run = False
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                p_name = p_name[:-1]
            elif event.key == pygame.K_RETURN:
                print(p_name)
            else:
                if len(p_name) < 10:
                    p_name += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(pygame.mouse.get_pos()):
                active = True
                if p_name == "NAME":
                    p_name = ""
            else:
                active = False
                if len(p_name) == 0 or p_name == " ":
                    p_name = "NAME"
            
            if utilities.p_mouse(pygame.mouse.get_pos(), (250, 368), (402, 433)) and len(p_name) > 0:
                if p_name != "NAME":
                    try:
                        dictionary = [Champion().load_save_json_file(p_name)]
                        player = Champion(p_name)
                        player.load_character(dictionary)
                        try:
                            import random
                            h_pointed = 0
                            d_pointed = 0
                            da_pointed = 0
                            ma_pointed = 0
                            sp_pointed = 0
                            player_die = False
                            monster_die = False
                            exec(open("Scenes/men_play.py").read())
                        except Exception as xpp:
                            print(xpp)
                        print(player)
                    except Exception as xpp:
                        print(xpp)
                    print("That player does not exist")
                    loading = False
                    run = False
            elif utilities.p_mouse(pygame.mouse.get_pos(), (418, 585), (400, 430)):
                loading = False

    pygame.display.update()