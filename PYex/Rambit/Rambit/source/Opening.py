import pygame
import BaseObject, Resources, Menu

# Classe da abertura do jogo
class Opening(BaseObject.BaseObject):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        BaseObject.BaseObject.__init__(self, manager)
        
        self.inputState = self.screenManager.inputState
        
        # musica
        pygame.mixer.music.load("res/sound/opening.ogg")
        pygame.mixer.music.play(-1)
        
        # imagens
        image = Resources.loadOpaqueImage("res/img/opening.jpg")
        self.image = pygame.transform.smoothscale(image, self.screenManager.resolution)
        
        self.text = Resources.loadImage("res/img/text.png")
        self.text.set_colorkey(Resources.BLACK)
        # posicao no eixo x para que o texto fique no centro da tela
        self.centerx = ( self.screenManager.resolution[0] - self.text.get_width() ) / 2
        # posicao do texto no eixo y
        self.posy = self.screenManager.resolution[1]
    
    # override BaseObject.update()
    def update(self):
        if self.inputState.clicked() or self.posy < -1360:
            # se apertou algo
            pygame.mixer.music.load("res/sound/title.ogg")
            pygame.mixer.music.play(-1)
            self.screenManager.setBaseObjectToUpdate(Menu.MainMenu(self.screenManager))
        else:
            self.posy -= 1

    # override BaseObject.draw()
    def draw(self):
        self.screenManager.blitNonCameraRelative(self.image, (0,0))
        
        self.screenManager.blitNonCameraRelative(self.text, (self.centerx, self.posy))
        