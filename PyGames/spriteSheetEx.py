
<!-- saved from url=(0070)http://www.scriptedfun.com/wp-content/uploads/2006/06/screencast02.txt -->
<html><object type="{0C55C096-0F1D-4F28-AAA2-85EF591126E7}" cotype="cs" id="cosymantecbfw" style="width: 0px; height: 0px; display: block;"></object><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">#
# scriptedfun.com
#
# Screencast #2
# Arinoid - Using Sprite Sheets and Drawing the Background
#

import os, pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(os.path.join('data', filename)).convert()
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
    tileside = 31
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

    spritesheet = Spritesheet('arinoid_master.bmp')

    Arena.tiles = spritesheet.imgsat([(129, 321, 31, 31),   # purple - 0
                                      (161, 321, 31, 31),   # dark blue - 1
                                      (129, 353, 31, 31),   # red - 2
                                      (161, 353, 31, 31),   # green - 3
                                      (129, 385, 31, 31)])  # blue - 4

    # make background
    arena = Arena()
    arena.makebg(0) # you may change the background color here
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
                return

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
</pre></body><style type="text/css"></style></html>