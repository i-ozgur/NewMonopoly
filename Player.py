class player:
    def __init__(self, name, money, index):
        self.name = name
        self.money = money #Money setlenebilir olsun istedim sonradan gelen üyelerin paraları farklı setlenebilir diye dilenirse defaultlanır.
        self.index = index #Playerlar arasındaki yeri, lazım olursa diye ekledim.
        self.position = 0
        self.properties = set()
        self.inJail = False
        self.isBankrupt = False

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getIndex(self):
        return self.index
    
    def getPosition(self):
        return self.position
    
    def getProperties(self):
        return self.properties

    def getNetValue(self):
        value = self.getMoney()
        for land in self.properties:
            value += land.get_value()   #Property değeri fonksiyonu
        return value

    def removeProperty(self, property):
        self.properties.remove(property)

    def setMoney(self, new_value):
        self.money = new_value

    def addMoney (self , value):
        self.money += value

    def deductMoney (self , value):
        self.money -= value

    def setPosition (self , pos):
        self.position = pos

    def __str__(self):
        return "Player: "+self.getName + \
                ". Position: "+str(self.getPosition) + \
                ". Money: $"+str(self.getMoney)
    