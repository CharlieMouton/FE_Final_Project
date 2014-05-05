import block
import character
import wall
import os, sys
import time
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
from var_scripts import *
from fe_view import *
from images import *

class Model:
    """
    This class encodes the game state.
    """
    def __init__(self):
        self.running = True
        self.ref = ref
        self.swidth = swidth
        self.sheight = sheight
        self.grid = {}
        self.character ={}
        self.otherObject={}
        self.turn = 0
        self.teams = []
        self.charselected = None
        self.statselect = None
        self.battlescreen = None
        self.gameover=None
        self.strings_of_actions = []
        self.level = 1

        # Generate map.
        if self.level == 0:
            for x in range(0, self.swidth, self.ref):
                for y in range(0, self.sheight, self.ref):
                    node = block.Grass(x,y)
                    self.grid[(x,y)] = node
                    self.character[(x,y)]=None
            for x in range(0, self.swidth, self.ref):
                for y in range(0, self.sheight, self.ref):
                    if x not in range(1 * self.ref, self.swidth - 1*self.ref,self.ref) or y not in range(1*self.ref, self.sheight-1*self.ref, self.ref):
                        boundary = block.Outeredge(x,y)
                        self.grid[(boundary.x,boundary.y)] = boundary

        if self.level == 1:
            #grass populate everything
            for x in range(0, self.swidth-2*ref, self.ref):
                for y in range(0, self.sheight-2*ref, self.ref):
                    self.grid[(x,y)] = block.Grass(x,y)
                    self.character[(x,y)]=None
            #add water
            for y in range(10):
                self.grid[(0,y*ref)] = block.Outeredge(0,y*ref)
            for x in range(2,6):
                self.grid[(x*ref,9*ref)] = block.Outeredge(x*ref,9*ref)
            for x in [6,7,8,10,11]:
                self.grid[(x*ref,8*ref)] = block.Outeredge(x*ref,8*ref)

            #add wall
            for x in [2,4,5,8,9,10]:
                self.otherObject[(x*ref,2*ref)] = block.Wall(x*ref,2*ref)
            for y in [3,4,5,7,8]:
                self.otherObject[(3*ref,y*ref)] = block.Wall(3*ref,y*ref)
            for y in [4,5]:
                self.otherObject[(10*ref,y*ref)] = block.Wall(10*ref,y*ref)


            #add high grass
            for y in [5,6,7]:
                self.otherObject[(4*ref,y*ref)] = block.HighGrass(4*ref,y*ref)
            for x in [3,4]:
                self.otherObject[(x*ref,1*ref)] = block.HighGrass(x*ref,1*ref)
            for x in [6,8]:
                self.otherObject[(x*ref,4*ref)] = block.HighGrass(x*ref,4*ref)
            for x in [6,8,10]:
                self.otherObject[(x*ref,6*ref)] = block.HighGrass(x*ref,6*ref)
            for x in [7,9]:

                self.otherObject[(x*ref,9*ref)] = block.HighGrass(x*ref,9*ref)
            self.otherObject[(9*ref,0*ref)] = block.HighGrass(9*ref,0*ref)
            self.grid[(7*ref,5*ref)] = block.HighGrass(7*ref,5*ref)
            self.otherObject[(7*ref,9*ref)] = block.HighGrass(7*ref,9*ref)
            self.otherObject[(10*ref,10*ref)] = block.HighGrass(10*ref,10*ref)

            #add bridge
            self.grid[(ref,9*ref)] = block.Bridge(ref,9*ref)
            self.grid[(9*ref,8*ref)] = block.Bridge(9*ref,8*ref)
            
            for key, value in self.otherObject.iteritems():
                self.grid[key]=self.otherObject[key]

        # Create players.
        self.populatePlayers()
        self.organize_teams()

    def populatePlayers(self):
        """
        This function creates all players and places them within teams.

        Inputs: Model
        Outputs: None
        """
        if self.level==0:
            
            self.character[(300,300)] = character.Warrior(self,location=(300,300), name='Julian', dodge = 5 , crit=5, team = 0)
            self.character[(300,350)] = character.Warrior(self,location=(300,350), name='David', dodge = 5 , crit=5, team = 1)
            self.character[(400,500)] = character.Archer(self,location=(400,500), name='Sae', dodge = 5 , crit=5, team = 0)
            self.character[(400,500)] = character.Archer(self,location=(450,500), name='Pan', dodge = 5 , crit=5, team = 1)
        
        if self.level==1:

            self.character[(ref*5,ref*0)] = character.Warrior(self,location=(ref*5,ref*0), name='Julian', dodge = 5 , crit=5, team = 0)
            self.character[(ref*7,ref*0)] = character.Warrior(self,location=(ref*7,ref*0), name='David', dodge = 5 , crit=5, team = 0)
            self.character[(ref*8,ref*1)] = character.Warrior(self,location=(ref*8,ref*1), name='Charlie', dodge = 5, crit=5, team = 0)
            self.character[(ref*7,ref*1)] = character.Warrior(self,location=(ref*7,ref*1), name='Jacob', dodge = 5 , crit=5, team = 0)
            self.character[(ref*5,ref*10)] = character.Warrior(self,location=(ref*5,ref*10), name='Bob', dodge = 5 , crit=5, team = 1)
            self.character[(ref*6,ref*11)] = character.Warrior(self,location=(ref*6,ref*11), name='Tom', dodge = 5 , crit=5, team = 1)
            self.character[(ref*7,ref*10)] = character.Warrior(self,location=(ref*7,ref*10), name='Pierre', dodge = 5 , crit=5, team = 1)
            self.character[(ref*8,ref*11)] = character.Warrior(self,location=(ref*8,ref*11), name='Fishhead', dodge = 5 , crit=5, team = 1)
            self.character[(ref*6,ref*0)] = character.Archer(self,location=(ref*6,ref*0), name='Babe', dodge = 5 , crit=5, team = 0)
            self.character[(ref*8,ref*0)] = character.Archer(self,location=(ref*8,ref*0), name='Ashley', dodge = 5 , crit=5, team = 0)
            self.character[(ref*6,ref*10)] = character.Archer(self,location=(ref*6,ref*10), name='Sae', dodge = 5 , crit=5, team = 1)
            self.character[(ref*7,ref*11)] = character.Archer(self,location=(ref*7,ref*11), name='Pan', dodge = 5 , crit=5, team = 1)

    def organize_teams(self):
        """
        This function places all players into the right teams.

        Inputs: Model
        Outputs: None
        """
        for point in self.character:
            if self.character[point] != None:
                if str(self.character[point].__class__)[19:len(str(self.character[point].__class__))] != "ock.Wall'>":
                    if self.character[point].team >= len(self.teams):
                        for adding in range(self.character[point].team - len(self.teams) + 1):
                            self.teams.append([])
                    self.teams[self.character[point].team].append(self.character[point])

        for character in self.teams[0]:
            character.can_move = True

    def location_update(self, list_of_locations):
        for index in range(len(list_of_locations)):
            if len(list_of_locations) > 0:
                if list_of_locations[index] in self.character:
                    if self.character[list_of_locations[index]]== None :
                        self.character[list_of_locations[index]]=self.character[list_of_locations[index-1]]
                        self.character[list_of_locations[index]].location= list_of_locations[index]
                        moved=int((abs(list_of_locations[index][0]-list_of_locations[index-1][0])+abs(list_of_locations[index][1]-list_of_locations[index-1][1]))/50)
    
                        if abs(list_of_locations[index][0]-list_of_locations[index-1][0]) > abs(list_of_locations[index][1]-list_of_locations[index-1][1]):
                            if list_of_locations[index][0]-list_of_locations[index-1][0] < 0:
                                direction = 'n'
                            else:
                                direction = 's'
                        else:
                            if list_of_locations[index][1]-list_of_locations[index-1][1] < 0:
                                direction = 'e'
                            else:
                                direction = 'w'
    
                        self.character[list_of_locations[index]].movementleft-=moved
    
                        # Delete old character in that location.
                        self.character[list_of_locations[index-1]]=None
    
                        # Returns the direction.
                        return direction

    def next_turn(self):
        """
        This function, when called, ends the turn of the current team.

        Inputs: the model 
        Outputs: None
        """
        choice = self.turn % len(self.teams)
        old_choice = choice
        self.charselected = None
        for character in self.teams[choice]:
            character.can_move = False
            character.movementleft = character.movement
            character.o_location = character.location

        self.turn += 1
        while self.turn % len(self.teams) == []:
            self.turn += 1
        
        choice = self.turn % len(self.teams)
        if choice == old_choice:
            self.end_game()

        for character in self.teams[choice]:
            character.can_move = True
            character.hasAttacked = False
            character.movementleft = character.movement

    def charselect(self, corner_x, corner_y):
        """
        """
        if (corner_x, corner_y) in self.character:
            if self.character[(corner_x,corner_y)] != None:
                self.statselect = self.character[(corner_x,corner_y)]
                self.charselected = self.character[(corner_x,corner_y)]
                self.character[(corner_x,corner_y)].orient = 's'

    def char_reset(self, character):
        """
        """
        if character.can_move == False:
            return
        else:
            character.orient = "s"
            self.location_update([character.location, character.o_location])
            character.movementleft=character.movement

    def move(self, player, corner_x, corner_y):
        if (corner_x, corner_y) in self.character:
            if player.movementleft==0:
                self.statselect = self.character[(corner_x,corner_y)]
                self.charselected = self.character[(corner_x,corner_y)]
            
            elif self.character[(corner_x, corner_y)]!=None:
                if player.team == self.character[(corner_x, corner_y)].team:
                    player.clickTwice = False
                    self.charselected = self.character[(corner_x, corner_y)]
                    self.statselect = self.character[(corner_x,corner_y)]
            
                # Fighting situation.
                elif self.character[(corner_x,corner_y)] != player:
                    self.complete_fighting_situation(player, corner_x, corner_y)
                    
            # If the place the character is moving to is empty,
            elif self.character[(corner_x,corner_y)] == None:
                player.clickTwice = False
                self.jump_to(player, corner_x, corner_y)

    def jump_to(self, player, corner_x, corner_y):
        """
        This function jumps a character to the selected location.
        """
        # If the character can reach this block,
        if player.can_move == False:
            return
        if (corner_x,corner_y) in player.availabilities:
            # Update to that location.
            player.orient = self.location_update([player.location, (corner_x, corner_y)])
        else:
            self.charselected = None

    def complete_fighting_situation(self, player, corner_x, corner_y):

        # If two players are within weaponrange,
        print 'got here'
        if int((abs(self.character[(corner_x,corner_y)].location[0]-player.location[0])+abs(self.character[(corner_x,corner_y)].location[1]-player.location[1]))/50) == player.weaponrange:

            # If the player has a clicktwice state,
            if player.clickTwice:
                if not player.hasAttacked:
                    if player.team != self.character[(corner_x, corner_y)].team:
                        self.strings_of_actions = player.battle(self.character[(corner_x, corner_y)])
                        
                        if player.CurrentHP <= 0:
                            self.character[player.location]=None
                        if self.character[(corner_x, corner_y)].CurrentHP <= 0:
                            self.character[self.character[(corner_x, corner_y)].location]=None
                
                        self.battlescreen = (player,self.character[(corner_x,corner_y)])

                        player.clickTwice = False
                        player.movementleft=0
                        self.battlescreen = None
            
            else:
                if player.team != self.character[(corner_x, corner_y)].team:
                    self.battlescreen = (player,self.character[(corner_x,corner_y)])
                player.clickTwice=True
            
        else:
            # Remove character selection.
            self.statselect = self.character[(corner_x,corner_y)]
            self.charselected = self.character[(corner_x,corner_y)]
            self.character[(corner_x,corner_y)].orient = 's'
            
    def end_game(self):
        """
        This function ends the gameself.
        """
        print "Game Ended."
    
    def update(self):
        """
        update is constantly run to keep check of what happens during the game.

        Inputs: the model
        Outputs: None
        """
        for point in self.character:
            if self.character[point] != None:
                self.character[point].generate_availabilities()
        
        for character in self.teams[self.turn%len(self.teams)]:
            if character.can_move == True:
                character.image = character.images[character.orient]
            if character.CurrentHP <= 0:
                character = None
<<<<<<< HEAD
        result=self.endgame()
        if result==(True,False):
            print "Team 1 wins!"
            self.gameover=1
        
        if result==(False, True):
            print "Team 2 wins!"
            self.gameover=2
                
                
            
            
            
   
            
            
            
            
            
            
=======
>>>>>>> 9e02350a5f5f9eae0b6b6d99b36996c10d6d6b6c
