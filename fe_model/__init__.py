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
    """Encodes game state."""
    def __init__(self):
        self.running = True

        self.ref = ref
        self.swidth = swidth
        self.sheight = sheight
        self.grid = {}
        self.character ={}
        self.turn = 0
        self.team1 = []
        self.team2 = []
        self.team3 = []
        self.teams = [self.team1, self.team2, self.team3]

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

        # Create players.
        self.populatePlayers()

    def populatePlayers(self):
        """This function creates all players and places them within teams."""
        self.character[(300,300)] = character.Warrior(self,location=(300,300), name='Julian', dodge = 5 , crit=5, team = 0)
        self.character[(300,350)] = character.Warrior(self,location=(300,350), name='David', dodge = 5 , crit=5, team = 1)
        self.character[(350,400)] = character.Archer(self,location=(350,400), name='Charlie', dodge = 5 , crit=5, team  = 1)
        self.character[(400,500)] = character.Archer(self,location=(400,500), name='Charlie', dodge = 5 , crit=5, team  = 2)
        
        for point in self.character:
            if self.character[point] != None:
                self.teams[self.character[point].team].append(self.character[point])

    def updateCharLocation(self, x, y):
        """'x' and 'y' are both input list of all locations along the path
        that the character is moving.  'x' and 'y' must be the same length.

        returns the direction the character should be facing after the move."""
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
        """This function allows for two characters to engage combat."""
        if not player1.hasAttacked:
            player1.battle(player2)
            if player1.CurrentHP == 0:
                self.character[player1.location]=None
            if player2.CurrentHP == 0:
                self.character[player2.location]=None

    # def team_turn_check(self, team = None):
    #     """
    #     Tests if a team can still move.
    #     Returns a boolean True or False depending on if the team can still move.
    #     """
    #     if len(team) == 0:
    #         return False
    #     else:
    #         for character in team:
    #             if character.can_move == True:
    #                 return True

    #         return False

    # def reset_can_move_to_team(self, choice):
    #     """Considers whose turn it is, and resets which team has moving abilities."""
    #     for character in self.teams[choice]:
    #         character.can_move = True

    def next_turn(self):
        """
        This function, when called, ends the turn of the current team.

        Inputs: the model 
        Outputs: None
        """
        self.turn += 1
        choice = teams[self.turn % 3]
        for character in choice:
            character.can_move = True
            character.hasAttacked = False

    def update(self):
        """
        update is constantly run to keep check of what happens during the game.

        Inputs: the model
        Outputs: None
        """
        for character in self.teams[self.turn%3]:
            character.available_locations()
            character.image = character.images[character.orient]
            if character.CurrentHP <= 0:
                character = None