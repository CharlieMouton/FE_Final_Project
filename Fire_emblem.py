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
import Blocks
from Scripts import *

from operator import itemgetter

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
        self.Character = Characters.Characters(self,'Player',1,2,3,4,5,6,7,8,9)
#        self.populateBlocks()
#        self.populateCharaceters()
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                node = (x,y)
                self.grid[(x,y)] = node  
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                if x not in range(3*ref,swidth-3*ref,ref) or y not in range(3*ref,sheight-3*ref,ref):
                    boundary = Blocks.Outeredge(x,y)
                    self.grid[(boundary.rect.x,boundary.rect.y)] = boundary

class PathView:
    """
    Game viewer in pygame window.
    """
    def __init__(self,world,screen):
        self.model= world
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))
        MAP_WIDTH =  4
        MAP_HEIGHT =  4
        TILE_WIDTH =  64
        TILE_HEIGHT =  32


        point1 = (300,300,0)
        point2 = (300+50,300,0)
        point3 = (300+50,300+50,0)
        point4 = (300,300+50,0)

        # Drawing a cube
        # point1 = (point[0],point[1],0)
        # point2 = (point[0]+50,point[1],0)
        # point3 = (point[0]+50,point[1]+50,0)
        # point4 = (point[0],point[1]+50,0)
        # point5 = (300+50,300,-50)
        # point6 = (300+50,300+50,-50)
        # point7 = (300,300+50,-50)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point1[0],point1[1],point1[2]),CartToIso(point2[0],point2[1],point2[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1],point2[2]),CartToIso(point3[0],point3[1],point3[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point3[0],point3[1],point3[2]),CartToIso(point4[0],point4[1],point4[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point4[0],point4[1],point4[2]),CartToIso(point1[0],point1[1],point1[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1],point2[2]),CartToIso(point5[0],point5[1],point5[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point5[0],point5[1],point5[2]),CartToIso(point6[0],point6[1],point6[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point6[0],point6[1],point6[2]),CartToIso(point3[0],point3[1],point3[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point6[0],point6[1],point6[2]),CartToIso(point7[0],point7[1],point7[2]),1)
        # pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point7[0],point7[1],point7[2]),CartToIso(point4[0],point4[1],point4[2]),1)
        ordgrid =[]
        for point in self.model.grid:
            # ordgrid.append(point)
            point1 = (point[0],point[1],0)
            point2 = (point[0]+50,point[1],0)
            point3 = (point[0]+50,point[1]+50,0)
            point4 = (point[0],point[1]+50,0)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point1[0],point1[1],point1[2]),CartToIso(point2[0],point2[1],point2[2]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1],point2[2]),CartToIso(point3[0],point3[1],point3[2]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point3[0],point3[1],point3[2]),CartToIso(point4[0],point4[1],point4[2]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point4[0],point4[1],point4[2]),CartToIso(point1[0],point1[1],point1[2]),1)

        ordgrid = sorted(self.model.grid, key=itemgetter(0,1))
        # print ordgrid
        grass = pygame.image.load('grass.png')
        for point in ordgrid:
            screen.blit(grass,(CartToIso(point[0],point[1],0)[0]-50,CartToIso(point[0],point[1],0)[1]-50))

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    
    world=world()
    size = (700,500)
    screen = pygame.display.set_mode(size)
    running = True
    view=PathView(world,screen)
    
    while running:
        screen.fill(pygame.Color(255,255,255))       
        view.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        
        pygame.display.update()

    pygame.quit()