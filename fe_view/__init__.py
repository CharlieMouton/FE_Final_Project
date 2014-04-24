import pygame
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *
from operator import itemgetter
from inputbox import *

class View:
    """
    Game viewer in pygame window.
    """
    def __init__(self, model, screen):
        self.size = size
        self.centerx = centerx
        self.centery = centery
        self.model= model
        self.screen = screen
        self.statselect = None

    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))

        ordgrid = sorted(self.model.grid, key=itemgetter(0,1))
        for point in ordgrid:
            tempobj = self.model.grid[point]
            self.screen.blit(tempobj.image,(CartToIso(point[0],point[1],0)[0]-50,CartToIso(point[0],point[1],0)[1]-10))

        if self.statselect != None:
            self.char_select(self.statselect)

        # This lines draws the characters in the wrong order.
        for point in self.model.character:
            if self.model.character[point] != None:
                self.screen.blit(self.model.character[point].image,(CartToIso(point[0],point[1],0)[0]-25,CartToIso(point[0],point[1],0)[1]-55))
            # HP = myfont.render("(%d)" % current.HP, 1, (255,255,0))
            # screen.blit(HP, (CartToIso(self.x,self.y,0)[0]-20,CartToIso(point[0],point[1],0)[1]+5))

        # This is my testing ground for visual stuff while I wait to characters to work right.
        # myfont = pygame.font.SysFont("times new roman", 16)
        # bot =  pygame.image.load('fe_model/images/Bot_stationary.png')
        # self.screen.blit(bot,(CartToIso(100,100,0)[0]-20,CartToIso(100,100,0)[1]+5))
        # statpage = pygame.image.load('fe_model/images/Statsblock_simple.png')
        # self.screen.blit(statpage,(900,530))
        # HP = myfont.render("40", 1, (0,0,0))
        # self.screen.blit(HP,(965,700))

        pygame.display.update()

    def char_select(self,character):   
        myfont = pygame.font.SysFont("arial", 16)
        statpage = pygame.image.load('fe_model/images/Statsblock_simple.png')
        self.screen.blit(statpage,(900,530))
        name = myfont.render(str(character.name), 1, (255,255,255))
        self.screen.blit(name,(910,535))
        # How do we access what class the character is?
        # classtype = myfont.render(str(_____), 1, (255,255,255))
        # self.screen.blit(classtype,(910,550))
        level = myfont.render(str(character.level), 1, (255,255,255))
        self.screen.blit(level,(938,567))
        xp = myfont.render(str(character.xp), 1, (255,255,255))
        self.screen.blit(xp,(959,567))
        currHP = myfont.render(str(character.CurrentHP), 1, (255,255,255))
        self.screen.blit(currHP,(935,582))
        MaxHP = myfont.render(str(character.MaxHP), 1, (255,255,255))
        self.screen.blit(MaxHP,(965,582))
        strength = myfont.render(str(character.strength), 1, (255,255,255))
        self.screen.blit(strength,(965,626))
        intelligence = myfont.render(str(character.intelligence), 1, (255,255,255))
        self.screen.blit(intelligence,(965,640))
        speed = myfont.render(str(character.agility), 1, (255,255,255))
        self.screen.blit(speed,(965,655))
        defense = myfont.render(str(character.defense), 1, (255,255,255))
        self.screen.blit(defense,(965,700))        
        for block in character.availabilities:
            pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0],block[1]),CartToIso(block[0]+50,block[1]),1)
            pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0]+50,block[1]),CartToIso(block[0]+50,block[1]+50),1)
            pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0]+50,block[1]+50),CartToIso(block[0],block[1]+50),1)
            pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0],block[1]+50),CartToIso(block[0],block[1]),1)
        # self.screen.blit(character.image,(CartToIso(character.location[0],character.location[1])[0]-20,CartToIso(character.location[0],character.location[1])[1]-40))

    def turn_display(self):
        """Displays the turn which the game is currently in."""
        myfont = pygame.font.SysFont("arial", 24)