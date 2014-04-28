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
            self.model.character[(temp_x,temp_y)].orient = 's'
        # self.model.delete_block(temp_x, temp_y)`
        #return [temp_x,temp_y]

    def move(self,event,player):
        # This should not be here. Refactor and move out of controller.
        mx, my = pygame.mouse.get_pos()
        cartX, cartY = IsoToCart(mx, my)
        temp_x = math.floor(cartX / ref) * ref
        temp_y = math.floor(cartY / ref) * ref

        # If the place the character is moving to is empty,
        if self.model.character[(temp_x,temp_y)] == None:
            # If the character can reach this block,
            if (temp_x,temp_y) in player.availabilities:
                # Update to that location.
                 player.orient = self.model.updateCharLocation([player.location[0],temp_x],[player.location[1],temp_y])

            else:
                # Remove character selection.
                self.charselected = None

        # Fighting situation.
        elif self.model.character[(temp_x,temp_y)] != None and self.model.character[(temp_x,temp_y)] != player:
            if int((abs(self.model.character[(temp_x,temp_y)].location[0]-player.location[0])+abs(self.model.character[(temp_x,temp_y)].location[1]-player.location[1]))/50)<=player.weaponrange:
                self.model.battleCall(player,self.model.character[(temp_x,temp_y)])
            else:
                # Remove character selection.
                self.view.statselect = self.model.character[(temp_x,temp_y)]
                self.charselected = self.model.character[(temp_x,temp_y)]
                self.model.character[(temp_x,temp_y)].orient = 's'

    def char_reset(self, character):
        print character.o_location
        print character.location
        character.orient = "s"
        self.model.updateCharLocation([character.location[0], character.o_location[0]], [character.location[1],character.o_location[1]])
        character.movementleft=character.movement        
        
    def handle_keyboard_event(self, event):
        pass