import pygame, sys, os
import CONST, SWSmenu, GameTime
from pygame.locals import *

from CONST import *
from SWSmenu import *
from GameTime import *


""" IDEAS:
        -make bools such as isInMenu, startedGame/isInAction

"""



pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()

    print "Welcome to the Main Menu"
    menu = Menu()
    menu.titleMenu(screen)

    print "GAME HAS STARTED!!"
    gametime = GameTime()
    gametime.playGame(screen)
    pygame.display.update()
            
