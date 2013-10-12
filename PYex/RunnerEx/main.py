# Shifter will be a strictly 2-dimensional game. It will have a start menu when first loaded,
# music, sounds, and graphics.

import pygame
from pygame import *
import CONST
from CONST import *
import random

screen = display.set_mode(WINSIZE)
clock = pygame.time.Clock()
caption("SHIFTER")
pygame.font.init()
#=============
#=============
# Sound things
if(checkfile("284253_BLIPPBLIPP.mp3")):
    musiclode("284253_BLIPPBLIPP.mp3")
bloop   = FXLODE("selectL.wav")
blip    = FXLODE("selectM.wav")
bleep   = FXLODE("selectH.wav")
bomb    = FXLODE("Blast.wav")
bomb1   = FXLODE("blast2.wav")
bomb2   = FXLODE("blast3.wav")
pulse   = FXLODE("deeppulse.wav")
laser   = FXLODE("laser.wav")
jet     = FXLODE("JET.wav")
deflect = FXLODE("blast1.wav",0.7)
siren   = FXLODE("warning2.wav")
goof    = FXLODE("warning.wav")
damage  = FXLODE("damage.wav")
attention = FXLODE("attention.wav")
ready1  = FXLODE("ready.wav",1)
ready2rock  = FXLODE("ready2.wav",1)
textblip    = FXLODE("textblit.wav")
powerup = FXLODE("ufo.wav")
charge  = FXLODE("ufo2.wav")
powerup = FXLODE("powerup1.wav")
die     = FXLODE("die.wav")
slice  = FXLODE("slice.wav")
bladekill   = FXLODE("bladekill.wav")
spinblade   = FXLODE("spinblade.wav")
bigblade    = FXLODE("bigblader.wav")
bigblast    = FXLODE("bigblast.wav")
roar    = FXLODE("roar.wav")
transform   = FXLODE("transform.wav")
bigcharge   = FXLODE("charging.wav")
slowcharge  = FXLODE("slow evil charge.wav")
opticcharge = FXLODE("opticcharge.wav")
opticblast  = FXLODE("opticblast.wav")
hammersmash = FXLODE("hammersmash.wav",0.7)
hammerspawn = FXLODE("hammerspawn.wav",1)
genspawn    = FXLODE("genspawn.wav")
invis   = FXLODE("invis.wav",1)
rush    = FXLODE("rush.wav")
shiny   = FXLODE("shiny.wav")
supershift  = FXLODE("supershift.wav")
BOOM    = FXLODE("cineboom.wav")

pygame.mixer.music.set_volume(0.5)

soundstatus = True
musicstatus = True

# The ground you run on
erection = pygame.Surface((WINSIZE[0],WINSIZE[1]))
erectpos = (WINSIZE[0],0)
erection.fill(BLACK)

# The stars in the back
Stars = pygame.sprite.Group()
Starinterval = 6
MAXSTARS = 20
STARSPEED = 20
STARSIZE = (4,4)
MAXSPEED = 60

# Some dots
DOTZ = pygame.sprite.Group()
# Some explosions
BLASTS = pygame.sprite.Group()
SHIELDS = pygame.sprite.Group()
# Some gens
GENES = pygame.sprite.Group()
# Some walls
walmart     = pygame.sprite.Group()
blastmart   = pygame.sprite.Group()
powermart   = pygame.sprite.Group()
spinmart    = pygame.sprite.Group()
#TESTING=============
invincible = False
startlevel = 1
superpowered = False
bossdead = False
currentsong = ""
#====================
class Maine:
    def __init__(self):
        self.running = 1
        self.INTRO()
        
    def INTRO(self):
        # Text Info
        Texty = texty("REDENSEK.TTF",20)
        firstpart   = Texty.render("STATICA PRESENTS",0,BLACK)
        secondpart  = Texty.render("THE THIRD GAME BY MICHAEL AREVALO",0,BLACK)
        thirdpart   = Texty.render("WITH MUSIC BY MAJS",0,RED)

        scripty = 0
        timer = 0
        if(checkfile("284253_BLIPPBLIPP.mp3")):
            musicplay(musicstatus)
        eventimer = 0
        
        erection = pygame.Surface((WINSIZE[0],WINSIZE[1]))
        erectpos = (WINSIZE[0],0)
        erection.fill(BLACK)
        
        checkok = 0
        
        while self.running:
            clock.tick(FPS)
            screen.fill(RED)
            eventimer+=1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0
                elif event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        self.MENU()
                    if (event.key == K_SPACE):
                        self.MENU()
            
            if (scripty == 0):
                if (eventimer != 120):
                    screen.blit(firstpart,(50,240))
                    if (erectpos[0] > 490):
                        erectpos = (erectpos[0]-4,erectpos[1])
                else:
                    print "first transition"
                    scripty = 1
            elif(scripty == 1):
                if (erectpos[1] > -330):
                    erectpos = (erectpos[0],erectpos[1]-20)
                else:
                    scripty = 2
            elif(scripty == 2):
                if (eventimer != 300):
                    if (erectpos[0] != 0):
                        erectpos = (erectpos[0]-8,erectpos[1])
                    else:
                        screen.blit(secondpart,(320,400))
                else:
                    print "second transition"
                    scripty = 3
                    checkok = 1
            elif(scripty == 3):
                if (timer < 200):
                    if (erectpos[1] != 0):
                        erectpos = (0,erectpos[1]+5)
                    timer+=1
                else:
                    scripty = 4
            elif(scripty == 4):
                if (eventimer != 600):
                    if (erectpos[1] < 420):
                        erectpos = (0, erectpos[1]+5)
                else:
                    print "final transition"
                    self.MENU()
            
            screen.blit(erection,erectpos)
            if (checkok):
                screen.blit(thirdpart,(240,240))
            display.flip()
        
    def MENU(self):
        Bigtex = texty("REDENSEK.TTF",60) #large text
        TITLE   = Bigtex.render("SHIFTER",0,BLACK)
        titlepos = (20,30)
        
        selection = 0
        if superpowered:
            START = TEXT("[START]+",BLACK,(535,360),1.5)
        else:
            START = TEXT("START",BLACK,(535,360),1.5)
        OPTIONS = TEXT("OPTIONS",BLACK,(520,380),1.5)
        EXIT = TEXT("EXIT",BLACK,(520,400),1.5)
        movethem = 0
        
        timer = 0
        startimer = 0
        box1 = (18,48)
        box2 = (185,35)
        boxrect = pygame.Rect(box1,box2)
        erectpos = (0,420)
        
        submenu = False
        subselect = 0
        
        global soundstatus
        global musicstatus

        SUB1 = TEXT("SOUND: ON",BLACK,(640,320))
        SUB2 = TEXT("MUSIC: ON",BLACK,(640,340))

        newthing = 0
        playgame = 0
        shifter = 0
        selectok = 0
        lightspeed = (5,0.5)
        tp = 0.7
        
        color = BLACK
        changingmodes = False
        changed = 0
        fader = FADED(0)
        faderok = 0
        #some cleanup
        for final in finals:
            final.kill()
        while self.running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_ESCAPE)and not changingmodes):
                        if (selection == -1): 
                            fxplay(blip,soundstatus)
                            subselect = 0
                            selection = 1
                            selectok = 1
                            TEXT.move(SUB1,640,20)
                            TEXT.move(SUB2,640,20)
                            lightspeed = (20,tp)
                    if ((event.key == K_UP)and not changingmodes):
                        selectok = 1
                        fxplay(bloop,soundstatus)
                        if (selection == -1):
                            if (subselect == 1):
                                subselect = 2
                            else: subselect = 1
                        elif (selection == 0):
                            selection = 2
                        else:
                            selection -= 1
                    if ((event.key == K_DOWN)and not changingmodes):
                        selectok = 1
                        fxplay(bloop,soundstatus)
                        if (selection == -1):
                            if (subselect == 2):
                                subselect = 1
                            else: subselect = 2
                        elif (selection == 2):
                            selection = 0
                        else:
                            selection += 1
                    if ((event.key == K_LEFT)and not changingmodes):
                        if (selection == -1): 
                            fxplay(blip,soundstatus)
                            subselect = 0
                            selection = 1
                            selectok = 1
                            TEXT.move(SUB1,640,20)
                            TEXT.move(SUB2,640,20)
                            lightspeed = (20,tp)
                    if ((event.key == K_RIGHT)and not changingmodes):
                        if (selection == 1):
                            fxplay(blip,soundstatus)
                            subselect = 1
                            selection = -1
                            TEXT.move(START,300,20,tp)
                            TEXT.move(OPTIONS,315,20,tp)
                            TEXT.move(EXIT,300,20,tp)
                            TEXT.move(SUB1,410,20,tp)
                            TEXT.move(SUB2,400,20,tp)
                            print "OPTIONS"
                    if ((event.key == K_RETURN)and not changingmodes):
                        if (selection == 0):
                            fxplay(bleep,soundstatus)
                            print "START"
                            if mixer.music.get_busy():
                                mixer.music.fadeout(600)
                            changingmodes = True
                        elif (selection == 1):
                            fxplay(blip,soundstatus)
                            selection = -1
                            subselect = 1
                            TEXT.move(START,300,20,tp)
                            TEXT.move(OPTIONS,315,20,tp)
                            TEXT.move(EXIT,300,20,tp)
                            TEXT.move(SUB1,410,20,tp)
                            TEXT.move(SUB2,400,20,tp)
                            print "OPTIONS"
                        elif (selection == 2):
                            print "EXIT"
                            self.running = 0
                        elif (selection == 3):
                            fxplay(bleep,soundstatus)
                        elif (subselect == 1):
                            if(soundstatus == True):
                                TEXT.changetext(SUB1, "SOUND: OFF")
                                soundstatus = False
                            else: 
                                TEXT.changetext(SUB1, "SOUND: ON")
                                soundstatus = True
                        elif (subselect == 2):
                            if(musicstatus == True):
                                mixer.music.set_volume(0.0)
                                TEXT.changetext(SUB2, "MUSIC: OFF")
                                musicstatus = False
                            else: 
                                mixer.music.set_volume(0.5)
                                TEXT.changetext(SUB2, "MUSIC: ON")
                                musicstatus = True
                            
                            
            if selectok:
                if (selection == 0):
                    TEXT.move(START,535)
                    TEXT.move(OPTIONS,520)
                    TEXT.move(EXIT,520)
                elif (selection == 1):
                    TEXT.move(START,520,lightspeed[0],lightspeed[1])
                    TEXT.move(OPTIONS,535,lightspeed[0],lightspeed[1])
                    TEXT.move(EXIT,520,lightspeed[0],lightspeed[1])
                    lightspeed = (5,0.5)
                elif (selection == 2):
                    TEXT.move(START,520)
                    TEXT.move(OPTIONS,520)
                    TEXT.move(EXIT,535)
                elif (subselect == 1):
                    TEXT.move(SUB1,410)
                    TEXT.move(SUB2,400)
                elif (subselect == 2):
                    TEXT.move(SUB1,400)
                    TEXT.move(SUB2,410)
                selectok = 0
                
            screen.fill(RED)
            # Title flash
            if (timer == 3):
                TITLE   = Bigtex.render("SHIFTER",0,WHITE)
                draw.rect(screen,WHITE,boxrect,2)
            elif(timer == 6):
                TITLE   = Bigtex.render("SHIFTER",0,BLACK)
                #draw.rect(screen,BLACK,boxrect,2)
                timer = 0
            timer+=1
            
            if(changingmodes):
                if(changed == 0):
                    TEXT.move(START,650,15)
                    TEXT.move(OPTIONS,650,15)
                    TEXT.move(EXIT,650,15)
                    
                if(changed < 20):
                    box1 = (18,box1[1]-5)
                    boxrect = pygame.Rect(box1,box2)
                    titlepos = (titlepos[0],titlepos[1]-5)
                else:
                    self.TUT()
                changed+=1
                    
            
            screen.blit(TITLE,titlepos)
            screen.blit(erection,erectpos)
            TEXT.update(START)
            TEXT.update(OPTIONS)
            TEXT.update(EXIT)
            TEXT.update(SUB1)
            TEXT.update(SUB2)
            
            if (len(Stars) != 0):
                Stars.update()
                
            if (startimer == Starinterval-(newthing/10)):
                startimer = 0
                if (len(Stars) < MAXSTARS):
                    if (color == BLACK): color = WHITE
                    else: color = BLACK
                    Stars.add(STARZ(-(STARSPEED+newthing),
                                    Starpos(),
                                    (STARSPEED+newthing,2),
                                    color))
            if faderok:
                if(fader.alphasz != 255):
                    fader.update()
                else:
                    self.ROLLCREDITS()
            startimer+=1
            display.flip()
            
    def TUT(self):
        startimer = 0
        color = BLACK
        mastertimer = 0
        pauser = False
        playerpos = 0
        player = pygame.Rect((50,420),(100,100))
        
        # Text Info
        Texty = texty("REDENSEK.TTF",20)
        part1 = Texty.render("WHEN PLAYING, PRESS K TO SHIFT OBJECTS",0,BLACK)
        part2 = Texty.render("YOUR RANGE IS LIMITED, SO TIME YOUR SHOTS",0,BLACK)
        part2a = Texty.render("RANGE",0,BLACK)
        part3 = Texty.render("GOOD LUCK!",0,BLACK)
        TUTORIAL = TEXT("TUTORIAL",RED,(550,430))
        
        eventz = 0
        blinky = 0
        pausetimer = 0
        while self.running:
            mastertimer+=1
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0
                elif event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        self.RESET("PLAY")
            screen.fill(RED)
            
            
            if pauser:
                pausetimer += 1
                if(eventz == 1):
                    if(pausetimer < 200):
                        screen.blit(part1,(100,50))
                    elif(pausetimer > 200):
                        pauser = False
                        pausetimer = 0
                elif(eventz == 2):
                    if(pausetimer < 200):
                        screen.blit(part2,(100,50))
                        blinky+=1
                        if(blinky < 6):
                            draw.circle(screen,BLACK,(100,400),200,2)
                        elif(blinky > 12):
                            blinky = 0
                            draw.circle(screen,RED,(100,400),200,2)
                    elif(pausetimer > 200):
                        pauser = False
                        pausetimer = 0
                elif(eventz == 3):
                    if(pausetimer < 200):
                        screen.blit(part3,(100,50))
                    elif(pausetimer > 200):
                        pauser = False
                        pausetimer = 0
                        
                
            else:
                Stars.update()
                BLASTS.update()
                TEXT.update(TUTORIAL)
                
                #STAR SHIT
                if (startimer == Starinterval):
                    startimer = 0
                    if (len(Stars) < MAXSTARS):
                        if (color == BLACK): color = WHITE
                        else: color = BLACK
                        Stars.add(STARZ(-(STARSPEED),
                                        Starpos(),
                                        (STARSPEED,2),
                                        color))
                        
                startimer+=1
                
                #scripted events
                if(mastertimer > 200):
                    pauser = True
                    eventz += 1
                    fxplay(textblip,soundstatus)
                    mastertimer = 0
                    if(eventz == 4):
                        print "PLAY BALL"
                        self.PLAY()
            
            bar.update()
            player = pygame.Rect((50,bar.ypos-playerpos+1),(100,102))
            draw.rect(screen,BLACK,player)
            
            if(playerpos < 100):
                playerpos += 2
            elif(playerpos == 100):
                playerpos+=1
                fxplay(damage,soundstatus)
                for xrange in (20,40,60,80):
                    DOTZ.add(DOTS((xrange,410)))
                BLASTS.add(EXPLOSION((100,400),50,0,1))
            DOTZ.update()
                    
            display.flip()
    def PLAY(self):
        if remote.endgame:
            remote.RESET()
        
        startimer = 0
        playerb = pygame.Rect((50,320),(100,100))
        
        Texty = texty("REDENSEK.TTF",20)
        
        newthing = 0
        newtimer = 0
        walltimer = 0
        wallinterval = 100
        pauseloop = 0
        
        PAUSER      = Texty.render("PAUSED",0,RED)
        INSTRUCT    = Texty.render("PRESS X TO EXIT",0,RED)
        INSTRUCT2   = Texty.render("R FOR MAIN MENU",0,RED)
        color = BLACK
        
        #Laser stuff
        #==================
        lightfromheaven = 0
        #==================
        lightflash = 0
        lightwid = 100
        lightxpos = 50
        lightrect = pygame.Rect((50,0),(100,420))
        lightcount = 100
        timedill = 10
        ticktock = 3
        cv = 0
                    
        fader = FADED(0)
        darthfader = FADED(0,WHITE)
        finals.add(FINALLITY())
        #===============
        global bossdead
        bossdead = False
        #===============
        while self.running:
            clock.tick(FPS)
            
            
            if(newtimer < 100):
                newtimer+=1
            else:
                newtimer = 0
                if(newthing < 20):
                    newthing+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_q):
                    self.running = 0
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if(event.key == K_RSHIFT) or (event.key == K_LSHIFT):
                        if(dude.ultrapowered == True):
                            dude.ultrapowered = False
                            for boss in bawss:
                                boss.DIEBOX()
                    if ((event.key == K_k) and dude.alive):
                        dude.STRIKU()
                        for wall in walmart:
                            if superpowered and (wall.pos[0] < 500):
                                newpos = (wall.pos[0]+50,wall.pos[1]+145)
                                shocks.add(SHOCKWAVE(newpos[0]))
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                randar = random.randrange(50,80)
                                swords.add(SWORDOFLIGHT(newpos[0],newpos[1]-randar,1))
                                wall.dead(1)
                                fxplay(bomb,soundstatus)
                            elif(wall.pos[0] < 300):
                                newpos = (wall.pos[0]+50,wall.pos[1]+145)
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                wall.dead(1)
                                fxplay(bomb,soundstatus)
                        for wall in blastmart:
                            if superpowered and (wall.pos[0] < 500):
                                newpos = (wall.pos[0],wall.pos[1]+145)
                                shocks.add(SHOCKWAVE(newpos[0]))
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                randar = random.randrange(50,80)
                                swords.add(SWORDOFLIGHT(newpos[0],newpos[1]-randar,1))
                                wall.dead(1)
                            elif(wall.pos[0] < 300):
                                newpos = (wall.pos[0],wall.pos[1]+145)
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                wall.pushback()
                        for wall in spinmart:
                            newrand = random.randrange(0,4)
                            if superpowered and (wall.pos[0] < 500):
                                newpos = (wall.pos[0],wall.pos[1]+55)
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                shocks.add(SHOCKWAVE(newpos[0]))
                                if(newrand == 0):
                                    wall.REFLECT()
                                else:
                                    BLASTS.add(EXPLOSION(newpos,50,0,1,BLACK)) 
                                    wall.dead()
                            elif(wall.pos[0] < 400):
                                newpos = (wall.pos[0],wall.pos[1]+55)
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                if(newrand == 0):
                                    wall.REFLECT()
                                else:
                                    BLASTS.add(EXPLOSION(newpos,50,0,1,BLACK)) 
                                    wall.dead()
                        for gen in bawls:
                            if not gen.initiate and superpowered and gen.eyeflash:
                                gen.damage(1)
                                newpos = (gen.pos[0],gen.pos[1])
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                randar = random.randrange(0,50)
                                swords.add(SWORDOFLIGHT(newpos[0]-80,newpos[1]-randar,1))
                                shocks.add(SHOCKWAVE(newpos[0]))
                        for ball in balls:
                            if(ball.pos[0] < 200):
                                fxplay(bomb1,soundstatus)
                                ball.tag()
                        for baws in bawss:
                            if(baws.attacktype == 2)and(baws.atktmr > 0):
                                ypwn = random.randrange(-40,40)
                                newpos = (baws.pos[0]+70,baws.pos[1]+128+ypwn)
                                BLASTS.add(EXPLOSION(newpos,60,0,1,BLACK))
                                swords.add(SWORDOFLIGHT(newpos[0]-80,newpos[1]-50,1))
                                baws.damage(0.2)
                                for lasic in lazor:
                                    lasic.xpos += 30
                            if(baws.pos[0] < 265) and (baws.attacktype == 4):
                                baws.damage(1)
                                fxplay(bomb1,soundstatus)
                                fxplay(bomb2,soundstatus)
                                baws.flash = True
                                newpos = (baws.pos[0]+70,baws.pos[1]+128)
                                BLASTS.add(EXPLOSION(newpos,20,0,1,BLACK))
                                randar = random.randrange(40,80)
                                swords.add(SWORDOFLIGHT(newpos[0],newpos[1]-randar,1))
                                baws.moveamount = -40
                        for turd in littleshit:
                            turd.shake()
                            newpos = (turd.pos[0],turd.pos[1]-40)
                            randar = random.randrange(-10,10)
                            swords.add(SWORDOFLIGHT(newpos[0]-50,newpos[1]+randar,1))
                    #==========================
                    if ((event.key == K_j)):
                        print remote.MasterTimer/30
                        #powermart.add(POWERBALL())
                    #==========================
                    if ((event.key == K_x)):
                        if pauseloop:
                            self.running = 0
                    if ((event.key == K_ESCAPE) or 
                    (event.key == K_p)):
                        # PAUSE MENU
                        if(pauseloop == 0):
                            pauseloop = 1
                        elif(pauseloop == 1):
                            mixer.music.unpause()
                            mixer.unpause()
                            pauseloop = 0
                    if (event.key == K_r):
                        if pauseloop: 
                            self.RESET()
                            
            #CHECK TO SEE IF THE GAME IS UNFOCUSED:
            if not pygame.display.get_active():
                # PAUSE MENU
                if(pauseloop == 0):
                    pauseloop = 1
                    
            if (pauseloop == 0):
                screen.fill(RED)
                if (len(Stars) != 0):
                    Stars.update()
                
                if (startimer == Starinterval-(newthing/10)):
                    startimer = 0
                    if (len(Stars) < MAXSTARS):
                        if (color == BLACK): color = WHITE
                        else: color = BLACK
                        Stars.add(STARZ(-(STARSPEED+newthing),
                                    Starpos(),
                                    (STARSPEED+newthing,2),
                                    color))
                startimer+=1
            
                SHIELDS.update()
                BLASTS.update()
                dude.update(bar.ypos)
                powermart.update()
                balls.update()
                lazor.update()
                waves.update()
                bar.update()
                spinmart.update()
                bawls.update()
                swords.update()
                bawss.update()
                gdamnhammers.update(bar.ypos)
                shocks.update(bar.ypos)
                littleshit.update()
                
                if bossdead:
                    for final in finals:
                        if(final.color > 200):
                            darthfader.update()
                            if(darthfader.alphasz == 255):
                                global RED
                                RED = (255,0,0)
                                self.PLANETBLAST()
                    finals.update()
                
                for item in walmart:
                    for thing in BLASTS:
                        if (item.rect.colliderect(thing.rect)and
                        thing.pain):
                            item.dead(0)
                    if (item.pos[0] < 70):
                        item.dead(0)
                        screen.fill(WHITE)
                        dude.DAMAGE()
                DOTZ.update()
                
                GENES.update()
                if dude.alive:
                    walmart.update((STARSPEED),(bar.ypos-420))
                    blastmart.update((bar.ypos-420))
                    remote.update()
                alarm.update()
                
                #INTRODUCTION
                if (lightfromheaven == 0):
                    draw.rect(screen,BLACK,playerb)
                    if(lightcount == 0):
                        fxplay(charge,soundstatus)
                        lightfromheaven = 1
                    else:
                        lightcount -= 1
                if (lightfromheaven == 1):
                    if(lightwid > 0):
                        lightwid -= 01
                        lightxpos+=0.5
                        lightrect = pygame.Rect((lightxpos,0),(lightwid,420))
                    else:
                        lightfromheaven = 2
                        lightflash = 0
                    
                    newcolor = (cv,cv,cv)
                    if (cv < 255):
                        cv+=1
                    
                    if(lightflash == 3):
                        draw.rect(screen,WHITE,lightrect)
                    elif(lightflash == 6):
                        lightflash = 0
                    lightflash += 1
                    draw.rect(screen,newcolor,playerb)
                elif(lightfromheaven == 2):
                    charge.stop()
                    for yval in (400,380,360):
                        DOTZ.add(DOTS((100,yval)))
                    screen.fill(WHITE)
                    fxplay(pulse,soundstatus)
                    BLASTS.add(EXPLOSION((100,400),50,0,1,WHITE))
                    dude.STRIKU()
                    lightfromheaven = 3
            else:
                mixer.pause()
                mixer.music.pause()
                screen.blit(PAUSER,(550,430))
                screen.blit(INSTRUCT,(480,445))
                screen.blit(INSTRUCT2,(480,455))
            
            if remote.endgame:
                if(fader.alphasz != 255):
                    fader.update()
                else:
                    self.ROLLCREDITS()
            if not dude.alive:
                alarm.RESET()
                # Kill EVERYTHING
                for wall in walmart:
                    wall.kill()
                for wall in blastmart:
                    wall.kill()
                for shit in powermart:
                    shit.kill()
                for gen in GENES:
                    gen.kill()
                for gen in bawls:
                    gen.pause = True
                for wall in spinmart:
                    wall.kill()
            display.flip()
    def ROLLCREDITS(self):
        finallity = imglode("END","concepts",False)
        finallity2 = imglode("final copy","concepts",False)
        picalpha = 0
        picalpha2 = 0
        Texty = texty("REDENSEK.TTF",20)
        #TEXTS
        lines = []
        lines2 = []
        linesb =   ("CREDITS:",
                    "ART, CODING: MICHAEL AREVALO",
                    "PLAYTESTING, IDEA MACHINE: JAY DIHENIA",
                    "                           MATTHEW GENG",
                    "LEVEL DESIGN: ZENON CUELLAR",
                    "MORAL SUPPORT: MY GIRLFRIEND",
                    "",
                    "SPECIAL THANKS: MAJS, BJRA, AND ALL THE",
                    "MUSICIANS FROM NEWGROUNDS.COM AUDIO PORTAL",
                    "SOUNDS MADE USING SFXR WRITTEN BY:",
                    "DR PETTER",
                    "",
                    "AND YOU, THE PLAYER!")
        lines2b =  ("MADE USING PYTHON AND PYGAME",
                    "DISTRIBUTED FREE OF CHARGE AND LICENSED",
                    "UNDER GNU LESSER GENERAL PUBLIC LICENSE",
                    "",
                    "SHIFTER - COPYRIGHT (C) MICHAEL AREVALO 2010",
                    "",
                    "THANKS FOR PLAYING!")
        for line in linesb:
            lines.append(Texty.render(line,0,RED))
        for line in lines2b:
            lines2.append(Texty.render(line,0,RED))
        shiftval = 420
        if(checkfile("202672_Excellent_use_of_Magic__my.mp3")):
            musiclode("202672_Excellent_use_of_Magic__my.mp3")
            musicplay(musicstatus,1)
        while self.running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0
                elif event.type == KEYDOWN:
                    if (event.key == K_ESCAPE):
                        mixer.music.fadeout(600)
                        self.RESET()
            
            screen.fill(BLACK)
            if (picalpha < 255):
                picalpha += 1
                finallity.set_alpha(picalpha)
                screen.blit(finallity,(0,0))
            else:
                screen.blit(finallity,(0,0))
                shiftval-= 0.2
                if(shiftval > -300):
                    shiftval -= 0.1
                    for line in (1,2,3,4,5,6,7,8,9,10,11,12):
                        screen.blit(lines[line-1],(20,(line*20)+shiftval))
                else:
                    for line in (1,2,3,4,5,6,7):
                        screen.blit(lines2[line-1],(20,(line*20)-10))
                if(shiftval < -400):
                    if(picalpha2 < 255):
                        picalpha2 += 1
                        finallity2.set_alpha(picalpha2)
                    screen.blit(finallity2,(0,0))
            display.flip()
    def RESET(self,mode="MENU"):
        remote.RESET()
        alarm.RESET()
        
        # Kill EVERYTHING
        for wall in walmart:
            wall.kill()
        for gen in GENES:
            gen.kill()
        for bawl in bawls:
            bawl.kill()
        for wall in blastmart:
            wall.kill()
        for shit in powermart:
            shit.kill() #>:3
        for dot in DOTZ:
            dot.kill()
        for boss in bawss:
            boss.kill()
        if(mode == "MENU"):
            self.MENU()
        else: self.PLAY()
    def PLANETBLAST(self):
        self.endtimer = 0
        planeet = imglode("Planet.bmp")
        STARS = imglode("stars.bmp")
        planeetpos = (470,200)
        planetoffset = 0
        
        blastradius = 50
        blastwid = 0
        greenrad = 20
        greenwid = 2
        increment = 0
        
        linewidth = 10
        linepos1 = (150,0)
        linepos2 = (710,480)
        lineshow = 0
        fader = FADED(0)
        darthfader = FADED(0,WHITE)
        while self.running:
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = 0
            
            screen.fill(RED)
            screen.blit(STARS,(0,0))
            
            if((self.endtimer < 200) and 
            (self.endtimer%2 == 0) and
            (self.endtimer > 70)):
                draw.line(screen,WHITE,linepos1,linepos2,linewidth)
                planetoffset = 5
            else:
                planetoffset = 0
                
            if(self.endtimer > 60) and (self.endtimer < 70):
                screen.fill(WHITE)
                
            if(self.endtimer > 70) and (self.endtimer < 150):
                if(increment == 6):
                    greenrad+= 7
                    increment = 0
                    blastradius+=3
                    
                    if(linewidth > 0):
                        linewidth -= 1
                increment+=1
                draw.circle(screen,GREEN,(570,350),greenrad,greenwid)
                draw.circle(screen,WHITE,(570,350),blastradius,blastwid)
            if(self.endtimer > 150) and (self.endtimer%5 == 0):
                if(increment == 6):
                    greenrad+= 7
                    increment = 0
                    blastradius+=3
                increment+=1
                draw.circle(screen,BLACK,(570,350),greenrad,greenwid)
                draw.circle(screen,WHITE,(570,350),blastradius,blastwid)
            
            screen.blit(planeet,
                    (planeetpos[0],planeetpos[1]+planetoffset))
            
            if(self.endtimer > 100):
                darthfader.update()
            if(self.endtimer > 600):
                if(fader.alphasz != 255):
                    fader.update()
                else:
                    self.ROLLCREDITS()
            self.endtimer+=1
            display.flip()  
            
class STARZ(pygame.sprite.Sprite):
    def __init__(self, speed, start, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.Spd = speed
        self.Pos = start
        self.image = Surface(size)
        self.image.fill(color)
    def update(self):
        self.Pos = (self.Pos[0]+self.Spd, self.Pos[1])
        screen.blit(self.image, self.Pos)
        if (self.Pos[0]< -30):
            self.kill()

class WALL(pygame.sprite.Sprite):
    def __init__(self,xval=WINSIZE[0],warn=False,super=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((60,200))
        self.image.fill(BLACK)
        self.pos = (xval,220)
        self.rect = pygame.rect.Rect(self.pos,(60,200))
        self.warning = warn
        self.warntimer = 0
        self.superwall = super
    def update(self,speed,alt):
        if self.warning:
            self.warntimer+=1
            if(self.warntimer == 1):
                alarm.sound()
            if(self.warntimer > 100):
                self.warning = 0
        else:
            self.rect = pygame.rect.Rect(self.pos,(60,200))
            self.pos = (self.pos[0]-speed,220+alt)
            screen.blit(self.image,self.pos)
    def dead(self, kill=0):
        self.image.fill(WHITE)
        bar.FUXXOR()
        screen.blit(self.image,self.pos)
        if kill:
            clown = 40
            for n in (270,280,290,300,310):
                DOTZ.add(DOTS((self.pos[0],n),clown*2,5))
        else:
            clown = 20
        for n in (220,260,300,340,380):
            DOTZ.add(DOTS((self.pos[0],n),clown))
        if(self.superwall):
            remote.RESET(True)
        self.kill()
        
class BLASTWALL(pygame.sprite.Sprite):
    def __init__(self,warn = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((60,200))
        self.image.fill(WHITE)
        self.pos = (WINSIZE[0],220)
        self.flash = 0
        self.timebomb = 200
        self.speed = 10
        
        self.warning = warn
        self.warntimer = 0
    def update(self,alt):
        if self.warning:
            self.warntimer+=1
            if(self.warntimer == 1):
                alarm.sound()
            if(self.warntimer > 100):
                self.warning = 0
        else:
            if (self.pos[0] < 100):
                self.speed = self.speed/2
            if (self.pos[0]>20):
                self.pos = (self.pos[0]-self.speed,220+alt)
            screen.blit(self.image,self.pos)
        
            if(self.timebomb == 0):
                self.dead(1)
            self.speed += 1
            self.flash += 1
            self.timebomb -= 1
            if(self.flash == 6):
                self.image.fill(WHITE)
            elif(self.flash == 12):
                self.image.fill(BLACK)
                self.flash = 0
    def pushback(self):
        self.speed = -25
        self.pos = (self.pos[0]+10,self.pos[1])
        fxplay(deflect,soundstatus)
    def dead(self,detonate):
        if (self.pos[0] < 200):
            screen.fill(WHITE)
            dude.DAMAGE()
        fxplay(bomb2,soundstatus)
        fxplay(pulse,soundstatus)
        if detonate:
            BLASTS.add(EXPLOSION((self.pos[0]+30,400),100,1))
            self.kill()
        else:
            self.kill()

class POWERBALL(pygame.sprite.Sprite):
    def __init__(self,startx = 640,yad = 0):
        pygame.sprite.Sprite.__init__(self)
        self.cpos = (startx,360-yad)
        self.rad = 10
        self.blindingflash = 0
    def update(self):
        self.rad-=1
        if self.blindingflash:
            pygame.draw.circle(screen,WHITE,self.cpos,30)
        self.cpos = (self.cpos[0]-10,self.cpos[1])
        pygame.draw.circle(screen,WHITE,self.cpos,10,self.rad)
        if(self.cpos[0] < 95):
            fxplay(powerup,soundstatus)
            SHIELDS.add(EXPLOSION((100,400),50,0,0,WHITE))
            pygame.draw.circle(screen,WHITE,(100,400),70)
            dude.HEAL()
            self.kill()
        if(self.rad == 0):
            self.rad = 10
    
class BLADEWALL(pygame.sprite.Sprite):
    def __init__(self,pos,ymove=5,sound=True):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = imglode("Spinwall.bmp")
        self.imgs = imgscale(self.imgs,3)
        self.imgs = getsub(self.imgs,32*3)
        self.frame = 0
        self.pos = pos
        self.xmove = 15
        self.xchange = 2
        self.ymove = ymove
        self.ychange = True
        self.framechange = 100
        self.framerate = 100
        if sound:
            fxplay(spinblade,soundstatus)
        self.rect = pygame.Rect(self.pos,(96,96))
        self.valid = True
    def update(self):
        self.rect = pygame.Rect(self.pos,(96,96))
        self.pos = (self.pos[0]+self.xmove,
                self.pos[1]+self.ymove)
        screen.blit(self.imgs[self.frame],self.pos)
        
        self.xmove-=self.xchange
        if (self.ymove != 0) and self.ychange:
            self.ymove -= 0.1
        
        if(self.ymove < 0) and self.ychange:
            self.ymove = 0
            
        if (self.framechange >= 0):
            self.framechange-=self.framerate
        else:
            #switch frame
            if(self.frame < 6):
                self.frame += 1
            else:
                if(self.frame == 6):
                    self.frame = 7
                else: self.frame = 6
            
            self.framechange = 100
            if (self.framerate < 50):
                self.framerate += 5
        
        if(self.pos[0] < 100):
            self.dead()
            dude.DAMAGE()
        
        if(self.pos[0] > 700):
            self.kill()
    def REFLECT(self):
        self.valid = False
        screen.fill(WHITE)
        self.xmove = 30
        self.xchange = 0
        for x in (0,5,1,15):
            DOTZ.add(DOTS((self.pos[0]+x,self.pos[1]+30)))
        fxplay(bladekill,soundstatus)
        self.ychange = False
        self.ymove = random.randrange(-20,0)
    def dead(self):
        if self.valid:
            fxplay(slice,soundstatus)
            for x in (0,5,1,15):
                DOTZ.add(DOTS((self.pos[0]+x,self.pos[1]+30)))
            self.kill()

class MINIGEN(pygame.sprite.Sprite):
    def __init__(self,type="nothing",xpos=560):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (xpos,-50)
        self.img = pygame.Surface((50,50))
        self.img2 = pygame.Surface((10,10))
        self.img.fill(WHITE)
        self.img2.fill(BLACK)
        self.rect = pygame.Rect(self.pos,(50,50))
        self.ychange = 21
        self.timer = 200
        self.timer2 = 12
        self.blades = 4
        
        if(type == "ROTATE"):
            self.rotateok = True
            self.xadd = 5
            self.yadd = 0
            self.switch = 0
            self.img.fill(GREEN)
        else:
            self.rotateok = False
        
        Texty = texty("REDENSEK.TTF",50)
        self.warn = Texty.render("X",0,BLACK)
    def update(self):
        if self.rotateok:
            self.switch += 1
            if(self.switch == 20):
                self.yadd = 5
                self.xadd = 0
            elif(self.switch == 40):
                self.yadd = 0
                self.xadd = 5
            elif(self.switch == 60):
                self.yadd = -5
                self.xadd = 0
            elif(self.switch == 80):
                self.yadd = 0
                self.xadd = -5
                self.switch = 0
        
            self.pos = (self.pos[0]+self.xadd,
                self.pos[1]+self.yadd)
        self.rect = pygame.Rect(self.pos,(50,50))
        for wall in spinmart:
            if(wall.rect.colliderect(self.rect) and
            not wall.valid):
                self.die()
        
        if(self.timer == 0):
            if(self.timer2 == 0):
                self.timer2 = 12
                if(self.blades > 0):
                    self.blades -= 1
                    spinmart.add(BLADEWALL(self.pos))
                else:
                    self.timer = 100
                    self.blades = 4
            else:
                self.timer2 -= 1
        else:
            self.timer -= 1
        
        if(self.timer < 20):
            screen.blit(self.warn,
                    (self.pos[0]+13,self.pos[1]-50))
        
        if(self.pos[1] < 150):
            self.pos = (self.pos[0],self.pos[1]+self.ychange)
        if(self.ychange > 1):
            self.ychange -= 1
        
        screen.blit(self.img, self.pos)
        screen.blit(self.img2,
                (self.pos[0]+55,self.pos[1]+10))
        screen.blit(self.img2,
                (self.pos[0]+55,self.pos[1]+30))
    def die(self):
        fxplay(bomb2,soundstatus)
        BLASTS.add(EXPLOSION((self.pos[0]+13,self.pos[1]+25),
                            50,0,0,BLACK))
        for xpos in (0,5,10,15,20):
            DOTZ.add(DOTS((self.pos[0]+xpos,self.pos[1])))
        self.kill()

class GENERATOR(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = imglode("THEEYE.bmp")
        self.images = imgscale(self.images,2)
        self.images = getsub(self.images,64)
        self.imglen = len(self.images)
        self.imgno = 0
        self.imgdelay = 0
        self.imgtrigger = False
        self.eyeflash = False
        
        self.pos = (560,0)
        self.image1 = pygame.Surface((60,60))
        self.image2 = pygame.Surface((10,10))
        self.image1.fill(BLACK)
        self.image2.fill(BLACK)
        self.initiate = 1
        self.mod = 5
        self.flash = 0
        
        # ATTACK STUFF
        self.warning = 0
        self.atkimg = pygame.Surface((6,15))
        self.atkimg.fill(BLACK)
        self.atktimer = 0
        self.attacking = 0
        self.atkseqZERO = 0
        self.atkseqONE = 0
        self.atkseqTWO = 0
        
        #HEALTH STUFF
        self.HP = 100
        self.hpbar = pygame.Surface((600,16))
        self.hpbarback = pygame.Surface((608,24))
        self.hpbarflash = pygame.Surface((608,24))
        self.hpbarflash.fill(WHITE)
        self.hpbar.fill(WHITE)
        self.hpbarback.fill(BLACK)
        self.hpflash = 0
        self.cv = 255
        
        #TEXT STUFF
        Texty = texty("REDENSEK.TTF",20)
        Bigtex = texty("REDENSEK.TTF",50)
        self.nametext = Texty.render("GENERATOR",0,BLACK)
        self.question = Bigtex.render("?",0,BLACK)
        self.lol = Bigtex.render(":)",0,BLACK)
        self.loltimer = 100
        
        #BIG ENTRANCE
        fxplay(jet,soundstatus)
        if mixer.music.get_busy():
            mixer.music.stop()
        if(checkfile("DANCE39.mp3")):
            musiclode("DANCE39.mp3")
        self.pause = False
    def update(self):
        screen.blit(self.image1,self.pos)
        screen.blit(self.image2,
                    (self.pos[0]-15,self.pos[1]+10))
        screen.blit(self.image2,
                    (self.pos[0]-15,self.pos[1]+40))
        if (self.mod > 1):
            self.mod-=.04
        if self.initiate:
            if(self.pos[1] < 300):
                self.pos = (560,self.pos[1]+self.mod)
            else:
                self.image1.fill(WHITE)
                BLASTS.add(EXPLOSION((self.pos[0]+30,self.pos[1]+30),50))
                derp = 1
                while(derp < 6):
                    derp+=1
                    DOTZ.add(DOTS((self.pos[0],self.pos[1]+90),20,2))
                self.initiate = 0
                screen.fill(WHITE)
                fxplay(pulse,soundstatus)
                if(checkfile("DANCE39.mp3")):
                    musicplay(musicstatus)
                self.imgtrigger = True
        else:
            if not self.pause:
                self.atktimer+=1
            else:
                if(self.loltimer == 0):
                    self.loltimer = -1
                    fxplay(textblip,soundstatus)
                elif(self.loltimer == -1):
                    screen.blit(self.lol,(self.pos[0]+20,self.pos[1]-50))
                else:
                    self.loltimer -= 1
            # ATTACK SEQUENCES
            if(self.atktimer == 100):
                self.atkNO = random.randrange(0,4)
                self.atktimer = 0
                self.warning = 1
                if(self.atkNO < 2):
                    self.atkseqZERO = 1
                elif(self.atkNO == 2):
                    self.atkseqONE = 1
                elif(self.atkNO == 3):
                    self.atkseqTWO = 1
            #WARNING
            if self.warning:
                self.attacking+=1
                if(self.attacking == 1):
                    fxplay(laser,soundstatus)
                if(self.attacking < 10):
                    if self.atkseqZERO:
                        screen.blit(self.atkimg,(self.pos[0]+20,self.pos[1]-20))
                        screen.blit(self.atkimg,(self.pos[0]+30,self.pos[1]-20))
                        screen.blit(self.atkimg,(self.pos[0]+40,self.pos[1]-20))
                    elif self.atkseqONE:
                        pygame.draw.circle(screen,BLACK,
                                           (self.pos[0]+30,self.pos[1]-18),
                                           10)
                    elif self.atkseqTWO:
                        screen.blit(self.question,
                                    (self.pos[0]+18,self.pos[1]-50))
                elif(self.attacking>20) and (self.attacking<30):
                    if self.atkseqZERO:
                        screen.blit(self.atkimg,(self.pos[0]+20,self.pos[1]-20))
                        screen.blit(self.atkimg,(self.pos[0]+30,self.pos[1]-20))
                        screen.blit(self.atkimg,(self.pos[0]+40,self.pos[1]-20))
                    elif self.atkseqONE:
                        pygame.draw.circle(screen,BLACK,
                                           (self.pos[0]+30,self.pos[1]-18),
                                           10)
                    elif self.atkseqTWO:
                        screen.blit(self.question,
                                    (self.pos[0]+18,self.pos[1]-50))
                elif(self.attacking>40) and (self.attacking<50):
                    if self.atkseqZERO:
                        screen.blit(self.atkimg,(self.pos[0]+20,self.pos[1]-20))
                        screen.blit(self.atkimg,(self.pos[0]+30,self.pos[1]-20))
                        screen.blit(self.atkimg,(self.pos[0]+40,self.pos[1]-20))
                    elif self.atkseqONE:
                        pygame.draw.circle(screen,BLACK,
                                           (self.pos[0]+30,self.pos[1]-18),
                                           10)
                    elif self.atkseqTWO:
                        screen.blit(self.question,
                                    (self.pos[0]+18,self.pos[1]-50))
            
            # ATTACKS
            if self.atkseqZERO :
                self.eyeflash = True
                if(self.attacking == 60):
                    walmart.add(WALL(540))
                if(self.attacking == 70):
                    walmart.add(WALL(540))
                if(self.attacking == 80):
                    walmart.add(WALL(540))
                    self.atkseqZERO = 0
                    self.warning = 0
                    self.atktimer = 0
                    self.attacking = 0
                    self.eyeflash = False
            elif self.atkseqONE:
                self.eyeflash = True
                if(self.attacking == 60):
                    blastmart.add(BLASTWALL())
                if(self.attacking == 100):
                    self.warning = 0
                    self.atkseqONE = 0
                    self.atktimer = 0
                    self.attacking = 0
                    self.eyeflash = False
            elif self.atkseqTWO:
                self.eyeflash = True
                if(self.attacking == 80):
                    if(random.randint(0,10) == 1):
                        powermart.add(POWERBALL(520,10))
                    elif(random.randint(0,20) == 0):
                        fxplay(bomb,soundstatus)
                        BLASTS.add(EXPLOSION((self.pos[0]+30,self.pos[1]+30),
                                             20,0,0,BLACK))
                        self.damage(5)
                    else:
                        walmart.add(WALL(540))
                    self.eyeflash = False
                    self.warning = 0
                    self.atkseqTWO = 0
                    self.atktimer = 0
                    self.attacking = 0
        
        screen.blit(self.hpbarback,(20,20))
        screen.blit(self.hpbar,(24,24))
        screen.blit(self.nametext,(24,22))
        if self.hpflash:
            self.hpflash = 0
            screen.blit(self.hpbarflash,(20,20))
        
        #COLLISION
        for explosion in BLASTS:
            if(explosion.pos[0]>400) and explosion.pain:
                self.damage(10)
                explosion.pain = 0
                
        if self.imgtrigger:
            if(self.imgno < self.imglen-2):
                self.imgdelay += 1
                if(self.imgdelay == 3):
                    self.imgdelay = 0
                    self.imgno+=1
                if(self.imgno == self.imglen-2):
                    self.imgtrigger = False
                    
        if self.eyeflash:
            screen.blit(self.images[7],
                    (self.pos[0]-2,self.pos[1]))
            if(self.flash == 3):
                draw.circle(screen,BLACK,
                        (self.pos[0]+30,self.pos[1]+30),10,2)
            draw.circle(screen,WHITE,
                (self.pos[0]+30,self.pos[1]+30),
                70,2)
        else:
            screen.blit(self.images[self.imgno],
                    (self.pos[0]-2,self.pos[1]))
        
        self.flash+=1
        if(self.flash == 3):
            self.image2.fill(BLACK)
        elif(self.flash == 6):
            self.image2.fill(WHITE)
            self.flash = 0
    def damage(self,amount):
        self.eyeflash = True
        self.cv-=2*amount
        if(self.cv < 0): self.cv = 0
        self.image1.fill((self.cv,self.cv,self.cv))
        self.HP -= amount
        if(self.HP < 0): self.HP = 0
        i = 1
        while(i < 5):
            i+=1
            DOTZ.add(DOTS((self.pos[0]+40,self.pos[1]+40)))
        self.hpbar = pygame.Surface(((6*self.HP),16))
        self.hpbar.fill(WHITE)
        
        #DEATH
        if(self.HP == 0):
            i = 1
            while(i < 5):
                i+=1
                DOTZ.add(DOTS((self.pos[0]+40,self.pos[1]+40)))
            fxplay(BOOM,soundstatus)
            global FPS
            FPS = 15
            BLASTS.add(EXPLOSION(self.pos,100,0,1,WHITE))
            remote.RESET(True)
            mixer.music.fadeout(600)
            self.kill()
bawls = pygame.sprite.Group()
class HAMMER(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = imglode("HAMMER.bmp")
        self.img = imgscale(self.img,4)
        self.img2 = imglode("HAMMER2.bmp")
        self.img2 = imgscale(self.img2,4)
        self.image = self.img2
        
        self.flickerok = True
        self.flicker = 0
        self.timer = 0
        self.pos = (400,0)
        self.ymove = 1
        self.shock = True
    def update(self,ypos):
        self.timer+=1
        if(self.timer > 30) and (self.timer < 100):
            self.flickerok = False
            if(self.pos[1] < 200):
                if(self.ymove < 20):
                    self.ymove+=5
                self.pos = (self.pos[0],
                        self.pos[1]+self.ymove)
            else:
                if self.shock:
                    screen.fill(WHITE)
                    self.shock = False
                    fxplay(hammersmash,soundstatus)
                    fxplay(bomb,soundstatus)
                    shocks.add(SHOCKWAVE(self.pos[0]-35))
                    self.pos = (self.pos[0],230)
        if(self.timer == 60):
            fxplay(hammersmash,soundstatus)
            fxplay(bomb,soundstatus)
            shocks.add(SHOCKWAVE(self.pos[0]-50))
        elif(self.timer == 80):
            fxplay(hammersmash,soundstatus)
            fxplay(bomb,soundstatus)
            shocks.add(SHOCKWAVE(self.pos[0]-100))
        elif(self.timer == 100):
            fxplay(hammersmash,soundstatus)
            fxplay(bomb,soundstatus)
            shocks.add(SHOCKWAVE(self.pos[0]-150,True))
        
        if(self.timer > 130):
            self.flickerok = True
        if(self.timer > 200):
            self.kill()
        
        if self.flickerok:
            self.flicker+=1
            if(self.flicker < 3):
                self.image = self.img2
            elif(self.flicker > 4):
                self.flicker = 0
                self.image = self.img
        screen.blit(self.image,(self.pos[0],self.pos[1]+(430-ypos)))
gdamnhammers = pygame.sprite.Group()
class ENERGYBLAST(pygame.sprite.Sprite):
    def __init__(self,xpos,type="NORMAL"):
        pygame.sprite.Sprite.__init__(self)
        if(type == "NORMAL"):
            self.pos = (xpos, 420)
            self.xmove = -5
            self.ymove = -10
        elif(type == "ABNORMAL"):
            self.pos = (xpos,200)
            self.xmove = -20
            self.ymove = 10
        self.type = type
        self.addok = 0
        self.reflecting = False
        self.tagging = False
        self.tagcount = 0
    def update(self):
        if(self.type == "NORMAL"):
            if self.tagging:
                if(self.xmove > -10):
                    self.xmove-=1
            if not self.reflecting and not self.tagging:
                if(self.ymove < 4):
                    self.ymove += 0.5
                    
        self.pos = (self.pos[0]+self.xmove,
                self.pos[1]+self.ymove)
            
        if(self.addok < 4):
            self.addok+=1
        else:
            self.addok = 0
            BLASTS.add(EXPLOSION(self.pos,50,0,0,GREEN))
        if(self.type == "NORMAL"):
            draw.circle(screen,GREEN,self.pos,30)
        else:
            draw.circle(screen,WHITE,self.pos,30)
        
        if((self.pos[0] > 400) and 
        (self.pos[1] < 300) and
        (self.type == "NORMAL")):
            fxplay(BOOM,soundstatus)
            BLASTS.add(EXPLOSION(self.pos,100,0,0,GREEN))
            for boss in bawss:
                boss.damage(20)
            fxplay(damage,soundstatus)
            screen.fill(WHITE)
            self.kill()
        if(self.pos[1] > 420) or (self.pos[0] < 0):
            fxplay(BOOM,soundstatus)
            BLASTS.add(EXPLOSION(self.pos,100,0,0,GREEN))
            dude.DEATH()
            fxplay(damage,soundstatus)
            screen.fill(WHITE)
            self.kill()
    def tag(self):
        if(self.type == "ABNORMAL"):
            BLASTS.add(EXPLOSION(self.pos,70,0,1,WHITE))
            self.kill()
            
        if(self.tagcount < 8):
            self.tagcount+=1
            self.tagging = True
            self.xmove = 10
            self.ymove = 0
            BLASTS.add(EXPLOSION(self.pos,40,0,1,BLACK))
        else:
            self.tagging = False
            self.REFLECT()
    def REFLECT(self):
        BLASTS.add(EXPLOSION(self.pos,80,0,0,GREEN,))
        self.reflecting = True
        self.xmove = 20
        self.ymove = -10
balls = pygame.sprite.Group()
class SHOCKWAVE(pygame.sprite.Sprite):
    def __init__(self,xpos,blast=False,detonate=False,size=3):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = imglode("Shockwave.bmp")
        self.imgs = imgscale(self.imgs,size)
        self.imgs = getsub(self.imgs,64*size)
        self.timer = 0
        self.frame = 0
        self.pos = (xpos,268)
        if not detonate:
            BLASTS.add(EXPLOSION((self.pos[0]+90,self.pos[1]+160),
                                40,0,1,BLACK))
        self.detonate = detonate
        if blast:
            balls.add(ENERGYBLAST(self.pos[0]))
        if self.detonate:
            BLASTS.add(EXPLOSION((self.pos[0],self.pos[1]+160),
                100,1,1,GREEN))
    def update(self,yalt):
        if(self.timer < 1):
            self.timer += 1
        else:
            self.timer=0
            self.frame+=1
            
        if(self.frame == 0):
            for y in (0,20,40,60,80,100,120,140):
                DOTZ.add(DOTS((self.pos[0],
                            self.pos[1]+y),20,5))
                DOTZ.add(DOTS((self.pos[0]+20,
                            self.pos[1]+y),20,5))
            bar.FUXXOR()
        elif(self.frame == 5):
            self.kill()
        else:
            if self.detonate:
                self.pos = (self.pos[0]-128,self.pos[1])
            screen.blit(self.imgs[self.frame],self.pos)
shocks = pygame.sprite.Group()
class LASER(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((100,0),(2,450))
        self.xpos = 100
        self.width = 2
        self.flash = 0
        self.color = WHITE
    def update(self):
        self.flash += 1
        if(self.flash < 3):
            self.color = WHITE
        else:
            self.flash = 0
            self.color = GREEN
        
        if(self.width > 2):
            self.width -= 4
        if(self.width <= 0):
            self.kill()
        
        if(self.xpos > 100):
            self.xpos -= 1
        
        self.rect = pygame.Rect((self.xpos-(self.width/2),0),(self.width,450))
        draw.rect(screen,self.color,self.rect)
    def grow(self):
        self.width = 50
lazor = pygame.sprite.Group()
class WAVE(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.Surface((100,480))
        self.img.fill(WHITE)
        self.width = 100
        self.xpos = -100
        bar.FUXXOR()
    def update(self):
        if(self.width > 0):
            self.xpos += 20
            self.width -= 2
        else:
            self.kill()
        self.img = pygame.Surface((self.width,480))
        self.img.fill(WHITE)
        screen.blit(self.img,(self.xpos,0))
waves = pygame.sprite.Group()
class FINALLITY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.MasterTimer = 0
        self.color = 0
        self.interval = 40
    def update(self):
        self.MasterTimer+=1
        if(self.MasterTimer < 500):
            if(self.color < 255):
                self.color+=1
                global RED
                RED = (255,self.color,self.color)
                
        if(self.MasterTimer%self.interval == 0):
            if(self.interval > 20):
                self.interval-=1
            waves.add(WAVE())
finals = pygame.sprite.Group()
#FUCK YEAR LET'S DO THIS
class BOSS(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #FIRST THE OBVIOUS STUFF
        self.HP = 100
        self.die = False
        self.dying = False
        self.deathsequence = 0
        self.deathx = 0
        self.summonok = True
        #Now the imaging
        self.alphasz = 255
        self.imgs = []
        #first the stills
        img1 = imglode("boxfirstform.bmp")
        img2 = imglode("boxdead.bmp")
        #then the animations
        imgs1 = imglode("boxtransform.bmp")
        imgs2 = imglode("boxsecondform.bmp")
        imgs3 = imglode("boxatk1.bmp")
        imgs4 = imglode("boxatk2.bmp")
        imgs5 = imglode("boxatk3.bmp")
        
        #next expand them
        img1 = imgscale(img1,4)
        img2 = imgscale(img2,4)
        imgs1 = imgscale(imgs1,4)
        imgs2 = imgscale(imgs2,4)
        imgs3 = imgscale(imgs3,4)
        imgs4 = imgscale(imgs4,4)
        imgs5 = imgscale(imgs5,4)
        
        #next split the ones that need splitting
        imgs1 = getsub(imgs1,256)
        imgs2 = getsub(imgs2,256)
        imgs3 = getsub(imgs3,256)
        imgs4 = getsub(imgs4,256)
        imgs5 = getsub(imgs5,256)
        
        for thing in (img1,img2,imgs1,imgs2,imgs3,
                    imgs4,imgs5):
            self.imgs.append(thing)
        #self.imgs now follows the format:
        # (first idle,dead,[transform],[second idle],
        #   [first attack],[second attack], [third attack])
        
        #other things that will need blitting
        self.hpbar1 = pygame.Surface((600,16))
        self.hpbar1.fill(GREEN)
        self.hpbar2 = pygame.Surface((600,16))
        self.hpbar2.fill(RED)
        self.hpbarback = pygame.Surface((608,24))
        self.hpbarback.fill(BLACK)
        self.hpbarflash = pygame.Surface((608,24))
        self.hpbarflash.fill(GREEN)
        self.hpshow = False
        #TEXT STUFF
        Texty = texty("REDENSEK.TTF",20)
        Bigtex = texty("REDENSEK.TTF",40)
        Liltex = texty("REDENSEK.TTF",10)
        self.name = Texty.render("BOX",0,BLACK)
        self.warn1 = Bigtex.render("WARNING!",0,BLACK)
        self.warn2 = Liltex.render("MASSIVE ENEMY APPROACHING",0,BLACK)
        
        #BIG ENTRANCE
        self.entrancetimer = 0
        self.me = pygame.Surface((20,20))
        self.mepos = (400,0)
        self.color = (0,0,0)
        self.cv = 0
        
        self.frame = 0
        self.frameswitch = 6
        self.pos = (400,100)
        self.bob = 0
        self.bobval = 1
        self.image = img1
        self.imgtype = -1
        self.flash = False
        self.fuck = False
        #========================
        self.transforming = False
        #========================
        self.transformtimer = 0
        self.firstform = True
        #Attack info
        self.spawninterval = 200
        self.paused = True
        self.attacktype = 0
        self.attacktimer2 = 0
        self.attacktimer = 0
        self.atktmr = 0
        
        self.moveok = 0
        self.moveamount = 0
        
        self.flicker = False
        self.alphasz = 255
        
        self.shockpos = 0
        
        #sounds
        mixer.music.stop()
    def update(self):
        #BIG ENTRANCE
        if(self.imgtype == -1):
            if(self.cv < 255):
                self.cv+=1
            self.color = (0,self.cv,0)
            if(self.entrancetimer == 100):
                screen.fill(self.color)
                fxplay(bomb2,soundstatus)
                self.me = pygame.Surface((20,20))
                self.me.fill(self.color)
            if(self.entrancetimer == 200):
                screen.fill(self.color)
                fxplay(bomb2,soundstatus)
                self.me = pygame.Surface((40,40))
                self.me.fill(self.color)
            if(self.entrancetimer == 250):
                screen.fill(self.color)
                fxplay(bomb2,soundstatus)
                self.me = pygame.Surface((70,70))
                self.me.fill(self.color)
                self.mepos = (self.mepos[0]+10,self.mepos[1]+10)
            if(self.entrancetimer == 270):
                screen.fill(self.color)
                fxplay(bomb2,soundstatus)
                self.me = pygame.Surface((100,100))
                self.me.fill(self.color)
                self.mepos = (self.mepos[0]+10,self.mepos[1]+10)
            if(self.entrancetimer == 300):
                screen.fill(self.color)
                fxplay(bomb2,soundstatus)
                self.me = self.imgs[0]
                self.mepos = (400,100)
            if(self.mepos[1] < 100):
                self.mepos = (self.mepos[0],self.mepos[1]+10)
            if(self.entrancetimer == 350):
                screen.fill(WHITE)
                fxplay(shiny,soundstatus)
                BLASTS.add(EXPLOSION(self.mepos,100))
            if(self.entrancetimer == 400):
                if(checkfile("296234_Awake___Supernova.mp3")):
                    musiclode("296234_Awake___Supernova.mp3")
                    musicplay(musicstatus)
                self.flash = True
                self.paused = False
                self.imgtype = 0
            screen.blit(self.me,self.mepos)
            self.entrancetimer+=1
        #HEALTH SHITS
        elif(self.imgtype >= 0) and not self.die:
            screen.blit(self.hpbarback,(20,20))
            screen.blit(self.hpbar2,(24,24))
            if self.firstform:
                screen.blit(self.hpbar1,(24,24))
            screen.blit(self.name,(24,20))
        
        #ATTACKS
        if(self.attacktimer2 > self.spawninterval) and not self.paused:
            BLASTS.add(EXPLOSION((self.pos[0]+128,self.pos[1]+128),50,0,0,GREEN))
            thing = random.randrange(0,2)
            fxplay(bomb1,soundstatus)
            if(thing == 0):
                walmart.add(WALL(600))
            elif(thing == 1):
                blastmart.add(BLASTWALL())
                
            self.attacktimer2 = 0
        else:
            self.attacktimer2 += 1
        
        if(self.paused == False):
            self.attacktimer += 1
        
        #regular mode attacks
        if(self.imgtype == 0):
            if(self.attacktimer == 220):
                self.paused = True
                self.attacktimer+=1
                self.attacktype = self.makechoice()
                print self.attacktype
            elif(self.attacktimer == 221):
                #SMASH YOU
                if(self.attacktype == 4):
                    if(self.pos[0] < 100):
                        self.flash = True
                        dude.DAMAGE()
                        self.atktmr = 201
                    self.bob = 0
                    self.atktmr+=1
                    if(self.atktmr < 200):
                        if(self.moveok == 1):
                            if(self.moveamount < 20):
                                self.moveamount+=5
                            self.pos = (self.pos[0]-self.moveamount,self.pos[1])
                        else:
                            if(self.pos[1] < 210):
                                self.pos=(self.pos[0],self.pos[1]+5)
                            else:
                                for x in (0,50,100,150,200):
                                    DOTZ.add(DOTS((x,self.pos[1]+256)))
                                fxplay(hammersmash,soundstatus)
                                fxplay(rush,soundstatus)
                                shocks.add(SHOCKWAVE(300))
                                BLASTS.add(EXPLOSION((self.pos[0]+128,self.pos[1]+128),
                                                70,0,0,BLACK))
                                self.moveok = 1
                    elif(self.atktmr > 200) and (self.atktmr < 250):
                        if(self.pos[0] != 400):
                            self.pos = (correct(self.pos[0],400,20,10),
                                    self.pos[1])
                        if(self.pos[1] != 100):
                            self.pos = (self.pos[0],
                                    correct(self.pos[1],100,20,10))
                    elif(self.atktmr > 250):
                        self.moveamount = 0
                        self.paused = False
                        self.atktmr = 0
                        self.attacktimer = 0
                        self.moveok = 0
                #SLICE N DICE YOU
                if(self.attacktype == 5):
                    self.bob = 0
                    if(self.flicker == False):
                        self.flicker = True
                    if (self.alphasz > 50):
                        self.alphasz -= 5
                    self.atktmr += 1
                    if((self.atktmr == 50)or
                    (self.atktmr == 70)or
                    (self.atktmr == 90)or
                    (self.atktmr == 110)):
                        fxplay(genspawn,soundstatus)
                        GENES.add(MINIGEN("ROTATE",350))
                    
                    if(len(GENES) == 0) and (self.atktmr > 50):
                        self.alphasz = 255
                        self.paused = False
                        self.atktmr = 0
                        self.attacktimer = 0
                #HAMMER TIME
                if(self.attacktype == 6):
                    self.bob = 0
                    if(self.atktmr < 100):
                        self.atktmr += 1
                    elif(self.atktmr == 100):
                        self.atktmr += 1
                        fxplay(hammerspawn,soundstatus)
                        gdamnhammers.add(HAMMER())
                    else:
                        if(len(balls) == 0):
                            self.paused = False
                            self.atktmr = 0
                            self.attacktimer = 0
                    
                
                
        
        #WTF mode attacks
        if(self.imgtype > 0):
            if(self.attacktimer == 150):
                self.paused = True
                self.attacktimer+=1
                self.attacktype = self.makechoice()
                print self.attacktype
            elif(self.attacktimer == 151):
                #THROW A FUCKTON OF BLADES
                if(self.attacktype == 0):
                    if(self.atktmr == 0):
                        fxplay(transform,soundstatus)
                        self.frameswitch = 0
                        self.imgtype = 3
                    elif((self.atktmr == 30)or
                        (self.atktmr == 40)or
                        (self.atktmr == 50)or
                        (self.atktmr == 60)or
                        (self.atktmr == 70)or
                        (self.atktmr == 80)):
                           fxplay(bigblade,soundstatus)
                           spinmart.add(BLADEWALL((self.pos[0]+100,self.pos[1]),
                                                10,False))
                    self.atktmr+=1
                    if(self.atktmr == 200):
                        self.atktmr = 0
                        self.attacktimer = 0
                        self.imgtype = 2
                        screen.fill(GREEN)
                        self.paused = False
                        
                #GIGA FLARE
                if(self.attacktype == 1):
                    if(self.atktmr == 0):
                        fxplay(roar,soundstatus)
                        self.flash = True
                        self.frameswitch = 0
                        self.imgtype = 4
                    if(self.atktmr == 40):
                        fxplay(slowcharge,soundstatus)
                        fxplay(bigcharge,soundstatus)
                    if((self.atktmr > 40) and
                    (self.atktmr%5 == 0) and
                    (self.atktmr < 500)):
                        BLASTS.add(EXPLOSION((self.pos[0]+128,self.pos[1]+128),
                                                50,0,0,GREEN))
                        draw.circle(screen,GREEN,
                                (self.pos[0]+128,self.pos[1]+128),40)
                    self.atktmr+=1
                    if(self.atktmr%50 == 0):
                        blastmart.add(BLASTWALL())
                    if(self.atktmr == 500):
                        fxplay(bigblast,soundstatus)
                        fxplay(BOOM,soundstatus)
                        fxplay(pulse,soundstatus)
                        balls.add(ENERGYBLAST(self.pos[0]+128,"ABNORMAL"))
                    if(self.atktmr > 510):
                        global FPS
                        FPS = 5
                        self.atktmr = 0
                        self.attacktimer = 0
                        self.imgtype = 2
                        screen.fill(GREEN)
                        self.paused = False
                        
                #LASER RAIN
                if(self.attacktype == 2):
                    if(self.atktmr == 0):
                        self.frameswitch = 0
                        self.imgtype = 5
                    if(self.atktmr == 20):
                        lazor.add(LASER())
                        fxplay(opticcharge,soundstatus)
                    if(self.atktmr == 200):
                        self.flash = True
                        for lasic in lazor:
                            lasic.grow()
                            self.shockpos = lasic.xpos
                        fxplay(opticblast,soundstatus)
                    if(self.atktmr == 220):
                        for lasic in lazor:
                            lasic.kill()
                        global FPS
                        FPS = 10
                        self.flash = True
                        fxplay(BOOM,soundstatus)
                        shocks.add(SHOCKWAVE(self.shockpos,False,True))
                        if(self.shockpos < 250):
                            dude.DEATH()
                        elif(self.shockpos > 400):
                            self.damage(40)
                    if(self.atktmr%5 == 0):
                        SHIELDS.add(EXPLOSION((self.pos[0],self.pos[1]+128),
                                                50,0,0,GREEN))
                    self.atktmr+=1
                    if(self.atktmr == 260):
                        self.atktmr = 0
                        self.attacktimer = 0
                        self.imgtype = 2
                        screen.fill(GREEN)
                        self.paused = False
                        
                
                        
        if not self.die:
            if(self.bob > 20):
                self.bobval = -1
            elif(self.bob < -20):
                self.bobval = 1
            
            self.bob+=self.bobval
            
        #TRANSFORMING SEQUENCE
        if self.transforming:
            self.bob = 0
            global RED
            if self.alphasz > 150:
                self.alphasz-=1
            RED = (self.alphasz,0,0)
            if(self.transformtimer == 0):
                mixer.music.fadeout(600)
            if((self.transformtimer == 60)or
            (self.transformtimer == 100)or
            (self.transformtimer == 160)or
            (self.transformtimer == 180)or
            (self.transformtimer == 200)or
            (self.transformtimer == 230)):
                fxplay(bomb1,soundstatus)
                screen.fill(WHITE)
                bar.FUXXOR()
            if(self.transformtimer > 270):
                fxplay(transform,soundstatus)
                fxplay(roar,soundstatus)
                self.imgtype = 1
            if(self.transformtimer > 300):
                mixer.music.stop()
                if(checkfile("252492_The_Hate_Patrol_With_Army_.mp3")):
                    musiclode("252492_The_Hate_Patrol_With_Army_.mp3")
                    musicplay(musicstatus)
                self.spawninterval = 100
                BLASTS.add(EXPLOSION((self.pos[0]+128,self.pos[1]+128),
                                    200,0,1,GREEN))
                
                self.transforming = False
                self.paused = False
                self.firstform = False
            self.transformtimer+=1
        
        #ANIMATIONS
        if self.flash:
            screen.fill(WHITE)
            self.flash = False
        
        
        if(self.frameswitch == 0):
            self.frameswitch = 6
            #first idle animation: just the box
            if(self.imgtype == 0):
                self.image = self.imgs[0]
            #transformation animation
            elif(self.imgtype == 1):
                if(self.frame < 6):
                    self.frame+=1
                    self.image = self.imgs[2][self.frame]
                else:
                    self.imgtype = 2 
                    self.frame = 0
            #second idle animation
            elif(self.imgtype == 2):
                if(self.frame < 2):
                    self.frame+=1
                else: self.frame = 0
                self.image = self.imgs[3][self.frame]
            #first attack
            elif(self.imgtype == 3):
                if(self.frame < 4):
                    self.frame+=1
                self.image = self.imgs[4][self.frame]
            #second attack
            elif(self.imgtype == 4):
                if(self.frame > 2):
                    self.frame = 0
                if(self.frame < 2):
                    self.frame+=1
                self.image = self.imgs[5][self.frame]
            #third attack
            elif(self.imgtype == 5):
                if(self.frame < 4):
                    self.frame+=1
                self.image = self.imgs[6][self.frame]
                
            #DEATH
            elif(self.imgtype == 6):
                self.image = self.imgs[1]
        else:
            self.frameswitch -= 1
            
        #OH FUCK
        if(self.imgtype > 0):
            if not self.fuck:
                bar.FUXXOR()
                self.fuck = True
        
        #SPECIAL EFFECTS
        if self.flicker:
            self.flicker = False
            self.image.set_alpha(self.alphasz)
        
        if(self.imgtype >= 0) and not self.die:
            if((self.frameswitch < 6) and (self.fuck==True)):
                self.pos2 = ((self.pos[0]+random.randrange(-10,10)),
                            (self.pos[1]+random.randrange(-10,10)+self.bob))
                screen.blit(self.image,self.pos2,None,BLEND_MIN)
            else:
                screen.blit(self.image,(self.pos[0],self.pos[1]+self.bob))
                
        #DEATH SEQUENCE
        if(self.dying) and not self.die:
            self.deathsequence+=1
            if(self.deathsequence%100 == 0):
                self.flash = True
                fxplay(bigcharge,soundstatus)
            if(self.deathsequence%5 == 0) or (self.deathsequence == 0):
                #fxplay()
                BLASTS.add(EXPLOSION((self.pos[0]+128,self.pos[1]+128),
                                    50,0,0,GREEN))
                draw.circle(screen,GREEN,
                        (self.pos[0]+128,self.pos[1]+128),40)
            if(self.deathsequence%40 == 0):
                BLASTS.add(EXPLOSION((self.pos[0]+128,self.pos[1]+128),
                                    200,0,0,GREEN))
            if(self.deathsequence == 400):
                if self.summonok:
                    self.summonok = False
                    littleshit.add(LILHELPER())
                self.deathsequence = 0
        
        if(self.die):
            screen.blit(self.image,self.pos)
            if(self.deathsequence > 100) and (self.deathsequence%2 == 0):
                self.deathx+=1
            if(self.deathsequence > 100):
                self.pos = (self.pos[0]-self.deathx,self.pos[1])
            self.deathsequence+=1
            if(self.pos[0] < -400):
                global bossdead
                bossdead = True
                self.kill()
    def switch(self,type):
        self.imgtype = type
    def makechoice(self):
        if(self.imgtype > 0):
            i = random.randrange(0,3)
        else:
            i = random.randrange(4,7)
        if(i == 5):
            fxplay(invis,soundstatus)
        return i
    def damage(self,amount):
        if(self.firstform == True):
            if(self.HP-amount < 0):
                self.hpbar1 = pygame.Surface((0,16))
                self.paused = True
                self.transforming = True
                self.atktmr = 0
                self.attacktimer = 0
                self.attacktimer2 = 0
                #reset values
                self.flicker = True
                self.alphasz = 255
                self.pos = (400,100)
                screen.fill(WHITE)
                
                self.HP = 100
            else:
                self.HP-=amount
                self.hpbar1 = pygame.Surface((self.HP * 6,16))
                self.hpbar1.fill(GREEN)
        else:
            if(self.HP-amount < 0):
                self.hpbar2 = pygame.Surface((0,20))
                self.dying = True
                self.imgtype = 4
                self.paused = True
                self.atktmr = 0
                self.attacktimer = 0
                self.attacktimer2 = 0
                # Kill EVERYTHING
                for wall in walmart:
                    wall.kill()
                for wall in blastmart:
                    wall.kill()
                for shit in powermart:
                    shit.kill()
                for wall in spinmart:
                    wall.kill()
                fxplay(slowcharge,soundstatus)
                self.HP = 0
                self.hpbar2 = pygame.Surface((self.HP * 6,16))
                self.hpbar2.fill((255,0,0))
            else:
                self.HP-=amount
                self.hpbar2 = pygame.Surface((self.HP * 6,16))
                self.hpbar2.fill((255,0,0))
        screen.blit(self.hpbarflash,(20,20))
    def DIEBOX(self):
        global FPS
        FPS = 1
        global RED
        for wave in waves:
            wave.kill()
        RED = (255,0,0)
        self.imgtype = 6
        mixer.music.fadeout(600)
        self.flash = True
        self.die = True
        self.paused = True
        self.atktmr = 0
        self.attacktimer = 0
        self.attacktimer2 = 0
        swords.add(SWORDOFLIGHT(self.pos[0]-50,80,0))
        self.deathsequence = 0
bawss = pygame.sprite.Group()
class SWORDOFLIGHT(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos=100,type=1):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if(self.type == 0):
            self.img = imglode("sword.bmp")
            self.img = imgscale(self.img,6)
        elif(self.type == 1):
            self.img = imglode("sword2.bmp")
            self.img = imgscale(self.img,2)
        self.timer = 0
        self.pos = (xpos,ypos)
    def update(self):
        if(self.timer == 0):
            fxplay(bladekill,soundstatus)
            if(self.type == 0):
                screen.fill(WHITE)
                mixer.music.fadeout(600)
                shocks.add(SHOCKWAVE(self.pos[0]+80))
        if(self.timer < 100):
            if(self.type == 1):
                if(self.timer%3 == 0):
                    self.pos = (self.pos[0]-1,self.pos[1])
                    screen.blit(self.img,self.pos)
            elif(self.type == 0):
                screen.blit(self.img,self.pos)
        else:
            if(self.type == 0):
                for ypos in (0,20,40,60,80,100):
                    DOTZ.add(DOTS((self.pos[0]+80,ypos+200)))
            self.kill()
        self.timer+=1
swords = pygame.sprite.Group()
class LILHELPER(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.Surface((40,40))
        self.img2 = pygame.Surface((10,10))
        self.img.fill(WHITE)
        self.img2.fill(BLACK)
        Bigtex = texty("REDENSEK.TTF",50)
        self.question = Bigtex.render("?",0,WHITE)
        self.lol = Bigtex.render(":)",0,WHITE)
        self.pos = (700,300)
        self.timer = 0
        self.xoffset = 0
    def update(self):
        if(self.xoffset > 0):
            self.xoffset-=1
        
        if(self.pos[0] > 400):
            self.pos = (self.pos[0]-1,self.pos[1])
        else:
            self.timer+=1
            if(self.timer == 50):
                fxplay(goof, soundstatus)
            if(self.timer < 200) and (self.timer > 50):
                screen.blit(self.question,
                        (self.pos[0]+10,self.pos[1]-50))
            if(self.timer == 200):
                powermart.add(POWERSWORD(self.pos[0]))
            if(self.timer > 250) and (self.timer < 400):
                screen.blit(self.lol,
                        (self.pos[0]+10,self.pos[1]-50))
            if(self.timer > 400):
                if(self.pos[1] > -50):
                    self.pos = (self.pos[0],self.pos[1]-20)
                else:
                    self.kill()
                
        screen.blit(self.img,(self.pos[0]+self.xoffset,
                            self.pos[1]))
        screen.blit(self.img2,(self.pos[0]-15+self.xoffset,
                            self.pos[1]+25))
        screen.blit(self.img2,(self.pos[0]-15+self.xoffset,
                            self.pos[1]+5))
    def shake(self):
        self.xoffset = 10
littleshit = pygame.sprite.Group()
class POWERSWORD(pygame.sprite.Sprite):
    def __init__(self,xpos=640):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = imglode("powerup.bmp")
        self.imgs = imgscale(self.imgs,3)
        self.imgs = getsub(self.imgs,3*16)
        self.frame = 0
        self.pos = (xpos,300)
    def update(self,spd=0):
        if(self.pos[0] > 100):
            self.pos = (self.pos[0]-5, self.pos[1])
        else:
            self.collect()
        screen.blit(self.imgs[self.frame],self.pos)
        if(self.frame == 3):
            self.frame = 0
        else: self.frame += 1
                
    def collect(self):
        fxplay(powerup,soundstatus)
        screen.fill(WHITE)
        if not superpowered:
            global superpowered
            superpowered = True
        elif(len(bawss) > 0):
            dude.ultrapowered = True
        self.collected = True
        self.kill()
        
class PLAYER:
    def __init__(self):
        self.imgs = imglode("Kobold.bmp")
        self.imgs = imgscale(self.imgs, 2)
        self.imgs = getsub(self.imgs, 48*2)
        self.imgs2 = imglode("Kobold2.bmp")
        self.imgs2 = imgscale(self.imgs2, 2)
        self.imgs2 = getsub(self.imgs2, 48*2)
        Texty = texty("REDENSEK.TTF",60)
        
        self.imglength = len(self.imgs)
        self.changeok = 0
        self.frame = 0
        self.ready = 0
        self.delay = 0
        self.ultrapowered = False
        self.ultratimer = 0
        #HEALTH SHIT
        self.HP = 90
        self.shieldflash = 0
        self.shieldpos = (100,400)
        self.breakshield = True
        self.exclaim = Texty.render("!",0,WHITE)
        self.warning = Texty.render("WARNING LOW SHIELD",0,WHITE)
        self.SHIFT = Texty.render("[SHIFT]!",0,WHITE)
        self.beepok = True
        self.beeptimer = 0
        #Death animation
        self.alive = True
        self.deathtimer = 200
    def update(self,ypos):
        global FPS
        
        if self.alive:
            if self.ultrapowered:
                if(self.ultratimer == 1):
                    fxplay(attention,soundstatus)
                if(self.ultratimer < 10):
                    screen.blit(self.SHIFT,(320,200))
                elif(self.ultratimer > 10):
                    self.ultratimer = 0
                self.ultratimer+=1
            self.delay+=1
            if (self.ready == 0):
                self.changeok = 0
            else:
                self.ready-=1
            if(self.delay == 3):
                self.delay = 0
                if self.frame < self.imglength-2:
                    self.frame += 1
                else:
                    self.frame = 0
                    
            self.pos = (50,ypos-90)
            if(self.changeok == 0):
                screen.blit(self.imgs[self.frame],self.pos)
            else:
                screen.blit(self.imgs2[self.frame],self.pos)
                
            
            #HP SHIT
            if(self.HP == 60):
                self.shieldflash+=1
                if(self.shieldflash == 60):
                    self.shieldflash = 0
                    SHIELDS.add(EXPLOSION(self.shieldpos,50,0,0,BLACK))
            elif(self.HP == 30):
                self.shieldflash+=1
                if(self.shieldflash == 30):
                    self.shieldflash = 0
                    SHIELDS.add(EXPLOSION(self.shieldpos,50,0,0,BLACK))
            elif(self.HP == 0):
                if self.beepok:
                    if((self.beeptimer == 0)or
                    (self.beeptimer == 5)or
                    (self.beeptimer == 10) or
                    (self.beeptimer == 15)):
                        screen.blit(self.warning,(50,400))
                        fxplay(attention,soundstatus)
                    self.beeptimer+=1
                    if(self.beeptimer > 15):
                        self.beepok = False
                        self.beeptimer = 0
                if self.breakshield:
                    self.breakshield = False
                    SHIELDS.add(EXPLOSION(self.shieldpos,200,0,1,BLACK))
                    for xpos in (0,50,100,150):
                        DOTZ.add(DOTS((xpos,420)))
                else:
                    self.shieldflash+=1
                    if (self.shieldflash > 15):
                        screen.blit(self.exclaim,(110,290))
                    if (self.shieldflash == 30):
                        self.shieldflash = 0
        else:
            if(self.deathtimer > 0):
                self.deathtimer-=1
            else:
                remote.RESETLEVEL()
        if(FPS < 60):
            FPS+=1
                
    def STRIKU(self):
        if superpowered:
            SHIELDS.add(EXPLOSION((self.pos[0]+90,self.pos[1]+40),
                            10,0,0,BLACK))
        self.ready = 50
        self.changeok = 1
    def DAMAGE(self):
        global FPS
        FPS=FPS/3
        SHIELDS.add(EXPLOSION(self.shieldpos,100,0,1,BLACK))
        fxplay(damage,soundstatus)
        self.shieldflash = 0
        if(self.HP > 0):
            self.HP-=30
        else: self.DEATH()
        if(self.HP == 0):
            self.beepok = True
    def HEAL(self):
        if(self.HP < 90):
            self.HP+=30
    def DEATH(self):
        if invincible:
            self.HP = 90
            self.breakshield = True
            self.shieldflash = 0
        else:
            global FPS
            FPS = 60
            screen.fill(WHITE)
            SHIELDS.add(EXPLOSION(self.shieldpos,100,0,1,BLACK))
            fxplay(die, soundstatus)
            mixer.music.pause()
            i = 1
            while(i < 8):
                i+=1
                DOTZ.add(DOTS(self.shieldpos))
            self.alive = False
            mixer.music.fadeout(600)

dude = PLAYER()

        
def correct(inputval,inputgoal,coreval,tollerance=2):
    if (inputval < inputgoal-tollerance):
        return inputval + coreval
    elif (inputval > inputgoal+tollerance):
        return inputval - coreval
    else:
        return inputgoal
        
class DOTS(pygame.sprite.Sprite):
    def __init__(self,pos,xspd = 20,yspd = 20):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.color = (0,0,0)
        self.xspd = random.randrange(xspd/2,xspd)
        self.yspd = random.randrange(-yspd,yspd)
        self.image = pygame.Surface((20,20))
    def update(self):
        self.image.fill(self.color)
        self.pos = (self.pos[0]+self.xspd,self.pos[1]+self.yspd)
        self.xspd-=3
        if (self.color[0]>=230):
            self.kill()
        else:
            self.color = (self.color[0]+10,self.color[1],self.color[2])
        screen.blit(self.image,self.pos)
class EXPLOSION(pygame.sprite.Sprite):
    def __init__(self,pos,size,pain=0,shakeok=1,color=WHITE):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.pos = pos
        self.rad = 0
        self.pain = pain
        self.rect = pygame.rect.Rect((pos[0]-size,400),(size*2,2))
        if shakeok:
            bar.FUXXOR(40)
        self.color = color
    def update(self):
        pygame.draw.circle(screen,self.color,self.pos,self.size)
        pygame.draw.circle(screen,RED,self.pos,self.rad)
        self.rect = pygame.rect.Rect((self.pos[0]-self.size,400),
                                     (self.size*2,2))
        if(self.rad <= self.size):
            self.rad += 15
            self.size+= 10
        else:
            self.kill()

class FLOOR:
    def __init__(self):
        self.ypos = 420
        self.correcter = 1
        self.imagio = pygame.surface.Surface((WINSIZE[0],70))
        self.imagio.fill(BLACK)
    def update(self):
        self.ypos = correct(self.ypos,420,self.correcter)
        screen.blit(self.imagio, (0,self.ypos))
        if (self.correcter > 1):
            self.correcter-=1
    def FUXXOR(self,correction = 20):
        self.ypos = 410
        self.correcter = correction
bar = FLOOR()

class WARNING:
    def __init__(self):
        self.timer = 0
        self.warning = imglode("warning.bmp")
        self.warning = imgscale(self.warning,2)
        self.playok = True
        self.playcount = 0
        self.longenough = 0
    def update(self):
        if(self.longenough == 0):
            if not self.playok:
                self.playok = True
        else:
            self.longenough -= 1
        
        if self.playok:
            if(self.timer%20 == 0) and (self.timer > 0):
                fxplay(siren,soundstatus)
            if(self.timer > 55):
                screen.blit(self.warning,(550,200))
            elif(self.timer < 40) and (self.timer > 35):
                screen.blit(self.warning,(550,200))
            elif(self.timer < 20) and (self.timer > 15):
                screen.blit(self.warning,(550,200))
                self.longenough = 600
                self.playok = False
            if(self.timer > 0):
                self.timer-=1
    def sound(self):
        self.longenough == 600
        self.timer = 60
    def RESET(self):
        self.longenough == 600
        self.timer = 0
        self.playok = True
alarm = WARNING()

class LEVELCONTROL:
    def __init__(self):
        self.SubTimer = 0
        self.MasterTimer = 0
        #=========================
        self.curlevel = startlevel
        #=========================
        self.level = loadlevel('LEVEL'+str(self.curlevel))
        self.position = 0
        self.active = 0
        self.multi = False
        self.multimer = 0
        self.wait = 100
        
        #TEXT STUFF
        Texty = texty("REDENSEK.TTF",40)
        self.text = Texty.render(self.level[0],0,RED)
        self.textcount = 0
        self.textshow = True
        if(checkfile(self.level[3])):
            global currentsong
            currentsong = self.level[3]
        
        self.init = (300,50)
        Texty = texty("REDENSEK.TTF",60)
        self.ready1 = Texty.render("3",0,BLACK)
        self.ready2 = Texty.render("2",0,BLACK)
        self.ready3 = Texty.render("1",0,BLACK)
        self.ready4 = Texty.render("GO!",0,BLACK)
        self.endgame = False
        self.resettinglevel = False
        self.resetmusic = True
    def update(self):
        if self.active:
            self.MasterTimer+=1
            self.position = 0
            for event in self.level[1]:
                if(self.MasterTimer == event):
                    addin = self.level[2][self.position]
                    if((addin=='w') or (addin=='W')):
                        walmart.add(WALL(640,1))
                    elif((addin=='b') or (addin=='B')):
                        blastmart.add(BLASTWALL(1))
                    elif((addin=='g') or (addin=='G')):
                        mixer.music.fadeout(600)
                        bawls.add(GENERATOR())
                        self.active = 0
                    elif((addin=='3w') or (addin=='3W')):
                        self.active = 0
                        self.multi = True
                    elif((addin=='k') or (addin=='K')):
                        walmart.add(WALL(640,1,1))
                    elif((addin=='x') or (addin=='X')):
                        fxplay(genspawn,soundstatus)
                        GENES.add(MINIGEN())
                    elif((addin=='f') or (addin=='F')):
                        bawss.add(BOSS())
                    elif((addin=='p') or (addin=='P')):
                        powermart.add(POWERBALL())
                    elif((addin=='s') or (addin=='S')):
                        powermart.add(POWERSWORD())
                self.position += 1
                
        if self.textshow:
            self.textcount+=1
            if((self.textcount > 20)and
            (self.textcount < 60)):
                screen.blit(self.ready1,self.init)
            if((self.textcount > 60)and
            (self.textcount < 100)):
                screen.blit(self.ready2,self.init)
            if((self.textcount > 100)and
            (self.textcount < 140)):
                screen.blit(self.ready3,self.init)
            if((self.textcount > 140)and
            (self.textcount < 180)):
                screen.blit(self.ready4,self.init)
            
            #SOUNDS
            if((self.textcount == 20)or
            (self.textcount == 60)or
            (self.textcount == 100)):
                fxplay(ready1,soundstatus)
            if(self.textcount == 140):
                fxplay(ready2rock,soundstatus)
                
                if self.resetmusic:
                    mixer.music.stop()
                    musiclode(self.level[3])
                    self.resetmusic = False
                    musicplay(musicstatus)
                
            if(self.textcount < 100):
                screen.blit(self.text,(10,425))
            elif(self.textcount > 140):
                self.active = 1
                self.textcount = 0
                self.textshow = 0
        
        if self.multi:
            if(self.multimer == 1):
                walmart.add(WALL(640,1))
            elif(self.multimer == 15):
                walmart.add(WALL(640,1))
            elif(self.multimer == 30):
                walmart.add(WALL(640,1))
                self.multimer = 0
                self.multi = False
                self.active = 1
            self.multimer+=1
                
    def RESET(self,switch=False):
        if switch:
            self.curlevel += 1
            print "LEVEL"+str(self.curlevel)+".txt"
            #CHECK IF THE NEXT LEVEL FILE EXISTS
            if checkfile("LEVEL"+str(self.curlevel)+".txt","levels"):
                self.level = loadlevel('LEVEL'+str(self.curlevel))
                self.wait = 100
                self.SubTimer = 0
                self.MasterTimer = 0
                self.position = 0
                self.active = 0
                #TEXT STUFF
                Texty = texty("REDENSEK.TTF",40)
                self.text = Texty.render(self.level[0],0,RED)
                self.textcount = 0
                self.textshow = True
                self.multimer = 0
                self.multi = False
                
                #MUSIC SHIT
                if(checkfile(self.level[3])):
                    global currentsong
                    if(currentsong != self.level[3]):
                        mixer.music.fadeout(600)
                        self.resetmusic = True
                        currentsong = self.level[3]
            else:
                print "NO NEXT LEVEL"
                self.active = 0
                self.endgame = True
        else:
            self.endgame = False
            self.curlevel = startlevel
            self.level = loadlevel('LEVEL'+str(self.curlevel))
            self.wait = 100
            self.SubTimer = 0
            self.MasterTimer = 0
            self.position = 0
            self.active = 0
            self.resetmusic = True
            global bossdead
            bossdead = False
            #TEXT STUFF
            Texty = texty("REDENSEK.TTF",40)
            self.text = Texty.render(self.level[0],0,RED)
            self.textcount = 0
            self.textshow = True
            self.multimer = 0
            self.multi = False
    def RESETLEVEL(self):
        if not dude.alive:
            dude.alive = True
            dude.HP = 90
            dude.deathtimer = 200
        self.resettinglevel = True
        self.resetmusic = True
        self.wait = 100
        self.SubTimer = 0
        self.MasterTimer = 0
        self.position = 0
        self.active = 0
        alarm.playcount = 0
        alarm.longenough = 0
        global RED
        RED = (255,0,0)
        for l in lazor:
            l.kill()
        
        #TEXT STUFF
        Texty = texty("REDENSEK.TTF",40)
        self.text = Texty.render(self.level[0],0,RED)
        self.textcount = 0
        self.textshow = True
        
        #CLEANUP
        for g in bawls:
            g.kill()
        for b in bawss:
            b.kill()
remote = LEVELCONTROL()

class TEXT:
    def __init__(self,textname,color,goal,decay=0.5,side="RIGHT",size=20):
        Texty = texty("REDENSEK.TTF",size)
        self.newtext = Texty.render(textname,0,color)
        self.size = size
        self.color = color
        if(side == "LEFT"):
            self.pos = (-100,goal[1])
            self.initializer = 1
            self.move = 20
        elif(side == "RIGHT"):
            self.pos = (640,goal[1])
            self.initializer = 1
            self.move = 20
        self.goal = goal[0]
        self.dk = decay
    def update(self):
        if(self.pos[0] != self.goal):
            if(self.move > 1):
                self.move -= self.dk
            self.pos = (correct(self.pos[0],self.goal,self.move),self.pos[1])
        screen.blit(self.newtext,self.pos)
    def move(self,newvalue,move=5,decay=0.5):
        self.dk = decay
        if(newvalue > 0):
            self.goal = newvalue
            self.move = move
        elif(newvalue < 0):
            self.goal = newvalue
            self.move = move
    def changetext(self,newtext):
        Texty = texty("REDENSEK.TTF",self.size)
        self.newtext = Texty.render(newtext,0,self.color)
        
class FADED:
    def __init__(self,option=1,color=BLACK):
        if(option == 1):
            self.alphasz = 255
        else: self.alphasz = 0
        self.option = option
        self.surfnturf = pygame.Surface((640,480))
        self.color = color
    def update(self):
        screen.blit(self.surfnturf,(0,0))
        if(self.option == 1):
            if(self.alphasz > 0):
                self.alphasz -= 1
        else:
            if(self.alphasz < 255):
                self.alphasz += 1
        self.surfnturf.fill(self.color)
        self.surfnturf.set_alpha(self.alphasz)

def Starpos():
    return (WINSIZE[0], random.randrange(0,WINSIZE[1]-60))
Maine()
