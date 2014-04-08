import pygame
import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *

class Controller:
    def __init__(self, model):
        self.model = model

    def handle_mouse_event(self, event):
        mx, my = pygame.mouse.get_pos()
        print mx, my
        isoX, isoY = CartToIso(mx, my)

    def handle_keyboard_event(self, event):
        pass