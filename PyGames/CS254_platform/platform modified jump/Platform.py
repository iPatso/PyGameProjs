from CONST import *

class Platform():
    def __init__(self, x, y, name):
        self.x, self.y = (x,y)
        self.image = pygame.image.load(os.path.join("data", name+".png")).convert_alpha()
        self.rect = self.image.get_rect()
        
    def update(self, bg_x, bg_y):
        screen.blit(self.image, (bg_x + self.x, bg_y + self.y))
        collide_wall = pygame.Rect(bg_x + self.x, bg_y + self.y, 1, self.rect.get_width())