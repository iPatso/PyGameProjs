import CONST
from CONST import *

clock = pygame.time.Clock()

class Menu():
    def __init__(self):
        self.bg_image = pygame.image.load(os.path.join("data","title1.png")).convert_alpha()
        self.subLogo = textFont("Initial Fantasy: Glitch", BLACK, 36, "Coalition.ttf")
        self.selection = 0;
        self.optionsSelections = 0

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
