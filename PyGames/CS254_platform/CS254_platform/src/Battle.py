from CONST import *

# NOTE: Not a class

def doSelection(selection):
    if selection == 0:
        print "ATTACKING!"
    elif selection == 1:
        print "NO ITEMS!"
    elif selection == 2:
        print "CANNOT RUN!"

def battle(player, enemy):
    lifeBarContainer = pygame.image.load(os.path.join("data", "lifeBarContainer.png")).convert_alpha()
    bg_image = pygame.image.load(os.path.join("data", "battlescene.png")).convert()
    isBattling = True
    selection = 0
    battle_text = "It is your turn"
    while(isBattling):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()
                #isBattling = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:           # Battle Menu Selections
                    selection -= 1
                    if selection == -1:
                        selection = 2
                elif event.key == K_DOWN:
                    selection +=1
                    if selection == 3:
                        selection = 0
                elif event.key == K_SPACE:
                    doSelection(selection)
                    if selection == 0:
                        battle_text = "Attacking!"
                        enemy.hp -= 10
                    elif selection == 1:
                        battle_text = "You have no items!"
                    elif selection == 2:
                        battle_text = "There is no escape!"
                
                
        
        #Sets up background
        screen.blit(bg_image, (0,0))
        
        
        
        #Sets up life bars
        fraction_player = player.hp/100.0
        fraction_enemy = enemy.hp/100.0
        if fraction_player < 0:
            fraction_player = 0
        if fraction_enemy < 0:
            fraction_enemy = 0
        lifeBar_player = pygame.image.load(os.path.join("data", "lifeBar.png")).convert_alpha()
        lifeBar_enemy = pygame.image.load(os.path.join("data", "lifeBar.png")).convert_alpha()
        
        screen.blit(lifeBarContainer, (5,5))
        screen.blit(lifeBarContainer, (screen.get_width()-lifeBarContainer.get_rect().width-6,5))
        
        lifeBar_player = scaleLifeBar(lifeBar_player, fraction_player)
        lifeBar_enemy = scaleLifeBar(lifeBar_enemy, fraction_enemy)
        
        screen.blit(lifeBar_player, (6,6))
        screen.blit(lifeBar_enemy, (screen.get_width()-lifeBarContainer.get_rect().width-5,6))
        
        
        # Blits characters on screen
        
        screen.blit(player.stand_R, (100,150))
        screen.blit(enemy.image, (750,170))
        
        # Sets up battle menu
        
        thickness = 5
        pygame.draw.rect(screen, LIGHT_GREY, (thickness/2, screen.get_height()-150, screen.get_width()-thickness, 150-thickness/2))
        pygame.draw.rect(screen, DARK_GREY, (thickness/2, screen.get_height()-150, screen.get_width()-thickness, 150-thickness/2), thickness)
        pygame.draw.line(screen, DARK_GREY, (screen.get_width()/2, screen.get_height()-150),(screen.get_width()/2,screen.get_height()),5)
        
        colors = [DARK_GREY,DARK_GREY,DARK_GREY]
        colors[selection] = DARK_ORANGE
        ATTACK = textFont("ATTACK", colors[0], 20, "Basica.ttf")
        ITEMS = textFont("ITEMS", colors[1], 20, "Basica.ttf")
        RUN = textFont("RUN", colors[2], 20, "Basica.ttf")
        BATTLE_TEXT = textFont(battle_text, DARK_GREY, 20, "Basica.ttf")

        ATTACK_pos = ATTACK.get_rect(left=screen.get_width()/6)
        ITEMS_pos = ITEMS.get_rect(left=screen.get_width()/6)
        RUN_pos = RUN.get_rect(left=screen.get_width()/6)
        BATTLE_TEXT_pos = BATTLE_TEXT.get_rect(left=screen.get_width()/2 + 110)

        screen.blit(ATTACK, (ATTACK_pos[0], screen.get_height()-103))
        screen.blit(ITEMS, (ITEMS_pos[0], screen.get_height()-83))
        screen.blit(RUN, (RUN_pos[0], screen.get_height()-63))
        screen.blit(BATTLE_TEXT, (BATTLE_TEXT_pos[0], screen.get_height()-85))
        
        
        
        
        
        
        
        
        pygame.display.update()
        

        
        