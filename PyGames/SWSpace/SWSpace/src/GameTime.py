import pygame, sys, os, CONST, random, main
from pygame.locals import *
from CONST import *
from Player import *
from Enemy import *
from FX import *

clock = pygame.time.Clock()
FPS = 60

GRAY = (150,150,150)

class GameTime():
    def __init__ (self):
        self.bg_image = pygame.image.load(os.path.join("data","game_time_background.jpg")).convert()

    def playAgainMenu(self, selection):
        #Try Again, Main Menu, Exit
        colors = [DARK_GREY,DARK_GREY,DARK_GREY]
        colors[selection] = DARK_ORANGE
        TRYAGAIN = textFont("Try Again", colors[0], 20, "Basica.ttf")
        MAINMENU = textFont("Main Menu", colors[1], 20, "Basica.ttf")
        EXIT = textFont("EXIT", colors[2], 20, "Basica.ttf")

        TRYAGAIN_pos = TRYAGAIN.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2-20)
        MAINMENU_pos = MAINMENU.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2)
        EXIT_pos = EXIT.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2+20)

        screen.blit(TRYAGAIN, (TRYAGAIN_pos[0], TRYAGAIN_pos[1]))
        screen.blit(MAINMENU, (MAINMENU_pos[0], MAINMENU_pos[1]))
        screen.blit(EXIT, (EXIT_pos[0], EXIT_pos[1]))    

    def getReady(self, screen):
        # ONLY prepared for level 1
        timer = 0
        while timer < 2000:
            level_text = textFont("LEVEL ONE", GRAY, 32, "Basica.ttf")
            # CENTER TEXT ON SCREEN SEEN BELOW!!!!!
            level_text_pos = level_text.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2 - 50)
            screen.blit(level_text, level_text_pos)
            pygame.display.update()
            timer += 1
        timer = 0
        screen.blit(self.bg_image, (0,0))
        while timer < 1000:
            GO_text = textFont("GO!", GRAY, 32, "Basica.ttf")
            GO_text_pos = GO_text.get_rect(centerx=screen.get_width()/2,centery=screen.get_height()/2 - 50)
            screen.blit(GO_text, GO_text_pos)
            pygame.display.update()
            timer += 1
        pygame.display.update()
        print "Done"
        


        