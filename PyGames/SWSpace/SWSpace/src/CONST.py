import pygame, os
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (800,400)
LIGHT_GREY = (200,200,200)
DARK_GREY = (150,150,150)
DARK_ORANGE = (230,50,18) # originally: DARK_YELLOW = (247,200,20)

screen = pygame.display.set_mode(WINDOW_SIZE)

# returns 'text' in the font specified
def textFont(text, color, size, font):
    fonty = pygame.font.Font((os.path.join('data',font)),size)
    return fonty.render(text, 1, color)

# makes a grid; used in aligning
def showGrid(screen):
    pygame.draw.line(screen, (255,255,255), (screen.get_width()/2,0),(screen.get_width()/2,screen.get_height()))
    pygame.draw.line(screen, (255,255,255), (0, screen.get_height()/2),(screen.get_width(), screen.get_height()/2))

# loads an image with an alpha channel (transparency)
def loadimage_alpha(name):
    full_path = os.path.join("data", name)
    try:
        image = pygame.image.load(full_path)
    except pygame.error, message:
        print 'Cannot load image: ', full_path
        raise SystemExit, message
    image = image.convert_alpha()
    return image, image.get_rect()

# Flickers ship when dying and losing a life
# Used in GameTime: playGame
def flicker(flicker_time, flicker_count, playerSprite):
    if flicker_time%20 >= 0 and flicker_time%20 <= 9:
        playerSprite.update()
        playerSprite.draw(screen)
    else:
        flicker_count += 1
    flicker_time += 1
    print flicker_time, flicker_count
    return flicker_time, flicker_count   

# Scales width of the life bar
def scaleLifeBar(img, fraction):
    newsize = img.get_size()
    newsize = (int(newsize[0]*fraction), newsize[1])
    return pygame.transform.scale(img, newsize)