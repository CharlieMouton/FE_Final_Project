# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 14:16:43 2014

@author: jacob
"""
class Characters(object):
    def __init__(self,name,level, HP,strength,defense,agility,intelligence,movement,weaponrange,x,y):
        self.name=name
        self.level=level
        self.HP=HP
        self.strength=strength
        self.defense=defense
        self.agility=agility
        self.intelligence=intelligence
        self.movement=movement
        self.weaponrange=weaponrange
        self.x=x
        self.y=y
        
    def LEVEL(self,LvlUp):
        """LvlUp is a list containing 7 components.  Each one matches up to the stats of the Characters Class."""
        self.level+=1
        self.HP+=LvlUp[0]
        self.strength+=LvlUp[1]
        self.defense+=LvlUp[2]
        self.agility+=LvlUp[3]
        self.intelligence+=LvlUp[4]
        self.movement+=LvlUp[5]
        self.weaponrange+=LvlUp[6]
    
    def Move(self,newX,newY):
        """Changes the x and y values for the location of the character."""
        self.x=newX
        self.y=newY