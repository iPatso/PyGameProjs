import pygame
from pygame.locals import *
from CONST import *

class EXPLOSION(pygame.sprite.Sprite):
    def __init__(self,pos,size,color=(255,255,255)):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.pos = pos
        self.rad = 0
        self.rect = pygame.rect.Rect((pos[0]-size,400),(size*2,2))
        self.color = color
        
    def update(self,):
        pygame.draw.circle(screen,self.color,self.pos,self.size)
        pygame.draw.circle(screen,(200,0,0),self.pos,self.rad)
        self.rect = pygame.rect.Rect((self.pos[0]-self.size,400),
                                     (self.size*2,2))
        if(self.rad <= self.size):
            self.rad += 15
            self.size+= 10
        else:
            self.kill()