import pygame
from CONST import *



class Button():
    def __init__(self, pos, text, dimensions, color = (255, 100, 100)):
        self.color = color
        self.text = text
        self.pos = pos
        self.dimensions = dimensions
        
    def update(self):
        if self.isHoveredOver():
            self.color = (255,200,200)
        else:
            self.color = (255,100,100)
        
        pygame.draw.rect(screen,self.color,(self.pos, self.dimensions))
        showText(self.text, (self.pos[0]+self.dimensions[0]/2,self.pos[1]+self.dimensions[1]/2),15)
        
    def isHoveredOver(self):
        if (pygame.mouse.get_pos()[0] <= self.pos[0]+self.dimensions[0] and
            pygame.mouse.get_pos()[0] >= self.pos[0] and 
            pygame.mouse.get_pos()[1] <= self.pos[1]+self.dimensions[1] and 
            pygame.mouse.get_pos()[1] >= self.pos[1]):
            
            return True
        else:
            return False