import pygame
import os, sys, time
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
        self.battlescreen = None

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
                if str(self.model.character[point].__class__)[19:len(str(self.model.character[point].__class__))] != "ock.Wall'>":
                    self.screen.blit(self.model.character[point].image,(CartToIso(point[0],point[1],0)[0]-25,CartToIso(point[0],point[1],0)[1]-55))
                else:
                    self.screen.blit(self.model.character[point].image,(CartToIso(point[0],point[1],0)[0]-50,CartToIso(point[0],point[1],0)[1]-40))

        # for point in ordchar:  
        #     tempobj = self.model.character[point]    
        #     if self.model.character[point] != None:
        #         if str(tempobj.__class__)[19:len(str(tempobj.__class__))] == "ock.Wall'>":
        #             self.screen.blit(tempobj.image,(CartToIso(point[0],point[1],0)[0]-50,CartToIso(point[0],point[1],0)[1]-60))

        if self.battlescreen != None:
            self.battlestats(self.battlescreen)
            # HP = myfont.render("(%d)" % current.HP, 1, (255,255,0))
            # screen.blit(HP, (CartToIso(self.x,self.y,0)[0]-20,CartToIso(point[0],point[1],0)[1]+5))

        pygame.display.update()

    def attackanim(self,char1,char2):
        for n in range(10):
            self.screen.blit(char1.image,char1.location[0])

    def crit(self,charnum):
        critpopup = pygame.image.load("fe_model/images/crit.png")
        print charnum
        if str(charnum) == '1':
            self.screen.blit(critpopup,(425,500))
        elif str(charnum) == '2':
            self.screen.blit(critpopup,(700,500))
        pygame.display.update()

    def dodge(self,charnum):
        dodgepopup = pygame.image.load("fe_model/images/dodge.png")
        if charnum == '1':
            self.screen.blit(dodgepopup,(425,530))
        elif charnum == '2':
            self.screen.blit(dodgepopup,(700,530))
        pygame.display.update()

    def battlestats(self,(char1,char2)):
        myfont = pygame.font.SysFont("arial", 16)
        battlestatpage = pygame.image.load("fe_model/images/BattleScreen.png")
        self.screen.blit(battlestatpage,(400,625))
        healthblock = pygame.image.load("fe_model/images/healthblock.png")
        emptyhealthblock = pygame.image.load("fe_model/images/emptyhealthblock.png")
        if char1 == None or char2 == None:
            self.battlescreen = None
            return
        name = myfont.render(str(char1.name), 1, (0,0,0))
        self.screen.blit(name,(400+120,625+25))
        hit = myfont.render(str(100-char2.dodge), 1, (0,0,0))
        self.screen.blit(hit,(400+50,625+2))
        dmg = myfont.render(str(char1.strength-char2.defense), 1, (0,0,0))
        self.screen.blit(dmg,(400+50,625+17))
        crit = myfont.render(str(char1.crit), 1, (0,0,0))
        self.screen.blit(crit,(400+50,625+32))
        CurrHP = myfont.render(str(char1.CurrentHP), 1, (255,255,255))
        self.screen.blit(CurrHP,(400+25,625+65))
        for n in range(char1.MaxHP):
            self.screen.blit(emptyhealthblock,(400+50+4*n,625+70))
        for n in range(char1.CurrentHP):
            self.screen.blit(healthblock,(400+50+4*n,625+70))
        
        name = myfont.render(str(char2.name), 1, (0,0,0))
        self.screen.blit(name,(400+300,625+25))
        hit = myfont.render(str(100-char1.dodge), 1, (0,0,0))
        self.screen.blit(hit,(400+450,625+2))
        dmg = myfont.render(str(char2.strength-char1.defense), 1, (0,0,0))
        self.screen.blit(dmg,(400+450,625+17))
        crit = myfont.render(str(char2.crit), 1, (0,0,0))
        self.screen.blit(crit,(400+450,625+32))
        CurrHP = myfont.render(str(char2.CurrentHP), 1, (255,255,255))
        self.screen.blit(CurrHP,(400+270,625+65))
        for n in range(char2.MaxHP):
            self.screen.blit(emptyhealthblock,(400+300+4*n,625+70))
        for n in range(char2.CurrentHP):
            self.screen.blit(healthblock,(400+300+4*n,625+70))

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
        dodge = myfont.render(str(character.dodge), 1, (255,255,255))
        self.screen.blit(dodge,(965+258,670-530))
        crit = myfont.render(str(character.crit), 1, (255,255,255))
        self.screen.blit(crit,(965+258,685-530))
        defense = myfont.render(str(character.defense), 1, (255,255,255))
        self.screen.blit(defense,(965+258,700-530))        
        for block in character.availabilities:
            bluesq = pygame.image.load('fe_model/images/BlueSquare.png')
            self.screen.blit(bluesq,(CartToIso(block[0],block[1])[0]-47,CartToIso(block[0],block[1])[1]+1))
        for block in character.attackrange:
            redsq = pygame.image.load('fe_model/images/RedSquare.png')
            self.screen.blit(redsq,(CartToIso(block[0],block[1])[0]-47,CartToIso(block[0],block[1])[1]+1))   

    def turn_display(self):
        """Displays the turn which the game is currently in."""
        myfont = pygame.font.SysFont("arial", 24)