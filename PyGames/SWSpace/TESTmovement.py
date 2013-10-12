import pygame, sys, os, CONST
from pygame import *


shipX, shipY = 0,0
MOVEshipX, MOVEshipY = 0,0
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
fighter = pygame.image.load(os.path.join("data","xWingSide.png")).convert_alpha()

bg  = pygame.image.load("data\\title_background(600x400).jpg").convert()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        shipY -= 10
    if keys[K_DOWN]:
        shipY += 10
        
        

    screen.blit(bg, (0,0))

    #SHIP movement
    shipX += MOVEshipX #not implemented yet
    shipY += MOVEshipY
    if shipY < 0:
        shipY = 0
    if shipY > screen.get_height() - fighter.get_height():
        shipY = screen.get_height() - fighter.get_height()
    screen.blit(fighter, (shipX, shipY))
    
    pygame.display.update()
