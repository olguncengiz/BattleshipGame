from board import Board
from ship import Ship
import common

class User(object):
    def __init__(self, name, bot=False, easy=True):
        self.name = name
        self.primaryBoard = Board()
        self.trackingBoard = Board(primary=False)
        self.bot = bot
        self.easy = easy
        self.gameSetUp()

    def gameSetUp(self):
        aircraft_carrier = Ship('Aircraft Carrier', 'A', 5, 0)
        battleship = Ship('Battleship', 'B', 4, 0)
        cruiser = Ship('Cruiser', 'C', 3, 0)
        destroyer = Ship('Destroyer', 'D', 2, 0)
        submarine = Ship('Submarine', 'E', 2, 0)

        self.ships = [aircraft_carrier, battleship, cruiser, destroyer, submarine]

    def positionShips(self, manual=False):
        for ship in self.ships:
            row, column = [-1, -1]
            cell = 'Z11'
            direction = -1
            length = ship.length

            while not self.primaryBoard.canPositionShip(cell, direction, length):
                if (self.bot) or (not manual):
                    row, column = common.randomCell()
                    cell = self.primaryBoard.encode(row, column)
                    direction = common.randomDirection()
                else:
                    while True:
                        common.clearScreen()
                        self.primaryBoard.printBoard()
                        cell = raw_input('Please Enter A Starting Cell For "%s": ' % ship.name)
                        direction = raw_input('Please Enter A Direction (0-Horizontal, 1-Vertical): ')
                        if (direction in ['0', '1']) and (self.primaryBoard.isValidCellAddress(cell)):
                            direction = int(direction)
                            row, column = self.primaryBoard.decode(cell)
                            break
                
            while length > 0:
                self.primaryBoard.cells[row][column] = ship.symbol
                row = row + direction
                column = column + (1 - direction)
                length = length - 1

    def playTurn(self):
        if not self.bot:
            cell = raw_input('Enter A Cell To Shoot: ')
            return cell
        else:
            row, column = [-1, -1]
            if self.easy:
                row, column = common.randomCell()
            else:
                row, column = self.findTargetCell()
            
            cell = self.trackingBoard.encode(row, column)
            return cell

    def getShip(self, symbol):
        for ship in self.ships:
            if ship.symbol == symbol:
                return ship

    def allShipsSunk(self):
        won = True
        for ship in self.ships:
            if not ship.isSunk():
                won = False
                break
        return won

    def findTargetCell(self):
        return common.randomCell()
        