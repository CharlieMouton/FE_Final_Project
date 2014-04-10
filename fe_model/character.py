import random


class Character(object):
    def __init__(self, model, name,level, HP,strength,defense,agility,intelligence,movement, weaponrange,x,y):
        self.model = model
        self.name=name
        self.level=level
        self.MaxHP=HP
        self.CurrentHP=HP
        self.strength=strength
        self.defense=defense
        self.agility=agility
        self.intelligence=intelligence
        self.movement=movement
        self.movementleft=movement
        self.weaponrange=weaponrange
        self.x=x
        self.y=y
        self.xp=0

    def Level(self):
        """LvlUp is a list containing 7 components.  Each one matches up to the stats of the Characters Class."""
        LvlUp=[1,2,3,4,5,6,7]
        for i in range(len(LvlUp)):
            LvlUp[i]=random.randint(1,3)
        self.level+=1
        self.MaxHP+=LvlUp[0]
        self.CurrentHP+=LvlUp[0]
        self.strength+=LvlUp[1]
        self.defense+=LvlUp[2]
        self.agility+=LvlUp[3]
        self.intelligence+=LvlUp[4]
        self.movement+=LvlUp[5]
        self.weaponrange+=LvlUp[6]
    
    def Move(self,newX,newY,movementleft):
        """Changes the x and y values for the location of the character."""
        self.movementleft=movementleft
        self.x=newX
        self.y=newY

# def Initiate(self,classtype,x,y):
#     if classtype.ascii_uppercase=='ARCHER':
#         self.newSpawn=Character(classtype.ascii_uppercase,1,6,2,1,3,3,2,3,x,y)
#     elif classtype.ascii_uppercase=='WARRIOR':
#         self.newSpawn=Character(classtype.ascii_uppercase,1,9,3,2,1,1,1,1,x,y)
#     elif classtype.ascii_uppercase=='HORSEMAN':
#         self.newSpawn=Character(classtype.ascii_uppercase,1,8,1,3,2,2,3,2,x,y)

class Archer(Character):
    def __init__(self, x,y, name='Archer', level=1, HP=6,strength=2,defense=1,agility=3,intelligence=3,movement=2, weaponrange=3):
        Character.__init__(self, name, level, HP,strength,defense,agility,intelligence,movement, weaponrange,x,y)

# class Warrior(Character):
#     def __init__(self, name='Archer', level=1, HP=6,strength=2,defense=1,agility=3,intelligence=3,movement=2, weaponrange=3,x,y):
#         Character.__init__(self,name,level, HP,strength,defense,agility,intelligence,movement, weaponrange,x,y)

# class Horseman(Character):
#     def __init__(self, name='Archer', level=1, HP=6,strength=2,defense=1,agility=3,intelligence=3,movement=2, weaponrange=3,x,y):
#         Character.__init__(self,name,level, HP,strength,defense,agility,intelligence,movement, weaponrange,x,y)