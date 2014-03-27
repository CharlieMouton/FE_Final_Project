# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:35:38 2014

@author: julian
"""

import pygame
from pygame.locals import *
import time

class Characters(object):
    def __init__(self,name,level, HP,strength,defense,agility,intelligence,movement,weaponrange):
        self.name=name
        self.level=level
        self.HP=HP
        self.strength=strength
        self.defense=defense
        self.agility=agility
        self.intelligence=intelligence
        self.movement=movement
        self.weaponrange=weaponrange

        

        
class world(object):
    """Encodes game state."""
    def __init__(self):
        self.world = {}
        self.characters=pygame.sprite.Group()
        
        self.populateBlocks()
        self.populateCharaceters()
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                node = Node(self,x,y)
                self.world[(node.x,node.y)] = node
                
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                if x not in range(3*ref,swidth-3*ref,ref) or y not in range(3*ref,sheight-3*ref,ref):
                    boundary = Wall(self,x,y)
                    boundary.color = black
                    self.world[(boundary.x,boundary.y)] = boundary
                    
    
                    
class Blocks():
    """
    Creates a block for the game. Currently it inherits from pygame sprite because of pygame's inherent edge detection code.
    """
    def __init__(self, color, x, y):
        self.color = color
        self.side = ref
        self.x = x
        self.y = y
        self.left = self.x
        self.right = self.x + self.side
        self.top = self.y
        self.bottom = self.y + self.side
        
class Wall(Block):
    """ A basic wall structure that stops the character."""
    def __init__(self, model, x, y):
        Block.__init__(self, wallcolor, x, y)





if __name__ == '__main__':
    pygame.init()
    

    size = (640,480)
    screen = pygame.display.set_mode(size)
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()