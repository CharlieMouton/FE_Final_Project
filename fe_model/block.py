import pygame
<<<<<<< HEAD:Blocks.py
import Characters
=======
from variables import *
>>>>>>> ac2a6a03d49c06b4f51568bd8867005a5408a3da:fe_model/block.py

class Block(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.length=SQUARELENGTH       
        
#class Grass(pygame.sprite.Sprite):
class Grass(Block):
    
    """This class encodes the state of a grass"""
    def __init__ (self,x,y):
        """
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        """
        self.image = pygame.image.load('images/grass.png')
        super(Grass,self).__init__(x,y)
        self.movementcost=1
    
<<<<<<< HEAD:Blocks.py
    def interaction(self,character):
        self.character.movementleft-=1

class Outeredge(pygame.sprite.Sprite):
=======
#class Outeredge(pygame.sprite.Sprite):
class Outeredge(Block):
>>>>>>> ac2a6a03d49c06b4f51568bd8867005a5408a3da:fe_model/block.py
    """This class encodes the state of the outer edge of the screen. It is just a black outer edge."""
    def __init__ (self,x,y):
        """
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/black_square.jpg')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
<<<<<<< HEAD:Blocks.py
    
    def interaction(self):
        pass
        
class Forest(pygame.sprite.Sprite):
=======
        """
        self.image = pygame.image.load('images/water.png')
        super(Outeredge,self).__init__(x,y)
        self.movementcost=0
            
#class Forest(pygame.sprite.Sprite):
class Forrest(Block):
>>>>>>> ac2a6a03d49c06b4f51568bd8867005a5408a3da:fe_model/block.py
    """This class encodes the state of the outer edge of the screen. It is just a black outer edge."""
    def __init__ (self,x,y):
        """
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/forestunit.jpg')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        """
        self.image = pygame.image.load('images/grass.png')
        super(Forrest,self).__init__(x,y)
        self.movementcost=2
        
<<<<<<< HEAD:Blocks.py
    def interaction(self):
        pass
        
        
class Fortress(pygame.sprite.Sprite):
=======
#class Fortress(pygame.sprite.Sprite):
class Fortress(Block):
>>>>>>> ac2a6a03d49c06b4f51568bd8867005a5408a3da:fe_model/block.py
    """This class encodes the state of the outer edge of the screen. It is just a black outer edge."""
    def __init__ (self,x,y):
        """
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Fortress.PNG')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
<<<<<<< HEAD:Blocks.py
<<<<<<< HEAD
        
    def interaction(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
=======
>>>>>>> d5f5fc1b0f8526f573f94259772c1143084fba95
=======
        """
        self.image = pygame.image.load('images/grass.png')
        super(Fortress,self).__init__(x,y)
        self.movementcost=0
        
>>>>>>> ac2a6a03d49c06b4f51568bd8867005a5408a3da:fe_model/block.py
