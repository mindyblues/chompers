# world.py
from player import *
from colors import *
from breeding import *
from helperfunctions import *
class World():
    def __init__(self, shop = 0, player ="Unknown", daycount = 0, breedingpoint = 0):
        self.m_shop = shop
        self.m_player = player
        self.m_daycount = daycount
        self.m_breedingpoint = breedingpoint
    def __str__(self):
        return("This is your world!\nCurrent player is: %s\nDay: %d" %
        (self.m_player,self.m_daycount))
    def gameLoop(self):
        print("Hello! What would you like to be called?\n")
        playername = str(input())
        self.m_player = Player(playername)
        print("INTRO TEXT")
        a = generateStarterList()
        copyofa = list(a)
        generateBaseGrid(a)
        kaput = True
        while kaput == True:
            # generateBaseGrid(a)
            print("WHATCHA WANT 1")
            first = input()
            for creature in a:
                if creature.getName() == first:
                    self.m_player.addCreature(creature)
                    print("WHAT CALL CRITTER")
                    newname = input()
                    copyofa.remove(creature)
                    creature.resetName(newname)
                    print("THANKS")
                else:
                    print("Names dont match")
            if len(copyofa) == len(a):
                print("Didnt delete anything, start over")
            else:
                print("Deleted something")
                kaput = False
        generateBaseGrid(a)
        print("WHATCHA WANT 2")
        second =  input()
        for creature in a:
            if creature.getName() == second:
                self.m_player.addCreature(creature)
                print("WHAT CALL CRITTER 2")
                newname = input()
                creature.resetName(newname)
                a.remove(creature)
        self.m_player.getItemList()
c = World()
c.gameLoop()
