import pygame
import BaseObject, Resources, Opening

class Intro(BaseObject.BaseObject):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        BaseObject.BaseObject.__init__(self, manager)
        
        self.inputState = self.screenManager.inputState
        
        # musica
        self.introSound = pygame.mixer.Sound("res/sound/intro.ogg")
        self.introSound.play()
        self.count = 0
        
        # imagens
        image = Resources.loadOpaqueImage("res/img/intro.png")
        self.image = pygame.transform.smoothscale(image, self.screenManager.resolution)
    
    # override BaseObject.update()
    def update(self):
        self.count += 1
        if self.inputState.clicked() or self.count > 135:
            # se apertou algo
            self.introSound.fadeout(180)
            self.screenManager.setBaseObjectToUpdate(Opening.Opening(self.screenManager))

    # override BaseObject.draw()
    def draw(self):
        self.screenManager.blitNonCameraRelative(self.image, (0,0))
        