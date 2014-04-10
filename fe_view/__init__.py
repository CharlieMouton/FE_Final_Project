import pygame
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *
from images import *
from operator import itemgetter
from inputbox import *

class View:
    """
    Game viewer in pygame window.
    """
    def __init__(self, model, screen):
        self.size = size
        self.centerx = centerx
        self.centery = centery
        self.model= model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))
        MAP_WIDTH =  4
        MAP_HEIGHT =  4
        TILE_WIDTH =  64
        TILE_HEIGHT =  32

        ordgrid = sorted(self.model.grid, key=itemgetter(0,1))
        for point in ordgrid:
            tempobj = self.model.grid[point]
            self.screen.blit(tempobj.image,(CartToIso(point[0],point[1],0)[0]-50,CartToIso(point[0],point[1],0)[1]-10))
        bot =  pygame.image.load('images/Bot_stationary.png')
        self.screen.blit(bot,(CartToIso(0,0,0)[0]-20,CartToIso(0,0,0)[1]+5))
        for person in self.model.character:
            self.screen.blit(person.image,CartToIso(self.x,self.y,0)[0]-20,CartToIso(point[0],point[1],0)[1]+5)

        pygame.display.update()

if __name__ == '__main__':
    pass

sys.path.remove(lib_path)