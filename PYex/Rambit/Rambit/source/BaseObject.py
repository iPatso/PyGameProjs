
# Uma classe que representa um objeto do jogo que tenha um update() e draw()
#obs.: essa era para ser uma classe abstrata, mas como nao existem em python, considerem que esta eh uma classe abstrata
#      qualquer classe que tenha um update() ou draw() deve extender essa classe: por exemplo, Stage e Shot 
'''abstract'''
class BaseObject:
    # inicializa o ScreenManager
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        self.screenManager = manager
    
    # metodo que atualiza o GameObject a cada frame
    '''abstract''' # sobrescreva esse metodo
    def update(self):
        pass
    
    # metodo que desenha o GameObject a cada frame
    '''abstract''' # sobrescreva esse metodo
    def draw(self):
        pass