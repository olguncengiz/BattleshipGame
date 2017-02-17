class Ship(object):
    def __init__(self, name, symbol, length, damage):
        self.name = name
        self.symbol = symbol
        self.length = length
        self.damage = damage

    def shoot(self):
            self.damage = self.damage + 1

    def isSunk(self):
        return self.damage == self.length
