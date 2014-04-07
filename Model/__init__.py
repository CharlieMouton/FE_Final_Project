import Characters
import Wall
import Blocks

class Model:
    """Encodes game state."""
    def __init__(self):
        self.grid = {}
        # self.characters=pygame.sprite.Group()
        self.Character = Characters.Characters(self,'Player',1,2,3,4,5,6,7,350,350)
        # self.populateBlocks()
        # self.populateCharaceters()
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                node = (x,y)
                self.grid[(x,y)] = node  
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                if x not in range(3*ref,swidth-3*ref,ref) or y not in range(3*ref,sheight-3*ref,ref):
                    boundary = Blocks.Outeredge(x,y)
                    self.grid[(boundary.rect.x,boundary.rect.y)] = boundary
        # print self.grid

    def update(self, mx, my):
        pass