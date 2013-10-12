from CONST import *

class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.x = 0
        self.y = screen.get_height()/2
        self.xvel = 0
        self.yvel = 0
        self.speed = 0
        self.gravity = 04.8
        self.friction = 0.8
        self.jumpvel = -40.75
        self.onGround = True
        self.rect = Rect(self.x, self.y, 32, 32)
        
        self.walk_L = pygame.image.load(os.path.join('data','character_L.png')).convert_alpha()
        self.walk_R = pygame.image.load(os.path.join('data','character_R.png')).convert_alpha()
        self.stand_L = pygame.image.load(os.path.join('data','character_sL.png')).convert_alpha()
        self.stand_R = pygame.image.load(os.path.join('data','character_sR.png')).convert_alpha()
        self.walkingRight = True
        self.running = False
        
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        
        
        # Array of walking images
        self.ani_L = arrayImg(self.walk_L, 53, 70)
        self.ani_R = arrayImg(self.walk_R, 53, 70)
        
        self.ani_pos = 0
        self.ani_max = 1                 # each animation has 2 frames
        self.img = self.ani_L[0]
        
    def update(self):

        #all key events will be captured in update()
        keys = pygame.key.get_pressed()

        #frame movements is slow, how to make it smoother?
        self.running = False
        self.ani_speed -= 1
        if self.ani_speed == 0:

                if keys[pygame.K_LEFT]:
                    self.img = self.ani_L[self.ani_pos]
                    self.xvel -= 1.7
                    self.running = True
                    self.walkingRight= False
                if keys[pygame.K_RIGHT]:
                    self.img = self.ani_R[self.ani_pos]
                    self.xvel += 1.7
                    self.walkingRight = True
                    self.running = True
                    
                #sets a maximum velocity so player wont accelerate forever
                if self.xvel < 10:
                    self.x += self.xvel
                else:
                    self.x += 10
                #slows down player according to friction
                self.xvel *= self.friction

                #if not running, replace image with standing image
                if not self.running:
                    self.img = self.stand_R
                    if not self.walkingRight:
                        self.img = self.stand_L

                #increases y velocity if key is pressed
                if keys[pygame.K_UP]:
                    if self.yvel == 0:
                        self.yvel += self.jumpvel
                #since there are no collisions or platform, used y velocity to check for max jump height
                if self.yvel != 0:
                    
                    #player accelerates downward with gravity if already in the air
                    self.yvel += self.gravity

                    #sets a maximum y velocity downward acceleration
                    if self.yvel > 30:
                        self.yvel = 30
                        
                #updates player's y position according to y velocity
                self.y += self.yvel

                #player will fall through the map since there are no platforms to stand on
                #otherwise jump function is working normally

                
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
                    
        #self.rect.move_ip((self.xvel, self.yvel))
        if self.y > screen.get_height()/2:
            self.y = screen.get_height()/2
            self.yvel = 0
        screen.blit(self.img, (self.x, self.y))


        # Check collision with platforms
