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
        # self.characters=pygame.sprite.Group()
        self.character ={}
        # self.populateBlocks()
        # self.populateCharaceters()
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

        self.character[(550,550)] = character.Archer(self,location=(550,550), name='Julian', movement=15)
        self.character[(550,550)].available_locations()

    def populatePlayers(self):
        pass
        # self.character[(,)]=character.Archer(self,location=(150,150), name='Julian', movement=4)

    def delete_block(self, x, y):
        if (x, y) in self.grid:
            del self.grid[(x, y)]
        print len(self.grid)

    def UpdateCharLocation(self, x, y):
        """'x' and 'y' are both input list of all locations along the path 
        that the character is moving.  'x' and 'y' must be the same length."""
        for i in range(len(x)):
            if i>0:
                self.character[(x(i),y(i))]=self.character(x(i-1), y(i-1))
                self.character[(x(i-1),y(i-1))]=None
                view.draw()
                time.sleep(.25)

    def CallBattle(self, x1, y1, x2, y2):
        self.character(x1,y1).Battle(self.character(x2,y2))    
    """
    def setupChar(self,classtype,x,y):
        self.character+=[character.Archer.]
    """