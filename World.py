# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:17:48 2014

@author: jacob
"""
import Wall

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
                    boundary = Wall.Wall(self,x,y)
                    boundary.color = black
                    self.world[(boundary.x,boundary.y)] = boundary
                    