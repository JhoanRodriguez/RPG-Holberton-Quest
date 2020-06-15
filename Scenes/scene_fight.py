import random

#monster = Enemy("Enemy")

#while(player.health > 0 and monster.health > 0):
#    utilities.fight(player, monster, "atkdamage")

back_fight = "Assets/BFights/bb{}.png".format(random.randint(0, 6))

back = utilities.n_render(back_fight, (800, 600))

run = True

while run:
    screen.blit(back, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False