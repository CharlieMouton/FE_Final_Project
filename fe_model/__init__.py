import block
import character
import wall
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *
from images import *

def available_locations(model, character):
    """
    This function takes in the map and character attributes to determine which spaces are available to move through.

    Returns: a list of available locations for inputted character.
    """
    # We need character location.
    # Using the location, map to ground and gather attributes (I.E does it take up a move? <- Actually unecessary.)
    # We also need character movement ability.
    # Do a range in a for loop based on the farness of the given movement range.
    # 4 possibilities. (Not the most effective.) ++ +- -+ --
    # If block not possible, do not add into next consideration.
    # We need a buffer.
    
    location = character.current_position    # This will be a tuple of x and y.
    move_range = character.move_range    # This will be a range represented as an int.

    buffer_dict = [position for position in model.grid.iteritems() if ((position[0]-location[0])**2 + (position[1]-location[1])**2)**0.5 == model.ref]
    availabilities = []

    # Base case, everything is false.
    if len(buffer_dict) == 0:
        return availabilities
    else:
        availabilities.append(location)
        for position in buffer_dict:
            look_around(position, move_range - grid[position].resistance)

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
        

# if __name__ == "__main__":
#     test_model = Model()
#     Julian = Archer(model=test_model,x=5,y=5, name='Julian')
#     print Julian
#     print Julian.name