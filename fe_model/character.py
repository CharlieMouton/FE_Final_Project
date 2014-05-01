import random
import pygame
import os, sys
import item
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import ref

class Character:
    def __init__(self, model, name,level,HP,strength,defense,agility,intelligence,movement,xpToNextLevel, weapontype,location, dodge = 5 , crit=5, team = 1, can_move = True, hasAttacked=False):
        self.model = model
        self.name = name
        
        self.level = level
        self.xp = 0
        self.xpToNextLevel = xpToNextLevel
        self.clickTwice = False
        self.MaxHP = HP
        self.CurrentHP = HP
        self.strength = strength
        self.defense = defense
        self.agility = agility
        self.intelligence = intelligence
        self.movement = movement
        self.movementleft = movement   
        self.weaponrange = weapontype.weaponrange
        self.dodge  =  dodge
        self.crit  =  crit

        self.location = location
        self.o_location = location

        self.availabilities = {}
        self.attackrange = {}
        self.can_move = can_move
        self.orient = 's'
        self.hasAttacked = hasAttacked            
            
        self.team = team

    def Level(self):
        """LvlUp is a list containing 7 components.  Each one matches up to the stats of the Characters Class."""
        LvlUp=[1,2,3,4,5,6,7]
        for i in range(len(LvlUp)):
            LvlUp[i]=random.randint(1,3)
        self.level+=1
        self.MaxHP+=LvlUp[0]
        self.CurrentHP+=LvlUp[0]
        self.strength+=LvlUp[1]
        self.defense+=LvlUp[2]
        self.agility+=LvlUp[3]
        self.intelligence+=LvlUp[4]
        self.movement+=LvlUp[5]
        self.weaponrange+=LvlUp[6]

    def generate_availabilities(self):
        """
        Generates a set of availabilities for a given character.

        Inputs: A character
        Outputs: That character's availabilities and attackrange
        """
        self.availabilities={}
        current_positions = {self.location: self.location}
        
        # Iterate throughout the map to find available positions.
        for step in range(int(self.movementleft)+int(self.weaponrange)):
            temp_buffer = {}
            for current_position in current_positions:
                blocks = self.surroundings(current_position)
                next_positions = [block for block in blocks if (block not in self.availabilities and self.model.grid[block].movementcost <= self.movementleft - step)]

                # if step< self.movementleft:
                #     self.availabilities += [current_position]
                #     temp_buffer += next_positions
                # else:
                #     self.attackrange += [current_position]
                #     temp_buffer += next_positions

                next_positions_dict = {}
                for next_position in next_positions:
                    next_positions_dict[next_position] = current_position

                self.availabilities[current_position] = current_positions[current_position]
                temp_buffer.update(next_positions_dict)
            
            current_positions = temp_buffer

        return self.availabilities, self.attackrange

    def surroundings(self, current_position):
        blocks = range(4)
        return_blocks = []
        blocks[0] = (current_position[0] + self.model.ref, current_position[1])
        blocks[1] = (current_position[0] - self.model.ref, current_position[1])
        blocks[2] = (current_position[0], current_position[1] + self.model.ref)
        blocks[3] = (current_position[0], current_position[1] - self.model.ref)

        for block in blocks:
            if block[0] >= 0 and block[0] < self.model.swidth and block[1] >= 0 and block[1] < self.model.sheight:
                return_blocks += [block]

        return return_blocks

    def battle(self, player2):
        
        self.hasAttacked=True        
        
        self.player2=player2
        #Player1 Attack
        if self.strength>=self.player2.defense:
            if random.randint(1,100) <= self.player2.dodge:
                pass
            else:
                if random.randint(1,100) <= self.crit:
                    self.player2.CurrentHP-=(self.strength-self.player2.defense)*3
                else:
                    self.player2.CurrentHP-=(self.strength-self.player2.defense)
        if self.player2.CurrentHP<=0:
            self.xp+=3
            if self.xp>=self.xpToNextLevel:
                self.LEVEL
                self.xp=self.xp-self.xpToNextLevel
                self.xpToNextLevel+=5
        #Player2 Counterattack
        else:
            if self.weaponrange<=self.player2.weaponrange:
                if self.player2.strength>=self.defense:
                    if random.randint(1,100) <= self.dodge:
                        pass
                    else:
                        if random.randint(1,100) <= self.player2.crit:
                            self.CurrentHP-=(self.player2.strength-self.defense)*3
                        else:
                            self.CurrentHP-=(self.player2.strength-self.defense)
            if self.CurrentHP<=0:
                self.player2.xp+=3
                if self.player2.xp>=self.player2.xpToNextLevel:
                    self.player2.LEVEL
                    self.player2.xp=self.player2.xp-self.player2.xpToNextLevel
                    self.player2.xpToNextLevel+=5
                pass
            #Possible Player1 second attack
            elif self.agility>(self.player2.agility*1.5):
                if random.randint(1,100) <= self.player2.dodge:
                    pass
                else:
                    if random.randint(1,100) <= self.crit:
                        self.player2.CurrentHP-=(self.strength-self.player2.defense)*3
                    else:
                        self.player2.CurrentHP-=(self.strength-self.player2.defense)
            if self.player2.CurrentHP<=0:
                self.xp+=3
                if self.xp>=self.xpToNextLevel:
                    self.LEVEL
                    self.xp=self.xp-self.xpToNextLevel
                    self.xpToNextLevel+=5
         
    def __str__(self):
        return 'This character is a ' + str(self.name)+'\nat Level ' + str(self.level)+'\nwith ' + str(self.CurrentHP) + ' of your total ' + str(self.MaxHP) + ' HP\n' + str(self.strength) + ' Strength\n' +str(self.defense) + ' Defense \n' + str(self.agility) + ' Agility \n' + str(self.intelligence) + ' Intelligence \n' +'This character has ' + str(self.movementleft) + ' movement left from ' + str(self.movement) + ' movement \n' + str(self.weaponrange) + ' weapon range \n'+'and has ' + str(self.xp) + 'xp of ' + str(self.xpToNextLevel) + 'xp required to levelup!'

class Archer(Character):
    def __init__(self, model, name='Archer', level=1, HP=6,strength=3,defense=1,agility=3,intelligence=3,movement=3, xpToNextLevel=100, weapontype=item.Bow(), location=(2*ref,3*ref), dodge = 5 , crit=5, team=1, can_move = False):
        Character.__init__(self, model, name,level,HP,strength,defense,agility,intelligence,movement,xpToNextLevel, weapontype,location, dodge, crit, team)
        self.images = {'s':pygame.image.load('fe_model/images/Anne.png'),'w':pygame.transform.flip(pygame.image.load('fe_model/images/Anne.png'),True,False),'e':pygame.transform.flip(pygame.image.load('fe_model/images/Anne_Back.png'),True,False),'n':pygame.image.load('fe_model/images/Anne_Back.png')}
        self.image = self.images[self.orient]

class Warrior(Character):
    def __init__(self, model, name='Warrior', level=1, HP=9,strength=2,defense=2,agility=1,intelligence=1,movement=3, xpToNextLevel=100, weapontype=item.Sword(), location=(2*ref,3*ref), dodge = 5 , crit=5, team=1, can_move = False):
        Character.__init__(self,model, name,level, HP,strength,defense,agility,intelligence,movement, xpToNextLevel,weapontype,location, dodge, crit, team)
        self.images = {'s':pygame.image.load('fe_model/images/Bot_stationary.png'),'w':pygame.transform.flip(pygame.image.load('fe_model/images/Bot_stationary.png'),True,False),'n':pygame.transform.flip(pygame.image.load('fe_model/images/bot_Stationary_Back.png'),True,False),'e':pygame.image.load('fe_model/images/bot_Stationary_Back.png')}
        self.image = self.images[self.orient]

class Horseman(Character):
    def __init__(self, x,y, name='Horsemen', level=1, HP=8,strength=1,defense=3,agility=2,intelligence=2,movement=3, xpToNextLevel=100, weapontype=item.Lance(), location=(2*ref,3*ref), dodge = 5 , crit=5, team=1, can_move = False):
        Character.__init__(self,model, name,level, HP,strength,defense,agility,intelligence,movement, xpToNextLevel,weapontype,location, dodge, crit, team)
        self.images = {'s':pygame.image.load('fe_model/images/Anne.png'),'w':pygame.transform.flip(pygame.image.load('fe_model/images/Anne.png'),True,False),'n':pygame.transform.flip(pygame.image.load('fe_model/images/Anne_Back.png'),True,False),'e':pygame.image.load('fe_model/images/Anne_Back.png')}
        self.image = self.images[self.orient]
