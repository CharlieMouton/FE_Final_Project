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

        self.character[(350,350)] = character.Archer(self,location=(350,350), name='Julian', movement=10)        
        # print test_model.grid
        # print test_model.grid[(500,500)]
        self.character[(350,350)].available_locations()
        # print self.character[(350,350)].surroundings((0,0))
        # print self.character[(350,350)].availabilities
        # print len(self.character[(350,350)].availabilities)
        # print self.character[(350,350)]


    def populatePlayers(self):
        pass
        # self.character[(,)]=character.Archer(self,location=(150,150), name='Julian', movement=4)

    def delete_block(self, x, y):
        if (x, y) in self.grid:
            del self.grid[(x, y)]
        print len(self.grid)

    def UpdateCharLocation(self, x, y):
        for i in range(len(x)):
	    for i in range(len(y)):
		self.character(x(0),y(0)).movementleft-=self.grid(x(i),y(i)).movementcost
	        if self.character(x(0),y(0)).movementleft>=0:
	             self.character[(x(-1),y(-1))]=self.character(x(0), y(0))
	             self.character[(x(0),y(0))]=None
    

    def CallBattle(self, x1, y1, x2, y2):
        self.character(x1,y1).Battle(self.character(x2,y2))    
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
        # for block in Julian.availabilities:
        #     pygame.draw.line(screen,(255,255,255),CartToIso(block[0],block[1]),CartToIso(block[0]+50,block[1]),1)
        #     pygame.draw.line(screen,(255,255,255),CartToIso(block[0]+50,block[1]),CartToIso(block[0]+50,block[1]+50),1)
        #     pygame.draw.line(screen,(255,255,255),CartToIso(block[0]+50,block[1]+50),CartToIso(block[0],block[1]+50),1)
        #     pygame.draw.line(screen,(255,255,255),CartToIso(block[0],block[1]+50),CartToIso(block[0],block[1]),1)

        for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
