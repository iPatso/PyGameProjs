import pygame, os




WINDOW_SIZE = (800,400)

def textFont(text, color, size, font):
    fonty = pygame.font.Font((os.path.join('data',font)),size)
    return fonty.render(text, 1, color)

def showGrid(screen):
    pygame.draw.line(screen, (255,255,255), (screen.get_width()/2,0),(screen.get_width()/2,screen.get_height()))
    pygame.draw.line(screen, (255,255,255), (0, screen.get_height()/2),(screen.get_width(), screen.get_height()/2))

