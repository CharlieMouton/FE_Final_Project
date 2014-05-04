import block
import character
import wall
import os, sys
import time
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *
from fe_view import *
from images import *

class Model:
    """
    This class encodes the game state.
    """
    def __init__(self):
        self.running = True

        self.ref = ref
        self.swidth = swidth
        self.sheight = sheight
        self.grid = {}
        self.character ={}
        self.turn = 0
        self.teams = []
        self.charselected = None
        self.statselect = None
        self.battlescreen = None
        self.strings_of_actions = []
        self.level = 1

        # Generate map.

        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                node = block.Grass(x,y)
                self.grid[(x,y)] = node
                self.character[(x,y)]=None
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                if x not in range(1 * self.ref, self.swidth - 1*self.ref,self.ref) or y not in range(1*self.ref, self.sheight-1*self.ref, self.ref):
                    boundary = block.Outeredge(x,y)
                    self.grid[(boundary.x,boundary.y)] = boundary

        if self.level == 0:
            for x in range(0, self.swidth, self.ref):
                for y in range(0, self.sheight, self.ref):
                    node = block.Grass(x,y)
                    self.grid[(x,y)] = node
                    self.character[(x,y)]=None
            for x in range(0, self.swidth, self.ref):
                for y in range(0, self.sheight, self.ref):
                    if x not in range(1 * self.ref, self.swidth - 1*self.ref,self.ref) or y not in range(1*self.ref, self.sheight-1*self.ref, self.ref):
                        boundary = block.Outeredge(x,y)
                        self.grid[(boundary.x,boundary.y)] = boundary

        if self.level == 1:
            #grass populate everything
            for x in range(0, self.swidth-2*ref, self.ref):
                for y in range(0, self.sheight-2*ref, self.ref):
                    self.grid[(x,y)] = block.Grass(x,y)
                    self.character[(x,y)]=None

            #add water
            for y in range(10):
                self.grid[(0,y*ref)] = block.Outeredge(0,y*ref)
            for x in range(2,6):
                self.grid[(x*ref,9*ref)] = block.Outeredge(x*ref,9*ref)
            for x in [6,7,8,10,11]:
                self.grid[(x*ref,8*ref)] = block.Outeredge(x*ref,8*ref)

            #add wall
            for x in [2,4,5,8,9,10]:
                self.character[(x*ref,2*ref)] = block.Wall(x*ref,2*ref)
            for y in [3,4,5,7,8]:
                self.character[(3*ref,y*ref)] = block.Wall(3*ref,y*ref)
            for y in [4,5]:
                self.character[(10*ref,y*ref)] = block.Wall(10*ref,y*ref)

            #add high grass
            # self.grid[(x*ref,9*ref)] = block.Outeredge(x*ref,9*ref)
            # self.grid[(x*ref,9*ref)] = block.Outeredge(x*ref,9*ref)

            #add bridge
            self.grid[(ref,9*ref)] = block.Bridge(ref,9*ref)
            self.grid[(9*ref,8*ref)] = block.Bridge(9*ref,8*ref)

        # Create players.
        self.populatePlayers()
        self.organize_teams()

    def populatePlayers(self):
        """
        This function creates all players and places them within teams.

        Inputs: Model
        Outputs: None
        """
        if self.level==0:
            
            self.character[(300,300)] = character.Warrior(self,location=(300,300), name='Julian', dodge = 5 , crit=5, team = 0)
            self.character[(300,350)] = character.Warrior(self,location=(300,350), name='David', dodge = 5 , crit=5, team = 1)
            self.character[(350,400)] = character.Archer(self,location=(350,400), name='Charlie', dodge = 5, crit=5, team  = 2)
            self.character[(400,500)] = character.Archer(self,location=(400,500), name='Jacob', dodge = 5 , crit=5, team  = 2)
        
        if self.level==1:
            self.character[(300,300)] = character.Warrior(self,location=(300,300), name='Julian', dodge = 5 , crit=5, team = 0)
            self.character[(300,350)] = character.Warrior(self,location=(300,350), name='David', dodge = 5 , crit=5, team = 1)
            self.character[(350,450)] = character.Archer(self,location=(350,400), name='Charlie', dodge = 5, crit=5, team  = 2)
            self.character[(400,500)] = character.Archer(self,location=(400,500), name='Jacob', dodge = 5 , crit=5, team  = 2)

    def organize_teams(self):
        """
        This function places all players into the right teams.

        Inputs: Model
        Outputs: None
        """
        for point in self.character:
            if self.character[point] != None:
                if str(self.character[point].__class__)[19:len(str(self.character[point].__class__))] != "ock.Wall'>":
                    if self.character[point].team >= len(self.teams):
                        for adding in range(self.character[point].team - len(self.teams) + 1):
                            self.teams.append([])
                    self.teams[self.character[point].team].append(self.character[point])

    def updateCharLocation(self, x, y):
        """
        This function updates the character location.

        Inputs: 'x' and 'y' are both input list of all locations along the path that the character is moving.  'x' and 'y' must be the same length.
        Outputs: the direction the character should be facing after the move."""
        for i in range(len(x)):
            if i>0:
                if self.character[(x[i],y[i])] == None:
                    self.character[(x[i],y[i])]=self.character[(x[i-1], y[i-1])]
                    self.character[(x[i],y[i])].location=(x[i],y[i])
                    moved=int((abs(x[i]-x[i-1])+abs(y[i]-y[i-1]))/50)
                    if abs(x[i]-x[i-1]) > abs(y[i]-y[i-1]):
                        if x[i]-x[i-1] < 0:
                            direction = 'n'
                        else:
                            direction = 's'
                    else:
                        if y[i]-y[i-1] < 0:
                            direction = 'e'
                        else:
                            direction = 'w'
                    self.character[(x[i],y[i])].movementleft-=moved
                    self.character[(x[i-1],y[i-1])]=None
                    return direction

    def next_turn(self):
        """
        This function, when called, ends the turn of the current team.

        Inputs: the model 
        Outputs: None
        """
        self.charselected = None
        for character in self.teams[self.turn % 3]:
            character.can_move = False

        self.turn += 1
        for character in self.teams[self.turn % 3]:
            character.can_move = True
            character.hasAttacked = False
            character.movementleft = character.movement

    def charselect(self, corner_x, corner_y):
        """
        """
        if self.character[(corner_x,corner_y)] !=  None:
            self.statselect = self.character[(corner_x,corner_y)]
            self.charselected = self.character[(corner_x,corner_y)]
            self.character[(corner_x,corner_y)].orient = 's'

    def char_reset(self, character):
        """
        """
        character.orient = "s"
        self.updateCharLocation([character.location[0], character.o_location[0]], [character.location[1],character.o_location[1]])
        character.movementleft=character.movement

    def move(self, player, corner_x, corner_y):
        if player.movementleft==0:
            self.statselect = self.character[(corner_x,corner_y)]
            self.charselected = self.character[(corner_x,corner_y)]
        else:
            # If the place the character is moving to is empty,
            if self.character[(corner_x,corner_y)] == None:
                player.clickTwice = False
                self.jump_to(player, corner_x, corner_y)
    
            # Fighting situation.
            elif self.character[(corner_x,corner_y)] != None and self.character[(corner_x,corner_y)] != player:
                self.complete_fighting_situation(player, corner_x, corner_y)

    def reset_charselect(self):
        """
        This function resets character selection.
        """
        self.charselected = None

    def jump_to(self, player, corner_x, corner_y):
        """
        This function jumps a character to the selected location.
        """
        # If the character can reach this block,
        if (corner_x,corner_y) in player.availabilities:
            # Update to that location.
            player.orient = self.updateCharLocation([player.location[0],corner_x],[player.location[1],corner_y])
        else:
            self.reset_charselect()

    def complete_fighting_situation(self, player, corner_x, corner_y):

        # If two players are within weaponrange,
        if int((abs(self.character[(corner_x,corner_y)].location[0]-player.location[0])+abs(self.character[(corner_x,corner_y)].location[1]-player.location[1]))/50) == player.weaponrange:

            # If the player has a clicktwice state,
            if player.clickTwice:
                if not player.hasAttacked:
                    self.strings_of_actions = player.battle(self.character[(corner_x, corner_y)])
                    if player.CurrentHP == 0:
                        self.character[player.location]=None
                    if self.character[(corner_x, corner_y)].CurrentHP == 0:
                        self.character[self.character[(corner_x, corner_y)].location]=None
                
                self.battlescreen = (player,self.character[(corner_x,corner_y)])

                player.clickTwice = False
                player.movementleft=0
                self.battlescreen = None
            
            else:
                self.battlescreen = (player,self.character[(corner_x,corner_y)])
                player.clickTwice=True
            
        else:
            # Remove character selection.
            self.statselect = self.character[(corner_x,corner_y)]
            self.charselected = self.character[(corner_x,corner_y)]
            self.character[(corner_x,corner_y)].orient = 's'
            
    def update(self):
        """
        update is constantly run to keep check of what happens during the game.

        Inputs: the model
        Outputs: None
        """
        for character in self.teams[self.turn%3]:
            if character.can_move == True:
                character.generate_availabilities()
            character.image = character.images[character.orient]
            if character.CurrentHP <= 0:
                character = None
        
        i=1
        for team in self.teams:
            numberofcharacter=0
            for character in team:
                if character in self.character.itervalues():
                    numberofcharacter+=1
                if numberofcharacter==0:
                    print "Team %s wins" %(i)
            i+=1
                    
                
                
            
            
            
   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
