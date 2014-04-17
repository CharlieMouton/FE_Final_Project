import random
import pygame
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import ref

class Character:
    def __init__(self, model, name,level,HP,strength,defense,agility,intelligence,movement,xpToNextLevel, weaponrange,location):
        self.model = model
        self.name=name
        self.level=level
        self.MaxHP=HP
        self.CurrentHP=HP
        self.strength=strength
        self.defense=defense
        self.agility=agility
        self.intelligence=intelligence
        self.movement=movement
        self.movementleft=movement
        self.weaponrange=weaponrange
        self.location = location
        self.xp=0
        self.xpToNextLevel=xpToNextLevel
        self.availabilities = []
        """
        # Load respective image for playeri and scale.
        self.image = pygame.image.load('images/cavalry_unit.jpg') #.format(playeri)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
"""
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

    def available_locations(self):

        # Save current location
        current_positions = [self.location]

        # Iterate throughout the map to find available positions.
        for step in range(self.movement):
            # if len(current_positions) == 0:
            #     break
            for current_position in current_positions:
                # Possible refactoring for mapping.
                next_positions = self.surroundings(current_position)
                # next_positions = [block for block in blocks if block not in self.availabilities]


                # next_positions = [next_position for next_position in self.model.grid if ((next_position[0]-current_position[0])**2 + (next_position[1]-current_position[1])**2)**0.5 == self.model.ref and next_position]
                # next_positions = [next_position for next_position in self.model.grid if ((next_position[0]-current_position[0])**2 + (next_position[1]-current_position[1])**2)**0.5 == self.model.ref and next_position not in self.availabilities]
                # print current_position
                self.availabilities += [current_position]
                # print self.availabilities
                current_positions = next_positions

        return self.availabilities

    def surroundings(self, current_position):
        blocks = range(4)
        blocks[0] = (current_position[0] + self.model.ref, current_position[1])
        blocks[1] = (current_position[0] - self.model.ref, current_position[1])
        blocks[2] = (current_position[0], current_position[1] + self.model.ref)
        blocks[3] = (current_position[0], current_position[1] - self.model.ref)

        for block in blocks:
            if block[0] <= 0 or block[0] >= self.model.swidth or block[1] <= 0 or block[1] >= self.model.sheight:
                blocks.remove(block)

        print blocks
        return blocks


    # def available_locations_v1(self, location, movement):
    #     """
    #     This function takes in the map and character attributes to determine which spaces are available to move through.

    #     Returns: a list of available locations for inputted character.
    #     """
    #     # We need character location.
    #     # Using the location, map to ground and gather attributes (I.E does it take up a move? <- Actually unecessary.)
    #     # We also need character movement ability.
    #     # Do a range in a for loop based on the farness of the given movement range.
    #     # 4 possibilities. (Not the most effective.) ++ +- -+ --
    #     # If block not possible, do not add into next consideration.
    #     # We need a buffer.
        
    #     buffer_dict = [position for position in self.model.grid if ((position[0]-location[0])**2 + (position[1]-location[1])**2)**0.5 == self.model.ref and position not in self.availabilities]

    #     # Base case, everything is false.
    #     if len(buffer_dict) == 0 or movement == 0:
    #         # print "Hello!"
    #         return self.availabilities
        
    #     self.availabilities.append(location)
    #     # print self.availabilities
    #     for position in buffer_dict:
    #         if self.model.grid[position].resistance <= movement:
    #             self.available_locations(position, movement - self.model.grid[position].resistance)
    #         else:
    #             return self.availabilities
    
    def Move(self,newX,newY,movementleft):
        """Changes the x and y values for the location of the character."""
        self.movementleft=movementleft
        self.x=newX
        self.y=newY

    def Battle(self, player2):
        
        self.player2=player2
        #Player1 Attack
        if self.strength>=self.player2.defence:
            self.player2.CurrentHP-=(self.strength-self.player2.defence)
        else:
            pass
        if self.player2.CurrentHP<=0:
            self.xp+=3
            if self.xp>=self.xpToNextLevel:
                self.LEVEL
                self.xp=self.xp-self.xpToNextLevel
                self.xpToNextLevel+=5
            pass
        #Player2 Counterattack
        else:
            if self.weaponrange<=self.player2.weaponrange:
                if self.player2.strength>=self.defence:
                    self.CurrentHP-=(self.player2.strength-self.defence)
                else:
                    pass
            else:
                pass
        
            if self.CurrentHP<=0:
                self.player2.xp+=3
                if self.player2.xp>=self.player2.xpToNextLevel:
                    self.player2.LEVEL
                    self.player2.xp=self.player2.xp-self.player2.xpToNextLevel
                    self.player2.xpToNextLevel+=5
                pass
            #Possible Player1 second attack
            elif self.agility>(self.player2.agility*1.5):
                if self.strength>=self.player2.defence:
                    self.player2.CurrentHP-=2*(self.strength-self.player2.defence)
                else:
                    pass
            else:
                pass
            
            if self.player2.CurrentHP<=0:
                self.xp+=3
                if self.xp>=self.xpToNextLevel:
                    self.LEVEL
                    self.xp=self.xp-self.xpToNextLevel
                    self.xpToNextLevel+=5
                
        
    def __str__(self):
        return 'This character is a ' + str(self.name)+'\nat Level ' + str(self.level)+'\nwith ' + str(self.CurrentHP) + ' of your total ' + str(self.MaxHP) + ' HP\n' + str(self.strength) + ' Strength\n' +str(self.defense) + ' Defense \n' + str(self.agility) + ' Agility \n' + str(self.intelligence) + ' Intelligence \n' +'This character has ' + str(self.movementleft) + ' movement left from ' + str(self.movement) + ' movement \n' + str(self.weaponrange) + ' weapon range \n'+'and has ' + str(self.xp) + 'xp of ' + str(self.xpToNextLevel) + 'xp required to levelup!'
#        print 'This character is at ' + str(self.x)+ ' and ' + str(self.y)

# def Initiate(self,classtype,x,y):
#     if classtype.ascii_uppercase=='ARCHER':
#         self.newSpawn=Character(classtype.ascii_uppercase,1,6,2,1,3,3,2,3,x,y)
#     elif classtype.ascii_uppercase=='WARRIOR':
#         self.newSpawn=Character(classtype.ascii_uppercase,1,9,3,2,1,1,1,1,x,y)
#     elif classtype.ascii_uppercase=='HORSEMAN':
#         self.newSpawn=Character(classtype.ascii_uppercase,1,8,1,3,2,2,3,2,x,y)

class Archer(Character):
    def __init__(self, model, name='Archer', level=1, HP=6,strength=2,defense=1,agility=3,intelligence=3,movement=4, xpToNextLevel=100, weaponrange=3, location=(2*ref,3*ref)):
        Character.__init__(self, model, name,level,HP,strength,defense,agility,intelligence,movement,xpToNextLevel, weaponrange,location)
        self.image = pygame.image.load('fe_model/images/Bot_stationary.png')

class Warrior(Character):
    def __init__(self, x,y, name='Warrior', level=1, HP=9,strength=3,defense=2,agility=1,intelligence=1,movement=1, weaponrange=1):
        Character.__init__(self,name,level, HP,strength,defense,agility,intelligence,movement, weaponrange,x,y)

class Horseman(Character):
    def __init__(self, x,y, name='Horsemen', level=1, HP=8,strength=1,defense=3,agility=2,intelligence=2,movement=3, weaponrange=2):
        Character.__init__(self,name,level, HP,strength,defense,agility,intelligence,movement, weaponrange,x,y)
        
# if __name__ == "__main__":
#     test_character1 = Character.Initiate('Archer',100,100)
#     test_character1
#     test_character2 = Character.Initiate('Archer',100,100)
#     test_character2
#     test_character1.Battle(test_character1,test_character2)
#     test_character1
#     test_character2
