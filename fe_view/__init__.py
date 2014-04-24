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
        ordchar = sorted(self.model.character, key=itemgetter(0,1))
        for point in ordchar:
            if self.model.character[point] != None:
                self.screen.blit(self.model.character[point].image,(CartToIso(point[0],point[1],0)[0]-25,CartToIso(point[0],point[1],0)[1]-55))
            # HP = myfont.render("(%d)" % current.HP, 1, (255,255,0))
            # screen.blit(HP, (CartToIso(self.x,self.y,0)[0]-20,CartToIso(point[0],point[1],0)[1]+5))

        pygame.display.update()

    def char_select(self,character):   
        myfont = pygame.font.SysFont("arial", 16)
        statpage = pygame.image.load('fe_model/images/Statsblock_simple.png')
        self.screen.blit(statpage,(900+258,530-530))
        name = myfont.render(str(character.name), 1, (255,255,255))
        self.screen.blit(name,(910+258,535-530))
        classtype = myfont.render(str(character.__class__)[19:len(str(character.__class__))], 1, (255,255,255))
        self.screen.blit(classtype,(910+258,550-530))
        level = myfont.render(str(character.level), 1, (255,255,255))
        self.screen.blit(level,(938+258,567-530))
        xp = myfont.render(str(character.xp), 1, (255,255,255))
        self.screen.blit(xp,(959+258,567-530))
        currHP = myfont.render(str(character.CurrentHP), 1, (255,255,255))
        self.screen.blit(currHP,(935+258,582-530))
        MaxHP = myfont.render(str(character.MaxHP), 1, (255,255,255))
        self.screen.blit(MaxHP,(965+258,582-530))
        strength = myfont.render(str(character.strength), 1, (255,255,255))
        self.screen.blit(strength,(965+258,626-530))
        intelligence = myfont.render(str(character.intelligence), 1, (255,255,255))
        self.screen.blit(intelligence,(965+258,640-530))
        speed = myfont.render(str(character.agility), 1, (255,255,255))
        self.screen.blit(speed,(965+258,655-530))
        defense = myfont.render(str(character.defense), 1, (255,255,255))
        self.screen.blit(defense,(965+258,700-530))        
        for block in character.availabilities:
            bluesq = pygame.image.load('fe_model/images/BlueSquare.png')
            self.screen.blit(bluesq,(CartToIso(block[0],block[1])[0]-47,CartToIso(block[0],block[1])[1]+1))
            
            # Drawing an array of squares
            # pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0],block[1]),CartToIso(block[0]+50,block[1]),1)
            # pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0]+50,block[1]),CartToIso(block[0]+50,block[1]+50),1)
            # pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0]+50,block[1]+50),CartToIso(block[0],block[1]+50),1)
            # pygame.draw.line(self.screen,(255,0,0),CartToIso(block[0],block[1]+50),CartToIso(block[0],block[1]),1)

    def turn_display(self):
        """Displays the turn which the game is currently in."""
        myfont = pygame.font.SysFont("arial", 24)