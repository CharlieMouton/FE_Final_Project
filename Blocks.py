# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:18:56 2014

@author: jacob
"""

class Blocks():
    """
    Creates a block for the game. Currently it inherits from pygame sprite because of pygame's inherent edge detection code.
    """
    def __init__(self, color, x, y):
        self.color = color
        self.side = ref
        self.x = x
        self.y = y
        self.left = self.x
        self.right = self.x + self.side
        self.top = self.y
        self.bottom = self.y + self.side