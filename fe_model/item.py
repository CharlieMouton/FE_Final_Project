

class Item():
    def __init__(self, usable=False, canBeSold=False):
        self.usable=usable
        self.canBeSold=canBeSold
        
class Weapon(Item):
    def __init__(self, damage=0, durability=0, usable=True, canBeSold=True):
        Item.__init__(self, usable, canBeSold)
        self.damage=damage
        self.durability=durability
        
class Bow(Weapon):
    def __init__(self,weaponrange=2,UsedBy='Archer'):
        Weapon.__init__(self)
        self.UsedBy=UsedBy
        self.weaponrange=weaponrange
        
class Sword(Weapon):
    def __init__(self,weaponrange=1,UsedBy='Warrior'):
        Weapon.__init__(self)
        self.UsedBy=UsedBy
        self.weaponrange=weaponrange
        
class Lance(Weapon):
    def __init__(self,weaponrange=2,UsedBy='Horseman'):
        Weapon.__init__(self)
        self.UsedBy=UsedBy
        self.weaponrange=weaponrange