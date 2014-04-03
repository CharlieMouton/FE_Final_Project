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
        
 # class Wall(Block):
 #  """ A basic wall structure that stops the character."""
 #   def __init__(self, model, x, y):
 #       Block.__init__(self, wallcolor, x, y)


class PyGamePathView:
    """
    Game viewer in pygame window.
    """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        MAP_WIDTH =  4
        MAP_HEIGHT =  4
        TILE_WIDTH =  64
        TILE_HEIGHT =  32
         
        for  x in  range (MAP_WIDTH):
             for  y in  range (MAP_HEIGHT):
                  tile =  MAP [y] [x]
                  tile_x =  (x - y) * (TILE_WIDTH / 2 ) + self . map_x
                  tile_y =  (x + y) * (TILE_HEIGHT / 2 ) + self . map_y
                  self . tiles [tile]. draw (tile_x, tile_y)



        # # We sweep through our world dictionary, drawing the world from the inputs.
        # for block in self.model.world:
        #     value = self.model.world[block]
        #     temp = pygame.Rect(value.x,value.y,value.side,value.side)
        #     pygame.draw.rect(self.screen, pygame.Color(value.color[0],value.color[1],value.color[2]),temp)
        # if model.endmode == True:
        #     # Draws save button.
        #     screen.blit(saveimage,(ref,3*ref))
        # else:
        #     temp = pygame.Rect(ref,3*ref,ref,ref)
        #     pygame.draw.rect(self.screen, pygame.Color(0,0,0),temp)

        # # Draws load button.
        # screen.blit(loadimage,(ref,5*ref))

        # if model.playmode == True:
        #     # Draws player.
        #     # temp = pygame.Rect(self.model.player.x,self.model.player.y,self.model.player.side,self.model.player.side)
        #     # pygame.draw.rect(self.screen, pygame.Color(playercolor[0],playercolor[1],playercolor[2]),temp)
        #     screen.blit(bob, (self.model.player.x, self.model.player.y))

        #     # Draws hidden rectangle.`````````````````````
        #     temp = pygame.Rect(3*ref,ref,len(model.palette)*2*ref,ref)
        #     pygame.draw.rect(self.screen, pygame.Color(0,0,0),temp)

        #     # Draws pause button.
        #     screen.blit(pausebutton,(ref,ref))
        # else:
        #     # Draws play button.
        #     screen.blit(playbutton,(ref,ref))

        pygame.display.update()

        # Keep time constant.
        clock.tick(60)



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