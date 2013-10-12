from CONST import *

class Background():
    def __init__(self):
        self.x = 0
        self.image = pygame.image.load(os.path.join("data", "sky.png")).convert()
        
    def update(self):
        screen.blit(self.image, (self.x, 0))