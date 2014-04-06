# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:18:26 2014

@author: jacob
"""
import pygame
import Blocks

class Wall(Blocks.Blocks):
    """ A basic wall structure that stops the character."""
    def __init__(self, model, x, y):
        Blocks.__init__(self, wallcolor, x, y)