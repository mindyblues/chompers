# breedinggame.txt

import random
from shop import ShopInventory
from helperfunctions import *
from breeding import makeBaby
from colors import Color
from player import Player

def GameLoop():
    print "Hello! What would you like to be called?\n"
    playername = str(raw_input())
    player1 = Player(playername)
    print "Awesome! You're a starving artist behind on your bills.\n"
    print "You applied for a Start Up loan of $2500 to begin your very own art business.\n"
    print "Unfortunately, you have no marketable skills!\n"
    print "Your loan was denied.\n"
    print "Fortunately, your mom lended you $500 to pay rent this week.\n"
    print "On your way home from mom's, you see multiple signs advertising premimum"
    print "CHOMPERS.\n"
    print "The guard animal of preference, Chompers are equal part cute and ferocious."
    print "You decide to head down to the local pound, where you can pick Chompers up"
    print "for real cheap."
    print "\n"
    print "\n"

print generateBaseCreature()
