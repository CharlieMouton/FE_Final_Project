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
        self.ref = ref
        self.swidth = swidth
        self.sheight = sheight
        self.grid = {}
        self.character ={}
        self.turn = 0
        self.phase = 0

        # Generate map.
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                node = block.Grass(x,y)
                self.grid[(x,y)] = node
                self.character[(x,y)]=None
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                if x not in range(3 * self.ref, self.swidth - 3*self.ref,self.ref) or y not in range(3*self.ref, self.sheight-3*self.ref, self.ref):
                    boundary = block.Outeredge(x,y)
                    self.grid[(boundary.x,boundary.y)] = boundary

        self.populatePlayers()

    def populatePlayers(self):
        self.character[(350,350)] = character.Archer(self,location=(350,350), name='Julian', movement=3)        
        self.character[(400,450)] = character.Warrior(self,location=(400,450), name='David', movement=4)
        self.character[(550,550)] = character.Archer(self,location=(550,550), name='Charlie', movement=5)

    def delete_block(self, x, y):
        if (x, y) in self.grid:
            del self.grid[(x, y)]
        print len(self.grid)

    def updateCharLocation(self, x, y):
        """'x' and 'y' are both input list of all locations along the path
        that the character is moving.  'x' and 'y' must be the same length."""
        for i in range(len(x)):
            if i>0:
                if self.character[(x[i],y[i])] == None:
                    self.character[(x[i],y[i])]=self.character[(x[i-1], y[i-1])]
                    self.character[(x[i],y[i])].location=(x[i],y[i])
                    moved=int((abs(x[i]-x[i-1])+abs(y[i]-y[i-1]))/50)
                    self.character[(x[i],y[i])].movementleft-=moved
                    self.character[(x[i-1],y[i-1])]=None

    def battleCall(self,player1, player2):
        player1.battle(player2)
        if player1.CurrentHP == 0:
            self.character[player1.location]=None
        if player2.CurrentHP == 0:
            self.character[player2.location]=None   

    def update(self):
        for point in self.character:
            if self.character[point] != None:
                self.character[point].available_locations()