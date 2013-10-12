import pygame, random
from gameUtils import loadImage, loadSoundFile, collide_edges
from config import *

# ----------------------------------------------------

class Mario(pygame.sprite.Sprite):

    def __init__(self, screen):
    
        pygame.sprite.Sprite.__init__(self)
        
        image, rect = loadImage('mario.png', -1)
        imagerun, rect = loadImage('mario_run.png', -1)
        self.stand = pygame.transform.scale2x(image).convert()
        self.run = pygame.transform.scale2x(imagerun).convert()
        self.standL = pygame.transform.flip(self.stand, 1, 0).convert()
        self.runL = pygame.transform.flip(self.run, 1, 0).convert()
        self.image = self.stand
        self.rect = self.image.get_rect()
        self.area = screen.get_rect()
        self.rect.topleft = (250, 200)
        self.x_vel, self.y_vel = 0, 0
        self.jumping = False
        self.midair = True
        self.walkingRight = True
        self.running = False
        self.fireball_lock = False
        self.jump_count = 0
        self.score = 0
        self.isDead = False
        self.animTick = 0
        
        self.jumpFX = loadSoundFile("jump.wav")
        self.hitFX = loadSoundFile("hit.wav")

    def update(self):

        # get all keys currently being pressed
        keys = pygame.key.get_pressed()
        
        self.running = False
        
        # increase/decrease x_vel if left/right keys are being pressed
        # then reduce x_vel according to friction
        if keys[pygame.K_RIGHT]:
            self.x_vel += MARIO_X_ACC
            self.walkingRight = True
            self.running = True
        if keys[pygame.K_LEFT]:
            self.x_vel -= MARIO_X_ACC
            self.running = True
            self.walkingRight = False
        self.x_vel *= MARIO_FRICTION
        
        if self.midair:
            self.animTick = 0
            oldrect = self.rect
            self.image = self.run
            self.rect = self.image.get_rect()
            self.rect.midbottom = oldrect.midbottom
            if not self.walkingRight:
                self.image = self.runL
        elif not self.running:
            self.animTick = 0
            oldrect = self.rect
            self.image = self.stand
            self.rect = self.image.get_rect()
            self.rect.midbottom = oldrect.midbottom
            if not self.walkingRight:
                self.image = self.standL
        else:
            self.animTick += 1
            if self.animTick == 10:
                self.animTick = 0
                oldrect = self.rect
                if self.walkingRight:
                    if self.image == self.stand or self.image == self.standL:
                        self.image = self.run
                    else:
                        self.image = self.stand
                else:
                    if self.image == self.run or self.image == self.runL:
                        self.image = self.standL
                    else:
                        self.image = self.runL
                self.rect = self.image.get_rect()
                self.rect.midbottom = oldrect.midbottom
    
        # if jumping, set y_vel to jump velocity
        if keys[pygame.K_SPACE] and not self.midair:
            self.jumpFX.play()
            self.jump_count += 1
            self.midair = True
            self.y_vel = MARIO_JUMP_VEL
        
        # effect of gravity pulling Mario to earth
        self.y_vel += MARIO_GRAVITY
        
        # is Mario shooting a fireball?
        if keys[pygame.K_e]:
            if not self.fireball_lock and Fireball.count <= MARIO_MAX_FIREBALLS :
                self.fireball_lock = True
                pos = self.rect.midright
                if not self.walkingRight:
                    pos = self.rect.midleft
                FIREBALLS.add( Fireball( pos, self.walkingRight ) )
        else:
            if self.fireball_lock:
                self.fireball_lock = False
                
        # move Mario
        self.rect.move_ip((self.x_vel, self.y_vel))
        
        # check collision with blocks. If Mario's underneath, stop him. If above, Mario
        # stands on blocks. If colliding from the side, he stops moving horizontally
        for block in BLOCKS:
            if block.rect.colliderect(self.rect):
                top, right, bottom, left = collide_edges(self.rect, block.rect)
                if top:
                    self.y_vel = 0
                    self.rect.top = block.rect.bottom
                elif bottom:
                    self.y_vel = 0
                    self.rect.bottom = block.rect.top
                    self.midair = False
                elif right:
                    self.x_vel = 0
                    self.rect.right = block.rect.left
                elif left:
                    self.x_vel = 0
                    self.rect.left = block.rect.right
        
        # if he jumps on top of a shell, shell dies and mario gets another point.
        # mario bounces of shell, shell falls off screen. If he hits shell otherwise,
        # game ends
        already_rebounded = False
        for shell in ENEMIES:
            if shell.rect.colliderect(self.rect):
                top, right, bottom, left = collide_edges(self.rect, shell.rect)
                if bottom:
                    if not already_rebounded:
                        self.y_vel *= -1
                        already_rebounded = True
                    shell.fall()
                    self.hitFX.play()
                    self.score += 1
                elif top:
                    self.isDead = True
                elif right:
                    self.isDead = True
                elif left:
                    self.isDead = True
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.area.width:
            self.rect.right = self.area.width
            
        if self.rect.bottom > self.area.height - 45:
            self.rect.bottom = self.area.height - 45
            self.y_vel = 0
            self.midair = False
        elif self.rect.top < 0:
            self.rect.top = 0
            
# ----------------------------------------------------

class Fireball(pygame.sprite.Sprite):

    image = None
    blueimage = None
    sound = None
    count = 0
    total_count = 0

    def __init__(self, start_pos, goingRight):
    
        pygame.sprite.Sprite.__init__(self)
        
        Fireball.total_count += 1
        
        if Fireball.image is None:
            Fireball.image, rect = loadImage("fireball.png", -1)
            Fireball.blueimage, rect = loadImage("bluefireball.png", -1)
            Fireball.FX = loadSoundFile("fireball.wav")
                    
        self.blue = False
        
        if random.choice( range(1,11) ) == 10: # roughly 1 out of 10 fireballs is blue
            self.blue = True
            
        if self.blue:
            self.image = Fireball.blueimage
            self.vel_y = BLUE_Y_VEL
            self.vel_x = random.choice( BLUE_X_VELS )
        else:
            self.image = Fireball.image
            self.vel_y = RED_Y_VEL
            self.vel_x = random.choice( RED_X_VELS )
            
        if not goingRight:
            self.vel_x *= -1
        
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
            
        Fireball.FX.play()
        
    def update(self):
    
        Fireball.count = len( FIREBALLS )
        self._move()
        
    def _move(self):
        
        self.vel_y += FIREBALL_GRAV
        
        self.rect.move_ip((self.vel_x, self.vel_y))
        
        for block in BLOCKS:
            if block.rect.colliderect(self.rect):
                top, right, bottom, left = collide_edges(self.rect, block.rect)
                if top:
                    self.vel_y = 0
                    self.rect.top = block.rect.bottom
                elif bottom:
                    self.vel_y *= -1
                    self.rect.bottom = block.rect.top
                elif right:
                    self.vel_x *= -1
                    self.rect.right = block.rect.left
                elif left:
                    self.vel_x *= -1
                    self.rect.left = block.rect.right
        
        if self.rect.right < 0:
            self.kill()
        elif self.rect.left > WIDTH:
            self.kill()
            
        if self.rect.bottom >= HEIGHT - 45:
            self.rect.bottom = HEIGHT - 45
            self.vel_y = RED_Y_VEL
            if self.blue:
                self.vel_y = BLUE_Y_VEL
            
# ----------------------------------------------------

class Shell(pygame.sprite.Sprite):

    image = None

    def __init__(self, screen, start_pos):
    
        pygame.sprite.Sprite.__init__(self)
        
        if Shell.image is None:
            tempimage, rect = loadImage("shell.png", -1)
            Shell.image = pygame.transform.scale2x(tempimage).convert()
            
        self.image = Shell.image
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.area = screen.get_rect()
        self.onGround = False
        self.falling = False
        
        self.vel_y = SHELL_Y_VEL
        self.vel_x = SHELL_X_VEL
        
        if start_pos[0] > self.area.width / 2:
            self.vel_x *= -1
            
    def fall(self):
        
        self.falling = True
                
    def update(self):
    
        self._move()
        
    def _move(self):
    
        # if the shell hasn't been jumped on
        if not self.falling:
            if not self.onGround:
                self.vel_y += SHELL_GRAVITY
        
            self.rect.move_ip((self.vel_x, self.vel_y))
            
            if self.rect.right < 0:
                self.kill()
            elif self.rect.left > self.area.width:
                self.kill()
                
            if self.rect.bottom >= self.area.height - 45:
                self.rect.bottom = self.area.height - 45
                self.vel_y = 0
                self.onGround = True
        
        # if the shell HAS been jumped on
        else:
            self.rect.move_ip((self.vel_x, 4))
            
            if self.rect.right < 0:
                self.kill()
            elif self.rect.left > self.area.width:
                self.kill()
                
            if self.rect.top > self.area.height:
                self.kill()
            
# ----------------------------------------------------

class PowBlock(pygame.sprite.Sprite):

    image = None

    def __init__(self, pos):
    
        pygame.sprite.Sprite.__init__(self)
        
        if PowBlock.image is None:
            PowBlock.image, rect = loadImage("pow.png", -1)
            PowBlock.image = pygame.transform.scale2x(PowBlock.image).convert()
            
        self.image = PowBlock.image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        #self.rect.topleft = pos
        self.onGround = False
                
    def update(self):
    
        pass
