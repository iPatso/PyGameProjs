import pygame, sys, os
from pygame.locals import *
#init
pygame.init()
height = 200;
width = 200;
 
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Gravity port")
 
#variables
plx = 90;
ply = 0;
speed = 0;
gravity = 0.1;
 
 
player = pygame.image.load(os.path.join('data', 'character_sR.png'))
player.convert()
clock = pygame.time.Clock()
 
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
        if plx < 0:
                plx = 0
        screen.fill((4, 6, 3))
        screen.blit(player, (plx, ply))
        ply = ply + speed;
        speed = speed + gravity;
        if (ply > height):
                speed = speed * -0.95;
        pygame.display.flip()
        clock.tick(50)
pygame.quit()
