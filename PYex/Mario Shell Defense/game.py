import random, os, time, pygame, time
from pygame.locals import *
from gameUtils import loadSoundFile, loadImage
from gameSprites import Mario, Fireball, Shell, PowBlock
from config import *

# ----------------------------------------------------

def gameOver():

    global background, background_orig, score, gameoverFX, clock

    gameoverFX.play()

    font = pygame.font.Font(None, 36)
    caption = font.render("Game over...", True, TEXT_COLOR)
    captionpos = caption.get_rect(centerx = background.get_width() / 2, centery = background.get_height()/3)
    scoreline = font.render("Final score: " + str(mario.score), True, TEXT_COLOR)
    scorepos = scoreline.get_rect( midtop = captionpos.midbottom )
    
    background.blit(background_orig, (0,0))
    background.blit(caption, captionpos)
    background.blit(scoreline, scorepos)
    screen.blit(background, (0,0))
    
    counter = 0
    while counter <= 6 * FRAMERATE:  #wait 6 seconds
        clock.tick(FRAMERATE)
        pygame.display.flip()
        counter += 1
        for event in pygame.event.get():
            pass
        
def fadeInOut():

    global clock, background, background_orig
    
    pygame.mixer.music.stop()
    
    ranDown = range(0,255,10)
    ranUp = range(0,255,10)
    ranUp.reverse()
    
    for x in ranDown:
        sur = pygame.Surface(screen.get_size())
        sur.fill((x,x,x))
        background.blit(background_orig, (0,0))
        #background.blit( sur, (0,0), special_flags = BLEND_SUB )
        background.blit( sur, (0,0))
        screen.blit(background, (0,0))
        pygame.display.flip()
        
        clock.tick(120)
    
    for x in ranUp:
        sur = pygame.Surface(screen.get_size())
        sur.fill((x,x,x))
        background.blit(background_orig, (0,0))
        #background.blit( sur, (0,0), special_flags = BLEND_SUB )
        background.blit( sur, (0,0))
        screen.blit(background, (0,0))
        pygame.display.flip()
        
        clock.tick(120)
        
def checkEnemy( counter ):

    counter -= 1
    
    if counter == 0:
        counter = random.choice(ENEMY_TICKS)
        start_pos = ( random.choice(ENEMY_X_POS), random.choice(ENEMY_Y_POS) )
        ENEMIES.add( Shell(screen, start_pos) )
        
    return counter
    
def renderStats():

    FONT = pygame.font.Font(None, 36)

    caption = FONT.render("It's a-me, Mario!", True, TEXT_COLOR)
    captionpos = caption.get_rect(centerx = background.get_width() / 4)
    fb = FONT.render("Fireballs: " + str(Fireball.total_count), True, TEXT_COLOR)
    fbpos = fb.get_rect(centerx = (background.get_width() / 5) * 4,)
    jump = FONT.render("Jumps: " + str(mario.jump_count), True, TEXT_COLOR)
    jumppos = jump.get_rect( midtop = fbpos.midbottom )
    scoreline = FONT.render("Score: " + str(mario.score), True, TEXT_COLOR)
    scorepos = scoreline.get_rect( midtop = jumppos.midbottom )
    
    background.blit(background_orig, (0,0))
    background.blit(caption, captionpos)
    background.blit(fb, fbpos)
    background.blit(jump, jumppos)
    background.blit(scoreline, scorepos)
    
    screen.blit(background, (0,0))
    
def init():

    global screen, clock, gameoverFX, hitFX, background, background_orig, mario

    # initialize main pygame stuff
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.mixer.pre_init() #default buffer size is 4096, causes a small delay when asking for a sound to play
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( SCREEN_SIZE )
    pygame.display.set_caption("Mario Shell Defense")
        
    # load sounds
    gameoverFX = loadSoundFile("gameover.wav")
    hitFX = loadSoundFile("hit.wav")
    
    # load music
    if pygame.mixer:
        pygame.mixer.music.load( BG_MUSIC )
    
    # set up background
    #background = pygame.Surface(screen.get_size()).convert()
    #background.fill((255,255,255))
    bg, rect = loadImage("background.jpg")
    background_orig = pygame.transform.scale2x(bg).convert()
    background = pygame.transform.scale2x(bg).convert()
    
    BLOCKS.add( PowBlock((250,390)) )
    BLOCKS.add( PowBlock((250+34,390)) )
    BLOCKS.add( PowBlock((250+34+34,390)) )
    BLOCKS.add( PowBlock((250+34+34+34,390)) )

    # set up sprites
    mario = Mario(screen)
    HERO.add( mario )
    
    if pygame.mixer:
        pygame.mixer.music.play(-1)
    
# ----------------------------------------------------

def main():

    init()
    enemycounter = 150
    playing = True
    # main game loop
    
    while playing:
    
        clock.tick(FRAMERATE)
        
        enemycounter = checkEnemy( enemycounter )
        
        renderStats()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return				
                
        HERO.update()
        FIREBALLS.update()
        ENEMIES.update()
        BLOCKS.update()
        
        for hit in pygame.sprite.groupcollide( ENEMIES, FIREBALLS, True, True):
            hitFX.play()
            mario.score += 1

        if mario.isDead:
            fadeInOut()
            gameOver()
            playing = False
        
        HERO.clear( screen, background )
        FIREBALLS.clear( screen, background )
        ENEMIES.clear( screen, background )
        BLOCKS.clear( screen, background )
        
        HERO.draw(screen)
        FIREBALLS.draw(screen)
        ENEMIES.draw(screen)
        BLOCKS.draw(screen)
        
        pygame.display.flip()

# ----------------------------------------------------

if __name__ == "__main__":
    
    main()
    pygame.quit()
