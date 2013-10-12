import pygame, sys, os, CONST
from pygame import *
from CONST import *

clock = pygame.time.Clock()
FPS = 60




GRAY = (150,150,150)

class GameTime():
    def __init__ (self):
        self.bg_image = pygame.image.load(os.path.join("data","game_time_background.jpg")).convert()
        self.fighter = pygame.image.load(os.path.join("data","xWingSide.png")).convert_alpha()

    def playGame(self,screen):
        """
        Most other functions in this class will be called in this one.
        """
        isPlaying = True
        shownLevel = False
        bgX = 0
        shipX, shipY = 0,0
        screen.blit(self.bg_image, (0,0))
        
        while (isPlaying):
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()

            # Show's user the level, only occurs once
            if not shownLevel:
                self.getReady(screen)
                shownLevel = True


            #Testing bg mvmt
            if bgX > -2200:
                bgX -= .5
            screen.blit(self.bg_image, (bgX,0))


            #SHIP movement
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                shipY -= 10
            if keys[K_DOWN]:
                shipY += 10

            if shipY < 0:
                shipY = 0
            if shipY > screen.get_height() - self.fighter.get_height():
                shipY = screen.get_height() - self.fighter.get_height()
            screen.blit(self.fighter, (shipX, shipY))

            
            pygame.display.update()


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
            
