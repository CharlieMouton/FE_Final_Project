import pygame
from pygame.locals import *
import time

import Characters
import Blocks
from Scripts import *
from Global_variables import *

class Model:
    """Encodes game state."""
    def __init__(self):
        self.grid = {}
        # self.characters=pygame.sprite.Group()
        self.Character = Characters.Characters('Player',1,2,3,4,5,6,7,350,350)
        # self.populateBlocks()
        # self.populateCharaceters()
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                node = (x,y)
                self.grid[(x,y)] = node  
        for x in range(0,swidth,ref):
            for y in range(0,sheight,ref):
                if x not in range(3*ref,swidth-3*ref,ref) or y not in range(3*ref,sheight-3*ref,ref):
                    boundary = Blocks.Outeredge(x,y)
                    self.grid[(boundary.rect.x,boundary.rect.y)] = boundary
        # print self.grid

    def update(self, mx, my):
        pass

class View:
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
        for point in self.model.grid:
            # Please refactor into something more intuitive.
            point1 = (point[0],point[1])
            point2 = (point[0]+ref,point[1])
            point3 = (point[0]+ref,point[1]+ref)
            point4 = (point[0],point[1]+ref)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point1[0],point1[1]),CartToIso(point2[0],point2[1]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point2[0],point2[1]),CartToIso(point3[0],point3[1]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point3[0],point3[1]),CartToIso(point4[0],point4[1]),1)
            pygame.draw.line(screen,pygame.Color(0,0,0),CartToIso(point4[0],point4[1]),CartToIso(point1[0],point1[1]),1)

        pygame.display.update()

class Controller:
    def __init__(self, model):
        self.model = model

    def handle_mouse_event(self, event):
        mx, my = pygame.mouse.get_pos()
        print mx, my
        print CartToIso(mx, my)
        # self.model.update(mx,my)

    def handle_keyboard_event(self, event):
        pass

if __name__ == '__main__':
    pygame.init()
    
    model = Model()
    screen = pygame.display.set_mode(size)
    running = True
    view=View(model,screen)
    controller = Controller(model)
    
    while running:
        screen.fill(pygame.Color(255,255,255))       
        view.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == MOUSEBUTTONDOWN:
                controller.handle_mouse_event(event)
            # KEYBOARDBUTTON is probably a lie. Fix below.
            # elif event.type == KEYBOARDDOWN:
            #     controller.handle_keyboard_event(event)
        time.sleep(.01)

    pygame.quit()