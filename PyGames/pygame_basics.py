import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,400))

img = pygame.image.load("ball.png").convert_alpha()
print "Original: ", img.get_rect()
img = pygame.transform.scale(img, (50, 100))
print "After Scale: ", img.get_rect()



while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_y):
            pygame.quit()
            sys.exit()



    pygame.display.update()
