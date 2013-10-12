import pygame, os
from pygame.locals import *
from CONST import *

class Board():
    def __init__(self): #TODO map_name to be passed in in future. Perhaps one indicating where to place map (ie. center, left, etc)
        self.board = pygame.image.load(os.path.join("data", "defaultMap.png")).convert_alpha()
        
    def showBoard(self):
        boardPos = self.board.get_rect(centerx = screen.get_width()/2, bottom = screen.get_height()-150)
        screen.blit(self.board, boardPos)
