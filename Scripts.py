# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:29:22 2014

@author: jacob
"""
def CartToIso(x,y):
	"""Takes an x and y pair and converts them to isometric position."""
	centerx = 640/2
	centery = 480/2
	isox = x - y+centerx
	isoy = (x+y)/2
	return (isox,isoy)
