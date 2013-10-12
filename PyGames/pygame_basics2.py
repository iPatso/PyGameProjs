
#
# scriptedfun.com
#
# Screencast #2
# Arinoid - Using Sprite Sheets and Drawing the Background
#

import os, pygame, sys
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(os.path.join(filename)).convert()
    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs

class Arena:
    tileside = 25
    numxtiles = 12
    numytiles = 14
    topx = (SCREENRECT.width - SCREENRECT.width/tileside*tileside)/2
    topy = (SCREENRECT.height - SCREENRECT.height/tileside*tileside)/2
    rect = Rect(topx + tileside, topy + tileside, tileside*numxtiles, tileside*numytiles)
    def __init__(self):
        self.background = pygame.Surface(SCREENRECT.size).convert()
    def drawtile(self, tile, x, y):
        self.background.blit(tile, (self.topx + self.tileside*x,    \
                                    self.topy + self.tileside*y))
    def makebg(self, tilenum):
        for x in range(self.numxtiles):
            for y in range(self.numytiles):
                self.drawtile(self.tiles[tilenum], x + 1, y + 1)

def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREENRECT.size)

    spritesheet = Spritesheet('ball.png')

    Arena.tiles = spritesheet.imgsat([(0, 0, 25, 25),
                                      (25, 0, 25, 25),
                                      (0, 25, 25, 25),  
                                      (25, 25, 25, 25)])

    # make background
    arena = Arena()
    arena.makebg(1) # you may change the background color here
    screen.blit(arena.background, (0, 0))
    pygame.display.update()

    # keep track of sprites
    all = pygame.sprite.RenderUpdates()

    # keep track of time
    clock = pygame.time.Clock()

    # game loop
    while 1:

        # get input
        for event in pygame.event.get():
            if event.type == QUIT   \
               or (event.type == KEYDOWN and    \
                   event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # clear sprites
        all.clear(screen, arena.background)

        # update sprites
        all.update()

        # redraw sprites
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # maintain frame rate
        clock.tick(30)

if __name__ == '__main__': main()
