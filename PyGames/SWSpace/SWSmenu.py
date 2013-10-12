import pygame, os, sys
from pygame.locals import *
import CONST
from CONST import *

clock = pygame.time.Clock()

LIGHT_GREY = (200,200,200)
DARK_GREY = (150,150,150)
DARK_ORANGE = (230,50,18) # originally: DARK_YELLOW = (247,200,20)



class Menu():
    def __init__(self):
        self.bg_image = pygame.image.load(os.path.join("data","title_background(800x400).jpg")).convert()
        self.logo = pygame.image.load(os.path.join("data","star_wars_logo.png")).convert_alpha()
        self.subLogo = textFont("SPACE BATTLES", LIGHT_GREY, 24, "Coalition.ttf")
        self.selection = 0;
        self.optionsSelections = 0

    def titleMenu(self, screen):
        """
        Does all menu commands/selections.
        Calls most commands in this function
        """
        isInOptions = False
        isInMenu = True

        while isInMenu:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and not isInOptions:
                    if event.key == K_UP:           #Menu Selections
                        self.selection -= 1
                        if self.selection == -1:
                            self.selection = 2
                    elif event.key == K_DOWN:
                        self.selection +=1
                        if self.selection == 3:
                            self.selection = 0
                    elif event.key == K_SPACE:      #Menu >> SPACE(bar) conditions
                        if self.selection == 0:         #START - INCOMPLETE!!
                            print "STARTing game.."
                            isInMenu = False
                        elif self.selection == 1:       #OPTIONS
                            isInOptions = True
                        else:
                            pygame.quit()
                            sys.exit()
                elif event.type == KEYDOWN and isInOptions:
                    if event.key == K_UP:           #OPTIONS Selections
                        self.optionsSelections -= 1
                        if self.optionsSelections == -1:
                            self.optionsSelections = 2
                    elif event.key == K_DOWN:
                        self.optionsSelections +=1
                        if self.optionsSelections == 3:
                            self.optionsSelections = 0
                    elif event.key == K_SPACE:      #Options >> SPACE(bar) conditions
                        if self.optionsSelections == 0:         #Music toggle
                            print "Music toggled.."
                        elif self.optionsSelections == 1:       #Sound fx toggle
                            print "Sound FX toggled.."
                        else:
                            isInOptions = False
                            self.optionsSelections = 0
                            
            
            screen.blit(self.bg_image, (0,0))                   #Background
            self.mainLogoAnimation(screen)                      #STARWARS
            self.subLogoAnimation(screen)                       #SPACE BATTLES
            self.showSelections(screen, self.selection)         #Selections
            if isInOptions:
                self.showOptions(screen, self.optionsSelections)


            #showGrid(screen)
            pygame.display.update()

#TODO        
    def mainLogoAnimation(self, screen):
        #Just scale the image up (tiny to big)
        logo_pos = self.logo.get_rect(centerx=screen.get_width()/2)
        screen.blit(self.logo, (logo_pos[0],0))              #NOTE: Final position is 10, 0

#TODO
    def subLogoAnimation(self, screen):
        subLogo_pos = self.subLogo.get_rect(centerx=screen.get_width()/2)
        screen.blit(self.subLogo, (subLogo_pos[0], 190))
        
    def showSelections(self, screen, selection):
        #Start, Options, Exit
        colors = [DARK_GREY,DARK_GREY,DARK_GREY]
        colors[selection] = DARK_ORANGE
        START = textFont("START", colors[0], 20, "Basica.ttf")
        OPTIONS = textFont("OPTIONS", colors[1], 20, "Basica.ttf")
        EXIT = textFont("EXIT", colors[2], 20, "Basica.ttf")

        START_pos = START.get_rect(centerx=screen.get_width()/2)
        OPTIONS_pos = OPTIONS.get_rect(centerx=screen.get_width()/2)
        EXIT_pos = EXIT.get_rect(centerx=screen.get_width()/2)

        screen.blit(START, (START_pos[0], 260))
        screen.blit(OPTIONS, (OPTIONS_pos[0], 280))
        screen.blit(EXIT, (EXIT_pos[0], 300))

    def showOptions(self, screen, optionsSelections):
        """
        Toggles the music and sound fx.
        MUST make toggles do what they must
        """
        colors = [DARK_GREY,DARK_GREY, DARK_GREY]
        colors[optionsSelections] = DARK_ORANGE
        TOGGLE_MUSIC = textFont("Music: ON", colors[0], 15, "Basica.ttf")
        TOGGLE_SOUNDFX = textFont("Sound FX: ON", colors[1], 15, "Basica.ttf")
        BACK = textFont("Back", colors[2], 15, "Basica.ttf")

        TOGGLE_MUSIC_pos = TOGGLE_MUSIC.get_rect(x=screen.get_width()/2 + 65)
        TOGGKE_SOUNDFX_pos = TOGGLE_SOUNDFX.get_rect(x=screen.get_width()/2 + 65)
        BACK_pos = BACK.get_rect(x=screen.get_width()/2 + 65)

        screen.blit(TOGGLE_MUSIC,   (TOGGLE_MUSIC_pos[0], 265))
        screen.blit(TOGGLE_SOUNDFX, (TOGGKE_SOUNDFX_pos[0], 280))
        screen.blit(BACK,           (BACK_pos[0], 300))
