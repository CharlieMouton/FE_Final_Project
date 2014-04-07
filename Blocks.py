import pygame
from Global_variables import *

class Blocks():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.length=SQUARELENGTH        
        
class Grass(pygame.sprite.Sprite):
    """This class encodes the state of a grass"""
    def __init__ (self,x,y):
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/grassunit.jpg')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
class Outeredge(pygame.sprite.Sprite):
    """This class encodes the state of the outer edge of the screen. It is just a black outer edge."""
    def __init__ (self,x,y):
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/black-square.jpg')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
            
class Forest(pygame.sprite.Sprite):
    """This class encodes the state of the outer edge of the screen. It is just a black outer edge."""
    def __init__ (self,x,y):
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/forestunit.jpg')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Fortress(pygame.sprite.Sprite):
    """This class encodes the state of the outer edge of the screen. It is just a black outer edge."""
    def __init__ (self,x,y):
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/Fortress.PNG')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y