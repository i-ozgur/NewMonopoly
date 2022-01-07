import random

class gameplay:
    def __init__(self, players, board):
        self.players = self.decide_Turn_order(players)
        self.board = board
        self.house_Count = 32
        self.hotel_Count = 12
        self.tax_Rate = 1

    def decide_Turn_Order(self, players):
        ord = []
        for i, player in enumerate(players):
            d1, d2 = self.roll_Dice()
            ord.append((i, (d1+d2)))
        ord.sort(key=lambda tup: tup[1], reverse=True)
        turn_Order = []
        for j in ord:
            turn_Order.append(players[j[0]])
        return turn_Order

    def roll_Dice(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)

        return (d1,d2)
    
    def mortgage_Property(self, property):
        property.mortgage = True
        property.owner.money += property.mortgage_Price

    def unMortgage_Property(self, property):
        property.mortgage = False
        property.owner.money -= property.mortgage_Price

    def passed_Go(self, player):
        player.money += 200
    
    def go_Jail(self, player):
        player.jailed[0] = True
    
    def check_Jailed(self, player):
        if player.jailed[1] == 3:
            player.jailed[0] == False
            player.jailed[1] == 0
            return
        else:
            d1,d2 = self.roll_Dice()
            if d1 == d2:
                player.jailed[0] == False
                player.jailed[1] == 0
                return
            else:
                player.jailed[1] += 1
                return
    
    