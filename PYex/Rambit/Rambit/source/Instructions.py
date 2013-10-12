import pygame
import BaseObject, Menu, Resources

# uma tela que mostra as instrucoes do jogo
class Instructions(BaseObject.BaseObject):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        BaseObject.BaseObject.__init__(self, manager)
        
        self.inputState = self.screenManager.inputState
        
        # imagens para as instrucoes
        image = Resources.loadOpaqueImage("res/img/instructionsBackground.png")
        self.image = pygame.transform.smoothscale(image, self.screenManager.resolution)
    
    # override BaseObject.update()
    def update(self):
        if not self.inputState.P_K_ESCAPE and self.inputState.K_ESCAPE:
            # se apertou ESC volta pro menu
            self.screenManager.setBaseObjectToUpdate(Menu.MainMenu(self.screenManager))

    # override BaseObject.draw()
    def draw(self):
        self.screenManager.blitNonCameraRelative(self.image, (0,0))