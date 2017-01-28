from creature import Creature
import random
from colors import Color

def generateBaseCreature():
    maximum = 100
    startinglist = []
    for thefive in range(5):
        i = random.uniform(0,maximum)
        startinglist.append(i)
    a = (Color.getColor(random.randint(101,106)))
    creature = Creature(0,startinglist[0],startinglist[1],startinglist[2],startinglist[3],startinglist[4])
    creature.setDomColor(a)
    creature.setSecColor(None)
    creature.setName(generateRandomName())
    creature.calculatePrice()
    if creature.baseStatsUnder(200):
        return creature
    else:
        return generateBaseCreature()

def generateShopCreature():
    maximum = 100
    shoplist = []
    for thethree in range(5):
        i = random.uniform(25,maximum-25)
        shoplist.append(i)
    creature = Creature(0,shoplist[0],shoplist[1],shoplist[2],shoplist[3],shoplist[4])

    return creature

def generateStarterList():
    starterlist = []
    for thesix in range(6):
        starterlist.append(generateBaseCreature())
    return starterlist


def generateBaseGrid(listofcreatures):
# name | Color1 | Color2
#Strength | Speed | stamina
#Intelligence | Ferocity
    for creature in listofcreatures:
        print(creature)

def generateRandomName():
    namelist = ["Albert","Alamo","Bartholomew","Babble","Caleb","Cairo","Douglas","Disaster","Edmund","Egypt",
    "Fennel","Freddy","Gareth","Gigi","Honesty","Hector","Indignity","Isaac","James","Joker","Katie","Kibble",
    "Lemon","Leslie","Markie","Monday","Noah","Nazareth","Oliver","Opal","Penance","Pepper","Quiz","Quigley",
    "Richard","Rocket","Solomon","Salmon","Treble","Timothy","Unity","Ulysses","Vasya","Victor","West","Walker",
    "Xavier","Xylophone","Yasmin","Yoghurt","Zane","Zoo"]
    return random.choice(namelist)
