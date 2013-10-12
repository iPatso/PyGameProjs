import pygame, os
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (900,500)
LIGHT_GREY = (200,200,200)
DARK_GREY = (150,150,150)
DARK_ORANGE = (230,50,18) # originally: DARK_YELLOW = (247,200,20)

screen = pygame.display.set_mode(WINDOW_SIZE)

# returns array of images; used for walking, jumping animation
def arrayImg(image, width, height):
    sub = image.get_rect()
    subx = sub[2]/width
    suby = sub[3]/height
    dummy = (0,0)
    images = []
    while dummy[0] < suby:
        while dummy[1] < subx:
            newrect = (dummy[1]*width,
                       dummy[0]*height,
                       width, height)
            images.append(image.subsurface(newrect))
            dummy = (dummy[0], dummy[1]+1)
        dummy = (dummy[0]+1, 0)
    return images

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
