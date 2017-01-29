#test def and class and etc
from breeding import *
from colors import *
from creature import *
from helperfunctions import *
from mutation import *
from player import *
from shop import *
'''
theshop = Shop()
player1 = Player()
for i in range(3):
    player1.addCreature(generateBaseCreature())
theshop.sellYouShit(player1)
inventory = player1.getInventory()
print(inventory)
'''
c = generateBaseCreature()
c.setMutationNumber(23)
c.giveStatBoost(c.getMutationNumber())
print(c)
