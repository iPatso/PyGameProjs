import pygame
from pygame.locals import *
from CONST import screen, MAPCOORDS
from Chart import Chart

class Team():
    def __init__(self, side, playerNum):
        self.primary = pygame.image.load("data/asajj.png").convert_alpha()
        self.secondary = []
        self.chart = Chart(side, playerNum)
        self.deck = 0
        self.primX = 0
        self.primY = 0
        self.buttonTimer = 0
        self.buttonMax = 40
        self.playerNum = playerNum
        
    def update(self):
        keys = pygame.key.get_pressed()
        self.buttonTimer += 1
        if self.buttonTimer >= self.buttonMax:
            if keys[K_DOWN] and self.primY < 6:
                self.primY += 1
            elif keys[K_UP] and self.primY > 0:
                self.primY -= 1
            elif keys[K_LEFT] and self.primX > 0:
                self.primX -= 1
            elif keys[K_RIGHT] and self.primX < 9:
                self.primX += 1
            
            self.buttonTimer = 0
                    
                    
        self.chart.update()
        primaryPos = self.primary.get_rect(centerx = MAPCOORDS[self.primY][self.primX][0],bottom = MAPCOORDS[self.primY][self.primX][1])
        screen.blit(self.primary,primaryPos)