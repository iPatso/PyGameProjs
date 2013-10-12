import pygame, os
from Team import Team

class Player():
    def __init__(self, side, playerNum):
        self.team = Team(side, playerNum)
        self.actions = 0
        self.side = side
        self.playerNum = playerNum
        
    def teamUpdate(self):
        self.team.update()
        