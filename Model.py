# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:53:54 2014

@author: jacob
"""
import World
import Characters

class Model(self):
    def __init__(self):
        self.Character = Characters.Characters(self,'Player',1,2,3,4,5,6,7,8)
        self.world = {}
        self.palette = {}
        self.playmode = False
        self.endmode = False
        self.choice = None