import pygame
import Resources, BaseObject, Instructions, Stage 

# escalas das distancias dos itens do menu
SCALE_MENU_X = 0.13
SCALE_MENU_Y = 0.17

# classe que representa os menus do jogo
'''abstract'''
class Menu(BaseObject.BaseObject):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        BaseObject.BaseObject.__init__(self, manager)
        
        # lista com os botoes do menu principal
        self.menuEntries = []
        
        res = self.screenManager.resolution
        # resolucao utilizada pelos menusEntry
        self.resolution = [0,0]
        self.resolution[0] = res[0]
        self.resolution[1] = res[1]
        
        # indice do botao selecionado
        self.arrowIndex = 0
        self.arrowImage = Resources.loadImage("res/img/carrot.png")
        self.xd = self.resolution[0] * SCALE_MENU_X
        self.yd = self.resolution[1] * SCALE_MENU_Y
        self.arrowPosition = [self.xd - self.arrowImage.get_width(), self.yd]
        
        self.inputState = self.screenManager.inputState
        
        self.clickSound = pygame.mixer.Sound("res/sound/click.wav")
        self.moveSound = pygame.mixer.Sound("res/sound/move.wav")
        
        background = Resources.loadImage("res/img/menubg.jpg")
        self.background = pygame.transform.smoothscale(background, res)
        
    # override BaseObject.update()
    def update(self):
        if not self.inputState.P_K_DOWN and self.inputState.K_DOWN:
            # se apertou a seta para baixo
            self.moveSound.play()
            self.arrowIndex = (self.arrowIndex + 1) % self.menuEntries.__len__()
        elif not self.inputState.P_K_UP and self.inputState.K_UP:
            # se apertour a seta para cima
            self.moveSound.play()
            self.arrowIndex -= 1
            if self.arrowIndex < 0:
                self.arrowIndex = self.menuEntries.__len__() - 1
        elif (not self.inputState.P_K_SPACE and self.inputState.K_SPACE) or (not self.inputState.P_K_ENTER and self.inputState.K_ENTER):
            # se apertou Espaco, Enter ou EnterNumerico
            self.clickSound.play()
            self.functions[self.arrowIndex](self) # chama uma funcao da lista
                
        self.arrowPosition[1] = self.menuEntries[self.arrowIndex].rect.top + 6
    
    # override BaseObject.draw()
    def draw(self):
        self.screenManager.blitNonCameraRelative(self.background, (0,0))
        
        for menuEntry in self.menuEntries:
            # desenha os botoes
            menuEntry.draw(self.screenManager)
        # desenha a seta que aponta para um botao
        self.screenManager.blitNonCameraRelative(self.arrowImage, self.arrowPosition)
        

##################################################################################################################
##################################################################################################################


# classe do menu principal
class MainMenu(Menu):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        Menu.__init__(self, manager)
        
        # lista com os botoes do menu principal
        self.menuEntries = [
            MenuEntry( (self.xd,self.yd), "res/img/startgame.png", self.resolution  ),
            MenuEntry( (self.xd,2*self.yd), "res/img/instructions.png", self.resolution ),
            MenuEntry( (self.xd,3*self.yd), "res/img/options.png", self.resolution ),
            MenuEntry( (self.xd,5*self.yd), "res/img/exitgame.png", self.resolution )
        ]
        
        rambit = Resources.loadImage("res/img/rambit.png")
        res = [0,0]
        res[0] = (int)(self.resolution[0] * 0.38)
        res[1] = (int)(self.resolution[1] * 0.38) 
        self.rambit = pygame.transform.scale(rambit, res)
    
    def fStartGame(self):
        self.screenManager.setBaseObjectToUpdate(StagesMenu(self.screenManager))
    def fInstructions(self):
        self.screenManager.setBaseObjectToUpdate(Instructions.Instructions(self.screenManager))
    def fOptions(self):
        self.screenManager.setBaseObjectToUpdate(OptionsMenu(self.screenManager))
    def fExitGame(self):
        self.screenManager.stop()
    
    # funcoes que serao chamadas ao abrir um MenuEntry
    functions = [fStartGame, fInstructions, fOptions, fExitGame]
    
    # override Menu.update
    def update(self):
        Menu.update(self) # chama o super
        
        if not self.inputState.P_K_ESCAPE and self.inputState.K_ESCAPE:
            self.fExitGame()
    
    # override Menu.draw()
    def draw(self):
        Menu.draw(self) # chama o super
        
        self.screenManager.blitNonCameraRelative(self.rambit, (self.resolution[0] - self.rambit.get_width() - self.xd, self.yd/2))


##################################################################################################################
##################################################################################################################


# classe do menu das fases
class StagesMenu(Menu):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        Menu.__init__(self, manager)
        
        # lista com os botoes do menu
        self.menuEntries = [
            MenuEntry( (self.xd,self.yd), "res/img/stage1.png", self.resolution  ),
            MenuEntry( (self.xd,2*self.yd), "res/img/stage2.png", self.resolution ),
            MenuEntry( (self.xd,5*self.yd), "res/img/back.png", self.resolution )
        ]
    
    def fStage1(self):
        self.screenManager.setBaseObjectToUpdate(Stage.Stage1(self.screenManager))
    def fStage2(self):
        self.screenManager.setBaseObjectToUpdate(Stage.Stage2(self.screenManager))
    def fBack(self):
        self.screenManager.setBaseObjectToUpdate(MainMenu(self.screenManager))
    
    # funcoes que serao chamadas ao abrir um MenuEntry
    functions = [fStage1, fStage2, fBack]

    # override Menu.update
    def update(self):
        Menu.update(self) # chama o super
        
        if not self.inputState.P_K_ESCAPE and self.inputState.K_ESCAPE:
            self.fBack()

##################################################################################################################
##################################################################################################################


# classe do menu das fases
class OptionsMenu(Menu):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        Menu.__init__(self, manager)
        
        self.yd = self.resolution[1] * 0.1
        
        # lista com os botoes do menu
        self.menuEntries = [
            MenuEntry( (self.xd,self.yd), "res/img/800x600.png", self.resolution ),
            MenuEntry( (self.xd,2*self.yd), "res/img/1024x768.png", self.resolution ),
            MenuEntry( (self.xd,3*self.yd), "res/img/1152x864.png", self.resolution ),
            MenuEntry( (self.xd,4*self.yd), "res/img/1280x768.png", self.resolution ),
            MenuEntry( (self.xd,5*self.yd), "res/img/1280x1024.png", self.resolution ),
            MenuEntry( (self.xd,6*self.yd), "res/img/1400x900.png", self.resolution ),
            MenuEntry( (self.xd,8*self.yd), "res/img/back.png", self.resolution )
        ]
        
        hint = Resources.loadImage("res/img/hint.png")
        res = [0,0]
        res[0] = (int)(self.resolution[0] * 0.5)
        res[1] = (int)(self.resolution[1] * 0.5) 
        self.hint = pygame.transform.scale(hint, res)
        
    def f800x600(self):
        self.screenManager.setResolution((800,600))
        self.resize()
    def f1024x768(self):
        self.screenManager.setResolution((1024,768))
        self.resize()
    def f1152x864(self):
        self.screenManager.setResolution((1152,864))
        self.resize()
    def f1280x768(self):
        self.screenManager.setResolution((1280,768))
        self.resize()
    def f1280x1024(self):
        self.screenManager.setResolution((1280,1024))
        self.resize()
    def f1400x900(self):
        self.screenManager.setResolution((1400,900))
        self.resize()
    def fBack(self):
        self.screenManager.setBaseObjectToUpdate(MainMenu(self.screenManager))
    
    # recria o menu depois de ter redimencionado, e rposiciona a seta
    def resize(self):
        op = OptionsMenu(self.screenManager)
        self.screenManager.setBaseObjectToUpdate(op)
        op.arrowIndex = 6
    
    # funcoes que serao chamadas ao abrir um MenuEntry
    functions = [f800x600, f1024x768, f1152x864, f1280x768, f1280x1024, f1400x900, fBack]
    
    # override Menu.update
    def update(self):
        Menu.update(self) # chama o super
        
        if not self.inputState.P_K_ESCAPE and self.inputState.K_ESCAPE:
            self.fBack()
    
    # override Menu.draw()
    def draw(self):
        Menu.draw(self) # chama o super
        
        self.screenManager.blitNonCameraRelative(self.hint, (self.resolution[0] - self.hint.get_width() - self.xd/2, self.yd/2))
        

##################################################################################################################
##################################################################################################################


# porcentagem da tela que um MenuEntry ocupara
SCALEX = 0.25
SCALEY = 0.08

# classe que representa os botoes do menu
class MenuEntry:
    # param: position - uma tupla com a posicao do MenuEntry na tela
    # param: imagePath - o caminho para carregar a imagem
    # param: resolution - resolucao total do menu
    def __init__(self, position, imagePath, resolution):
        image = Resources.loadImage(imagePath)
        res = [0,0]
        res[0] = (int)(resolution[0] * SCALEX)
        res[1] = (int)(resolution[1] * SCALEY)
        self.image = pygame.transform.scale(image, res)
        rect = self.image.get_rect()
        self.rect = rect.move(position)
    
    # desenha a MenuEntry na tela
    # param: manager - a instancia do manager para desenhar na tela 
    def draw(self, manager):
        manager.blitNonCameraRelative(self.image, self.rect)