
# classe que faz a animacao dos sprites
class SpriteAnimation:
    # param: animationDic - um dicionario com as animacoes
    # param: delayMax - um dicionario com o delayMax de cada animacao
    def __init__(self, animationDic, delayMax):
        # contador para o delay em frames da animacao
        self.delay = 0
        # o indice da animacao
        self.spriteIndex = 0
        # uma dicionario com as animacoes (cada animacao eh uma sequencia de indices do sprite para a animacao)
        self.animationDic = animationDic
        # uma dicionario com o delay maximo de cada animacao da lista de animacoes
        self.delayMax = delayMax
        
    # muda o sprite da animacao de acordo com o delay estabelecido
    # param: state - uma string com a chave do dicionario para a animacao
    # return: retorna se a animacao ainda deve continuar, se for uma animacao circular o retorno nao precisa ser levado em conta
    def nextFrame(self, state):
        self.delay = (self.delay + 1) % self.delayMax[state]
        if self.delay == 0:
            self.spriteIndex = (self.spriteIndex + 1) % self.animationDic[state].__len__()
            if self.spriteIndex == 0:
                return False
        return True
    
    # zera o spriteIndex
    def clear(self):
        self.spriteIndex = 0
    
    # retorna o indice do sprite de acordo com o 'state' passado
    # param: state - uma string com a chave do dicionario da animacao atual
    def getSpriteIndex(self, state):
        return self.animationDic[state][self.spriteIndex]