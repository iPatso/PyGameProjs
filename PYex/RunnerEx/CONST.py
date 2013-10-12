#This document is not a standalone file, and is merely for
# personal development purposes. This file will contain constants
# for use in various projects. It is modular and only needs to be
# imported using <import CONST> and using CONST. commands

#IMPORT HELPERS
import pygame
import os
from pygame import *
import random

#PREPROCESSING
pygame.mixer.init()
clock = pygame.time.Clock()

#COLORS
RED = (255,0,0)
MAGENTA = (255, 56, 156)
ORANGE = (240, 240, 0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLU = (83,190,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127, 127, 127)
LGRAY = (200, 200, 200)
DGRAY = (55, 55, 55)

#VARIOUS DEFAULT VALUES
WINSIZE = (640,480)
FPS = 60

#PLACEHOLDER DUMMY FUNCTION
def derp():
    counter = 0
    while counter <= 50:
        counter+=1
        clock.tick(FPS)
    counter = 0
    print 'nothing to see here'
    
#Takes the name of a text sheet and returns a text-object
def texty(name,size):
	name = os.path.join("data", name)
	Texty = pygame.font.Font(name, size)
	return Texty
        
#HELPER FUNCTIONS
def imglode(file,folder="data",alpha=True):
    img = pygame.image.load(os.path.join(folder, file))
    if alpha:
        colorkey = img.get_at((0,0))
        img.set_colorkey(colorkey, RLEACCEL)
    return img.convert()

#Takes the file name for a given "sound" file (.wav,
# .ogg, or .mp3), returns a "sound" object. Sound file 
# must be located in "data" subfolder.
def FXLODE(file,volume=0.4,path="FX"):
    FX = pygame.mixer.Sound(os.path.join(path, file))
    print "Sound " + file + " successfully loaded"
    FX.set_volume(volume)
    return FX
def fxplay(thing,sure=True):
	if sure:
		thing.play()

#Takes the file name for a given "music" file (.mp3),
# and loads it for playback. Due to audio constraints,
# pygame restricts music playback to 1 stream, therefore
# musiclode() returns nothing. Music file imported must
# be in subfolder named "data"
def musiclode(file):
	if(checkfile(file)):
		pygame.mixer.music.load(os.path.join("data", file))
		print "music successfuly loaded: " + file
	else:
		print "Error, " + file + " does not exist."

# if sure is true, then music plays on infinite loop b/c amount = -1
def musicplay(sure=True,amount=-1):
    if sure: pygame.mixer.music.play((amount))
    print "playing.."
    
#Changes the name of the program on the toolbar
def caption(name):
    pygame.display.set_caption(name)

#To be used in conjunction with the imglode function, this
 #function takes a surface and increases the size by a
 #given amount, maintaining proportions
def imgscale(image, amount):
    newsize = image.get_size()
    newsize = (newsize[0]*amount, newsize[1]*amount)
    return pygame.transform.scale(image, newsize)

#This function takes an image and splits it into multiple
 #frames contained within the suface array that it returns.
 #The image is split up first by row, and then by column.
 #The coder must enter the name of the surface, as well as
 #the size of the length/width of the square
def getsub(image, size):
    sub = image.get_rect()
    subx = sub[2]/size
    suby = sub[3]/size
    dummy = (0,0)
    images = []
    while dummy[0] < suby:
        while dummy[1] < subx:
            newrect = (dummy[1]*size,
                       dummy[0]*size,
                       size, size)
            images.append(image.subsurface(newrect))
            dummy = (dummy[0], dummy[1]+1)
        dummy = (dummy[0]+1, 0)
    return images

#File handling function. All files read are assumed to be in
# text format, and are also assumed to be contained in a folder
# named "levels" which is in this directory. Second parameter
# determines the mode of opening the file. If left off, mode 
# defaults to "read"
def FILE(name,code='r'):
    return open(os.path.join("levels", name+'.txt'),code)

#String->Int or String->Float converter. If an error occurs
# the string is simply returned
def convertStr(s):
    try:
        ret = int(s)
    except ValueError:
        try:
            ret = float(s)
        finally:
            print "ERROR, INPUT IS NOT A NUMBER"
            return "FAIL"
    return ret

#Text-handling function for the easy and rapid development of
# levels for linearly-designed games or otherwise-choreographed
# scripted events within the game. This function takes only one
# parameter, the name of the file where the text document is
# located (e.g. 'LEVELS'). If successful, function returns a
# list in the form:
# list(level title, list of integers, list of letters, end title)
def loadlevel(textname):
    f = FILE(textname)
    z = f.readlines()
    title = z[0][0:(len(z[0])-1)]
    alternator = 1
    lineno = 1
    numbers = []
    letters = []
    returner = []
    for i in z[1:(len(z)-1)]:
        lineno+=1
        if alternator:
            number = convertStr(i[0:len(i)-1])
            if(number != "FAIL"):
                numbers.append(number*30)
            else:
                print "ERROR ON LINE %d: " % lineno
                print " LINE IS NOT A NUMBER"
                return False
            alternator = 0
        else:
            letter = i[0:len(i)-1]
            if((letter == 'w') or
			(letter=='b') or (letter=='B') or
			(letter=='g') or (letter=='G') or
			(letter=='f') or (letter=='F') or
			(letter=='3w')or (letter=='3W') or
			(letter=='k') or (letter=='K') or
			(letter=='x') or (letter=='X') or
			(letter=='p') or (letter=='P') or
			(letter=='s') or (letter=='S')):
                letters.append(i[0:len(i)-1])
            else:
                print "ERROR ON LINE %d: " % lineno
                print " LINE IS NOT A VALID LETTER"
                print " MUST BE 'w', 'b', '3w', 'k', 'g', 'x', 'f'"
                print "		'p', or 's'"
                return False
            alternator = 1
    returner.append(title)
    returner.append(numbers)
    returner.append(letters)
    returner.append(z[(len(z))-1])
    print returner
    return returner
   
#checkfile() is a function that takes two inputs:
# *A filename (e.g. "levels.txt", "scores.txt", et al)
# *A folder (e.g. "data", "music", et al)
#Using these parameters, function will return true if the
# file exists and false if it does not. For the sake of
# streamlining, folder will default to "data"
def checkfile(file,folder="data"):
	if os.path.isfile(os.path.join(folder, file)):
		return True
	else: return False
