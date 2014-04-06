# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:35:38 2014

@author: julian
"""
import pygame
from pygame.locals import *
import time
import Characters
import Wall
import World
from Scripts import *

class PyGamePathView:
    """
    Game viewer in pygame window.
    """
    def __init__(self,world,screen):
        self.model=world
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        MAP_WIDTH =  4
        MAP_HEIGHT =  4
        TILE_WIDTH =  64
        TILE_HEIGHT =  32
        point1 = (0,0)
        point2 = (100,100)
        pygame.draw.line(self.screen,pygame.Color(0,0,0),CartToIso(point1),CartToIso(point2),width=1)
         




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
        point1 = (300,300)
        point2 = (300,200)
        point3 = (200,200)
        point4 = (200,300)
        pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point1[0],point1[1]),CartToIso(point2[0],point2[1]),1)
        pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1]),CartToIso(point3[0],point3[1]),1)
        pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point3[0],point3[1]),CartToIso(point4[0],point4[1]),1)
        pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point4[0],point4[1]),CartToIso(point1[0],point1[1]),1)
         

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()