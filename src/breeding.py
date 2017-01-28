# breeding.py
import random
from creature import Creature
def chooseFerocity(Parent1,Parent2):
    innateferocity = 0
    chance = random.uniform(0,100)
    if 0 > chance > 75:
        innateferocity = random.uniform(-5,5)
    elif 75 > chance > 95:
        innateferocity = random.uniform(-10,10)
    else:
        innateferocity = random.uniform(-20,20)

    babyFerocity = ((Parent1.getFerocity() + Parent2.getFerocity())/2) + innateferocity
    return babyFerocity

def chooseStrength(Parent1,Parent2):
    innatestrength = 0
    chance = random.uniform(0,100)
    if 0 > chance > 70:
        innatestrength = random.uniform(-5,5)
    else:
        innatestrength = random.uniform(-10,10)

    babyStrength = ((Parent1.getStrength() + Parent2.getStrength())/2) + innatestrength
    return babyStrength

def chooseSpeed(Parent1,Parent2):
    innatespeed = 0
    chance = random.uniform(0,100)
    if 0 > chance > 70:
        innatespeed = random.uniform(-5,5)
    else:
        innatespeed = random.uniform(-10,10)

    babySpeed = ((Parent1.getSpeed() + Parent2.getSpeed())/2) + innatespeed
    return babySpeed

def chooseIntelligence(Parent1,Parent2):
    innateintelligence = 0
    chance = random.uniform(0,100)
    if 0 > chance > 70:
        innateintelligence = random.uniform(-5,5)
    else:
        innateintelligence = random.uniform(-10,10)

    babyIntelligence = ((Parent1.getIntelligence() + Parent2.getIntelligence())/2) + innateintelligence
    return babyIntelligence

def chooseStamina(Parent1,Parent2):
    innatestamina = 0
    chance = random.uniform(0,100)
    if 0 > chance > 70:
        innatestamina = random.uniform(-5,5)
    else:
        innatestamina = random.uniform(-10,10)

    babyStamina = ((Parent1.getStamina() + Parent2.getStamina())/2) + innatestamina
    return babyStamina

def checkMutation(Parent1,Parent2):
    mutationlevel = 0
    chance = random.randint(0,1000)
    print chance
    if (Parent1.getMutationNumber() + Parent2.getMutationNumber()) == 0:
        if ((0 < chance) and (chance < 935)):
            mutationlevel = 0
            print mutationlevel
        elif ((935 < chance) and (chance < 985)):
            mutationlevel = 1
        elif ((985 < chance) and (chance < 995)):
            mutationlevel = 2
        else:
            mutationlevel = 3

    elif (Parent1.getMutation() + Parent2.getMutation()) > 0:
        if ((0 < chance) and (chance < 700)):
            mutationlevel = 1
        elif ((700 < chance) and (chance < 980)):
            mutationlevel = 2
        else:
            mutationlevel = 3
    return mutationlevel

def typeMutation():
    mutationtype = 0
    chance = random.uniform(0,100)
    if chance > 50:
        mutationtype = 1
    else:
        mutationtype = 2
    return mutationtype

def giveMutationType1(mutationlevel):
    chance = random.uniform(0,50)
    mutationnumber = 0
    if mutationlevel == 1:
        mutationnumber = 11
    elif mutationlevel == 2:
        if chance > 50:
            mutationnumber = 12
        else:
            mutationnumber = 13
    elif mutationlevel == 3:
        mutationnumber = 14

    return mutationnumber

def giveMutationType2(mutationlevel):
    mutationnumber = 0
    chance = random.uniform(0,100)
    if (mutationlevel == 1):
        if ((0 < chance) and (chance < 20)):
            mutationnumber = 201
        if ((20 < chance) and (chance < 40)):
            mutationnumber = 202
        if ((40 < chance) and (chance < 60)):
            mutationnumber = 203
        if ((60 < chance) and (chance < 80)):
            mutationnumber = 204
        else:
            mutationnumber = 205
    elif (mutationlevel == 2):
        if((0 < chance) and (chance < 33)):
            mutationnumber = 301
        if ((33 < chance) and (chance < 66)):
            mutationnumber = 302
        else:
            mutationnumber = 303
    elif (mutationlevel == 3):
        mutationnumber = 401
    return mutationnumber

def chooseColor(Parent1,Parent2):
    chance = random.uniform(0,100)
    randcol = random.uniform(101,106)
    babyDomColor = None
    babySecColor = None
    if ((Parent1.getSecColor() == None) and (Parent2.getSecColor()) == None) : # for monocolor parents
        print "FIRST LOOP"
        if ((0 < chance) and (chance < 40)):
            babyDomColor = Parent1.getDomColor()
        elif ((40 < chance) and (chance < 80)):
            babyDomColor = Parent2.getDomColor()
        elif ((80 < chance) and (chance < 89)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = getDomColor(Parent2)
        elif ((89 < chance) and (chance < 97)):
            babyDomColor = Parent2.getDomColor()
            babySecColor = Parent1.getDomColor()
        elif ((97 < chance) and (chance < 98)):
            babyDomColor = Color.getColor(randcol)
        elif ((98 < chance) and (chance < 99)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = Color.getColor(randcol)
        else:
            babyDomColor = Parent2.getDomColor()
            babySecColor = Color.getColor(randcol)

    elif ((Parent1.getSecColor() != None) and (Parent2.getSecColor()) == None): # Parent 1 bicolor, # Parent 2 monocolor
        if ((0 < chance) and (chance < 20)):
            babyDomColor = Parent1.getDomColor()
        elif ((20 < chance) and (chance < 40)):
            babyDomColor = Parent2.getDomColor()
        elif ((40 < chance) and (chance < 55)):
            babyDomColor = Parent1.getDomColor()
        elif ((55 < chance) and (chance < 68)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = Parent2.getDomColor()
        elif ((68 < chance) and (chance < 81)):
            babyDomColor = Parent2.getDomColor()
            babySecColor = Parent1.getDomColor()
        elif ((81 < chance) and (chance < 86)):
            babyDomColor = Parent2.getDomColor()
            babySecColor = Parent1.getDomColor()
        elif ((86 < chance) and (chance < 91)):
            babyDomColor = getSecColor(Parent1)
            babySecColor = getDomColor(Parent2)
        elif ((91 < chance) and (chance < 93)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = Color.getColor(randcol)
        elif ((93 < chance) and (chance < 95)):
            babyDomColor = Parent2.getDomColor()
            babySecColor = Color.getColor(randcol) # must pull from random Level 1 color
        elif ((95 < chance) and (chance < 96)):
            babyDomColor = Color.getColor(randcol) #same
        elif ((96 < chance) and (chance < 97)):
            babyDomColor = Color.getColor(randcol)
            babySecColor = Parent1.getSecColor()
        elif ((97 < chance) and (chance < 98)):
            babyDomColor = Color.getColor(randcol)
            babySecColor = Parent1.getDomColor()
        elif ((98 < chance) and (chance < 99)):
            babyDomColor = Color.getColor(randcol)
            babySecColor = Parent2.getDomColor()
        elif ((97 < chance) and (chance < 98)):
            babyDomColor = Parent1.getSecColor()
            babySecColor = Color.getColor(randcol)

    elif ((Parent1.getSecColor() == None) and (Parent2.getSecColor()) != None): #Parent1 monocolor, parent 2 bicolor
        if ((0 < chance) and (chance < 20)):
            babyDomColor = Parent1.getDomColor()
        elif ((20 < chance) and (chance < 40)):
            babyDomColor = Parent2.getDomColor()
        elif ((40 < chance) and (chance < 55)):
            babyDomColor = Parent2.getSecColor()
        elif ((55 < chance) and (chance < 68)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = Parent2.getDomColor()
        elif ((68 < chance) and (chance < 81)):
            babyDomColor = Parent2.getDomColor()
            babySecColor = Parent1.getDomColor()
        elif ((81 < chance) and (chance < 86)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = Parent2.getSecColor()
        elif ((86 < chance) and (chance < 91)):
            babyDomColor = Parent2.getSecColor()
            babySecColor = Parent1.getDomColor()
        elif ((91 < chance) and (chance < 93)):
            babyDomColor = Parent1.getDomColor()
            babySecColor = Color.getColor(randcol) # must pull from random Level 1 color
        elif ((93 < chance) and (chance < 95)):
            babyDomColor = Parent2.getDomColor()
            babySecColor = Color.getColor(randcol) # must pull from random Level 1 color
        elif ((95 < chance) and (chance < 96)):
            babyDomColor = Color.getColor(randcol) #same
        elif ((96 < chance) and (chance < 97)):
            babyDomColor = Color.getColor(randcol)
            babySecColor = Parent2.getSecColor()
        elif ((97 < chance) and (chance < 98)):
            babyDomColor = Color.getColor(randcol)
            babySecColor = Parent1.getDomColor()
        elif ((98 < chance) and (chance < 99)):
            babyDomColor = Color.getColor(randcol)
            babySecColor = Parent2.getDomColor()
        elif ((97 < chance) and (chance < 98)):
            babyDomColor = Parent2.getSecColor()
            babySecColor = Color.getColor(randcol)

    else:
        pass

    return [babyDomColor,babySecColor]

def makeBaby(Parent1,Parent2):
    babyStamina = chooseStamina(Parent1,Parent2)
    babySpeed = chooseSpeed(Parent1,Parent2)
    babyIntelligence = chooseIntelligence(Parent1,Parent2)
    babyStrength = chooseStrength(Parent1,Parent2)
    babyFerocity = chooseFerocity(Parent1,Parent2)

    print "Please give your new Chomper a name!\n"
    babyName = str(raw_input())
    c = Creature(0,babyStrength,babyStamina,babyIntelligence,babySpeed,babyFerocity)
    c.checkNegativeStats()
    c.calculatePrice()
    mutlvl = checkMutation(Parent1,Parent2)
    if (mutlvl > 0):
        muttype = typeMutation()
        if muttype == 1:
            muttypen = giveMutationType1(mutlvl)
        else:
            muttypen = giveMutationType2(mutlvl)
        c.setMutationNumber(muttypen)

    c.setBabyName(babyName)
    l = chooseColor(Parent1,Parent2)
    c.setDomColor(l[0])
    c.setSecColor(l[1])
    return c
