# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:40:05 2014

@author: jacob
"""
 
import Blocks

class Node(Blocks):
    """A node is a floor block of our character."""
    def __init__(self, model, x, y):
        Blocks.__init__(self, nodecolor, x, y)
        self.player = model.player