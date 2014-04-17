import pygame
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.charselected = None

    def charselect(self, event):
        mx, my = pygame.mouse.get_pos()
        cartX, cartY = IsoToCart(mx, my)
        temp_x = math.floor(cartX / ref) * ref
        temp_y = math.floor(cartY / ref) * ref
        print temp_x, temp_y
        if self.model.character[(temp_x,temp_y)]!= None:
            self.view.statselect = self.model.character[(temp_x,temp_y)]
            self.charselected = self.model.character[(temp_x,temp_y)]
        # self.model.delete_block(temp_x, temp_y)`
        #return [temp_x,temp_y]

     

    def move(self,event,player):
        mx, my = pygame.mouse.get_pos()
        cartX, cartY = IsoToCart(mx, my)
        temp_x = math.floor(cartX / ref) * ref
        temp_y = math.floor(cartY / ref) * ref
        if self.model.character[(temp_x,temp_y)] == None:
            if (temp_x,temp_y) in player.availabilities:
                self.model.updateCharLocation([player.location[0],temp_x],[player.location[1],temp_y])
            else:
                self.charselected = None
        elif self.model.character[(temp_x,temp_y)] != None and self.model.character[(temp_x,temp_y)] != player:
            if int((abs(self.model.character[(temp_x,temp_y)].location[0]-player.location[0])+abs(self.model.character[(temp_x,temp_y)].location[1]-player.location[1]))/50)<=player.weaponrange:
                self.model.battle(player,self.model.character[(temp_x,temp_y)])
                    
            

        
    def handle_keyboard_event(self, event):
        pass