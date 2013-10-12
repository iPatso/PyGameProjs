# Uma classe que representa um vetor com duas dimensoes
class Vector2:

    def __init__(self, x, y):
        # eixo x do vector2
        self.x = x
        # eixo y do vector2
        self.y = y
    
    # Soma este Vector2 com um outro
    # param: vector2 - um Vector2 para ser somado
    def add(self, vector2):
        self.x += vector2.x
        self.y += vector2.y
    
    # Subtrai este Vector2 com um outro
    # param: vector2 - um Vector2 para ser subtraido
    def sub(self, vector2):
        self.x -= vector2.x
        self.y -= vector2.y
        
    # Divide este Vector2 por um inteiro
    # param: number - um inteiro para dividir este Vector2
    def div(self, number):
        if number != 0:
            self.x /= number
            self.y /= number
    
    # Verifica se este Vector2 eh igual ao outro, ou seja, tem os mesmos valores de x e y
    # param: vector2 - uma Vector2 para ser comparado
    # return: True caso este Vector2 seja igual ao param, False caso seja diferente
    def equals(self, vector2):
        if self.x == vector2.x and self.y == vector2.y:
            return True
        else:
            return False
    
    # return: uma nova instancia deste objeto
    def copy(self):
        x1 = self.x
        y1 = self.y
        return Vector2(x1, y1)
    
    # return: uma tupla de dois elementos x,y
    def t(self):
        return (self.x, self.y)