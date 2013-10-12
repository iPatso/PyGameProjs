import pygame, os
from pygame.locals import *
from Button import Button
from CONST import screen, WINDOW_SIZE

class Chart():
    def __init__(self, side, characterName=""): # TODO: characterName
        self.image = pygame.image.load(os.path.join("data", "defaultChart.jpg")).convert()
        self.side = side
        
        
    def update(self):
        if self.side == "light":
            screen.blit(self.image, (20,20))
        elif self.side == "dark":
            chartPos = self.image.get_rect(right=screen.get_width()-20, top = 20)
            screen.blit(self.image, chartPos)
        else:
            print "INVALID Player section"