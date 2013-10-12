import pygame, sys, os
import CONST, SWSmenu, GameTime
from pygame.locals import *

from CONST import *
from SWSmenu import *
from GameTime import *


""" IDEAS:
        -make bools such as isInMenu, startedGame/isInAction [no need. yet maybe]
"""



pygame.init()

clock = pygame.time.Clock()

enemyExplosion = pygame.mixer.Sound(os.path.join("data", "enemyExplosion.wav"))

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()
    
        print "Welcome to the Main Menu"
        menu = Menu()
        isInOptions = False
        isInMenu = True
# MENU ############################ MENU ######################## MENU ################################ MENU ################
        while isInMenu:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and not isInOptions:
                    if event.key == K_UP:                       #Menu Selections
                        menu.selection -= 1
                        if menu.selection == -1:
                            menu.selection = 2
                    elif event.key == K_DOWN:
                        menu.selection +=1
                        if menu.selection == 3:
                            menu.selection = 0
                    elif event.key == K_SPACE:                  #Menu >> SPACE(bar) conditions
                        if menu.selection == 0:                     #START - INCOMPLETE!!
                            print "STARTing game.."
                            isInMenu = False
                        elif menu.selection == 1:                   #OPTIONS
                            isInOptions = True
                        else:
                            pygame.quit()
                            sys.exit()
                elif event.type == KEYDOWN and isInOptions:
                    if event.key == K_UP:                       #OPTIONS Selections
                        menu.optionsSelections -= 1
                        if menu.optionsSelections == -1:
                            menu.optionsSelections = 2
                    elif event.key == K_DOWN:
                        menu.optionsSelections +=1
                        if menu.optionsSelections == 3:
                            menu.optionsSelections = 0
                    elif event.key == K_SPACE:                  #Options >> SPACE(bar) conditions
                        if menu.optionsSelections == 0:             #Music toggle
                            print "Music toggled.."
                        elif menu.optionsSelections == 1:           #Sound fx toggle
                            print "Sound FX toggled.."
                        else:
                            isInOptions = False
                            menu.optionsSelections = 0
                            
            
            screen.blit(menu.bg_image, (0,0))                   #Background
            menu.mainLogoAnimation(screen)                      #STARWARS
            menu.subLogoAnimation(screen)                       #SPACE BATTLES
            menu.showSelections(screen, menu.selection)         #Selections
            if isInOptions:
                menu.showOptions(screen, menu.optionsSelections)


            #showGrid(screen)                                    #shows grid for alignment
            pygame.display.update()
        
        
# GAMETIME ############################ GAMETIME ######################## GAMETIME ############################ GAMETIME #############
        
        print "GAME HAS STARTED!!"
        gametime = GameTime()
        isPlaying = True        # Only used when player dies and wants to play again
        while isPlaying:
            """
            Most other functions in this class will be called in this one.
            """
            isInLevel = True    # Loops thru game/updates/draws/etc during gameplay
            shownLevel = False
            bgX = 0
            screen.blit(gametime.bg_image, (0,0))
    
            player = Player()
            playerSprite = pygame.sprite.RenderPlain((player))
            
            
            enemySprites = pygame.sprite.RenderPlain(())
    
            boom = pygame.sprite.RenderPlain(())                # Holds list of collisions that cause explosions
    
            ftimer, fcount = 0, 0
            inDeathPrompt = False
            selection = 0
    
            while (isInLevel):
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                        pygame.quit()
                        sys.exit()
                    # IN DEATH PROMPT
                    if inDeathPrompt:
                        if event.type == KEYDOWN:
                            if event.key == K_UP:                       #Menu Selections
                                selection -= 1
                                if selection == -1:
                                    selection = 2
                            elif event.key == K_DOWN:
                                selection +=1
                                if selection == 3:
                                    selection = 0
                            elif event.key == K_SPACE:                  #Menu >> SPACE(bar) conditions
                                if selection == 0:                     #Try again - INCOMPLETE!!
                                    print "STARTing game.."
                                    isInLevel = False
                                elif selection == 1:                   #Main menu - INCOMPLETE!!
                                    print "Back to main menu.."
                                    isPlaying = False
                                    isInLevel = False
                                else:
                                    pygame.quit()
                                    sys.exit()
    
                # Show's user the level, only occurs once
                if not shownLevel:
                    gametime.getReady(screen)
                    shownLevel = True
    
                #Testing bg mvmt
                if bgX > -(gametime.bg_image.get_width()-WINDOW_SIZE[0]):
                    bgX -= .5
                screen.blit(gametime.bg_image, (bgX,0))
                
                # Show Life Bar and Lives
                player.showLifeBar()
                player.showLives()
    
                    
                # Randomly spawns enemies
                randomtime = random.randrange(0,1000)
                if randomtime >= 990:
                    enemySprites.add(Enemy((800,random.randrange(0,WINDOW_SIZE[1]))))
                
                
                # Collision of bullet and enemies
                for laser in laserSprites:
                    for enemy in enemySprites:                  # player's laser hits enemy
                        if laser.bullet.colliderect(enemy):
                            enemyExplosion.play()
                            enemy.kill()
                            laser.kill()
                            boom.add(EXPLOSION(enemy.rect.center, 5))
                    for eLaser in enemyLaserSprites:            # laser hits laser
                        if eLaser.bullet.colliderect(laser):
                            laser.kill()
                            eLaser.kill()
                            boom.add(EXPLOSION(eLaser.rect.midleft, 3))
                            
                if not player.isDead():                             # When player is dead with no more lives, then detects no collision
                    for eLaser in enemyLaserSprites:                # enemy laser hits player
                        if eLaser.bullet.colliderect(player):
                            eLaser.kill()
                            player.loseHP(10)
                            boom.add(EXPLOSION(eLaser.rect.midleft, 5))
                            print "YOU WERE SHOT!"
                    for enemy in enemySprites:                      # enemy collides with player
                        if player.rect.colliderect(enemy):
                            enemyExplosion.play()
                            enemy.kill()
                            player.loseHP(15)
                            boom.add(EXPLOSION(enemy.rect.center, 10))
                            print "YOU'RE HIT"
    
    
                
    
                if inDeathPrompt:
                    gametime.playAgainMenu(selection)
    
                # Updates and draws
                if player.isDead() and not inDeathPrompt:
                    if player.hasLives():
                        ftimer, fcount = flicker(ftimer, fcount, playerSprite)
                        if fcount == 50:
                            ftimer = 0
                            fcount = 0
                            player.revive()
                            print "LIVES: ", player.lives
                    else:
                        player.kill()
                        print "No more lives"
                        inDeathPrompt = True
                elif not player.isDead():
                    playerSprite.update()
                    laserSprites.update()
                    playerSprite.draw(screen)
                    laserSprites.draw(screen)
                    
                enemySprites.update()
                enemyLaserSprites.update()
                boom.update()
    
                enemySprites.draw(screen)
                enemyLaserSprites.draw(screen)
                
                pygame.display.update()
        
        
        
        
        
        pygame.display.update()
            
if __name__ == '__main__':
    main()