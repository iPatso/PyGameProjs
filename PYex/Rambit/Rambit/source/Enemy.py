import pygame
import GameObject, Resources, SpriteAnimation, Vector2, Shot

# tipos de inimigos
SHOOTER = 'SHOOTER'
RUNNER = 'RUNNER'

STOP = 'ss'
RUN = 'sr'
DYING = 'sd'
# constante especial, o estado eh parado mas esta atirando
FIRING = 'f'

DELAY_MAX = {
        STOP: -1,
        RUN: 5,
        DYING: -1,
        FIRING: 7
}

BLOOD = 'sb'
BLOOD_DELAY = { BLOOD: 2 }

# Classe que represenda os inimigos
class Enemy(GameObject.GameObject):

    # param: manager - instancia do ScreenManager
    # param: stage - instancia da fase
    def __init__(self, manager, stage):
        GameObject.GameObject.__init__(self, manager)
        # fase que o inimigo esta
        self.stage = stage
        
        self.bloodDic = Resources.BLOOD
        self.bloodList = Resources.loadTileList(self.bloodDic['s'], self.bloodDic['sw'], self.bloodDic['sh'])
        self.bloodAnimation = SpriteAnimation.SpriteAnimation(self.bloodDic, BLOOD_DELAY)
        
        self.type = ''
                    
    # override GameObject.draw()
    def draw(self):
        surface = self.spriteList[self.animation.getSpriteIndex(self.state)]
        # se estiver andando para a esquerda, da um flip horizontal na imagem
        if not self.directionX:
            surface = pygame.transform.flip(surface, True, False)
        
        if self.state == DYING:
            spriteIndex = self.bloodAnimation.getSpriteIndex(BLOOD)
            bloodSurface = self.bloodList[spriteIndex]
            pos = self.position.copy()
            tam2 = self.size.copy()
            tam2.div(2)
            pos.add(tam2) # agora a posicao esta no centro do objeto
            pos.x -= self.bloodDic['sw'] / 2
            pos.y -= self.bloodDic['sh'] / 2 # agora o centro do sprite do sangue eh o mesmo do centro do Enemy

            surface.set_alpha(255 - spriteIndex * 18) # diminui o alpha do inimigo quando ele morre
            self.screenManager.blit(surface, self.position)
            
            self.screenManager.blit(bloodSurface, pos)
        else:
            self.screenManager.blit(surface, self.position)
        
    
    # override GameObject.changeState()
    # param: newState - uma String o novo estado (as constantes para o estado no inicio deste arquivo)
    def changeState(self, newState):
        # se o estado for diferente, muda o estado, se nao continua
        if self.state != newState:
            self.animation.clear()
            self.state = newState


###########################################################################################################################################
###########################################################################################################################################


# Classe que represenda o inimigo lenhador
class LumberjackEnemy(Enemy):
    # param: manager - instancia do ScreenManager
    # param: stage - instancia da fase
    def __init__(self, manager, stage):
        Enemy.__init__(self, manager, stage)
        
        self.spriteDic = Resources.LUMBERJACK
        self.spriteList = Resources.loadTileList(self.spriteDic['s'], self.spriteDic['sw'], self.spriteDic['sh'])
        self.nonHitArea = self.spriteDic['nha']

        self.animation = SpriteAnimation.SpriteAnimation(self.spriteDic, DELAY_MAX)
        
        self.state = RUN
        
        self.size.x = self.spriteDic['sw']
        self.size.y = self.spriteDic['sh']
        
        self.type = RUNNER
        
        self.velocity = Vector2.Vector2(-14,0)
        
        self.directionX = False # direcao padrao, vem da direita para esquerda
    
    # override GameObject.update()
    def update(self):
        hasNext = True
        if self.state == RUN:
            self.move(self.velocity)
            self.animation.nextFrame(self.state)
        elif self.state == DYING:
            hasNext = self.bloodAnimation.nextFrame(BLOOD)
            self.animation.clear()
        
        if self.state == DYING and not hasNext:
            # se o state == None, este inimigo esta morto
            self.state = None
            
    # overrride GameObject.postCollision()
    def postCollision(self):
        # se nao mudou de posicao
        if self.previousPosition.equals(self.position) and self.state != DYING:
            self.changeDirection()
            
    # muda a direcao se o inimigo colidir com uma parede
    def changeDirection(self):
        if self.directionX:
            self.directionX = False
        else:
            self.directionX = True
        self.velocity.x *= -1


###########################################################################################################################################
###########################################################################################################################################


# Classe que represenda o inimigo cacador
class HunterEnemy(Enemy):
    # param: manager - instancia do ScreenManager
    # param: stage - instancia da fase
    def __init__(self, manager, stage):
        Enemy.__init__(self, manager, stage)
        
        self.spriteDic = Resources.HUNTER
        self.spriteList = Resources.loadTileList(self.spriteDic['s'], self.spriteDic['sw'], self.spriteDic['sh'])
        self.nonHitArea = self.spriteDic['nha']

        self.animation = SpriteAnimation.SpriteAnimation(self.spriteDic, DELAY_MAX)
        
        self.state = STOP
        
        self.size.x = self.spriteDic['sw']
        self.size.y = self.spriteDic['sh']
        
        self.type = SHOOTER
        
        bulletVelocity = Vector2.Vector2(24,0)
        self.shot = Shot.Shot(self, bulletVelocity, 1, 77)
        # o delay para o recuo do tiro (quando atira a arma vai para tras e fica um tempo la)
        self.recoilDelay = 0
        # indica se o player acabou de atirar
        self.justFired = False
        self.maxShotDelay = 1.5 * self.screenManager.framerate # 1.5 segundos
        self.shotDelay = 0
        
        self.playerVisibility = False
        self.previousPlayerVisibility = False
        
        self.position = Vector2.Vector2(700,700)
        
        self.shotSound = pygame.mixer.Sound("res/sound/gun1.ogg")
    
    # override GameObject.update()
    def update(self):
        self.previousPlayerVisibility = self.playerVisibility
        
        hasNext = True
        if self.state == STOP:
            player = self.stage.player
            
            # se o player esta atras do hunter, inverte a direcao
            self.updateDirection(player)
            
            # se o player esta no campo de visao, e hunter pode atirar
            self.playerVisibility = self.isVisible(player)
            if self.playerVisibility:
                if not self.previousPlayerVisibility:
                    self.shotDelay = self.maxShotDelay / 2
                if not self.justFired:
                    self.shotDelay += 1
                    if self.shotDelay > self.maxShotDelay:
                        self.shot.addBullet()
                        self.justFired = True
                        self.shotDelay = 0
                        inscreen = self.screenManager.isInsideScreen(self.position, (60,0))
                        if inscreen:
                            self.shotSound.play()

        elif self.state == DYING:
            hasNext = self.bloodAnimation.nextFrame(BLOOD)
            self.animation.clear()
        
        if self.state == DYING and not hasNext:
            # se o state == None, este inimigo esta morto
            self.state = None
            
    # atualisa os tiros mesmo se o inimigo esta fora da tela
    def updateShot(self):
        self.shot.update()
    
    # override Enemy.draw()
    def draw(self):
        if self.state == STOP and self.justFired:
            # surface do enemy atirando, com o recuo da arma
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
        
        if self.state == DYING:
            spriteIndex = self.bloodAnimation.getSpriteIndex(BLOOD)
            bloodSurface = self.bloodList[spriteIndex]
            pos = self.position.copy()
            tam2 = self.size.copy()
            tam2.div(2)
            pos.add(tam2) # agora a posicao esta no centro do objeto
            pos.x -= self.bloodDic['sw'] / 2
            pos.y -= self.bloodDic['sh'] / 2 # agora o centro do sprite do sangue eh o mesmo do centro do Enemy

            surface.set_alpha(255 - spriteIndex * 18) # diminui o alpha do inimigo quando ele morre
            self.screenManager.blit(surface, self.position)
            
            self.screenManager.blit(bloodSurface, pos)
        else:
            self.screenManager.blit(surface, self.position)
        
        
    # desenha os tiros, mesmo se o inimigo esta fora da tela
    def drawShot(self):
        self.shot.draw()
        
    # verifica se o player esta visivel
    # param: player - o Player do Stage
    # return: um boolean indicando se o player esta visivel para o enemy atirar
    def isVisible(self, player):
        playerPos = player.position
        playerSizeY = player.size.y
        if playerPos.y < self.position.y + self.size.y and playerPos.y + playerSizeY > self.position.y:
            return True
        else:
            return False
    
    # atualisa a direcao do enemy
    # param: player - o Player do Stage
    def updateDirection(self, player):
        playerPosX = player.position.x
        if playerPosX > self.position.x:
            self.directionX = True
        else:
            self.directionX = False
    
    # verifica se o enemy esta no state = STOP
    def isStop(self):
        if self.state == STOP:
            return True
        else:
            return False