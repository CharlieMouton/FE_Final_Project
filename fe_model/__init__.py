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
        
    def Battle(self, player1,player2):
        
        self.player1=player1
        self.player2=player2
        
        if self.player1.strength>=self.player2.defence:
            self.player2.CurrentHP-=(self.player1.strength-self.player2.defence)
        else:
            pass
        if self.player2.CurrentHP<=0:
            pass
        else:
            if self.player1.weaponrange<=self.player2.weaponrange:
                if self.player2.strength>=self.player1.defence:
                    self.player1.CurrentHP-=(self.player2.strength-self.player1.defence)
                else:
                    pass
            else:
                pass
        
            if self.player1.CurrentHP<=0:
                pass
        
            elif self.player1.agility>(self.player2.agility*1.5):
                if self.player1.strength>=self.player2.defence:
                    self.player2.CurrentHP-=2*(self.player1.strength-self.player2.defence)
                else:
                    pass
            else:
                pass
        

if __name__ == "__main__":
    test_model = Model()