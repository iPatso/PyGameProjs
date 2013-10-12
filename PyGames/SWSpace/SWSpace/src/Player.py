import pygame, sys, os
from pygame.locals import *
from CONST import *

global laserSprites
laserSprites = pygame.sprite.RenderPlain(())

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadimage_alpha("xWingSide.png")
        self.rect.midleft = (0,200)
        self.x, self.y = self.rect.topleft
        self.laser_timer = 0
        self.laser_max = 10
        self.laser_sound = pygame.mixer.Sound(os.path.join("data","enemyExplosion.wav"))
        
        self.hp = 100
        self.lives = 3
        self.lifeBarContainer = pygame.image.load(os.path.join("data", "lifeBarContainer.png")).convert_alpha()
        self.lifeSymbol = pygame.image.load(os.path.join("data", "LifeSymbol.png")).convert_alpha()

    def showLives(self):
        for life in range(self.lives):
            screen.blit(self.lifeSymbol, (50*life, 40))
        
    def showLifeBar(self):
        fraction = self.hp/100.0
        if fraction < 0:
            fraction = 0
        lifeBar = pygame.image.load(os.path.join("data", "lifeBar.png")).convert_alpha()
        screen.blit(self.lifeBarContainer, (5,5))
        lifeBar = scaleLifeBar(lifeBar, fraction)
        screen.blit(lifeBar, (6,6))

    def update(self):
        self.rect.topleft = (self.x, self.y)
        
        #Checks if player just died
        if self.hp >= -10 and self.hp <= 0:
            self.lives -= 1
            self.hp = -100
        
        #SHIP movement
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.y -= 10
        if keys[K_s]:
            self.y += 10
        if keys[K_a]:
            self.x += -10
        if keys[K_d]:
            self.x += 10
        
        if self.y < 60:
            self.y = 60
        if self.y > screen.get_height() - self.rect.height:
            self.y = screen.get_height() - self.rect.height
        if self.x < 0:
            self.x = 0
        if self.x > screen.get_width() - self.rect.width:
            self.x = screen.get_width() - self.rect.width
                
        # Fire laser
        key = pygame.key.get_pressed()
        self.laser_timer += 1
        if key[K_RIGHT]:
            if self.laser_timer >= self.laser_max:
                self.laser_sound.play()
                laserSprites.add(Laser(self.rect.midright))
                self.laser_timer = 0
                
    def reset(self):
        self.rect.left = 0
        
    def loseHP(self, damage):
        self.hp -= damage
        print "HP: ", self.hp

    def isDead(self):
        if self.hp <= 0:
            return True
        return False
    
    def revive(self):
        self.hp = 100
    
    def removeLife(self):
        self.lives -=1
        print "Lives: ",self.lives
        
    def hasLives(self):
        if self.lives > 0:
            return True
        return False


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = loadimage_alpha("Player_laser.png")
        self.rect.midleft = pos
        self.bullet = self.rect         #TODO: make the bullet the tip/bullet of the laser
        
    def update(self):
        if self.rect.right > 800:
            self.kill()
        else:
            self.rect.move_ip(15, 0)