class board:
    
    def __init__(self):
        self.lands = []
        self.generateLands()

    def getLands(self):
        return self.lands
    
    def getLand(self, index):
        return self.lands[index]

    def generateLands(self):
        #Monopoly şehirler append edilecek.
        
        