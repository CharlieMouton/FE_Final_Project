import pygame

import character
from variables import *


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
        self.image = pygame.image.load('fe_model/images/grass.png')
        super(Grass,self).__init__(x,y)
        self.movementcost = 1
    
    def interaction(self,character):
        self.character.movementleft-=1

class HighGrass(Grass):
<<<<<<< HEAD
    def __init__(self, x, y):
        super(HighGrass, self).__init__(x,y)
        
        self.movementcost=2
        
    def interaction(self,character):
        self.character.movementleft-=2
        self.character.dodge+=5
=======
    def __init__(self,x,y):
        self.image = pygame.image.load("fe_model/images/grass.png")
        self.imagesupp = pygame.image.load("fe_model/images/highgrass.png")
        super(HighGrass,self).__init__(x,y)

class Bridge(Grass):
    def __init__(self,x,y):
        super(Bridge,self).__init__(x,y)
        self.image = pygame.image.load("fe_model/images/bridge.png")

>>>>>>> fa6d21eedd1ae482c8db42a0a35a20b122848631


        

class Water(Block):
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

        """
        self.image = pygame.image.load('fe_model/images/water_new.png')
        super(Water,self).__init__(x,y)
        self.movementcost = 100
        
#class Forest(pygame.sprite.Sprite):
class Forrest(Block):
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
        self.image = pygame.image.load('fe_model/images/grass.png')
        super(Forrest,self).__init__(x,y)
        self.movementcost=2
        
    def interaction(self):
        pass
        
        
#class Fortress(pygame.sprite.Sprite):
class Fortress(Block):
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
        """
        self.image = pygame.image.load('fe_model/images/grass.png')
        super(Fortress,self).__init__(x,y)
        self.movementcost=0


class Wall(Block):
    """ A basic wall structure that stops the character."""
    def __init__(self, x, y):
        Block.__init__(self, x, y)
        self.image = pygame.image.load('fe_model/images/wall.png')
        self.movementcost = 100
        