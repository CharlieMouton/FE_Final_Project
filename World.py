# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:17:48 2014

@author: jacob
"""
import Wall
import Node
import Characters

# Define colors.
black = 0,0,0
white = 255,255,255
red = 255,0,0   # This is the side reference for creating the whole game grid.
playercolor = 255,56,25
nodecolor = 217,217,217
wallcolor = 130,130,130
lavacolor = 217,15,0
icecolor = 94,227,255
mudcolor = 127,87,52
reversecolor = 145,33,196
startcolor = 255,235,62
endcolor = 63,255,62
playbuildcolor = 0,0,0

# Set screen sizes and declare ref for future reference for blocks.
ref = 50
swidth = 14*ref
sheight = 10*ref




class world(object):
    """Encodes game state."""
    def __init__(self):
        self.grid = {}
        self.characters=pygame.sprite.Group()
        self.Character = Characters.Characters(self,'Player',1,2,3,4,5,6,7,8)
        self.populateBlocks()
        self.populateCharaceters()
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                node = Node.Node(self,x,y)
                self.grid[(node.x,node.y)] = node
                
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                if x not in range(3*ref,swidth-3*ref,ref) or y not in range(3*ref,sheight-3*ref,ref):
                    boundary = Wall.Wall(self,x,y)
                    boundary.color = black
                    self.grid[(boundary.x,boundary.y)] = boundary
                    