import pygame, os
from pygame.locals import *

# ----------------------------------------------------

def loadImage(name, colorkey=None):

    fullname = os.path.join("data", name)
    
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print "Cannot load image:", name
        raise SystemExit, message
        
    image = image.convert()
    
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
        
    return image, image.get_rect()
    
# ----------------------------------------------------
    
def loadSoundFile( name ):

    class NoneSound:
        def play( self ): pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join( "data", name )

    try:
        sound = pygame.mixer.Sound( fullname )
    except pygame.error, message:
        print "Cannot load sound:", fullname
        raise SystemExit, message

    return sound
	
# ----------------------------------------------------

def collide_edges( a, c ):

	l, r, t, b = False, False, False, False

	Rect = pygame.Rect
	left = Rect(a.left, a.top+1, 1, a.height-2)
	right = Rect(a.right, a.top+1, 1, a.height-2)
	top = Rect(a.left + 1, a.top, a.width-2, 1)
	bottom = Rect(a.left + 1, a.bottom, a.width-2, 1)
	
	if left.colliderect(c):
		l = True
	if right.colliderect(c):
		r = True
	if top.colliderect(c):
		t = True
	if bottom.colliderect(c):
		b = True

	return (t,r,b,l)
	