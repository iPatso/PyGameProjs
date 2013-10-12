import pygame, sys, os
from pygame.locals import *
from Player import Player
from Background import Background
from CONST import *


def main():
    
    pygame.init()
    clock = pygame.time.Clock()

    player = Player()
    bg = Background()
      
    while True:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit()      
              
        bg.update()
        player.update()
        pygame.display.flip()
    

  
if __name__ == '__main__':
    main()
