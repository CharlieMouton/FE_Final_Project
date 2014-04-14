import block
import character
import wall
import os, sys
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
        self.character[(350,350)] = character.Archer(self,location=(350,350), name='Julian', movement=4)        
        # print test_model.grid
        # print test_model.grid[(500,500)]
        self.character[(350,350)].available_locations(self.Julian.location, self.Julian.movement)
        print self.character[(350,350)].availabilities
        print len(self.character[(350,350)].availabilities)
        print self.character[(350,350)]

    def delete_block(self, x, y):
        if (x, y) in self.grid:
            del self.grid[(x, y)]
        print len(self.grid)
    
    """
    def setupChar(self,classtype,x,y):
        self.character+=[character.Archer.]
    """    

if __name__ == "__main__":
    pygame.init()
    test_model = Model()

    running = True
    while running:
        # screen = pygame.display.set_mode(size)
        # screen.fill((255,255,255))
        for block in Julian.availabilities:
            pygame.draw.line(screen,(255,255,255),CartToIso(block[0],block[1]),CartToIso(block[0]+50,block[1]),1)
            pygame.draw.line(screen,(255,255,255),CartToIso(block[0]+50,block[1]),CartToIso(block[0]+50,block[1]+50),1)
            pygame.draw.line(screen,(255,255,255),CartToIso(block[0]+50,block[1]+50),CartToIso(block[0],block[1]+50),1)
            pygame.draw.line(screen,(255,255,255),CartToIso(block[0],block[1]+50),CartToIso(block[0],block[1]),1)

        for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
