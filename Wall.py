# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:18:26 2014

@author: jacob
"""
import pygame

SQUARELENGTH=50
WHITE = (255, 255, 255)

class Wall(pygame.sprite.Sprite):
    """This class encodes the state of a wall"""
    def __init__ (self,x,y):
        #Call the parent class (Sprite) constructor     
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/castle-wall.jpg')
        self.image = pygame.transform.scale(self.image, (SQUARELENGTH, SQUARELENGTH))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
