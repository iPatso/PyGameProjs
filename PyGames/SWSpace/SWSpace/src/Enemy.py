import pygame, sys, os, random
from pygame.locals import *
from CONST import *

global enemyLaserSprites
enemyLaserSprites = pygame.sprite.RenderPlain(())

class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadimage_alpha("enemy.png")
        self.rect.center = (WINDOW_SIZE)        # Prevents enemies from spawning at (0,0)
        self.x, self.y = pos
        self.laser_timer = 0
        self.laser_max = 30
        self.moveX = -5
        self.moveY = random.randrange(-2,3,4)   # returns either a -2 or 2; 2nd parameter. is exclusive
        
    def update(self):
        # Position
        if self.x < 0 - self.rect.width:
            self.kill()
            
        if self.y < 60:
            self.moveY = +2
        elif self.y > WINDOW_SIZE[1]-self.image.get_height():
            self.moveY = -2
        
        self.x += self.moveX
        self.y += self.moveY
        
        self.rect.topleft = (self.x, self.y)
        
        # Randomly shoot laser
        randLaser = random.randrange(0,100)
        self.laser_timer += 1
        if randLaser > 90 and self.laser_timer >= self.laser_max:
            enemyLaserSprites.add(EnemyLaser(self.rect.midleft))
            self.laser_timer = 0
        
class EnemyLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadimage_alpha("Player_laser.png")
        self.rect.midright = pos
        self.bullet = self.rect         #TODO: make the bullet the tip/bullet of the laser
        
    def update(self):
        if self.rect.right < 0:
            self.kill()
        else:
            self.rect.move_ip(-15, 0)