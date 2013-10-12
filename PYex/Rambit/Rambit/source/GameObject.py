import pygame
import Vector2, BaseObject

# Uma classe que representa um objeto que se move na tela, como o Player, Enemy
'''abstract'''
class GameObject(BaseObject.BaseObject):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # chama o 'super'
        BaseObject.BaseObject.__init__(self, manager)
        
        # posicao antiga do objeto
        self.previousPosition = Vector2.Vector2(0,0)
        # posicao do objeto
        self.position = Vector2.Vector2(0,0)
        # velocidade do objeto
        self.velocity = Vector2.Vector2(0,0)
        # largura e altura do objeto
        self.size = Vector2.Vector2(0,0)
        
        # lista de quatro elementos que indica a area que nao eh colidida (area ignorada na colisao) dete GameObject
        # lembrando que essa area deve ser menor do que a do objeto, ou seja: nonHitArea[0] + nonHitArea[2] < largura do sprite; e nonHitArea[1] + nonHitArea[3] < altura do sprite
        # indice 0: numero de pixels que sera ignorado a esquerda do GameObject
        # indice 1: numero de pixels que sera ignorado em cima do GameObject
        # indice 2: numero de pixels que sera ignorado a direita do GameObject
        # indice 3: numero de pixels que sera ignorado em baixo do GameObject
        self.nonHitArea = [0, 0, 0, 0]
        # uma string que guarda o estado do GameObject
        self.state = None
        # GameObject andando para direita
        self.directionX = True
    
    # metodo chamado depois do tratamento de colisao com a fase
    '''abstract'''
    def postCollision(self):
        pass
    
    # metodo que move o GameObject
    # param: *args
    # caso passe um parametro:
    #    param: args[0] - um Vector2 indicando o quanto o GameObject vai mover (x,y)
    # caso passe dois parametros:
    #    param: args[0] - um inteiro indicando o quanto o GameObject vai mover no eixo x
    #    param: args[1] - um inteiro indicando o quanto o GameObject vai mover no eixo y
    def move(self, *args):
        if args.__len__() == 1:
            self.position.add(args[0])
        elif args.__len__() == 2:
            self.position.x += args[0]
            self.position.y += args[1]
    
    # calcula e pega o Rect colidivel deste GameObject
    # param: *args
    # caso nao passe parametros:
    #    args = () - retorna o hitBox do GameObject na sua posicao atual
    # caso passe um parametro:
    #    (tupla com a posicao x,y ) - args = (position) - retorna o hitBox do GameObject considerando que ele esteja na posicao passada como argumento (e nao sua posicao atual)
    # return: um Rect com o retangulo colidivel deste GameObject
    def getHitBox(self, *args):
        pos = None
        if args.__len__() > 0:
            pos = args[0][0] + self.nonHitArea[0], args[0][1] + self.nonHitArea[1]
        else:
            pos = self.position.x + self.nonHitArea[0], self.position.y + self.nonHitArea[1]
        size = self.size.x - self.nonHitArea[0] - self.nonHitArea[2], self.size.y - self.nonHitArea[3] - self.nonHitArea[1]
        return pygame.Rect(pos, size)
    
    # muda o estado atual do GameObject
    # param: newState - uma String o novo estado que o GameObject recebera
    '''abstract'''
    def changeState(self, newState):
        pass
    
    # verifica se o player esta no state = STOP
    '''abstract'''
    def isStop(self):
        pass