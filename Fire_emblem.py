# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:35:38 2014

@author: julian
"""

import pygame
from pygame.locals import *
import time

class Model():
    def update(self):
        pass
  
class World(object):
    """Encodes game state."""
    pass
    # def __init__(self):
        # self.world = {}
        # self.characters=pygame.sprite.Group()
        
        # self.populateBlocks()
        # self.populateCharaceters()
        # for x in range(0,swidth,ref):
        #     for y in range(0,sheight,ref):
        #         node = Node(self,x,y)
        #         self.world[(node.x,node.y)] = node
                
        # for x in range(0,swidth,ref):
        #     for y in range(0,sheight,ref):
        #         if x not in range(3*ref,swidth-3*ref,ref) or y not in range(3*ref,sheight-3*ref,ref):
        #             boundary = Wall(self,x,y)
        #             boundary.color = black
        #             self.world[(boundary.x,boundary.y)] = boundary


class Character(object):
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
                                    
class Block():
    """
    Creates a block for the game. Currently it inherits from pygame sprite because of pygame's inherent edge detection code.
    """
    def __init__(self, x, y, side):
        self.color = color
        self.side = ref
        self.x = x
        self.y = y

class Grass(Block):
    pass
    # def __init__(self,)

class Wall(Block):
    """ A basic wall structure that stops the character."""
    def __init__(self, model, x, y):
        Block.__init__(self, wallcolor, x, y)

class View():
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0,255,255))
        pygame.display.update()

class Controller():
    def __init__(self, model):
        self.model = model

    def handle_event(self,event):
        pass

if __name__ == '__main__':
    pygame.init()
    
    size = (1024,768)
    print size[0]
    screen = pygame.display.set_mode(size) 

    model = Model()
    view = View(model, screen)
    controller = Controller(model)

    running = True
    while running:
        # screen.fill(pygame.Color(0,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_event(event)

        model.update()
        view.draw()
        time.sleep(.01)

    pygame.quit()