
# Classe responsavel pelo pulo do personagem
class Jump:
    
    # param: gameObject - um GameObject no qual o pulo sera executado
    def __init__(self, gameObject):
        self.gameObject = gameObject
        # altura maxima do pulo
        self.maxJumpHeight = 400
        # um int para a velocidade do pulo, tem que ser maior do que a gravidade, senao o cara nao pula
        self.jumpVelocity = gameObject.velocity.y
        # altura atual do pulo
        self.jumpHeigh = 0
    
    # aplica o pulo de acordo com a velocidade atual do pulo
    def doJump(self):
        if self.jumpHeigh < self.maxJumpHeight - self.jumpVelocity:
            self.jumpHeigh += self.jumpVelocity
            self.gameObject.move(0, -self.jumpVelocity)
    
    # termina o pulo atual
    def finishJump(self):
        self.jumpHeigh = 0