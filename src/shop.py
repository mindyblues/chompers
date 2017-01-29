from helperfunctions import generateShopCreature

class ShopInventory:
    def __init__(self):
        self.m_itemlist = []
        for x in range(3):
            c = generateShopCreature()
            c.calculatePrice()
            self.m_itemlist.append(c)

    def __str__(self):
        returnstr = ""
        for creature in self.m_itemlist:
            returnstr = returnstr + creature.__str__()
        return returnstr

class ShopItem:
    def __init__(self,name):
        self.m_name = name

class Shop:
    def __init__(self):
        self.m_inventory = ShopInventory()

    def sellYouShit(self,Player):
        playerin = Player.getInventory()
        playeritemlist = playerin.getItemList()
        print("Which creature would you like to sell?\n")
        print(playerin)
        print("Select by name!\n")
        selected = str(input())
        for creature in playeritemlist:
            if selected == creature.getName():
                addedmoney = creature.getPrice()
                playeritemlist.remove(creature)
                Player.addMoney(addedmoney)
