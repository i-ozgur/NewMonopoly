class Player:
  name = ""

  def __init__(self, name, money):
    self.name = name
    self.money = money

class Property:
  
  def __init__(self, price, type, color, rent, monopoly, owner, house, hotel, mortgage):
    self.price = price
    self.type = type
    self.color = color
    self.rent = rent
    self.monopoly = monopoly
    self.owner = owner
    self.house = house
    self.hotel = hotel
    self.mortgage = mortgage
  
  def collect_rent(self, player):
    if self.owner == None:
      return
    else:
      self.owner.money += self.rent
      player.money -= self.rent

p1 = Property(36, "property", "brown", 2, 0, Player("Osman"), 0, 0, 0)

print(p1.price)
print(p1.type)
print(p1.owner.name)

p1.price = 40
print(p1.price)

p1.owner = Player("Ali")
print(p1.owner.name)

p1.owner.name = "Murat"
print(p1.owner.name)
