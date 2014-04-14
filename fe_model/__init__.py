import block
import character
import wall
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *
from images import *

class Model:
    """Encodes game state."""
    def __init__(self):
        self.ref = ref
        self.swidth = swidth
        self.sheight = sheight
        self.grid = {}
        # self.characters=pygame.sprite.Group()
        self.character =[]
        # self.populateBlocks()
        # self.populateCharaceters()
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                node = block.Grass(x,y)
                self.grid[(x,y)] = node  
        for x in range(0, self.swidth, self.ref):
            for y in range(0, self.sheight, self.ref):
                if x not in range(3 * self.ref, self.swidth - 3*self.ref,self.ref) or y not in range(3*self.ref, self.sheight-3*self.ref, self.ref):
                    boundary = block.Outeredge(x,y)
                    self.grid[(boundary.x,boundary.y)] = boundary

    def delete_block(self, x, y):
        if (x, y) in self.grid:
            del self.grid[(x, y)]
        print len(self.grid)
    
    def setupChar(self,classtype,x,y):
        self.character=[character.Character.Initiate(classtype,x,y)]
        

if __name__ == "__main__":
    test_model = Model()
    Julian = character.Archer(model=test_model,location=(500,500), name='Julian', movement=6)
    # print Julian.name
    # print Julian.location
    # print test_model.grid
    # print test_model.grid[(500,500)]
    Julian.available_locations(Julian.location, Julian.movement)
    print Julian.availabilities
    print len(Julian.availabilities)
