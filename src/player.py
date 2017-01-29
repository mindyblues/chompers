class Player: # holds player traits
    def __init__(self, name = "Unknown", money = 500, inventory = [], ):
        self.m_name = name
        self.m_money = money
        self.m_inventory = PlayerInventory()


    def __str__(self): # calls player stats
        return ("You are %s ! \n[These are your stats:\nMoney: %d\nInventory: %s\n" %
         (self.m_name,self.m_money,self.m_inventory.__str__()))

    def getInventory(self):
        return self.m_inventory

    def addMoney(self,moneytoadd):
        self.m_money += moneytoadd

    def addCreature(self,creature):
        self.m_inventory.addCreature(creature)

class PlayerInventory: # creates an empty list for chompers to be placed into
    def __init__(self):
        self.m_itemlist = []

    def __str__(self): # returns contents of inventory in string form
        returnstring = ""
        for creature in self.m_itemlist:
            returnstring += creature.__str__()
        return returnstring

    def addCreature(self,creature):
        self.m_itemlist.append(creature)

    def getItemList(self):
        return self.m_itemlist
