# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:35:38 2014

@author: julian
"""

import pygame
from pygame.locals import *
import time
import Characters
import World


if __name__ == '__main__':
    pygame.init()
    

    size = (640,480)
    screen = pygame.display.set_mode(size)
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()