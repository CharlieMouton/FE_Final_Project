import pygame
import Blocks

class Wall(Blocks.Blocks):
    """ A basic wall structure that stops the character."""
    def __init__(self, model, x, y):
        Blocks.__init__(self, wallcolor, x, y)