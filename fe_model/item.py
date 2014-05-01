

class Item():
    def __init__(self, usable=False, canBeSold=False):
        self.usable=usable
        self.canBeSold=canBeSold
        
class Weapon(Item):
    def __init__(self, weaponrange, damage=0, durability=0, usable=True, canBeSold=True):
        Item.__init__(self, usable, canBeSold)
        self.damage=damage
        self.durability=durability
        self.weaponrange=weaponrange
        
class Bow(Weapon):
    def __init__(self,weaponrange=2,UsedBy='Archer'):
        Weapon.__init__(self,weaponrange=weaponrange)
        self.UsedBy=UsedBy

        
class Sword(Weapon):
    def __init__(self,weaponrange=1,UsedBy='Warrior'):
        Weapon.__init__(self,weaponrange=weaponrange)
        self.UsedBy=UsedBy
        
class Lance(Weapon):
    def __init__(self,weaponrange=2,UsedBy='Horseman'):
        Weapon.__init__(self,weaponrange=weaponrange)
        self.UsedBy=UsedBy
        
