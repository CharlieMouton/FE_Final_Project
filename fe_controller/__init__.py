import pygame
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_mouse_event(self, event):
        mx, my = pygame.mouse.get_pos()
        cartX, cartY = IsoToCart(mx, my)
        temp_x = math.floor(cartX / ref) * ref
        temp_y = math.floor(cartY / ref) * ref
        print temp_x, temp_y
        if self.model.character[(temp_x,temp_y)]!= None:
            self.view.statselect = self.model.character[(temp_x,temp_y)]
        # self.model.delete_block(temp_x, temp_y)
        #return [temp_x,temp_y]

        
    def handle_keyboard_event(self, event):
        pass