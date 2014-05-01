import pygame
from pygame.locals import *
import os, sys, time
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *

class Controller:
    """
    This class represents the PyGame controller.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.charselected = None

    def control(self):
        """
        control is the main function of Controller and delegates everything accordingly.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.model.running = False

            if event.type == MOUSEBUTTONDOWN:
                self.handle_mouse_event(event)
                
            if event.type == KEYDOWN:
                self.handle_keyboard_event(event)

    def handle_mouse_event(self, event):
        """
        This function handles all mouse events and translates the information into the model.
        """
        if self.charselected != None:
            self.move(event,self.charselected)
        else:
            self.charselect()

    def handle_keyboard_event(self, event):
        """
        This function handles all keyboard events and translates the information into the model.
        """
        if event.key == K_SPACE:
            self.model.next_turn()
        if event.key == K_ESCAPE:
            if self.charselected != None:
                if self.charselected.hasAttacked != True:
                    self.char_reset(self.charselected)

    def box_select(self, ):
        """
        Generates coordinates of a selected box after mouse selection.

        Inputs: Controller and click event.
        Outputs: corner x and y coordinates for the selected boxself.
        """
        mx, my = pygame.mouse.get_pos()
        cartX, cartY = IsoToCart(mx, my)
        corner_x = math.floor(cartX / ref) * ref
        corner_y = math.floor(cartY / ref) * ref

        return corner_x, corner_y

    def charselect(self):
        """
        """
        corner_x, corner_y = self.box_select()
        if self.model.character[(corner_x,corner_y)] !=  None:
            self.view.statselect = self.model.character[(corner_x,corner_y)]
            self.charselected = self.model.character[(corner_x,corner_y)]
            self.model.character[(corner_x,corner_y)].orient = 's'

    def move(self,event,player):
        # This should not be here. Refactor and move out of controller.
        mx, my = pygame.mouse.get_pos()
        cartX, cartY = IsoToCart(mx, my)
        temp_x = math.floor(cartX / ref) * ref
        temp_y = math.floor(cartY / ref) * ref
        
        if player.movementleft==0:
            self.view.statselect = self.model.character[(temp_x,temp_y)]
            self.charselected = self.model.character[(temp_x,temp_y)]
        else:
            # If the place the character is moving to is empty,
            if self.model.character[(temp_x,temp_y)] == None:
                # If the character can reach this block,
                player.clickTwice=False
                if (temp_x,temp_y) in player.availabilities:
                    # Update to that location.
                     player.orient = self.model.updateCharLocation([player.location[0],temp_x],[player.location[1],temp_y])
    
                else:
                    # Remove character selection.
                    self.charselected = None
    
            # Fighting situation.
            elif self.model.character[(temp_x,temp_y)] != None and self.model.character[(temp_x,temp_y)] != player:
                if int((abs(self.model.character[(temp_x,temp_y)].location[0]-player.location[0])+abs(self.model.character[(temp_x,temp_y)].location[1]-player.location[1]))/50) == player.weaponrange:
                    if player.clickTwice:
                        self.model.battleCall(player,self.model.character[(temp_x,temp_y)])
                        self.view.battlescreen = (player,self.model.character[(temp_x,temp_y)])
                        player.clickTwice=False
                        player.movementleft=0
                    else:
                        self.view.battlescreen = (player,self.model.character[(temp_x,temp_y)])
                        player.clickTwice=True
                else:
                    # Remove character selection.
                    self.view.statselect = self.model.character[(temp_x,temp_y)]
                    self.charselected = self.model.character[(temp_x,temp_y)]
                    self.model.character[(temp_x,temp_y)].orient = 's'

    def char_reset(self, character):
        """
        """
        character.orient = "s"
        self.model.updateCharLocation([character.location[0], character.o_location[0]], [character.location[1],character.o_location[1]])
        character.movementleft=character.movement