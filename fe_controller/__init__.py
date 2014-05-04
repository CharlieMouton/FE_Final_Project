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
        # self.model.charselected = None

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
        corner_x, corner_y = self.box_select()
        if self.model.charselected != None:
            print 1
            self.model.move(self.model.charselected, corner_x, corner_y)
            print 2

        else:
            self.model.charselect(corner_x, corner_y)

    def handle_keyboard_event(self, event):
        """
        This function handles all keyboard events and translates the information into the model.
        """
        if event.key == K_SPACE:
            self.model.next_turn()
        if event.key == K_ESCAPE:
            if self.model.charselected != None:
                if self.model.charselected.hasAttacked != True:
                    self.model.char_reset(self.model.charselected)
            else:
                pass

    def box_select(self):
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