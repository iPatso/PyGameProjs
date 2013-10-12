import random, os, time, pygame, time, sys
from pygame.locals import *
from gameUtils import loadSoundFile, loadImage
from gameSprites import Mario, Fireball, Shell, PowBlock
from config import *
import psyco

psyco.full()
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode( (30*32, 30*32) )
background = pygame.Surface((30*32,30*32))
screen.blit(background, (0,0))

levelIMG = pygame.image.load("data\\test.bmp").convert_alpha()

for x in range(levelIMG.get_width()):
	for y in range(levelIMG.get_height()):
		color = levelIMG.get_at((x, y))
		if color == (0, 0, 0, 255):
			BLOCKS.add( PowBlock(( x * 32, y * 32)) )
			
			
			
while True:

	clock.tick(60)

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			break		
			
	BLOCKS.update()
	BLOCKS.clear( screen, background )
	BLOCKS.draw(screen)
	
	pygame.display.flip()
