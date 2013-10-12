import pygame
import Resources, GameObject, Vector2, Jump, Shot, SpriteAnimation

# Constantes para o estado do jogador
STOP = 'ss'
RUN = 'sr'
JUMP = 'sj'
FALL = 'sf'
# constante especial, o estado eh parado mas esta atirando
FIRING = 'f'

DELAY_MAX = {
          STOP: -1,
          RUN: 4,
          JUMP: 4,
          FALL: 4,
          FIRING: 3
}

# Classe que representa o jogador
class Player(GameObject.GameObject):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        GameObject.GameObject.__init__(self, manager)
        
        self.spriteDic = Resources.PLAYER
        self.spriteList = Resources.loadTileList(self.spriteDic['s'], self.spriteDic['sw'], self.spriteDic['sh'])

        self.inputState = self.screenManager.inputState
        self.nonHitArea = self.spriteDic['nha']
        
        self.animation = SpriteAnimation.SpriteAnimation(self.spriteDic, DELAY_MAX)
        
        self.state = RUN
        
        self.size.x = self.spriteDic['sw']
        self.size.y = self.spriteDic['sh']
        
        self.velocity = Vector2.Vector2(12,22)
        
        self.jump = Jump.Jump(self)
        bulletVelocity = Vector2.Vector2(25,0)
        self.shot = Shot.Shot(self, bulletVelocity, 5, 83)
        # o delay para o recuo do tiro (quando atira a arma vai para tras e fica um tempo la)
        self.recoilDelay = 0
        # indica se o player acabou de atirar
        self.justFired = False
        
        # indica a ultima posicao que o personagem estava no chao (pra caso ele cair em um buraco volta ele pra ca)
        self.lastSafePosition = Vector2.Vector2(0,0)
        
        # variavel que guarda se o player esta invencivel e faz sua animacao
        self.invencible = Invencible(self.screenManager.framerate, 3)
        
        # numero de vidas do jogador
        self.numberOfLifes = 3
        # imagens para a vida
        oneLife = Resources.loadImage("res/img/carrot1.png")
        twoLifes = Resources.loadImage("res/img/carrot2.png")
        threeLifes = Resources.loadImage("res/img/carrot3.png")
        # lista com as imagens da vida
        self.lifeSpriteList = [oneLife, twoLifes, threeLifes]
        
        # sons
        self.jumpSound = pygame.mixer.Sound("res/sound/jump.wav")
        self.shotSound = pygame.mixer.Sound("res/sound/gun2.ogg")
        self.hitSound = pygame.mixer.Sound("res/sound/hit.wav")
    
    # override GameObject.update()
    def update(self):        
        self.handleInput()
        
        # se o estado atual eh JUMP, faz o personagem pular
        if self.state == JUMP:
            self.jump.doJump()

        self.shot.update()
        
    
    # overrride GameObject.postCollision()
    # aqui que atualisa o 'state' do jogador depois da colisao
    def postCollision(self):
        
        # se a posicao (eixo y) anterior eh menor do que a atual, estado = FALL
        if self.previousPosition.y < self.position.y:
            self.changeState(FALL)
            
        if self.state == FALL:
            # se o personagem nao mudou de posicao no eixo y, nao esta mais caindo
            if self.previousPosition.y == self.position.y:
                self.changeState(RUN) #obs:quando eu colocava em STOP e o jogador esta correndo, da pra perceber a mudanca de STOP para RUN
        elif self.state == JUMP:
            # se o personagem nao mudou de posicao no eixo y, nao esta mais pulando
            if self.previousPosition.y == self.position.y:
                # se o personagem nao alcancou a altura maxima, colidiu com o teto
                if self.jump.jumpHeigh < self.jump.maxJumpHeight:
                    self.jump.jumpHeigh = self.jump.maxJumpHeight
                else:
                    self.changeState(STOP)
        else:
            # se o personagem nao mudou de posicao, faz estado atual = STOP
            if self.previousPosition.equals(self.position):
                self.changeState(STOP)
            # personagem mudou de posicao, estado atual = RUN
            else:
                self.changeState(RUN)
        
        if self.state == STOP:
            self.animation.clear() # se nao quiser ter animacao, coloca o indice sempre zero e nao chame o self.nextFrame(), soh pra economizar processamento
        else:
            self.animation.nextFrame(self.state)
        
        if self.state == STOP or self.state == RUN:
            self.lastSafePosition = self.position.copy()
            
    # override GameObject.draw()
    def draw(self):
        
        if self.state == STOP and self.justFired:
            # surface do coelho atirando, com o recuo da arma
            surface = self.spriteList[self.spriteDic['f']]
            self.recoilDelay += 1
            if self.recoilDelay > DELAY_MAX[FIRING]:
                self.justFired = False
                self.recoilDelay = 0
        else:
            surface = self.spriteList[self.animation.getSpriteIndex(self.state)]
        # se estiver andando para a esquerda, da um flip horizontal na imagem
        if not self.directionX:
            surface = pygame.transform.flip(surface, True, False)
        
        surface.set_alpha(self.invencible.alphaAnimation())

        self.screenManager.blit(surface, self.position)
        
        self.shot.draw()
    
    # manipula o input do usuario e faz as acoes necessarias
    def handleInput(self):
        # verifica se as teclas estao pressionadas
        if self.inputState.K_RIGHT:
            self.directionX = True
            self.move(self.velocity.x, 0)
        if self.inputState.K_LEFT:
            self.directionX = False
            self.move(-self.velocity.x, 0)
        # atira
        if self.inputState.K_a and not self.inputState.P_K_a:
            added = self.shot.addBullet()
            if added:
                self.shotSound.play()
            self.justFired = True
        # pula
        if self.inputState.K_SPACE:
            if not self.inputState.P_K_SPACE:
                # antes o 'space' nao estava pressionado e agora esta
                if self.state != FALL:
                    self.changeState(JUMP)
        elif self.state == JUMP:
            # solta o 'space' antes de terminar o pulo
            self.jump.jumpHeigh = self.jump.maxJumpHeight
    
    # muda o estado atual do jogador
    # param: newState - uma String o novo estado que o jogador recebera (as constantes para o estado do jogador no inicio deste arquivo)
    def changeState(self, newState):
        # se o estado for diferente, muda o estado, se nao continua
        if self.state != newState:
            
            if newState == JUMP:
                # toca o som do cara pulando
                #self.jumpSound.play()
                
                # termina o ultimo pulo comecado
                self.jump.finishJump()                
                # acabou de sair do chao, salva a ultima posicao segura
                self.lastSafePosition = self.position.copy()
            elif newState == FALL and self.state != JUMP:
                # se comecou a cair de algum lugar, a nao ser de um pulo, salva a ultima posicao segura
                self.lastSafePosition = self.position.copy()
                if self.directionX:
                    # se tiver andando pra direita, volta um pouco
                    self.lastSafePosition.x -= self.spriteDic['sw'] / 2
                else:
                    # se tiver andando pra esquerda
                    self.lastSafePosition.x += self.spriteDic['sw'] / 2
            
            self.animation.clear()
            self.state = newState
            
    
    # verifica se o player esta no state = STOP
    def isStop(self):
        if self.state == STOP:
            return True
        else:
            return False
        
    # reinicia a posicao do jogador, eh chamado quando ele perde uma vida
    # param: position - um Vector2 com a nova posicao
    def resetPosition(self):
        self.position = self.lastSafePosition.copy()
        self.position.y -= self.spriteDic['sh'] / 3
        self.invencible.isInvencible = True
        
    # player perde uma vida
    def loseLife(self):
        if not self.invencible.isInvencible:
            self.numberOfLifes -= 1
            self.hitSound.play()
            self.resetPosition()
    
    # retorna a imagem da vida do jogador de acordo com o seu numero de vidas
    # return: uma Surface da vida do jogador, retorna 'None' caso nao tenha mais vidas
    def getLifeSurface(self):
        if self.numberOfLifes > 0:
            return self.lifeSpriteList[self.numberOfLifes - 1]
        else:
            return None
        
        
##################################################################################################################

# classe que salva o estado invencivel e sua animacao de alpha
class Invencible:
    # param: famerate - quantos frames por segundo o jogo esta rodando
    # param: invencibleTime - quanto tempo em segundos o player vai ficar invencivel 
    def __init__(self, framerate, invencibleTime):
        # boolean que indica se o player esta no modo invencivel
        self.isInvencible = False
        # indica o alpha da animacao do player invencivel
        self.alpha = 255
        # indica o contador da animacao do player invencivel
        self.invencibleCount = 0
        # indica o tempo que o player fica invencivel
        self.invencibleTime = invencibleTime * framerate
        # incremento do alpha
        self.increment = -30
        
    # faz a animacao do alpha para o player ficar brilhando
    # return: um int representando o alpha da animacao
    def alphaAnimation(self):
        if not self.isInvencible:
            return 255
        
        self.alpha += self.increment
        if (self.increment < 0 and self.alpha < 0) or (self.increment > 0 and self.alpha > 255):
            self.increment *= -1
            self.alpha += self.increment
            
        self.invencibleCount += 1
        if self.invencibleCount > self.invencibleTime:
            self.invencibleCount = 0
            self.alpha = 255
            self.isInvencible = False
            
        return self.alpha