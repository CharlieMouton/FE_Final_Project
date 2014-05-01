import pygame
from pygame.locals import *
import os, sys, time
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.charselected = None

    def control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.model.running = False

            # Model
            if event.type == MOUSEBUTTONDOWN:
                if self.charselected != None:
                    self.move(event,self.charselected)
                else:
                    self.charselect(event)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if self.charselected != None:
                        if self.charselected.hasAttacked != True:
                            self.char_reset(self.charselected)
                # if event.key == K_SPACE:

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
            player.clickTwice=False
            if (temp_x,temp_y) in player.availabilities:
                # Update to that location.
                 player.orient = self.model.updateCharLocation([player.location[0],temp_x],[player.location[1],temp_y])

            else:
                # Remove character selection.
                self.charselected = None

        # Fighting situation.
        elif self.model.character[(temp_x,temp_y)] != None and self.model.character[(temp_x,temp_y)] != player:
            if int((abs(self.model.character[(temp_x,temp_y)].location[0]-player.location[0])+abs(self.model.character[(temp_x,temp_y)].location[1]-player.location[1]))/50)<=player.weaponrange:
                if player.clickTwice:
                    x = self.model.battleCall(player,self.model.character[(temp_x,temp_y)])
                    self.view.battlescreen = (player,self.model.character[(temp_x,temp_y)])
                    self.view.battlestats(self.view.battlescreen)
                    self.view.draw
                    if x != []:
                        for event in x:
                            if 'dodge' in event:
                                print 'dodge'
                                self.view.dodge(event[-1])
                            elif 'crit' in event:
                                print 'crit'
                                self.view.crit(event[-1]) 
                    player.clickTwice=False
                    player.movementleft=0
                    self.view.battlescreen = None
                else:
                    self.view.battlescreen = (player,self.model.character[(temp_x,temp_y)])
                    player.clickTwice=True
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
        """
        This function handles all keyboard events and translates the information into the model.
        """
        pass
        # if 
        # self.model.next_turn