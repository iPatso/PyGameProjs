import pygame
import Resources, InputState, Vector2, Factory

BG_COLOR = Resources.BLACK

# Classe que armazena a Surface principal do jogo onde tudo sera desenhado
class ScreenManager:
    def __init__(self):
        #pygame.font.init()
        #pygame.mixer.init()
        # quantidade de frames por segundo maxima
        self.framerate = 30
        
        # Surface onde tudo sera desenhado
        self.screen = pygame.display.get_surface()
        # guarda as intaracoes do jogador com o teclado e mouse
        self.inputState = InputState.InputState()
        
        # o BaseObject que sera atualizado (pode ser uma fase, tela de menu, etc)
        self.baseObject = None
        
        self.clock = pygame.time.Clock()
        
        # uma Vector2 de dois elementos que indica a posicao da camera, onde o indice 0 armazena a posicao no eixo 'x' e o indice 1 no eixo 'y'
        self.camera = Vector2.Vector2(0, 0)
        # uma tupla de dois elementos que armazena o tamanho da tela
        self.resolution = self.getLastUsedResolution()
        # sempre que o jogo abrir ele vai pegar a ultima resolucao utilizada e setar a tela com esta resolucao
        self.setResolution(self.resolution)
        
        self.factory = Factory.Factory(self)
        
        # indica se o jogo esta rodando
        self.running = False
    
    # atribui o BaseObject que sera atualisado
    # param: obj - um objeto do tipo BaseObject
    def setBaseObjectToUpdate(self, obj):
        self.baseObject = obj
    
    # loop principal do jogo
    def run(self):
        self.running = True
        while self.running:
            # limpa a tela
            self.screen.fill(BG_COLOR)
            # atualisa os inputs do jogador
            self.inputState.update()
            self.running = not self.inputState.QUIT
            
            # chama o metodo update() do BaseObject
            self.baseObject.update()
            # chama o metodo draw() do GameObject
            self.baseObject.draw()
                    
            pygame.display.flip() # atualiza a tela
            
            self.clock.tick(self.framerate)
            
        pygame.quit()
    
    # Preenche a tela com uma cor 'color'
    # param: color - uma tupla com tres elementos para indicar a cor em RGB
    def fill(self, color):
        self.screen.fill(color)
    
    # Desenha uma surface, relativa ao mapa
    # param: surface - a Surface que sera desenhada
    # param: position - um Vector2 com a posicao no mapa em que a surface sera desenhada
    def blit(self, surface, position):
        pos = self.getSimplePosition(position)
        self.screen.blit(surface, pos)
    
    # Desenha uma surface que nao eh relativa a camera, ou seja, desenha em uma posicao fixa da tela, independente da posicao da camera no mapa
    # param: surface - a Surface que sera desenhada
    # param: position - uma tupla com a posicao na tela
    def blitNonCameraRelative(self, surface, position):
        self.screen.blit(surface, position)
        
    # Retorna uma tupla com a posicao do objeto no mapa relativo a camera
    # param: position - um Vector2 com a posicao no mapa
    # return: tupla com a posicao
    def getSimplePosition(self,position): 
        return (position.x - self.camera.x, position.y - self.camera.y)
    
    # Verifica se uma posicao no mapa esta visivel pela camera
    # param: position - um Vector2 com a posicao no mapa
    # param: offset - uma tupla que indica a quantidade a ser desconsiderada em cada, ou seja,
    #              o quanto pra fora da tela o objeto pode estar, mas ainda considera dentro da tela
    # return: um boolean indicando se esta visivel
    def isInsideScreen(self, position, offset):
        pos = self.getSimplePosition(position)
        # ve se esta fora da tela no eixo x
        if pos[0] + offset[0] < 0 or pos[0] -offset[0]  > self.resolution[0]:
            # esta fora da tela no eixo x
            return False
        # esta dentro da tela no eixo x
        else:
            # agora ve se esta dentro da tela no eixo y
            if pos[1] + offset[1] < 0 or pos[1] - offset[1] > self.resolution[1]:
                # esta fora da tela no eixo y
                return False
            else:
                # esta dentro da tela nos dois eicos
                return True
    
    # Atualiza a posicao da camera
    # param: mapSize: uma tupla de dois elementos indicando a largura (indice 0) e a altura (indice 1) do mapa em pixels
    # param: referencePoint: um Vector2 com um ponto de referencia para a camera, esse ponto sempre deve estar visivel
    def updateCamera(self, mapSize, referencePoint):
        self.camera.x = referencePoint.x - self.resolution[0]/2 # do jeito que ta aki a o ponto de referencia sempre fica no meio da tela (eixo x)
        if self.camera.x < 0:
            self.camera.x = 0
        elif self.camera.x + self.resolution[0] > mapSize[0]:
            self.camera.x = mapSize[0] - self.resolution[0]
        
        self.camera.y = referencePoint.y - self.resolution[1]/2 # do jeito que ta aki a o ponto de referencia sempre fica no meio da tela (eixo y)
        if self.camera.y < 0:
            self.camera.y = 0
        elif self.camera.y + self.resolution[1] > mapSize[1]:
            self.camera.y = mapSize[1] - self.resolution[1]
    
    # funcao que retorna uma tupla de dois elementos indicando a ultima resolucao utilisada na tela
    # param: resolution - uma tupla de dois inteiros que indica a resolucao da tela que sera setada
    def setResolution(self, resolution):
        self.resolution = resolution
        try:
            pygame.display.set_mode(resolution, pygame.FULLSCREEN)
        except Exception:
            self.resolution = Resources.DEFAULT_SCREEN_SIZE
            pygame.display.set_mode(Resources.DEFAULT_SCREEN_SIZE, pygame.FULLSCREEN)
        f = file('res/files/resolution.txt','w')
        f.write(str(self.resolution))
    
    # funcao que retorna uma tupla de dois elementos indicando a ultima resolucao utilisada na tela
    # return: tupla com a ultima resolucao
    def getLastUsedResolution(self):
        try:
            f = file('res/files/resolution.txt', 'r')
            res = eval(f.read())
        except Exception:
            # se der merda, retorna a resolucao default 800,600
            res = Resources.DEFAULT_SCREEN_SIZE
        return res
    
    # para o ScreenManager, termina o loop do jogo
    def stop(self):
        self.running = False