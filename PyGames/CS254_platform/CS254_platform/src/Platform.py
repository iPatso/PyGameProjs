from CONST import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, name, moves = False):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(os.path.join("data", name+".png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.initX, self.initY = pos
        self.x, self.y = pos
        self.rect.center = pos
        self.moves = moves
        
        self.IsRight = True
        
    def update(self):
        if self.moves:
            if self.x <= self.initX + 100 and self.IsRight:
                self.x += 1
                if self.x == self.initX + 100:
                    self.IsRight = False
            if self.x  >= self.initX and not self.IsRight:
                self.x -= 1
                if self.x == self.initX:
                    self.IsRight = True
                    
        self.rect.center = (self.x,self.y)
        
