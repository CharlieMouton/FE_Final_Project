# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:45:44 2014

@author: julian
"""
import pygame
from pygame import mixer # Load the required library

def playmusic():

    pygame.mixer.init()
    pygame.mixer.music.load('FireEmblemmusic.mp3')
    pygame.mixer.music.play()
    

