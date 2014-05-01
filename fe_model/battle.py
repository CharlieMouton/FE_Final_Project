import Character

class Battle(object):
    def __init__(self, player1, player2):
        self.player1=player1
        self.player2=player2
        """if self.player1.agility<=self.player2.agility*1.5:"""
        if self.player1.strength>=self.player2.defence:
            self.player2.CurrentHP-=(self.player1.strength-self.player2.defence)
        else:
            pass
        if self.player2.CurrentHP==0:
            pass
        else:
            if self.player1.weaponrange>=self.player2.weaponrange:
                if self.player2.strength>=self.player1.defence:
                    self.player1.CurrentHP-=(self.player2.strength-self.player1.defence)
                else:
                    pass
            else:
                pass
        
            elif self.player1.agility>(self.player2.agility*1.5):
                if self.player1.strength>=self.player2.defence:
                    self.player2.CurrentHP-=2*(self.player1.strength-self.player2.defence)
                else:
                    pass