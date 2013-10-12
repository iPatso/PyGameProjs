import pygame, os, sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (900,500)
BLACK = (0,0,0)
LIGHT_GREY = (200,200,200)
DARK_GREY = (100,100,100)
DARK_ORANGE = (230,50,18) # originally: DARK_YELLOW = (247,200,20)

screen = pygame.display.set_mode(WINDOW_SIZE)

PLAYERS = pygame.sprite.RenderClear()
PLATFORMS = pygame.sprite.RenderClear()
ENEMIES = pygame.sprite.RenderClear()

# Checks collision of a completely solid platform
# a -> rect of Player; c -> rect of platform/wall/SOLID
def collide_edges( a, c ):

    l, r, t, b = False, False, False, False

    left = pygame.Rect(a.left, a.top+1, 1, a.height-2)
    right = pygame.Rect(a.right, a.top+1, 1, a.height-2)
    top = pygame.Rect(a.left + 1, a.top, a.width-2, 1)
    bottom = pygame.Rect(a.left + 1, a.bottom, a.width-2, 1)
    
    if left.colliderect(c):
        l = True
    if right.colliderect(c):
        r = True
    if top.colliderect(c):
        t = True
    if bottom.colliderect(c):
        b = True

    return (t,r,b,l)

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

# Scales width of the life bar
def scaleLifeBar(img, fraction):
    newsize = img.get_size()
    newsize = (int(newsize[0]*fraction), newsize[1])
    return pygame.transform.scale(img, newsize)