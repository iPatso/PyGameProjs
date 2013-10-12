import Player, Enemy

class Factory:
    # param: manager - instancia do ScreenManager
    def __init__(self, manager):
        self.screenManager = manager
        
    # retorna um player
    # return: um objeto Player
    def getPlayer(self):
        return Player.Player(self.screenManager)
        
    # retorna um novo inimigo
    # param: stage - um objeto Stage, que eh a fase que o inimigo sera adicionado
    # param: position - um Vector2 com a posicao no mapa que o inimigo sera criado
    # param: enemyType - uma String com o tipo do inimigo
    # param: direction - um boolean indicando a direcao do inimigo
    # return: um objeto Enemy
    def getEnemy(self, stage, position, enemyType, direction):
        enemy = None
        if enemyType == Enemy.RUNNER:
            enemy = Enemy.LumberjackEnemy(self.screenManager, stage)
            if direction:
                enemy.velocity.x *= -1
        elif enemyType == Enemy.SHOOTER:
            enemy = Enemy.HunterEnemy(self.screenManager, stage)
        
        enemy.position = position.copy()
        enemy.directionX = direction
        
        return enemy