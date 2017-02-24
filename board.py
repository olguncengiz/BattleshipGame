from colorama import init, Fore, Back, Style
import common
init()

class Board(object):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, primary=True):
        self.chr_blank = ' '
        self.chr_miss = 'X'
        self.chr_hit = 'O'
        self.primary = primary
        #self.ships = dict()

        self.size = 10
        self.cells = [[self.chr_blank for x in range(self.size)] for y in range(self.size)]

    def decode(self, address):
        try:
            row = address[0].upper()
            column = int(address[1:])

            if row in self.alphabet and column in self.numbers:
                return [self.alphabet.index(row), self.numbers.index(column)]
            else:
                return [-1, -1]
        except Exception as e:
            return [-1, -1]

    def encode(self, row, column):
        try:
            if row in range(self.size) and column in range(self.size):
                return self.alphabet[row] + str(self.numbers[column])
            else:
                return 'NA'
        except Exception as e:
            return 'NA'

    def mask(self, cellValue):
        if self.primary:
            return cellValue
        else:
            if cellValue not in [self.chr_blank, self.chr_miss, self.chr_hit]:
                return self.chr_blank
            else:
                return cellValue

    def wrapMarineColors(self, string):
        if string == self.chr_hit:
            string = Fore.RED + string
        elif string == self.chr_miss:
            string = Fore.YELLOW + string
        else:
            string = Fore.GREEN + string
        return Back.BLUE + Style.BRIGHT + string + Style.RESET_ALL

    def printBoard(self):
        print '  12345678910'
        for row in range(self.size):
            line = Board.alphabet[row] + ' '
            for column in range(self.size):
                cellValue = self.getCellValue(self.encode(row, column))
                maskedValue = self.mask(cellValue)
                line = line + self.wrapMarineColors(maskedValue)
            print line
        print '\n'

    def shoot(self, address):
        cellValue = self.getCellValue(address)
        row, column = self.decode(address)

        if self.canShootCell(address):
            if self.cells[row][column] == self.chr_blank:
                self.cells[row][column] = self.chr_miss
            else:
                self.cells[row][column] = self.chr_hit
        return cellValue

    def canShootCell(self, address):
        row, column = self.decode(address)
        if self.isValidCellAddress(address):
            return (self.cells[row][column] != self.chr_miss) and (self.cells[row][column] != self.chr_hit)
        else:
            return False

    def isValidCellAddress(self, address):
        row, column = self.decode(address)
        if row != -1 and column != -1:
            return True
        else:
            return False

    def getCellValue(self, address):
        row, column = self.decode(address)
        return self.cells[row][column]

    def canPositionShip(self, startAddress, direction, length):
        if length == 1:
            if self.isValidCellAddress(startAddress) and (self.getCellValue(startAddress) == self.chr_blank):
                return True
        else:
            if self.isValidCellAddress(startAddress) and (self.getCellValue(startAddress) == self.chr_blank):
                row, column = self.decode(startAddress)
                row = row + direction
                column = column + (1 - direction)
                nextAddress = self.encode(row, column)
                return self.canPositionShip(nextAddress, direction, length - 1)
            else:
                return False

    def markTrackingBoard(self, cell, hit):
        row, column = self.decode(cell)
        if hit:
            self.cells[row][column] = self.chr_hit
        else:
            self.cells[row][column] = self.chr_miss

    def getNextTargetCell(self):
        # Find any hits on the board
        for r in range(self.size):
            for c in range(self.size):
                if self.cells[r][c] == self.chr_hit:
                    targets = [[r - 1, c], [r, c - 1], [r + 1, c], [r, c + 1]]

                    for i in range(len(targets)):
                        cell = self.encode(targets[i][0], targets[i][1])
                        if self.isValidCellAddress(cell) and self.canShootCell(cell):
                            return targets[i]
        
        tries = 0
        while tries < 10:
            cellAddress = common.randomCell
            cell = self.encode(r, c)
            if self.getCellValue(cell) == self.chr_blank:
                targets = [[r - 1, c], [r, c - 1], [r + 1, c], [r, c + 1]]

                allEmpty = True
                for i in range(len(targets)):
                    neighborCell = self.encode(targets[i][0], targets[i][1])
                    if self.isValidCellAddress(neighborCell):
                        if not self.canShootCell(neighborCell):
                            allEmpty = False
                            break
                if allEmpty:
                    return self.decode(cell)
            tries += 1
        
        cellAddress = common.randomCell() 
        return cellAddress
