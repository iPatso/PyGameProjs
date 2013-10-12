import pygame, random, os
from gameUtils import loadImage, loadSoundFile

# -------------------------------------------
#     Global constants and objects
# -------------------------------------------
FRAMERATE = 120

WIDTH = 1000
HEIGHT = 540
SCREEN_SIZE = (WIDTH, HEIGHT)

ENEMY_TICKS = [25,30,50,75,100,150]
ENEMY_X_POS = [WIDTH/5, WIDTH/6, WIDTH/7, 4*WIDTH/5, 5*WIDTH/6, 6*WIDTH/7]
ENEMY_Y_POS = [HEIGHT/2, 6*HEIGHT/7]

TEXT_COLOR = (10,10,10)

BG_MUSIC = os.path.join("data","bgmusic.mp3")

HERO = pygame.sprite.RenderClear()
FIREBALLS = pygame.sprite.RenderClear()
ENEMIES = pygame.sprite.RenderClear()
BLOCKS = pygame.sprite.RenderClear()


# -------------------------------------------
#         Mario-related constants
# -------------------------------------------
if FRAMERATE == 60:
	MARIO_X_ACC = 0.5
	MARIO_FRICTION = 0.92
	MARIO_JUMP_VEL = -10.75
	MARIO_GRAVITY = 0.4
else:
	MARIO_X_ACC = 0.25
	MARIO_FRICTION = 0.93
	MARIO_JUMP_VEL = -8
	MARIO_GRAVITY = 0.2
    
MARIO_MAX_FIREBALLS = 7


# -------------------------------------------
#       Fireball-related constants
# -------------------------------------------
if FRAMERATE == 60:
	FIREBALL_GRAV = 0.5
	RED_Y_VEL = -6.5
	RED_X_VELS = [(x / 4.0) for x in range (12,21)]
	BLUE_Y_VEL = RED_Y_VEL * 1.8
	BLUE_X_VELS = [(x * 0.65) for x in RED_X_VELS]
else:
	FIREBALL_GRAV = 0.25
	RED_Y_VEL = -5
	RED_X_VELS = [((x / 4.0) / 2) for x in range (12,21)]
	BLUE_Y_VEL = RED_Y_VEL * 1.6
	BLUE_X_VELS = [(x * 0.9) for x in RED_X_VELS]


# -------------------------------------------
#       Shell-related constants
# -------------------------------------------
if FRAMERATE == 60:
	SHELL_GRAVITY = 0.5
	SHELL_X_VEL = 3
	SHELL_Y_VEL = 2
else:
	SHELL_GRAVITY = 0.5
	SHELL_X_VEL = 1.5
	SHELL_Y_VEL = 2