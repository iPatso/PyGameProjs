import pygame

# classe que guarda todos os inputs do jogador
class InputState:
    
    def __init__(self):
        self.events = []
        # inicializa as teclas como False, indicando que nao estao pressionadas
        self.QUIT = False
        self.K_RIGHT = False
        self.K_LEFT = False
        self.K_UP = False
        self.K_DOWN = False
        self.K_SPACE = False
        self.K_a = False
        self.K_ENTER = False
        self.K_ESCAPE = False
        self.K_p = False
        
        
        # previousState - estados do teclado anterior ao update
        self.P_K_a = False
        self.P_K_SPACE = False
        self.P_K_UP = False
        self.P_K_DOWN = False
        self.P_K_ENTER = False
        self.P_K_ESCAPE = False
        self.P_K_p = False
    
    # metodo que pega o input do jogador
    def update(self):
        self.updatePreviousStates()
        
        self.events = pygame.event.get()
        for event in self.events:
            # evento para sair do jogo
            if event.type == pygame.QUIT:
                self.QUIT = True
            # alguma tecla foi pressionada
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.K_RIGHT = True
                elif event.key == pygame.K_LEFT:
                    self.K_LEFT = True
                elif event.key == pygame.K_UP:
                    self.K_UP = True
                elif event.key == pygame.K_DOWN:
                    self.K_DOWN = True
                elif event.key == pygame.K_SPACE:
                    self.K_SPACE = True
                elif event.key == pygame.K_a:
                    self.K_a = True
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # enter numerico ou tecla Return
                    self.K_ENTER = True
                elif event.key == pygame.K_ESCAPE:
                    self.K_ESCAPE = True
                elif event.key == pygame.K_p:
                    self.K_p = True
            # alguma tecla foi solta
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.K_RIGHT = False
                elif event.key == pygame.K_LEFT:
                    self.K_LEFT = False
                elif event.key == pygame.K_UP:
                    self.K_UP = False
                elif event.key == pygame.K_DOWN:
                    self.K_DOWN = False
                elif event.key == pygame.K_SPACE:
                    self.K_SPACE = False
                elif event.key == pygame.K_a:
                    self.K_a = False
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # enter numerico ou tecla Return
                    self.K_ENTER = False
                elif event.key == pygame.K_ESCAPE:
                    self.K_ESCAPE = False
                elif event.key == pygame.K_p:
                    self.K_p = False

    # atualiza os estados anteriores do teclado
    def updatePreviousStates(self):
        self.P_K_a = self.K_a
        self.P_K_SPACE = self.K_SPACE
        self.P_K_UP = self.K_UP
        self.P_K_DOWN = self.K_DOWN
        self.P_K_ENTER = self.K_ENTER
        self.P_K_ESCAPE = self.K_ESCAPE
        self.P_K_p = self.K_p
    
    # retorna se alguma tecla de acao pressionada
    def clicked(self):
        return self.K_a or self.K_ENTER or self.K_ESCAPE or self.K_p or self.K_SPACE