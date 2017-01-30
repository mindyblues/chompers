# creature.py
from PyQt5.QtCore import *

class Creature(QObject):
    # these are the traits of the creatures
    def __init__(self, price = 0, strength = 0, stamina = 0, intelligence = 0,
        speed = 0, ferocity = 0, domcolor = None, seccolor = None, inbreeding = [], mutation = 0, name = "Unknown",
        papa = 0, mama = 0, uniqueID = 0):
        self.m_price = price
        self.m_strength= strength
        self.m_stamina = stamina
        self.m_intelligence = intelligence
        self.m_speed = speed
        self.m_ferocity = ferocity
        self.m_domcolor = domcolor
        self.m_seccolor = seccolor
        self.m_inbreeding = inbreeding
        self.m_mutation = mutation
        self.m_name = name
        self.m_papa = papa
        self.m_mama = mama
        self.m_uniqueID = uniqueID

    def __str__(self): # calls chomper traits in a readable list
        return ("This is %s !\n It is %s and %s. \nThese are its stats:\nStrength: %d\nStamina: %d\nIntelligence: %d\nSpeed: %d\nFerocity: %d\nAnd the value is: %d\n" %
         (self.m_name,self.m_domcolor,self.m_seccolor,self.m_strength,self.m_stamina,self.m_intelligence,self.m_speed,self.m_ferocity,self.m_price))

### PULLS THE VARIOUS TRAITS FROM THE CREATURE AND RETURNS IT

    def getPrice(self):
        return self.m_price

    def getFerocity(self):
        return self.m_ferocity

    def getStrength(self):
        return self.m_strength

    def getSpeed(self):
        return self.m_speed

    def getStamina(self):
        return self.m_stamina

    def getIntelligence(self):
        return self.m_intelligence

    def getMutationNumber(self):
        return self.m_mutation

    def getDomColor(self):
        return self.m_domcolor

    def getSecColor(self):
        return self.m_seccolor

    def getInbreedingList(self):
        return self.m_inbreeding

    def getName(self):
        return self.m_name

## FIXES POSSIBLE STAT BUGS AND LIMITS stats

    def checkNegativeStats(self):
        if 0 > self.m_strength:
            self.m_strength = 0
        if 0 > self.m_stamina:
            self.m_stamina = 0
        if 0 > self.m_intelligence:
            self.m_intelligence = 0
        if 0 > self.m_speed:
            self.m_speed = 0
        if 0 > self.m_ferocity:
            self.m_ferocity = 0

    def baseStatsUnder(self,limit):
        stats = self.m_strength + self.m_stamina + self.m_intelligence + self.m_speed + self.m_ferocity
        if stats > 200:
            return False
        elif self.m_strength > 50:
            return False
        elif self.m_stamina > 50:
            return False
        elif self.m_intelligence > 50:
            return False
        elif self.m_speed > 50:
            return False
        elif self.m_ferocity > 50:
            return False
        else:
            return True

## MANUALLY SETS STATS

    def setBabyName(self,babyName):
        self.m_name = babyName

    def setName(self,name):
        self.m_name = name

    def resetName(self,name):
        self.setName(name)

    def setMutationNumber(self,mutationNumber):
        self.m_mutation = mutationNumber

    def setDomColor(self, color):
        self.m_domcolor = color

    def setSecColor(self, color):
        self.m_seccolor = color

## GENERATES STATS FROM THINGS OUTSIDE DIRECT CONTROL

    def generateUniqueID(self):
        self.m_uniqueID = id(self)

    def generateInbreedingList(self, Parent1, Parent2):
        self.m_inbreeding.append(id(self))
        self.m_inbreeding.extend(Parent1.getInbreedingList())
        self.m_inbreeding.extend(Parent2.getInbreedingList())

    def checkInbreeding(self):
        a = (len(set(self.m_inbreeding)))
        b = (len(self.m_inbreeding))
        c = b - a
        if c == 0:
            return 0
        elif ((0 < c) and (chance < 2)):
            return 1
        elif ((2 < c) and (chance < 6)):
            return 2
        elif c > 6:
            return 3

    def calculatePrice(self):
        self.m_price = (self.m_strength + self.m_stamina + self.m_intelligence + self.m_speed + self.m_ferocity)

    def giveStatBoost(self,mutationnumber):
        if mutationnumber == 11:
            self.m_strength += 10
            self.m_ferocity += 10
            self.m_intelligence -= 5
            self.m_price += 50
        elif mutationnumber == 12:
            self.m_strength += 20
            self.m_ferocity += 20
            self.m_intelligence -= 10
            self.m_price += 100
        elif mutationnumber == 13:
            self.m_speed += 10
            self.m_price += 125
        elif mutationnumber == 14:
            self.m_strength -= 40
            self.m_ferocity -= 40
            self.m_stamina += 50
            self.m_intelligence += 25
            self.m_price -= 75
        elif mutationnumber == 21:
            self.m_speed -= 15
            self.m_stamina -= 10
            self.m_price -= 50
        elif mutationnumber == 22:
            self.m_speed -= 15
            self.m_intelligence -= 30
            self.m_price -= 100
        elif mutationnumber == 23:
            self.m_strength -= 40
            self.m_ferocity -= 40
            self.m_stamina += 50
            self.m_intelligence += 25
            self.m_price -= 75
        elif mutationnumber == 201:
            self.m_price += 100
        elif mutationnumber == 202:
            self.m_price += 100
        elif mutationnumber == 203:
            self.m_price += 100
        elif mutationnumber == 204:
            self.m_price += 100
        elif mutationnumber == 205:
            self.m_price += 100
        elif mutationnumber == 301:
            self.m_price += 200
        elif mutationnumber == 302:
            self.m_price += 200
        elif mutationnumber == 303:
            self.m_price += 200
        elif mutationnumber == 401:
            self.m_price += 400
        elif mutationnumber == 501:
            self.m_price -= 50
        elif mutationnumber == 502:
            self.m_price -= 50
        elif mutationnumber == 503:
            self.m_price -= 50
        self.checkNegativeStats()
############################## QT STUFF #################
    def handle_clicked(self):
        qDebug('test message')
