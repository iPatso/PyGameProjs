from CONST import *
from Player import Player
from Background import Background
from Platform import Platform
from Enemy import Enemy
from menu import Menu


def main():
    
    pygame.init()
    clock = pygame.time.Clock()

    player = Player()
    bg = Background()
    
    menu = Menu()    
    isInMenu = True
    
    PLAYERS.add( player )
    PLATFORMS.add( Platform((200, 450), "higherplatform", False) )
    PLATFORMS.add( Platform((400, 250), "platform", True) )
    PLATFORMS.add( Platform((800, 200), "platform") )
    PLATFORMS.add( Platform((1200, 470), "ground") )
    PLATFORMS.add( Platform((200, 470), "ground"))
    PLATFORMS.add( Platform((3600, 470), "ground"))
    ENEMIES.add( Enemy((850, 120), "angryboo" ))
      
      
    while True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()     

# MENU ############################ MENU ######################## MENU ################################

        isInOptions = False
        while isInMenu:
            
            print "Welcome to the Main Menu"
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and not isInOptions:
                    if event.key == K_UP:                           #Menu Selections
                        menu.selection -= 1
                        if menu.selection == -1:
                            menu.selection = 2
                    elif event.key == K_DOWN:
                        menu.selection +=1
                        if menu.selection == 3:
                            menu.selection = 0
                    elif event.key == K_SPACE:                      #Menu >> SPACE(bar) conditions
                        if menu.selection == 0:                     #START - INCOMPLETE!!
                            print "STARTing game.."
                            isInMenu = False
                        elif menu.selection == 1:                   #OPTIONS
                            isInOptions = True
                        else:
                            pygame.quit()
                            sys.exit()
                elif event.type == KEYDOWN and isInOptions:
                    if event.key == K_UP:                           #OPTIONS Selections
                        menu.optionsSelections -= 1
                        if menu.optionsSelections == -1:
                            menu.optionsSelections = 2
                    elif event.key == K_DOWN:
                        menu.optionsSelections +=1
                        if menu.optionsSelections == 3:
                            menu.optionsSelections = 0
                    elif event.key == K_SPACE:                      #Options >> SPACE(bar) conditions
                        if menu.optionsSelections == 0:             #Music toggle
                            print "Music toggled.."
                        elif menu.optionsSelections == 1:           #Sound fx toggle
                            print "Sound FX toggled.."
                        else:
                            isInOptions = False
                            menu.optionsSelections = 0
                            
            
            screen.blit(menu.bg_image, (0,0))                   #Background
            menu.subLogoAnimation(screen)
            menu.showSelections(screen, menu.selection)         #Selections
            if isInOptions:
                menu.showOptions(screen, menu.optionsSelections)


            pygame.display.update()
        
 # END MENU ############################ END MENU ######################## END MENU ################################             
              
              
              
        # Player check in bounds       
        if player.rect.left < 0:
            player.rect.left = 0
        elif player.rect.right > 900:
            player.rect.right = 900
              
              
              
              
              
              
              
        bg.update()
        PLATFORMS.update()
        ENEMIES.update()
        PLAYERS.update()
        
        PLAYERS.draw(screen)
        ENEMIES.draw(screen)
        PLATFORMS.draw(screen)
        
        
        pygame.display.flip()
        
    

  
if __name__ == '__main__':
    main()
