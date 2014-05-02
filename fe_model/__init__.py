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
        self.level = 0

        # Generate map.
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
            for x in range(0, self.swidth, self.ref):
                for y in range(0, self.sheight, self.ref):
                    self.grid[(x,y)] = block.Grass(x,y)
                    self.character[(x,y)]=None

            #add water
            for y in range(9):
                self.grid[(0,y*ref)] = block.Outeredge(0,y*ref)
            for x in range(2,5):
                self.grid[(x*ref,9*ref)] = block.Outeredge(x*ref,9*ref)
            for x in [6,7,8,10,11]:
                self.grid[(x*ref,8*ref)] = block.Outeredge(x*ref,8*ref)

            #add wall
            for x in [2,4,5,8,9,10]:
                self.grid[(x*ref,2*ref)] = block.Outeredge(x*ref,2*ref)
            for y in [4,5,6,8,9]:
                self.grid[(3,y*ref)] = block.Outeredge(3,y*ref)
            for y in [4,5]:
                self.grid[(10,y*ref)] = block.Outeredge(10,y*ref)



            print self.grid



        # Create players.
        self.populatePlayers()
        self.organize_teams()

    def populatePlayers(self):
        """
        This function creates all players and places them within teams.

        Inputs: Model
        Outputs: None
        """
        self.character[(300,300)] = character.Warrior(self,location=(300,300), name='Julian', dodge = 5 , crit=5, team = 0)
        self.character[(300,350)] = character.Warrior(self,location=(300,350), name='David', dodge = 5 , crit=5, team = 1)
        self.character[(350,400)] = character.Archer(self,location=(350,400), name='Charlie', dodge = 5, crit=5, team  = 2)
        self.character[(400,500)] = character.Archer(self,location=(400,500), name='Charlie', dodge = 5 , crit=5, team  = 2)

    def organize_teams(self):
        """
        This function places all players into the right teams.

        Inputs: Model
        Outputs: None
        """
        for point in self.character:
            if self.character[point] != None:
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

    def battleCall(self,player1, player2):
        """
        This function allows for two characters to engage combat.

        Inputs: Model, two characters
        Outputs: None
        """
        if not player1.hasAttacked:
            x = player1.battle(player2)
            if player1.CurrentHP == 0:
                self.character[player1.location]=None
            if player2.CurrentHP == 0:
                self.character[player2.location]=None
            print x
            return x

    def next_turn(self):
        """
        This function, when called, ends the turn of the current team.

        Inputs: the model 
        Outputs: None
        """
        for character in self.teams[self.turn % 3]:
            character.can_move = False

        self.turn += 1
        for character in self.teams[self.turn % 3]:
            character.can_move = True
            character.hasAttacked = False
            character.movementleft = character.movement
        
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
