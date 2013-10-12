import pygame
import Vector2, BaseObject, Enemy, Resources, Menu

# Classe que gerencia as fases do jogo
class Stage(BaseObject.BaseObject):
    
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        # sempre lembrar de chamar o 'super'
        BaseObject.BaseObject.__init__(self, manager)
        
        map_ = Resources.MAP
        # lista com os tiles do mapa    # como todas as fases terao os mesmos tiles, entao pode ler o tile de qualquer stage
        self.tileList = Resources.loadTileList(map_['ts'], map_['tw'], map_['th'])
        Resources.optimizeSurfacesToBlit(self.tileList, [5,6,7,8,13,14,15,16,17,18,19,20])
        
        # o estado do input do jogador
        self.inputState = self.screenManager.inputState
        # tamanho do mapa em pixels
        self.stageSize = Vector2.Vector2(0,0)
        
        # ponto de referencia que sera passado para a camera
        self.referencePoint = Vector2.Vector2(0,0)
        
        # gravidade do mapa
        self.gravity = Vector2.Vector2(0,10)
        
        # jogador principal
        self.player = self.screenManager.factory.getPlayer()
        
        # lista de inimigos para adicionar na fase
        # enemyList[0] = Vector2 com a posicao do inimigo
        # enemyList[1] = uma String com o tipo do inimigo
        # enemyList[2] = um boolean com a direcao do inimigo
        self.enemyList = []
        
        # lista com todos os GameObjects deste mapa, com execao do player
        self.gameObjects = []
        # lista com os GameObjects que serao removidos do mapa
        self.gameObjectsToRemove = []
        # offset que indica o quanto um objeto pode sair da tela, mas seu update() ainda eh chamado
        self.updateOffset = 450, 300 # valores relativos a partir da resolucao maxima
        # offset que indica o quanto um objeto pode sair da tela, mas o updateModifier deste stage ainda pode ser chamado
        self.modifierOffset = 700, 600 # valores relativos a partir da resolucao maxima
        
        # boolean que guarda se o jogador esta morto (perdeu todas as vidas)
        self.gameOver = False
        # imagem da tela de game over
        gameOverImage = Resources.loadOpaqueImage("res/img/gameover.png")
        self.gameOverImage = pygame.transform.scale(gameOverImage, self.screenManager.resolution)
        self.goAlpha = 0 # alpha da imagem do game over
        self.gameOverSound = pygame.mixer.Sound("res/sound/defeat.ogg")
        self.flCount = 0 # contador para a animacao do finish level
        self.finishLevelSound = pygame.mixer.Sound("res/sound/pass.ogg")
        self.killSound = pygame.mixer.Sound("res/sound/kill.wav")
        # musica de fundo
        self.backgroundMusic = None
        
        self.isPause = False
        
        background = Resources.loadOpaqueImage("res/img/background.png")
        self.background = pygame.transform.smoothscale(background, self.screenManager.resolution)
        #self.m = Resources.loadTileList("res/img/City Day.png", 64, 64)
        
    # override GameObject.update()
    def update(self):
        # verifica se o jogador pausou o jogo ou se saiu da fase
        if not self.gameOver and not self.inputState.P_K_p and self.inputState.K_p:
            if self.isPause:
                self.isPause = False
                pygame.mixer.music.set_volume(1)
            else:
                self.isPause = True
                pygame.mixer.music.set_volume(0.15)
        elif not self.inputState.P_K_ESCAPE and self.inputState.K_ESCAPE:
            # se apertar ESC, volta pro menu
            self.screenManager.setBaseObjectToUpdate(Menu.StagesMenu(self.screenManager))
            self.finishLevelSound.fadeout(100)
            self.gameOverSound.fadeout(150)
            pygame.mixer.music.load("res/sound/title.ogg")
            pygame.mixer.music.play(-1)
            
        if not self.isPause: # se o jogador nao 'pausou' o jogo
            if self.gameOver: # se fim de jogo
                if self.goAlpha == 0:
                    pygame.mixer.music.stop()
                    self.gameOverSound.play()
                self.goAlpha += 2
                if self.goAlpha > 200 and (self.inputState.K_ESCAPE or self.inputState.K_ENTER or self.inputState.K_SPACE or self.inputState.K_a):
                    self.gameOverSound.fadeout(600)
                    # depois de morrer abre o menu de fase
                    self.screenManager.setBaseObjectToUpdate(Menu.StagesMenu(self.screenManager))
                    pygame.mixer.music.load("res/sound/title.ogg")
                    pygame.mixer.music.play(-1)
                    
            elif self.isFinished(): # se passou de fase
                if self.flCount == 0:
                    pygame.mixer.music.stop()
                    self.finishLevelSound.play()
                elif self.flCount > self.screenManager.resolution[0]:
                    self.finishLevelSound.fadeout(900)
                    # depois de terminar a fase abre o menu de fase
                    self.screenManager.setBaseObjectToUpdate(Menu.StagesMenu(self.screenManager))
                    pygame.mixer.music.load("res/sound/title.ogg")
                    pygame.mixer.music.play(-1)
                self.flCount += 20
                
                
            else: # update da propria fase
                self.handlePlayer()
                
                self.handleGameObjects()
                    
                if self.gameObjectsToRemove.__len__() > 0:
                    self.kill()
                    
                # referencePoint = centro do jogador no eixo x, um pouco acima do jogador no eixo y
                self.referencePoint.x = self.player.position.x + self.player.size.x / 2
                self.referencePoint.y = self.player.position.y + self.player.size.y / 2 # esta tirando 200 pro jogador ficar um pouco abaixo do centro da camera
                self.screenManager.updateCamera(self.stageSize.t(), self.referencePoint)
                
                self.putEnemies()    
    
    # manipula o jogador, faz suas atualizacoes e tratamentos
    def handlePlayer(self):
        # atualisa o player
        self.updateGameObject(self.player)
        playerPosX = self.player.position.x
        # nao deixa o player sair do mapa na horizontal
        if playerPosX < 0:
            self.player.position.x = 0
        elif playerPosX + self.player.size.x > self.stageSize.x:
            self.player.position.x = self.stageSize.x - self.player.size.x
        # ve se o player saiu do mapa na vertical
        playerOutOfStage = self.updateStageModifiers(self.player)
        
        if playerOutOfStage:
            self.player.loseLife()
    
    # manipula os gameObjects, faz suas atualizacoes e tratamentos
    def handleGameObjects(self):
        # atualisa os outros GameObjects
        for go in self.gameObjects:
            goOutOfStage = False
            if self.screenManager.isInsideScreen(go.position, self.modifierOffset):
                # se 'go' esta dentro da tela
                if self.screenManager.isInsideScreen(go.position, self.updateOffset):
                    self.updateGameObject(go)
                # se 'go' esta dentro do offset
                goOutOfStage = self.updateStageModifiers(go)
                
            # se tiver fora do offset nao atualisa o 'go' e nem aplica os modificadores da fase
            
            if go.type == Enemy.SHOOTER:
                go.updateShot() # atualisa os tiros dos inimigos
                
                goAmmunition = go.shot.ammunition
                playerCollided = self.gameObjectAndBulletsCollided(self.player, goAmmunition)
                if playerCollided:
                    self.player.loseLife()
            
            if goOutOfStage:
                self.addToKill(go)
            
            if go.state == None:
                self.addToKill(go)
            elif go.state != Enemy.DYING:
                if self.gameObjectsCollided(go, self.player):
                    self.player.loseLife()

                playerAmmunition = self.player.shot.ammunition
                goCollided = self.gameObjectAndBulletsCollided(go, playerAmmunition)
                if goCollided:
                    self.killSound.play()
                    go.changeState(Enemy.DYING)
                    
    # atualisa o gameObject
    # param: gameObject - um GameObject para ser atualisado
    def updateGameObject(self, gameObject):
        gameObject.previousPosition = gameObject.position.copy()
        gameObject.update()
    
    # aplica os modificadores da fase no gameObject
    # param: gameObject - um GameObject para ser aplicado as mudancas da fase
    # retorna se o gameObject saiu do mapa
    def updateStageModifiers(self, gameObject):
        self.applyGravity(gameObject)
        self.applyCollision(gameObject)
        gameObject.postCollision()
        
        return self.isOutOfStage(gameObject)
    
    # dependendo da posicao do jogador coloca os inimigos na fase
    def putEnemies(self):
        if self.enemyList.__len__() > 0:
            enemy = self.enemyList[0]
            enemyPos = enemy[0]
            enemyDirection = enemy[2]
            if enemyDirection: # se for um cara que corre da esquerda pra direita
                enemyPos.x = self.screenManager.camera.x - 200
        
            if self.screenManager.isInsideScreen(enemyPos, self.updateOffset):
                enemyType = enemy[1]
                # adiciona o inimigo na fase
                self.gameObjects.append( self.screenManager.factory.getEnemy(self, enemyPos, enemyType, enemyDirection) )
                # retira o inimigo da lista de inimigos restantes
                self.enemyList.remove(enemy)
    
    # override GameObject.draw()
    def draw(self):
        self.drawMap()
        
        self.player.draw()
        
        for go in self.gameObjects:
            if self.screenManager.isInsideScreen(go.position, go.size.t()):
                go.draw()
            
            if go.type == Enemy.SHOOTER:
                go.drawShot() # desenha os tiros dos inimigos
        
        lifeSurface = self.player.getLifeSurface()
        if lifeSurface != None: # o jogador ainda tem vida
            self.screenManager.blitNonCameraRelative(lifeSurface, (25,15))
        else: # se o jogador morreu
            self.gameOver = True
            self.gameOverImage.set_alpha(self.goAlpha)
            self.screenManager.blitNonCameraRelative(self.gameOverImage, (0,0))
        
        if self.isFinished():
            surface = self.screenManager.screen
            res1 = self.screenManager.resolution[1]
            for i in range(0, self.flCount):
                pygame.draw.line( surface, Resources.BLACK, (i, 0), (i, res1) )
    
    # desenha o mapa na tela, de acordo com a posicao da camera
    def drawMap(self):
        self.screenManager.blitNonCameraRelative(self.background, (0,0))
        
        camRow = self.screenManager.camera.y / self.tileHeight
        camCol = self.screenManager.camera.x/self.tileWidth
        camEndRow = (self.screenManager.camera.y + self.screenManager.resolution[1])/self.tileHeight
        camEndCol = (self.screenManager.camera.x + self.screenManager.resolution[0])/self.tileWidth

        for row in range(camRow, camEndRow + 1):
            for col in range(camCol, camEndCol + 1):
                # verifica se nao esta fora de indice
                if row >= 0 and col >= 0 and row < self.mapDic['mh'] and col < self.mapDic['mw']:
                    # posicao do tile na lista de tiles 'tileList'
                    tilePos = self.mapDic['tl'][row][col] - 1
                    if tilePos > -1:
                        pos = Vector2.Vector2(col * self.tileWidth ,row * self.tileHeight)
                        self.screenManager.blit(self.tileList[tilePos], pos)
        
        
    
    # aplica a gravidade no objeto
    # param: gameObject - Um objeto do tipo GameObject para a posicao ser alterada de acordo com a gravidade    
    def applyGravity(self, gameObject):
        gameObject.move(self.gravity)
    
    # aplica a colisao do objeto com o mapa
    # param: gameObject - um objeto do tipo GameObject para vericiar a colisao
    def applyCollision(self, gameObject):        
        # deslocamento no eixo x
        dx = gameObject.position.x - gameObject.previousPosition.x
        # deslocamento no eixo y
        dy = gameObject.position.y - gameObject.previousPosition.y
        if dx != 0:
            self.validateDx(dx, gameObject, gameObject.previousPosition.y)
        if dy != 0:
            # o previousPositionX agora eh o x do gameObject, ja que ele mudou na validacao do eixo x (caso nao tenha mudado nao fara diferenca)
            self.validateDy(dy, gameObject, gameObject.position.x)
    
    # verifica a colisao no eixo x e ajusta o objeto de acordo
    # param: dx - um int que representa o deslocamento no eixo x
    # param: gameObject - um objeto do tipo GameObject para vericiar a colisao
    # param: previousPositionY - um int com a posicao anterior do objeto no eixo y
    def validateDx(self, dx, gameObject, previousPositionY):
        row_ = (previousPositionY + gameObject.nonHitArea[1]) / self.tileHeight
        col_ = (gameObject.position.x + gameObject.nonHitArea[0]) / self.tileWidth
        endRow = (previousPositionY + gameObject.size.y - gameObject.nonHitArea[3]) / self.tileHeight
        endCol = (gameObject.position.x + gameObject.size.x - gameObject.nonHitArea[2]) / self.tileWidth
        
        for row in range(row_, endRow + 1):
            for col in range(col_, endCol + 1):
                # verifica se nao esta fora de indice
                if row >= 0 and col >= 0 and row < self.mapDic['mh'] and col < self.mapDic['mw']:
                    # o valor do tile, o numero que indica aquele tile
                    tileNum = self.mapDic['tl'][row][col]
                    # verifica se eh um tile que pode ser colidido
                    if self.canCollide(tileNum):
                        blockPosX = col * self.tileWidth
                        blockPosY = row * self.tileHeight
                        # posicao do gameObject, mantendo o eixo y
                        goPos = gameObject.position.x, previousPositionY
                        # Rect do gameObject, mantendo o eixo y
                        goRect = gameObject.getHitBox(goPos)
                        # Rect do bloco do mapa
                        blockRect = pygame.Rect(blockPosX, blockPosY, self.tileWidth, self.tileHeight)
                        # verifica se o gameObject colide com o bloco do mapa
                        if goRect.colliderect(blockRect):
                            if dx > 0:
                                # se deslocou para a direita e colidiu, volta o personagem para esquerda
                                gameObject.position.x = blockPosX - gameObject.size.x + gameObject.nonHitArea[2]
                            elif dx < 0:
                                # se deslocou para a esquerda e colidiu, volta o personagem para direita
                                gameObject.position.x = blockPosX + self.tileWidth - gameObject.nonHitArea[0]
                            return
    
    # verifica a colisao no eixo y e ajusta o objeto de acordo
    # param: dy - um int que representa o deslocamento no eixo y
    # param: gameObject - um objeto do tipo GameObject para vericiar a colisao
    # param: previousPositionX - um int com a posicao anterior do objeto no eixo x 
    def validateDy(self, dy, gameObject, previousPositionX):
        row_ = (gameObject.position.y + gameObject.nonHitArea[1]) / self.tileHeight
        col_ = (previousPositionX + gameObject.nonHitArea[0]) / self.tileWidth
        endRow = (gameObject.position.y + gameObject.size.y - gameObject.nonHitArea[3]) / self.tileHeight
        endCol = (previousPositionX + gameObject.size.x - gameObject.nonHitArea[2]) / self.tileWidth
        
        for row in range(row_, endRow + 1):
            for col in range(col_, endCol + 1):
                # verifica se nao esta fora de indice
                if row >= 0 and col >= 0 and row < self.mapDic['mh'] and col < self.mapDic['mw']:
                    # o valor do tile, o numero que indica aquele tile
                    tileNum = self.mapDic['tl'][row][col]
                    # verifica se eh um tile que pode ser colidido
                    if self.canCollide(tileNum):
                        blockPosX = col * self.tileWidth
                        blockPosY = row * self.tileHeight
                        # posicao do gameObject, mantendo o eixo y
                        goPos = previousPositionX, gameObject.position.y
                        # Rect do gameObject, mantendo o eixo y
                        goRect = gameObject.getHitBox(goPos)
                        # Rect do bloco do mapa
                        blockRect = pygame.Rect(blockPosX, blockPosY, self.tileWidth, self.tileHeight)
                        # verifica se o gameObject colide com o bloco do mapa
                        if goRect.colliderect(blockRect):
                            if dy > 0:
                                # se deslocou para baixo e colidiu, volta o personagem para cima
                                gameObject.position.y = blockPosY - gameObject.size.y + gameObject.nonHitArea[3]
                            elif dy < 0:
                                # se deslocou para cima e colidiu, volta o personagem para baixo
                                gameObject.position.y = blockPosY + self.tileHeight - gameObject.nonHitArea[1]
                            return
    
    # verifica se um tile com o indice 'tileNum' eh um tile que pode ser colidido
    # param: tileNum - um inteiro indicando o indice do tile
    def canCollide(self, tileNum):
        # verifica se o tileNum esta no intervalo [1, ultimaPosicaoColidivel]
        if tileNum > 0 and tileNum <= self.mapDic['ct']:
            return True
        else:
            return False
    
    # veficica se dois gameObjects colidiram
    # param: gameObject1 e gameobject2 - dois GameObjects
    # return: retorna se os dois GameObjects se colidiram
    def gameObjectsCollided(self, gameObject1, gameObject2):
        go1Rect = gameObject1.getHitBox()
        go2Rect = gameObject2.getHitBox()
        if go1Rect.colliderect(go2Rect):
            return True
        else:
            return False
    
    # verifica se um gameObject se colidiu com balas
    # param: gameObject - um GameObject para testar a colisao com as balas
    # param: ammunition - uma lista com as balas
    # return: retorna um boolean indicando se ouve ou nao a colisao
    def gameObjectAndBulletsCollided(self, gameObject, ammunition):
        ammoToRemove = []
        collided = False
        for ammo in ammunition:
            bullet = ammo[0].t()
            goRect = gameObject.getHitBox()
            if goRect.collidepoint(bullet):
                collided = True
                ammoToRemove.append(ammo)
        for ammo in ammoToRemove:
            ammunition.remove(ammo)
        return collided    
    
    # veririfa se um GameObject do Stage saiu do mapa no eixo y
    # param: gameObject - um GameObject que sera feito a verificacao
    def isOutOfStage(self, gameObject):
        if gameObject.position.y > self.stageSize.y:
            return True
        else:
            return False
    
    # adiciona o gameObject para ser removido do mapa
    # param: um gameObject para ser 'matado' (removido da lista)
    def addToKill(self, gameObject):
        self.gameObjectsToRemove.append(gameObject)
            
    # mata os GameObjects, ou seja, retira eles da lista de atualizacoes self.gameObjects
    def kill(self):
        try:
            for go in self.gameObjectsToRemove:
                self.gameObjects.remove(go)
            self.gameObjectsToRemove = []
        except ValueError:
            pass
        
    '''abstract'''
    # verifica se o jogador terminou a fase
    # return: um boolean indicando se o jogador terminou ou nao a fase
    def isFinished(self):
        if self.player.position.x > 18945: # como as duas fases tem o mesmo tamanho, as duas podem usar essa funcao
            return True
        else:
            return False


#################################################################################################################################
#################################################################################################################################


class Stage1(Stage):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        Stage.__init__(self, manager)
        # o dicionario com as informacoes do mapa
        self.mapDic = Resources.STAGE1
        # largura de um tile do mapa em pixels
        self.tileWidth = self.mapDic['tw']
        # altura de um tile do mapa em pixles
        self.tileHeight = self.mapDic['th']
        # largura do mapa em pixels
        self.stageSize.x = self.tileWidth * self.mapDic['mw']
        # altura do mapa em pixels
        self.stageSize.y = self.tileHeight * self.mapDic['mh']
        
        self.backgroundMusic = pygame.mixer.music.load("res/sound/stage1.ogg")
        pygame.mixer.music.play(-1)

        e1 = Vector2.Vector2(3970,1664), Enemy.RUNNER, False
        e2 = Vector2.Vector2(4650,1600), Enemy.SHOOTER, False
        e3 = Vector2.Vector2(6530,1152), Enemy.SHOOTER, False
        e4 = Vector2.Vector2(8385,1024), Enemy.RUNNER, False
        e5 = Vector2.Vector2(10303,1280), Enemy.SHOOTER, False
        e6 = Vector2.Vector2(11111,1280), Enemy.RUNNER, False
        e7 = Vector2.Vector2(13440,512), Enemy.SHOOTER, False
        e8 = Vector2.Vector2(17150,1280), Enemy.RUNNER, False
        e9 = Vector2.Vector2(17350,1280), Enemy.SHOOTER, False
        
        self.enemyList = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
        
        
#################################################################################################################################
#################################################################################################################################


class Stage2(Stage):
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        Stage.__init__(self, manager)
        # o dicionario com as informacoes do mapa
        self.mapDic = Resources.STAGE2
        # largura de um tile do mapa em pixels
        self.tileWidth = self.mapDic['tw']
        # altura de um tile do mapa em pixles
        self.tileHeight = self.mapDic['th']
        # largura do mapa em pixels
        self.stageSize.x = self.tileWidth * self.mapDic['mw']
        # altura do mapa em pixels
        self.stageSize.y = self.tileHeight * self.mapDic['mh']
        
        self.backgroundMusic = pygame.mixer.music.load("res/sound/stage2.ogg")
        pygame.mixer.music.play(-1)
        
        e1 = Vector2.Vector2(2085,768), Enemy.RUNNER, False
        e2 = Vector2.Vector2(2675,960), Enemy.SHOOTER, False
        e3 = Vector2.Vector2(4715,1152), Enemy.SHOOTER, False
        e4 = Vector2.Vector2(6120,1408), Enemy.RUNNER, False
        e5 = Vector2.Vector2(6245,1408), Enemy.RUNNER, False
        e6 = Vector2.Vector2(6695,1408), Enemy.RUNNER, False
        e7 = Vector2.Vector2(7250,1408), Enemy.SHOOTER, False
        e8 = Vector2.Vector2(4820,1280), Enemy.RUNNER, True
        e9 = Vector2.Vector2(8760,1920), Enemy.SHOOTER, False
        e10 = Vector2.Vector2(9510,1920), Enemy.RUNNER, False
        e11 = Vector2.Vector2(9780,1920), Enemy.SHOOTER, False
        e12 = Vector2.Vector2(9915,1920), Enemy.RUNNER, False
        e13 = Vector2.Vector2(10160,1920), Enemy.SHOOTER, False
        e14 = Vector2.Vector2(10600,1920), Enemy.RUNNER, False
        e15 = Vector2.Vector2(10740,1920), Enemy.SHOOTER, False
        e16 = Vector2.Vector2(10870,1920), Enemy.SHOOTER, False
        e17 = Vector2.Vector2(9720,1920), Enemy.RUNNER, True
        e18 = Vector2.Vector2(11240,1920), Enemy.RUNNER, False
        e19 = Vector2.Vector2(11685,1920), Enemy.RUNNER, False
        e20 = Vector2.Vector2(11968,1920), Enemy.RUNNER, False
        e21 = Vector2.Vector2(12070,1920), Enemy.SHOOTER, False
        e22 = Vector2.Vector2(10570,1920), Enemy.RUNNER, True
        e23 = Vector2.Vector2(12330,1920), Enemy.RUNNER, False
        e24 = Vector2.Vector2(11010,1920), Enemy.RUNNER, True
        e25 = Vector2.Vector2(13720,1600), Enemy.SHOOTER, False
        e26 = Vector2.Vector2(14910,1728), Enemy.SHOOTER, False
        e27 = Vector2.Vector2(15275,1536), Enemy.SHOOTER, False
        e28 = Vector2.Vector2(15599,1728), Enemy.RUNNER, False
        e29 = Vector2.Vector2(15740,1536), Enemy.SHOOTER, False
        e30 = Vector2.Vector2(16320,1024), Enemy.SHOOTER, False
        e31 = Vector2.Vector2(16685,1216), Enemy.RUNNER, False
        e32 = Vector2.Vector2(16895,1024), Enemy.SHOOTER, False
        e33 = Vector2.Vector2(17195,1024), Enemy.RUNNER, False
        
        self.enemyList = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24, e25, e26, e27, e28, e29, e30, e31, e32, e33]