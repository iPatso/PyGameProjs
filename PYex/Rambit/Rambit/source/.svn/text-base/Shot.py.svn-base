import pygame, random
import Resources, BaseObject, Vector2, SpriteAnimation

FIRE = 'sf'
DELAY_MAX = { FIRE: 2 }
                
# Classe responsavel por fazer o personagem atirar
'''Obs: quem for usar a classe Shot deve implementar o metodo isStop()'''
class Shot(BaseObject.BaseObject):
    # param: gameObject - um GameObject no qual a acao de atirar
    # param: bulletVelocity - um Vector2 com a velocidade da bala
    # param: maxAmmunition - um int com o numero maximo de balas que pode atira
    # param: bulletAddY - a posicao da arma relativa ao GameObject no eixo y
    def __init__(self,gameObject, bulletVelocity, maxAmmunition, bulletAddY):
        # sempre lembrar de chamar o 'super'
        BaseObject.BaseObject.__init__(self, gameObject.screenManager)
        
        self.spriteFireDic = Resources.FIRE
        self.bulletDic = Resources.BULLET
        
        self.spriteFireList = Resources.loadTileList(self.spriteFireDic['s'], self.spriteFireDic['sw'], self.spriteFireDic['sh'], 175)
        self.bulletSprite = Resources.loadImage(self.bulletDic['s'])
               
        self.gameObject = gameObject
        
        # lista de tupla, com a posicao da bala e a direcao da bala
        # ammunition[0] = Vector2 com a posicao da bala
        # ammunition[1] = Boolean com a direcao da bala, se for True bala indo para direita
        self.ammunition = []
        
        self.maxAmunition = maxAmmunition
                
        self.shotVelocity = bulletVelocity
        
        # o fogo que sera animado
        self.fireAnimation = None
        # a posicao do fogo quando atirou
        self.firePosition = Vector2.Vector2(0,0)
        
        self.bulletAddY = bulletAddY
        
    # aplica o pulo de acordo com a velocidade atual do pulo
    # return: retorna True se adicionou a bala, e False caso contrario
    def addBullet(self):
        if self.ammunition.__len__() < self.maxAmunition:
            goingToRight = self.gameObject.directionX
            bulletPos = self.gameObject.position.copy()
            
            offset = self.generateOffset()
            
            bulletPos.y += self.bulletAddY + offset
            firePos = bulletPos.copy()
            
            if goingToRight:
                bulletPos.x += self.gameObject.spriteDic['sw'] - self.bulletDic['sw']
                firePos.x += self.gameObject.spriteDic['sw'] - self.spriteFireDic['sw'] / 2
            else:
                firePos.x -= self.spriteFireDic['sw'] / 2
                
            self.ammunition.append( (bulletPos, goingToRight) )
            
            firePos.y -= self.spriteFireDic['sh'] / 2
            
            self.firePosition = firePos
            self.fireAnimation = SpriteAnimation.SpriteAnimation(self.spriteFireDic, DELAY_MAX)
            return True
        else:
            return False
        
    # atualisa a posicao das balas
    def update(self):
        if self.ammunition.__len__() > 0:
            ammoToRemove = []
            for ammo in self.ammunition:
                bullet = ammo[0]
                goingToRight = ammo[1]
                # atira pra direita
                if goingToRight:
                    bullet.x += self.shotVelocity.x
                else:
                    bullet.x -= self.shotVelocity.x
                if not self.screenManager.isInsideScreen(bullet, (35,35)):
                    ammoToRemove.append(ammo)
            
            for ammo in ammoToRemove:
                self.ammunition.remove(ammo)

        if self.fireAnimation != None:
            self.animateFire()
    
    # override GameObject.draw()
    def draw(self):
        if self.fireAnimation != None:
            self.drawFire()
        
        if self.ammunition.__len__() > 0: 
            self.drawBullets()
            
    # desenha o fogo da arma
    def drawFire(self):
        surface = self.spriteFireList[self.fireAnimation.animationDic[FIRE][self.fireAnimation.spriteIndex]]
        # nao dou o flip no fire porque ele eh igual de traz pra frente
        self.screenManager.blit(surface, self.firePosition)
        
    # desenha as balas
    def drawBullets(self):
        surface = self.bulletSprite
        flippedSurface = pygame.transform.flip(surface, True, False)
        for ammo in self.ammunition:
            bullet = ammo[0].copy()
            goingToRight = ammo[1]
            if goingToRight:
                self.screenManager.blit(surface, bullet)
            else:
                self.screenManager.blit(flippedSurface, bullet)
    
    # anima os fogos
    def animateFire(self):
        hasNext = self.fireAnimation.nextFrame(FIRE)
        if not hasNext:
            self.fireAnimation = None
        
    # retorna um offset para a posicao do tiro    
    def generateOffset(self):
        if self.gameObject.isStop():
            return random.randrange(-5,5)
        else:
            return random.randrange(-20,2)