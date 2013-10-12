from CONST import *
from Battle import battle

class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.x = 0
        self.y = 300
        self.xvel = 0
        self.yvel = 0
        self.speed = 0
        self.gravity = 4.2
        self.friction = 0.7
        self.jumpvel = -15
        self.onGround = False
        self.rect = Rect(self.x, self.y, 52, 70)
        
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
        self.image = self.ani_L[0]
        
        # Used in battle
        self.hp = 100
        
    def update(self):

        #all key events will be captured in update()
        keys = pygame.key.get_pressed()

        #frame movements is slow, how to make it smoother?
        self.running = False
        self.ani_speed -= 1
        if self.ani_speed == 0:

                if keys[pygame.K_LEFT]:
                    self.image = self.ani_L[self.ani_pos]
                    self.xvel -= 1.7
                    self.running = True
                    self.walkingRight= False
                if keys[pygame.K_RIGHT]:
                    self.image = self.ani_R[self.ani_pos]
                    self.xvel += 1.7
                    self.walkingRight = True
                    self.running = True

                #slows down player according to friction
                self.xvel *= self.friction

                #if not running, replace image with standing image
                if not self.running:
                    self.image = self.stand_R
                    if not self.walkingRight:
                        self.image = self.stand_L

                #increases y velocity if key is pressed
                if keys[pygame.K_UP] and self.onGround:
                        self.yvel = self.jumpvel
                        self.onGround = False

                if not self.onGround:
                    
                    #player accelerates downward with gravity if already in the air
                    self.yvel += self.gravity

                    #sets a maximum y velocity downward acceleration
                    if self.yvel > 30:
                        self.yvel = 30

                #player will fall through the map since there are no platforms to stand on
                #otherwise jump function is working normally

                
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1
                    
        self.rect.move_ip((self.xvel, self.yvel))
        if self.rect.bottom > screen.get_height() - 10:
            self.rect.bottom = screen.get_height() - 10
            self.yvel = 0
        #screen.blit(self.image, (self.x, self.y))


        # Check collision with platforms
        for platform in PLATFORMS:
            if platform.rect.colliderect(self.rect):
                top, right, bottom, left = collide_edges(self.rect, platform.rect)
                if top:
                    self.y_vel = 0
                    self.rect.top = platform.rect.bottom
                elif bottom:
                    self.y_vel = 0
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                elif right:
                    self.x_vel = 0
                    self.rect.right = platform.rect.left
                elif left:
                    self.x_vel = 0
                    self.rect.left = platform.rect.right        
                    
        # Check collision with platforms
        for enemy in ENEMIES:
            if enemy.rect.colliderect(self.rect):
                top, right, bottom, left = collide_edges(self.rect, enemy.rect)
                if top:
                    self.rect.top = enemy.rect.bottom
                    print "Collided under"
                    battle(self, enemy)
                elif bottom:
                    self.rect.bottom = enemy.rect.top
                    print "Collided top"
                    battle(self, enemy)
                elif right:
                    self.rect.right = enemy.rect.left
                    print "Collided left"
                    battle(self, enemy)
                elif left:
                    self.rect.left = enemy.rect.right
                    print "Collided right"
                    battle(self, enemy)
