if s_stat:
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.draw.rect(screen, (220, 0, 60), (150, 100, 500, 400), 0)

    p_stats = {"health": player.health,
                "damage": player.atkdamage,
                "magic": player.magic,
                "speed": player.speed,
                "weapon": player.weapon.name,
                "armor": player.armor,
                "defense": player.defense}

    back_ = utilities.r_text("BACK", (0, 0, 0),
                            "./Assets/Fonts/bitwise.ttf", 40)

    screen.blit(avatar, (153, 103))
    stat_ = utilities.r_text("STATS", (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    health_ = utilities.r_text("{} > {:.2f}".format("HEALTH", p_stats["health"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    weapon_ = utilities.r_text("{} > {}".format("WEAPON", p_stats["weapon"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    damage_ = utilities.r_text("{} > {:.2f}".format("DAMAGE", p_stats["damage"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    magic_ = utilities.r_text("{} > {:.2f}".format("MAGIC", p_stats["magic"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    speed_ = utilities.r_text("{} > {:.2f}".format("SPEED", p_stats["speed"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    armor_ = utilities.r_text("{} > {:.2f}".format("ARMOR", p_stats["armor"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)
    
    defense_ = utilities.r_text("{} > {:.2f}".format("DEFENSE", p_stats["defense"]), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    w_dmg = utilities.r_text("{} > {:.2f}".format("DAMAGE", player.weapon.damage), (255, 255, 255),
                            "./Assets/Fonts/bitwise.ttf", 30)

    screen.blit(back_, (530, 460))
    screen.blit(stat_, (380, 110))
    screen.blit(health_, (300, 160))
    screen.blit(speed_, (300, 190))
    screen.blit(damage_, (300, 220))
    screen.blit(magic_, (300, 250))
    screen.blit(defense_, (300, 280))
    screen.blit(armor_, ((300, 310)))
    screen.blit(weapon_, (300, 340))
    screen.blit(w_dmg, (315, 368))
