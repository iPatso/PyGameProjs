import pygame, os, random


class Die():
    def __init__(self):
        self.value = 0
        self.faceValue = ""
        self.image = 0 # TODO: put pygame.image...
        
    def rollDie(self):
        self.value = random.randrange(0,6)
        if self.value == 0:
            self.faceValue = "ALL 2"
        elif self.value == 1:
            self.faceValue = "ALL 3"
        elif self.value == 2:
            self.faceValue = "ALL 4"
        elif self.value == 3:
            self.faceValue = "3"
        elif self.value == 4:
            self.faceValue = "4"
        elif self.value == 5:
            self.faceValue = "5"
        
        print "You rolled: ", self.faceValue