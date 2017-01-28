# creature.py

class Creature:
    # these are the traits of the creatures
    def __init__(self, price = 0, strength = 0, stamina = 0, intelligence = 0,
        speed = 0, ferocity = 0, domcolor = None, seccolor = None, inbreeding = 0, mutation = 0, name = "Unknown",
        papa = 0, mama = 0):
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

    def __str__(self): # calls chomper traits in a readable list
        return ("This is %s !\n It is %s and %s. \n[These are its stats:\nStrength: %d\nStamina: %d\nIntelligence: %d\nSpeed: %d\nFerocity: %d\nAnd the value is: %d]\n" %
         (self.m_name,self.m_domcolor,self.m_seccolor,self.m_strength,self.m_stamina,self.m_intelligence,self.m_speed,self.m_ferocity,self.m_price))

    def calculatePrice(self):
        self.m_price = (self.m_strength + self.m_stamina + self.m_intelligence + self.m_speed + self.m_ferocity)

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

    def setBabyName(self,babyName):
        self.m_name = babyName

    def setName(self,name):
        self.m_name = name

    def setMutationNumber(self,mutationNumber):
        self.m_mutation = mutationNumber

    def getMutationNumber(self):
        return self.m_mutation

    def getDomColor(self):
        return self.m_domcolor

    def getSecColor(self):
        return self.m_seccolor

    def setDomColor(self, color):
        self.m_domcolor = color
    def setSecColor(self, color):
        self.m_seccolor = color
